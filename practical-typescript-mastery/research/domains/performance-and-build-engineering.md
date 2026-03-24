# Performance and Build Engineering

## Overview

This domain covers the practical skills needed to diagnose, measure, and optimize TypeScript compilation performance — and to architect build pipelines that scale across monorepos, CI systems, and large codebases. The focus is on type-check speed, build graph design, caching strategies, emit separation, and benchmarking methodology.

This is an advanced domain that builds on compiler configuration knowledge (D-2), tooling ergonomics (D-8), and refactoring skills (D-9). Mastery here directly enables teams to maintain fast feedback loops as codebases grow, and feeds into governance practices (D-12).

---

## Key Concepts

### 1. Performance Diagnostics with `--generateTrace`

The `--generateTrace` flag (TypeScript 4.1+) instruments the compiler to produce detailed trace files showing exactly where time is spent during compilation. Usage:

```bash
tsc --generateTrace ./traceDir --project tsconfig.json
```

This produces `trace.json` and `types.json` files. Analyze them with:
- **Chrome Trace Viewer** (`chrome://tracing/`) or **Perfetto UI** for visual timeline inspection
- **`@typescript/analyze-trace`** (npm package) for quick CLI summaries of hot spots

The trace reveals per-file and per-expression time costs, expensive type instantiations, and which compilation phases dominate. The checking phase is almost always the bottleneck.

**Relationship:** This is the primary entry point for all other optimization work. You diagnose before you optimize.

### 2. `--extendedDiagnostics` Flag

A lighter-weight alternative to `generateTrace` that prints summary metrics:
- Total type instantiations
- Memory usage
- Parse, bind, check, and emit times
- File counts

Use this for quick before/after comparisons when benchmarking optimizations.

### 3. `@typescript/analyze-trace` Tool

A CLI tool from the TypeScript team that processes `generateTrace` output and produces a ranked list of compilation hot spots. Options include `--skipMillis` (filter noise) and `--forceMillis` (highlight significant delays). It can also detect duplicate npm package versions that inflate type-checking work.

### 4. Expensive Type Patterns

Patterns that make the compiler work disproportionately hard:

- **Deep recursive types:** Types that recurse many levels (e.g., deeply nested JSON schemas, recursive tree types)
- **Large union/intersection types:** Combining many members forces combinatorial checking
- **Unconstrained generics:** `<T>` without bounds forces the compiler to consider all possibilities
- **Complex conditional + mapped type chains:** Deeply nested `T extends X ? A : B` combined with `{ [K in keyof T]: ... }` can explode instantiation counts
- **Excessive type instantiations:** Each unique generic parameterization creates a new type instance

**Mitigation strategies:**
- Name complex types (named types are more compact than inlined anonymous types)
- Prefer interfaces over intersections (`interface A extends B` is cheaper than `A & B`)
- Add explicit return type annotations to reduce inference work
- Limit recursion depth with counter patterns
- Break large conditional type trees into named helper types

### 5. Hot Files Identification

"Hot files" are source files where the compiler spends disproportionate time. Identify them via `analyze-trace` output or visual inspection in Perfetto. Common causes:
- Files that re-export large type surfaces
- Files with complex generic utilities used project-wide
- Barrel files (`index.ts`) that pull in entire module trees

### 6. Build Graph with Project References

TypeScript Project References split a large project into smaller sub-projects, each with its own `tsconfig.json`. Key settings:

- `composite: true` — enables incremental builds and declaration generation
- `declaration: true` — generates `.d.ts` files for cross-project type checking
- `declarationMap: true` — enables "Go to Definition" across project boundaries
- `references: [{ path: "../other-package" }]` — declares dependencies

Build with `tsc --build` (or `tsc -b`), which respects the dependency graph and only rebuilds stale projects.

**Benefits:** Faster incremental builds, enforced module boundaries, better editor performance (smaller project contexts).

**Relationship:** This is the structural foundation for all monorepo TypeScript optimization.

### 7. Incremental Compilation and `.tsbuildinfo`

When `incremental: true` is set, TypeScript writes `.tsbuildinfo` files containing a snapshot of the project graph. On subsequent compilations, only changed files and their dependents are rechecked. This is the single most impactful setting for reducing rebuild times.

The `tsBuildInfoFile` option controls where these files are written.

### 8. Cache-Aware CI Pipelines

Strategies for preserving compilation caches across CI runs:

- **Cache `.tsbuildinfo` files** between CI runs (GitHub Actions cache, etc.)
- **Use Turborepo remote caching** — hashes inputs per task, skips unchanged tasks, shares cache across developers and CI
- **Use Nx Cloud** — similar remote caching plus distributed task execution
- **Nx `affected` command** — uses git diff + project graph to run tasks only on changed projects
- **Turborepo task pipelines** — define explicit inputs/outputs in `turbo.json` for granular cache invalidation

**Key insight:** Separate "restore cache + install" from "type-check + emit" in CI job structure.

### 9. Emit Separation

Decoupling the three compilation concerns for speed:

1. **Transpilation** (TS → JS): Use fast tools like **SWC** (Rust-based, ~20x faster than Babel) or **esbuild** (Go-based, ~10-100x faster than Webpack). These strip types without checking them.
2. **Type checking**: Run `tsc --noEmit` separately — can run in parallel with transpilation
3. **Declaration generation**: Run `tsc --emitDeclarationOnly` to produce `.d.ts` files

This architecture gives instant dev feedback (fast transpiler) while maintaining type safety (parallel tsc).

### 10. `isolatedDeclarations` (TypeScript 5.5+)

A compiler option that requires explicit type annotations on all exports, enabling declaration files to be generated without full type inference. This unlocks:

- **Parallel declaration emit** — each file can produce `.d.ts` independently
- **Third-party tooling** — SWC/esbuild could potentially generate declarations
- **Faster monorepo builds** — 3x to 15x speedup reported for declaration generation

Trade-off: requires more explicit annotations, but TypeScript provides Quick Fix assistance for migration.

### 11. `skipLibCheck` and `skipDefaultLibCheck`

- `skipLibCheck: true` — skips type-checking all `.d.ts` files (including `node_modules`)
- `skipDefaultLibCheck: true` — skips only the default lib files

`skipLibCheck` is a pragmatic setting for most projects that dramatically reduces check time with minimal risk (library declarations are already validated by their authors).

### 12. `isolatedModules`

Forces TypeScript to analyze each file independently, which is required by transpile-only tools (SWC, esbuild, Babel). It prohibits certain patterns (const enums across files, namespace merging) but enables faster per-file processing.

### 13. Monorepo Build Orchestration

Tools that manage the build graph beyond TypeScript:

- **Turborepo** — task runner with caching and parallelization; recommends NOT using TS project references (uses its own graph)
- **Nx** — full monorepo toolkit with project graph, affected commands, remote caching, and TSC batch mode that generates project references on-the-fly
- **Rush** — Microsoft's monorepo manager with phased builds
- **moon** — Rust-based monorepo tool with TypeScript project reference support

### 14. Benchmarking Methodology

A disciplined approach to measuring and improving compilation performance:

**The BAM Method (Branch, Adjust, Measure):**
1. Branch — create an isolated branch for the experiment
2. Adjust — make one change at a time
3. Measure — run `tsc --extendedDiagnostics` or `--generateTrace` and compare

**Practical benchmarking steps:**
1. Establish a baseline: `tsc --extendedDiagnostics` on current state (record check time, instantiations, memory)
2. Generate a trace: `tsc --generateTrace ./trace`
3. Identify hot spots: `npx @typescript/analyze-trace ./trace`
4. Apply one optimization
5. Re-measure and compare
6. Repeat

**CI benchmarking:** Track `--extendedDiagnostics` output over time. Alert on regressions in check time or instantiation count.

### 15. Project Corsa / TypeScript 7 (Go Rewrite)

Microsoft is porting the TypeScript compiler to Go, targeting ~10x compilation speedup. Key improvements:
- Native execution eliminates JIT overhead (3-4x)
- True parallelism for parsing, binding, and emit (2-3x)
- VS Code project load: 9.6s → 1.2s in benchmarks

This will arrive as TypeScript 7.0 and changes the performance landscape significantly, but current optimization skills remain valuable for TypeScript 5.x/6.x projects.

---

## Concept Relationships

```
generateTrace + extendedDiagnostics + analyze-trace
    → Hot Files Identification
    → Expensive Type Patterns (diagnosis)
        → Mitigation (naming types, interfaces, annotations)

Project References + Incremental Compilation
    → Build Graph Optimization
    → Cache-Aware CI (tsbuildinfo caching)

Emit Separation (SWC/esbuild + tsc --noEmit)
    → isolatedDeclarations (parallel .d.ts)
    → isolatedModules (per-file transpilation)

Benchmarking Methodology
    → Wraps all of the above into a measurement-driven workflow
```

---

## Prerequisites for Other Domains

- **D-12 (Team Practices & Governance):** Benchmarking methodology, CI cache configuration, and build graph optimization feed directly into team-level governance of TypeScript performance budgets and build time SLAs.

---

## Learning Resources

### Documentation and Reference Materials

1. **TypeScript Performance Wiki** — Microsoft's official guide to writing fast-to-compile TypeScript
   - URL: https://github.com/microsoft/TypeScript/wiki/Performance
   - Covers: code patterns, project configuration, build tools, investigation techniques
   - Difficulty: Intermediate-Advanced
   - *This is THE canonical reference. Start here.*

2. **TypeScript Performance Tracing Wiki** — Official guide to `--generateTrace`
   - URL: https://github.com/microsoft/TypeScript/wiki/Performance-Tracing
   - Covers: generating traces, analyzing with Chrome/Perfetto, using analyze-trace
   - Difficulty: Intermediate

3. **TypeScript Project References Handbook** — Official documentation
   - URL: https://www.typescriptlang.org/docs/handbook/project-references.html
   - Covers: composite projects, build mode, declaration emit, solution-style tsconfigs
   - Difficulty: Intermediate

4. **TypeScript `isolatedDeclarations` Documentation** — Official tsconfig reference
   - URL: https://www.typescriptlang.org/tsconfig/isolatedDeclarations.html
   - Covers: what the flag requires, migration guidance
   - Difficulty: Advanced

5. **Turborepo TypeScript Guide** — Official Turborepo docs for TypeScript projects
   - URL: https://turborepo.dev/docs/guides/tools/typescript
   - Covers: caching strategy, task configuration, monorepo setup
   - Difficulty: Intermediate

6. **Nx TypeScript Monorepo Management** — Managing TS packages in Nx monorepos
   - URL: https://nx.dev/blog/managing-ts-packages-in-monorepos
   - Covers: project references, batch mode, caching layers
   - Difficulty: Intermediate-Advanced

### Video Tutorials and Conference Talks

7. **"Navigating TypeScript Performance for Better Dev Experience" — Aleksandra Sikora (Armada JS 2023)**
   - URL: https://www.youtube.com/watch?v=IzzvGrZrFSE
   - Duration: ~30 min
   - Covers: real-world TypeScript perf debugging with metrics and tooling
   - Difficulty: Intermediate-Advanced

8. **"A 10x Faster TypeScript" — Anders Hejlsberg (Microsoft Build 2025)**
   - URL: https://www.youtube.com/watch?v=pNlq-EVld70
   - Duration: ~45 min
   - Covers: TypeScript 7 Go rewrite, architecture, benchmarks, future of TS perf
   - Difficulty: All levels

9. **"Porting the TypeScript Compiler to Go" — Jake Bailey (GopherCon 2025)**
   - URL: https://www.youtube.com/watch?v=PZm_YbE3fcA
   - Duration: ~40 min
   - Covers: technical details of the Go port, parallelism challenges, performance gains
   - Difficulty: Advanced

### Books

10. **"Effective TypeScript" (2nd Edition) — Dan Vanderkam (O'Reilly, 2024)**
    - Relevant: Chapter 9 "Writing and Running Your Code" — includes item on compiler performance
    - Difficulty: Intermediate-Advanced
    - Note: The performance-specific content is a single item, but the broader code quality advice throughout the book reduces type complexity

11. **"Programming TypeScript" — Boris Cherny (O'Reilly, 2019)**
    - Relevant: Chapter on compiler internals and project configuration
    - Difficulty: Intermediate
    - Note: Dated on newer features but good for foundational understanding of the compiler pipeline

### Blog Posts and Articles (Authoritative)

12. **"An Approach to Optimizing TypeScript Type-Checking Performance" — Gel (formerly EdgeDB)**
    - URL: https://www.geldata.com/blog/an-approach-to-optimizing-typescript-type-checking-performance
    - Covers: real-world case study of optimizing a complex type system, BAM method
    - Difficulty: Advanced

13. **"Fixing TypeScript Performance Problems" — Viget**
    - URL: https://www.viget.com/articles/fixing-typescript-performance-problems
    - Covers: practical step-by-step debugging of slow TypeScript compilation
    - Difficulty: Intermediate

14. **"Agonizing Over TypeScript Performance" — Outschool Engineering**
    - URL: https://engineering.outschool.com/posts/agonizing-typescript/
    - Covers: real production case study of diagnosing and fixing TS perf issues
    - Difficulty: Intermediate-Advanced

15. **"Benchmarking TypeScript Type Checking" — Spiko Engineering**
    - URL: https://tech.spiko.io/posts/benchmarking-typescript-type-checking/
    - Covers: systematic benchmarking methodology for type checking
    - Difficulty: Advanced

16. **"Speed Up Your TypeScript Monorepo with esbuild" — Matteo Mazzarolo**
    - URL: https://mmazzarolo.com/blog/2021-11-06-speed-up-your-typescript-monorepo-with-esbuild/
    - Covers: practical emit separation setup using esbuild
    - Difficulty: Intermediate

### GitHub Repositories

17. **`microsoft/typescript-benchmarking`** — Official TypeScript benchmarking infrastructure
    - URL: https://github.com/microsoft/typescript-benchmarking
    - Contains: build scripts, `ts-perf` CLI, benchmark suites
    - Useful for understanding how the TS team measures performance

18. **`@typescript/analyze-trace`** — Official trace analysis tool
    - URL: https://www.npmjs.com/package/@typescript/analyze-trace
    - Install: `npm install -g @typescript/analyze-trace`

### Interactive Exercises and Practice

19. **TypeScript Playground** — Test type patterns and observe compilation behavior
    - URL: https://www.typescriptlang.org/play
    - Use to experiment with type complexity in isolation

20. **Nx Interactive Tutorial** — Hands-on monorepo setup with TypeScript
    - URL: https://nx.dev/getting-started/intro
    - Covers project references, caching, affected commands

### Community Resources

21. **r/typescript** — Active subreddit with performance discussions
    - URL: https://www.reddit.com/r/typescript/
22. **TypeScript Discord** — Official community server
    - URL: https://discord.gg/typescript

---

## Learning Path

### Phase 1: Diagnostics Foundation (3-4 hours)

**Concepts:** `--extendedDiagnostics`, `--generateTrace`, `@typescript/analyze-trace`, hot files identification

1. Read the TypeScript Performance Wiki (resource #1)
2. Read the Performance Tracing Wiki (resource #2)
3. Run `tsc --extendedDiagnostics` on a real project and interpret the output
4. Run `tsc --generateTrace ./trace` and analyze with `npx @typescript/analyze-trace ./trace`
5. Open the trace in Perfetto UI and explore the visual timeline

**Milestone:** You can identify the top 3 slowest files in any TypeScript project and explain why they're slow.

### Phase 2: Expensive Type Patterns (4-5 hours)

**Concepts:** Recursive types, large unions, unconstrained generics, conditional/mapped type chains, instantiation costs, mitigation strategies

1. Read the Gel blog post on type-checking optimization (resource #12)
2. Read the Viget article (resource #13) and Outschool case study (resource #14)
3. Practice: Take a project with known slow types, apply the BAM method to optimize one pattern at a time
4. Study the "Writing Easy-to-Compile Code" section of the Performance Wiki

**Milestone:** You can refactor an expensive type pattern and demonstrate measurable improvement using `--extendedDiagnostics`.

### Phase 3: Build Graph and Project References (4-5 hours)

**Concepts:** Project references, composite projects, `tsc --build`, solution-style tsconfigs, declaration maps

1. Read the Project References handbook (resource #3)
2. Set up a small monorepo with 3+ packages using project references
3. Test incremental builds — change one package and observe only dependents rebuild
4. Configure `declarationMap` and verify "Go to Definition" works across packages

**Milestone:** You can convert a single-tsconfig project into a multi-project setup with correct build ordering.

### Phase 4: Emit Separation (3-4 hours)

**Concepts:** transpileOnly, SWC, esbuild, `--noEmit`, `--emitDeclarationOnly`, `isolatedDeclarations`, `isolatedModules`

1. Read the `isolatedDeclarations` documentation (resource #4)
2. Read the esbuild monorepo article (resource #16)
3. Set up a build pipeline: esbuild/SWC for transpilation + `tsc --noEmit` for type checking
4. Enable `isolatedDeclarations` in a project and resolve any annotation requirements
5. Measure the speed difference vs. plain `tsc`

**Milestone:** You have a working build setup where transpilation takes <1 second and type checking runs in parallel.

### Phase 5: Cache-Aware CI (3-4 hours)

**Concepts:** `.tsbuildinfo` caching, Turborepo remote cache, Nx Cloud, affected commands, CI job architecture

1. Read the Turborepo TypeScript guide (resource #5) and Nx monorepo guide (resource #6)
2. Configure `.tsbuildinfo` caching in a CI pipeline (GitHub Actions or similar)
3. Set up either Turborepo or Nx remote caching
4. Implement an "affected-only" CI strategy
5. Measure CI time before and after

**Milestone:** Your CI pipeline skips type-checking unchanged packages and shares cache across runs.

### Phase 6: Benchmarking Discipline (2-3 hours)

**Concepts:** BAM method, regression tracking, instantiation budgets, CI performance monitoring

1. Read the Spiko benchmarking article (resource #15)
2. Establish a baseline benchmark for your project
3. Set up a CI step that runs `tsc --extendedDiagnostics` and records metrics
4. Define a "performance budget" (e.g., check time < 30s, instantiations < 500K)
5. Watch the Anders Hejlsberg talk on TypeScript 7 (resource #8) for future context

**Milestone:** You have automated performance tracking and can demonstrate a trend over time.

---

## Practical Exercises

### Exercise 1: Performance Audit (Beginner)
Take any medium-sized TypeScript project (or use the TypeScript compiler source itself). Run `--extendedDiagnostics` and `--generateTrace`. Use `analyze-trace` to identify the top 5 hot spots. Write a brief report of findings.

### Exercise 2: Type Pattern Optimization (Intermediate)
Create a file with intentionally expensive patterns:
- A recursive type that processes a 10-level deep object
- A mapped type over a 50-member union
- A generic function with no constraints used in 20 call sites

Measure with `--extendedDiagnostics`, then optimize each pattern and re-measure. Target a 2x improvement.

### Exercise 3: Project References Setup (Intermediate)
Convert a single-package TypeScript application into a 3-package monorepo (e.g., `core`, `api`, `web`). Configure project references, verify incremental builds work, and measure build time improvement vs. the monolithic setup.

### Exercise 4: Emit Separation Pipeline (Advanced)
Build a complete dev pipeline:
- SWC or esbuild handles transpilation (dev server)
- `tsc --noEmit` runs in watch mode alongside
- `tsc --emitDeclarationOnly` runs during CI
- Enable `isolatedDeclarations` and fix all annotation requirements

Compare total build time to pure-tsc approach.

### Exercise 5: CI Cache Optimization (Advanced)
Set up a GitHub Actions (or similar) CI pipeline for a multi-package TypeScript monorepo:
- Cache `node_modules` and `.tsbuildinfo` files
- Run type-checking only on affected packages
- Add a performance budget check that fails CI if check time exceeds threshold
- Bonus: Add Turborepo or Nx remote caching

### Exercise 6: Full Benchmarking Workflow (Expert)
For a production-scale project:
1. Establish baseline metrics (check time, instantiations, memory)
2. Profile with `generateTrace`, identify top 3 bottlenecks
3. Apply optimizations using the BAM method
4. Document each change and its measured impact
5. Set up automated regression tracking in CI
6. Achieve at least 30% reduction in type-check time

---

## Connections to Other Domains

- **D-2 (Strictness and Compiler Configuration):** Direct prerequisite — understanding `tsconfig.json` options is essential for performance tuning. Options like `strict`, `skipLibCheck`, `incremental`, and `isolatedModules` are covered in D-2 but applied for performance here.
- **D-8 (Tooling and Editor Ergonomics):** Editor performance (tsserver) is directly affected by the same type patterns. Project references improve editor responsiveness. tsserver logging complements `generateTrace` for IDE-specific issues.
- **D-9 (Refactoring and Legacy Migration):** Migration projects often have mixed `any`/strict patterns that create unusual performance profiles. The diagnostic skills from this domain help identify migration-induced performance issues.
- **D-12 (Team Practices and Governance):** Performance budgets, CI benchmarking, and build architecture decisions are team-level governance concerns that depend on the technical skills in this domain.
