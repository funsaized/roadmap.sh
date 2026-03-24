# D-9: Refactoring and Legacy Migration

## Overview

This domain covers the practical strategies, tools, and patterns for migrating JavaScript codebases to TypeScript, tracking and eliminating type debt (`any`, `@ts-ignore`), using codemods for automated refactoring, establishing contract tests as safety nets during migration, measuring type coverage, and adopting monorepo patterns with clear dependency boundaries. This is an advanced domain that builds on foundations (D-1), strictness configuration (D-2), type modeling (D-3), runtime boundaries (D-4), and tooling (D-8).

**Prerequisites from other domains:**
- D-1: Structural typing, union/intersection types, narrowing fundamentals
- D-2: `tsconfig.json` configuration, `strict` mode, `allowJs`/`checkJs` options
- D-3: Discriminated unions, branded types, utility types for modeling
- D-4: Runtime validation, schema-first patterns, `unknown` parsing
- D-8: Editor ergonomics, `tsc --noEmit`, CI integration patterns

**Feeds into:**
- D-10: Performance and Build Engineering (build graph optimization, project references at scale)
- D-12: Team Practices, Governance, and Anti-Patterns (migration governance, code review during migration)

---

## Key Concepts

### 1. Incremental JS-to-TS Migration Strategy
**What it is:** A phased approach to converting a JavaScript codebase to TypeScript without a disruptive "big bang" rewrite. JavaScript and TypeScript files coexist during the transition period.

**Core mechanics:**
- Enable `allowJs: true` in `tsconfig.json` to let TS compiler process `.js` files
- Optionally enable `checkJs: true` to type-check JS files using JSDoc annotations
- Start with `strict: false` and `noImplicitAny: false`, tighten progressively
- Rename files from `.js`/`.jsx` to `.ts`/`.tsx` one at a time
- Begin with "leaf" files (few dependencies) to minimize cascading errors
- Enforce all new code in TypeScript from day one

**Migration plan template:**
1. **Phase 0 — Setup (1-2 days):** Install TypeScript, create `tsconfig.json` with `allowJs: true`, configure build tools
2. **Phase 1 — Coexistence (1-2 weeks):** Convert leaf files (utilities, constants, config), install `@types/*` packages
3. **Phase 2 — Core Layer (2-4 weeks):** Migrate data models, API clients, shared types; establish type boundaries
4. **Phase 3 — Feature Code (ongoing):** Convert feature modules file-by-file, prioritize high-churn areas
5. **Phase 4 — Strictness Ratchet (ongoing):** Enable strict flags incrementally, burn down `any` usage
6. **Phase 5 — Completion:** Remove `allowJs`, enforce 100% TypeScript, enable full strict mode

**Relates to:** Strictness ratcheting, type coverage tracking, codemod tools

### 2. The `allowJs` and `checkJs` Compiler Options
**What they are:** TypeScript compiler flags that enable gradual migration by allowing JS files in the compilation and optionally type-checking them.

- `allowJs: true` — Includes `.js` files in TypeScript compilation output
- `checkJs: true` — Reports type errors in `.js` files (equivalent to `// @ts-check` per file)
- Together they enable JSDoc-based typing before renaming files to `.ts`

**Key tradeoff:** `checkJs` can surface hundreds of errors in existing JS code. Start with it off, enable per-file with `// @ts-check`, then globally once most files are converted.

### 3. `@ts-ignore` vs `@ts-expect-error` — Error Suppression Tracking
**What they are:** Directives that suppress TypeScript errors on the following line.

- `@ts-ignore` — Silently suppresses errors; stays even after the error is fixed (dangerous)
- `@ts-expect-error` (TS 3.9+) — Suppresses errors but reports "unused directive" if no error exists (self-cleaning)

**Best practice:** Always prefer `@ts-expect-error` over `@ts-ignore`. Use the ESLint rule `@typescript-eslint/prefer-ts-expect-error` to enforce this. Track total count of suppression directives as a migration health metric.

**Relates to:** Type debt tracking, migration quality gates

### 4. `any` Debt Tracking and Burndown
**What it is:** Systematic identification, quantification, and progressive elimination of `any` types and type assertions in a codebase.

**Tracking patterns:**
- Use `$TSFixMe` (Airbnb pattern) or `// TODO: type this` aliases for `any` to make them searchable
- Count `any` occurrences with grep/search: `grep -r ": any" --include="*.ts" | wc -l`
- Track `@ts-expect-error` and `@ts-ignore` counts over time
- Set CI gates: fail builds if `any` count increases above baseline

**Automation tools:**
- **type-coverage** CLI: Reports percentage of identifiers with known types vs `any`
- **typescript-coverage-report**: Generates HTML reports from type-coverage data
- **Knip**: Finds unused files, dependencies, and exports (dead code that complicates migration)
- **ts-prune** / **ts-unused-exports**: Identify exported symbols that are never imported

**Measurable milestones:**
- Milestone 1: Baseline type coverage measured (e.g., 62%)
- Milestone 2: No new `any` allowed in PRs (CI gate)
- Milestone 3: Type coverage reaches 80%
- Milestone 4: All `$TSFixMe`/`@ts-expect-error` tracked in issue tracker
- Milestone 5: Type coverage reaches 95%+
- Milestone 6: Full strict mode enabled, zero `any` outside intentional escape hatches

### 5. Codemod Tools for Automated Migration
**What they are:** Tools that programmatically transform source code using Abstract Syntax Tree (AST) manipulation.

**Primary tools:**

| Tool | Engine | Best For |
|------|--------|----------|
| **ts-migrate** | jscodeshift + TS compiler | Full JS→TS conversion at scale (Airbnb) |
| **jscodeshift** | recast (AST) | General AST transforms, framework migrations |
| **ts-morph** | TypeScript Compiler API | Type-aware refactoring, code generation |
| **Codemod.com** | jscodeshift + ts-morph | Community codemod registry, AI-assisted |

**ts-migrate workflow:**
1. `ts-migrate init <folder>` — Creates `tsconfig.json`
2. `ts-migrate rename <folder>` — Renames `.js`→`.ts`, `.jsx`→`.tsx`
3. `ts-migrate migrate <folder>` — Applies codemods to fix compile errors (adds `any`/`@ts-expect-error`)
4. `ts-migrate reignore <folder>` — Re-runs error suppression

**jscodeshift for custom transforms:**
- jQuery-like API for AST navigation and manipulation
- Preserves original formatting via recast
- Write transforms in TypeScript targeting TypeScript ASTs
- Useful for: API migration (e.g., updating deprecated function signatures), enforcing patterns

**ts-morph for type-aware refactoring:**
- Full access to TypeScript type checker during transforms
- Can query symbol types, find references, rename across files
- Used by Microsoft internally for their TypeScript module migration
- Ideal for: adding type annotations, extracting interfaces from usage patterns

### 6. Contract Tests as Migration Safety Nets
**What they are:** Tests that verify the "contract" (expected API shape) between consumers and providers remains stable during migration.

**Why they matter for migration:** When converting JS to TS, you risk changing runtime behavior even though you're "just adding types." Contract tests catch:
- Renamed or removed fields
- Changed nullability
- Altered function signatures
- Import path changes

**Approaches:**

**a) Consumer-Driven Contract Tests (Pact)**
- Consumer defines expected interactions (request/response shapes)
- Provider verifies it can fulfill those contracts
- Contracts stored in Pact Broker, versioned per environment
- TypeScript types can be generated from/compared to Pact contracts
- Tool: [Pact JS](https://docs.pact.io/implementation_guides/javascript/readme)

**b) Schema-Based Contract Tests**
- Define API contracts as OpenAPI/JSON Schema specs
- Generate TypeScript types from schemas
- Test that actual API responses match schemas at CI time
- Tools: openapi-typescript, zod schema validation

**c) Snapshot-Based Contract Tests**
- Capture API response shapes as snapshots
- Detect drift when responses change unexpectedly
- Lighter-weight than Pact but less rigorous

**d) Type-Level Contract Tests**
- Use `tsd` or `expect-type` to assert that exported types match expected shapes
- Catches breaking changes in library/package public APIs
- Essential for internal package migrations in monorepos

### 7. Type Coverage Metrics
**What they are:** Quantitative measures of how much of your codebase has specific (non-`any`) type annotations.

**Tools:**
- **type-coverage** (`npx type-coverage`): Reports percentage and lists untyped identifiers
  - `--at-least 80` flag for CI enforcement
  - `--detail` shows every untyped identifier location
  - `--strict` counts type assertions as uncovered
- **typescript-coverage-report**: HTML visualization of type-coverage data

**Integration pattern:**
```bash
# CI script example
npx type-coverage --at-least 85 --strict
# Fails CI if coverage drops below 85%
```

**Ratchet pattern:** After each sprint, update the `--at-least` threshold upward. Never let it decrease.

### 8. Monorepo Migration Patterns
**What they are:** Strategies for structuring and migrating to TypeScript monorepos with clear package boundaries and dependency management.

**Project References for boundaries:**
- Each package gets its own `tsconfig.json` with `composite: true`
- Root `tsconfig.json` lists all packages in `references`
- Key settings: `declaration: true`, `declarationMap: true`, `incremental: true`
- Enforces: no circular dependencies, explicit import boundaries
- Build with `tsc --build` for incremental compilation

**tsconfig layering strategy:**
```
tsconfig.base.json          # Shared compiler options
├── packages/core/tsconfig.json    # extends base, composite: true
├── packages/api/tsconfig.json     # extends base, references: [core]
├── packages/web/tsconfig.json     # extends base, references: [core, api]
└── tsconfig.json                  # Root solution file, references all
```

**Monorepo tooling:**
- **Turborepo**: Fast builds with caching and parallel execution
- **Nx**: Dependency graph analysis, affected-only testing, TS project reference support (Nx 20+)
- **pnpm workspaces**: Efficient dependency management with strict isolation
- **Lerna**: Package versioning and publishing (often paired with Nx)

**Migration anti-patterns to avoid:**
- "Monorepo Death Star": One huge shared package that everything imports
- Circular dependencies between packages (introduce a "core" package to break cycles)
- Leaky abstractions: Backend ORM types exposed to frontend (use shared kernel types instead)
- Manual reference management at scale (use tooling to auto-sync)

**Dependency boundary enforcement:**
- Use `@typescript-eslint/no-restricted-imports` to prevent cross-boundary imports
- Package `exports` field in `package.json` controls public API surface
- `references` in `tsconfig.json` restricts what each package can import

### 9. Safe Large Refactoring Patterns
**What they are:** Techniques for confidently executing large-scale code changes in TypeScript codebases.

**Key patterns:**
- **Strangler Fig**: Build new TS code alongside legacy JS, gradually route to new code
- **Feature Flags**: Gate migrated code behind flags for incremental rollout
- **Parallel Runs**: Run old JS and new TS code in parallel, compare outputs
- **Atomic PRs**: Keep each migration PR small, focused, reviewable

**Safety nets:**
- `tsc --noEmit` as pre-commit/CI gate (catches type errors without building)
- Comprehensive test suite (unit + integration) run before and after migration
- Contract tests for API surfaces
- Type coverage metrics to prevent regression
- `git bisect` for identifying which migration PR introduced a bug

### 10. Declaration Files and Type Stubs
**What they are:** `.d.ts` files that provide type information for JavaScript code without modifying the source.

**Use cases during migration:**
- Write `.d.ts` stubs for JS modules not yet converted
- Use `declare module` for untyped third-party libraries without `@types/*`
- Gradual enhancement: start with loose declarations, tighten over time

**DefinitelyTyped workflow:**
- Install `@types/*` packages for third-party JS libraries
- When `@types` doesn't exist, write custom `.d.ts` declarations
- Contribute back to DefinitelyTyped when declarations mature

### 11. JSDoc-Based Typing (Pre-Migration)
**What it is:** Adding TypeScript type information to JavaScript files via JSDoc comments, enabling type checking without renaming files.

**When to use:**
- Large codebases where renaming files is risky or politically difficult
- Teams not ready to commit to full TypeScript adoption
- Testing TypeScript benefits before full migration

**Key JSDoc annotations:**
- `@param {Type}` — Function parameter types
- `@returns {Type}` — Return type
- `@type {Type}` — Variable type
- `@typedef` — Custom type definitions
- `@template T` — Generic type parameters

### 12. Codemod-Assisted Compiler Upgrades
**What they are:** Using codemods to automatically update code when upgrading TypeScript versions or enabling stricter compiler flags.

**Scenarios:**
- Upgrading from TS 4.x to 5.x (breaking changes in module resolution, decorators)
- Enabling `strict: true` on a previously non-strict codebase
- Enabling `noUncheckedIndexedAccess` (requires adding null checks everywhere arrays are indexed)
- Enabling `exactOptionalPropertyTypes` (changes how `undefined` is handled in optional properties)

**Approach:**
1. Create canary branch with new TS version / stricter flag
2. Run `tsc --noEmit` to collect all errors
3. Write or find codemods to fix common error patterns automatically
4. Apply codemods, manually fix remaining errors
5. Run full test suite to verify no runtime behavior changes
6. Merge with team review

### 13. Dead Code Elimination
**What it is:** Identifying and removing code that is never executed or imported.

**Tools:**
- **Knip**: Comprehensive project analysis — finds unused files, dependencies, exports, types
  - `npx knip` — Run analysis
  - `npx knip --fix` — Auto-remove unused exports
  - Supports monorepos and plugin systems
- **ts-prune**: Finds unused TypeScript exports
- **ts-unused-exports**: Similar to ts-prune, focused on exported symbols

**Why it matters for migration:** Dead code adds noise, slows type-checking, and creates false migration targets. Remove it first before spending effort adding types.

---

## Learning Resources

### Documentation and Reference Materials (Primary Sources)

1. **TypeScript Official: Migrating from JavaScript**
   - URL: https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html
   - Coverage: Official migration guide covering `allowJs`, `checkJs`, declaration files, incremental strictness
   - Freshness: Continuously maintained
   - Type: Documentation

2. **TSConfig Reference: allowJs, checkJs**
   - URL: https://www.typescriptlang.org/tsconfig/#allowJs
   - URL: https://www.typescriptlang.org/tsconfig/#checkJs
   - Coverage: Detailed explanation of migration-enabling compiler options
   - Type: Documentation

3. **TypeScript Official: Project References**
   - URL: https://www.typescriptlang.org/docs/handbook/project-references.html
   - Coverage: `composite`, `references`, `tsc --build`, monorepo structuring
   - Type: Documentation

4. **TypeScript 3.9 Release Notes (@ts-expect-error)**
   - URL: https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-9.html
   - Coverage: `@ts-expect-error` directive introduction and rationale
   - Type: Documentation

5. **TypeScript's Migration to Modules (Microsoft DevBlog)**
   - URL: https://devblogs.microsoft.com/typescript/typescripts-migration-to-modules/
   - Coverage: How the TypeScript team itself migrated to ES modules using ts-morph, lessons learned
   - Freshness: 2024
   - Type: Official blog / case study

### Books

6. **"Tackling TypeScript" by Dr. Axel Rauschmayer**
   - Chapter: "Migrating to TypeScript" (ch_migrating-to-typescript)
   - URL: https://exploringjs.com/ts/book/ch_migrating-to-typescript.html
   - Difficulty: Intermediate
   - Coverage: Comprehensive migration strategy, `allowJs`, declaration files, gradual strictness
   - Type: Book (free online)

7. **"Effective TypeScript" by Dan Vanderkam (2nd Edition, 2024)**
   - Relevant items: Item 75 (migrate JS to TS), Item 76 (incremental strictness), strictness adoption
   - Difficulty: Intermediate-Advanced
   - Coverage: Practical migration advice with before/after examples
   - Type: Book (paid)

8. **"Learning TypeScript" by Josh Goldberg (O'Reilly, 2022)**
   - Chapters on type system fundamentals supporting migration decisions
   - Difficulty: Beginner-Intermediate
   - Type: Book (paid)

### Video Tutorials and Talks

9. **"TypeScript Migration: A Love Story" — Various Conference Talks**
   - Search: YouTube "TypeScript migration production" or "JS to TypeScript at scale"
   - Coverage: Real-world migration case studies from companies
   - Type: Video

10. **Martin Fowler: "Codemods for API Refactoring"**
    - URL: https://martinfowler.com/articles/codemods-api-refactoring.html
    - Coverage: jscodeshift-based codemods for large-scale API changes
    - Freshness: Recent
    - Type: Article / tutorial

### GitHub Repositories and Tools

11. **ts-migrate (Airbnb)**
    - URL: https://github.com/airbnb/ts-migrate
    - Stars: 5k+
    - Coverage: Full JS→TS migration toolchain with plugin architecture
    - Type: Tool / Repository

12. **type-coverage**
    - URL: https://github.com/plantain-00/type-coverage
    - Coverage: CLI for measuring and enforcing type coverage percentage
    - Type: Tool / Repository

13. **Knip — Find unused files, dependencies, and exports**
    - URL: https://github.com/webpro-nl/knip
    - Docs: https://knip.dev/
    - Stars: 7k+
    - Coverage: Dead code detection, unused export elimination, monorepo support
    - Type: Tool / Repository

14. **ts-morph**
    - URL: https://github.com/dsherret/ts-morph
    - Docs: https://ts-morph.com/
    - Coverage: Programmatic TypeScript AST manipulation for type-aware codemods
    - Type: Library / Repository

15. **jscodeshift (Facebook)**
    - URL: https://github.com/facebook/jscodeshift
    - Docs: https://jscodeshift.com/overview/introduction
    - Coverage: AST-based codemod runner for JS/TS
    - Type: Tool / Repository

16. **typescript-coverage-report**
    - URL: https://www.npmjs.com/package/typescript-coverage-report
    - Coverage: HTML visualization of type-coverage results
    - Type: Tool

17. **Pact JS — Consumer-Driven Contract Testing**
    - URL: https://docs.pact.io/implementation_guides/javascript/readme
    - Coverage: Contract testing for API boundaries during migration
    - Type: Tool / Documentation

18. **monorepo-utils — Workspaces to Project References**
    - URL: https://github.com/azu/monorepo-utils
    - Coverage: Auto-convert npm/yarn/pnpm workspaces to TypeScript project references
    - Type: Tool

### Interactive Exercises and Practice

19. **Exercism TypeScript Track**
    - URL: https://exercism.org/tracks/typescript
    - Coverage: Practice exercises that reinforce type safety patterns used in migration
    - Type: Interactive exercises

20. **TypeScript Playground**
    - URL: https://www.typescriptlang.org/play
    - Coverage: Experiment with `allowJs`, compiler options, type checking behavior
    - Type: Interactive tool

### Community Resources

21. **r/typescript (Reddit)**
    - URL: https://www.reddit.com/r/typescript/
    - Coverage: Migration discussions, tooling recommendations, real-world experiences
    - Type: Community forum

22. **TypeScript Discord**
    - URL: https://discord.gg/typescript
    - Coverage: Real-time help with migration issues
    - Type: Community

23. **Airbnb Engineering Blog: ts-migrate**
    - URL: https://medium.com/airbnb-engineering/ts-migrate-a-tool-for-migrating-to-typescript-at-scale-cd23bfeb5cc
    - Coverage: Design decisions and lessons from migrating 6M+ lines at Airbnb
    - Type: Blog / case study

24. **Nx Blog: TypeScript Project References**
    - URL: https://nx.dev/blog/typescript-project-references
    - Coverage: Monorepo-scale project references with Nx tooling
    - Freshness: 2024
    - Type: Blog / documentation

25. **Microsoft Engineering Playbook: Consumer-Driven Contract Testing**
    - URL: https://microsoft.github.io/code-with-engineering-playbook/automated-testing/cdc-testing/
    - Coverage: Best practices for contract testing in service architectures
    - Type: Documentation / guide

---

## Learning Path

### Phase 1: Migration Fundamentals (8-10 hours)

**Concepts:** allowJs/checkJs, migration strategy, declaration files, JSDoc typing

1. Read the official TypeScript migration guide
2. Study `allowJs`/`checkJs` behavior in the TSConfig reference
3. Read "Tackling TypeScript" migration chapter
4. Practice: Set up a small JS project, enable `allowJs`, convert 3-5 files incrementally

**Milestone:** Can configure a TypeScript project to accept mixed JS/TS code and convert individual files without breaking the build.

### Phase 2: Automated Migration Tools (6-8 hours)

**Concepts:** ts-migrate, jscodeshift, ts-morph, codemod authoring

1. Study ts-migrate README and Airbnb blog post
2. Run ts-migrate on a sample JS project
3. Learn jscodeshift basics — write a simple AST transform
4. Explore ts-morph API for type-aware transforms
5. Practice: Write a custom codemod that adds explicit return types to functions

**Milestone:** Can run ts-migrate on a project and write basic custom codemods for recurring patterns.

### Phase 3: Type Debt Tracking and Elimination (5-7 hours)

**Concepts:** any tracking, @ts-expect-error, type coverage, dead code elimination, Knip

1. Set up type-coverage on a project, establish baseline
2. Configure CI gate with `--at-least` threshold
3. Replace all `@ts-ignore` with `@ts-expect-error`
4. Run Knip to find and remove unused code
5. Practice: Create a $TSFixMe alias, grep-based tracking script, and dashboard

**Milestone:** Can measure type coverage, enforce it in CI, and systematically reduce `any` usage.

### Phase 4: Contract Tests and Safety Nets (5-7 hours)

**Concepts:** Pact contract testing, schema-based contracts, type-level tests, snapshot contracts

1. Study Pact JS documentation and set up a basic consumer test
2. Learn schema-based contract testing with OpenAPI + TypeScript types
3. Explore `tsd`/`expect-type` for type-level contract assertions
4. Practice: Write contract tests for an API endpoint, verify provider compatibility

**Milestone:** Can set up contract tests that catch breaking changes during migration.

### Phase 5: Monorepo Patterns and Boundaries (6-8 hours)

**Concepts:** Project references, composite builds, tsconfig layering, Nx/Turborepo, dependency boundaries

1. Read TypeScript project references documentation
2. Set up a multi-package project with `composite: true` and `references`
3. Configure `tsc --build` for incremental compilation
4. Explore Nx or Turborepo for build orchestration
5. Practice: Extract shared types into a separate package with enforced boundaries

**Milestone:** Can structure a monorepo with TypeScript project references, enforce dependency boundaries, and build incrementally.

### Phase 6: Large-Scale Refactoring (4-6 hours)

**Concepts:** Strangler fig pattern, compiler upgrade codemods, strictness ratcheting

1. Study the strangler fig migration pattern
2. Practice enabling a new strict flag on an existing project using codemods
3. Simulate a TypeScript version upgrade with canary branch strategy
4. Practice: Enable `noUncheckedIndexedAccess` on a codebase, fix errors with a codemod

**Milestone:** Can safely upgrade TypeScript versions and enable stricter flags on production codebases.

**Total estimated time: 34-46 hours**

---

## Practical Exercises

### Exercise 1: Convert a JS Utility Library to TypeScript (Beginner)
**Objective:** Practice incremental migration on a small project
1. Clone a small JS utility library (e.g., lodash-like helpers)
2. Add `tsconfig.json` with `allowJs: true`, `strict: false`
3. Convert files one by one, starting with leaves
4. Measure type coverage before and after each file
5. Enable `strict: true` once all files are `.ts`

### Exercise 2: Run ts-migrate on a React App (Intermediate)
**Objective:** Experience automated migration tooling
1. Create or clone a JS React app (Create React App or Vite)
2. Run `ts-migrate-full` on the project
3. Catalog all `$TSFixMe`/`@ts-expect-error` annotations added
4. Fix 10 of the most impactful type issues manually
5. Measure type coverage improvement

### Exercise 3: Build a Type Coverage CI Pipeline (Intermediate)
**Objective:** Implement automated type debt tracking
1. Set up type-coverage in a project
2. Create a CI script that fails if coverage drops below threshold
3. Generate an HTML coverage report
4. Implement ratcheting: script that updates threshold after each PR
5. Run Knip and remove unused exports

### Exercise 4: Write Consumer-Driven Contract Tests (Advanced)
**Objective:** Protect API boundaries during migration
1. Set up a simple Express API with 2-3 endpoints
2. Create a consumer client in a separate package
3. Write Pact contract tests from the consumer side
4. Verify the provider against the generated contracts
5. Intentionally break the API and watch the contract test fail

### Exercise 5: Set Up a TypeScript Monorepo with Boundaries (Advanced)
**Objective:** Practice monorepo migration patterns
1. Create a monorepo with 3 packages: `core`, `api`, `web`
2. Configure TypeScript project references with `composite: true`
3. Set up `tsc --build` for incremental compilation
4. Add ESLint rules to prevent cross-boundary imports
5. Extract shared types into `core` with explicit exports
6. Configure Turborepo or Nx for build orchestration

### Exercise 6: Codemod to Enable Stricter Flags (Advanced)
**Objective:** Practice automated compiler flag upgrades
1. Take a project without `noUncheckedIndexedAccess`
2. Enable the flag and collect all errors
3. Write a jscodeshift or ts-morph codemod to add null checks at array index access
4. Apply the codemod and verify all errors are fixed
5. Run the test suite to confirm no regressions

---

## Connections to Other Domains

- **D-1 (Foundations):** Understanding structural typing and type erasure is essential for knowing what migration preserves vs. changes
- **D-2 (Strictness):** The strictness ratcheting pattern is the endgame of migration — progressively enabling flags
- **D-3 (Type Modeling):** Migrated code needs proper type models — discriminated unions, branded types replace loose JS objects
- **D-4 (Runtime Boundaries):** Contract tests and schema validation protect boundaries that migration can destabilize
- **D-8 (Tooling):** Editor ergonomics and CI gates are the feedback loops that make migration measurable
- **D-10 (Performance):** Project references and incremental builds from migration directly feed build engineering
- **D-12 (Team Practices):** Migration governance, code review during conversion, and anti-pattern prevention are team concerns

---

## Migration Plan Template (Copy-Paste Ready)

```markdown
# TypeScript Migration Plan — [Project Name]

## Current State
- Language: JavaScript (ES20XX)
- Files: XXX .js files, XXX .jsx files
- Test coverage: XX%
- Build tool: [Webpack/Vite/etc.]
- Package manager: [npm/yarn/pnpm]

## Phase 0: Setup (Day 1-2)
- [ ] Install typescript, @types/* packages
- [ ] Create tsconfig.json (allowJs: true, strict: false)
- [ ] Configure build tool for .ts/.tsx
- [ ] Verify build passes with zero TS files
- [ ] Measure baseline type-coverage: ___%

## Phase 1: Foundation (Week 1-2)
- [ ] Convert config files and constants
- [ ] Convert utility functions (leaf modules)
- [ ] Install missing @types/* packages
- [ ] Write .d.ts stubs for untyped dependencies
- [ ] New code policy: all new files must be .ts/.tsx
- [ ] Type coverage target: 30%

## Phase 2: Core (Week 3-6)
- [ ] Convert data models and domain types
- [ ] Convert API clients and service layers
- [ ] Convert shared hooks/utilities
- [ ] Set up contract tests for API boundaries
- [ ] Enable checkJs for remaining .js files
- [ ] Type coverage target: 60%

## Phase 3: Features (Week 7-12)
- [ ] Convert feature modules (prioritize high-churn)
- [ ] Run ts-migrate on remaining bulk files
- [ ] Track $TSFixMe / @ts-expect-error count: ___
- [ ] CI gate: type-coverage --at-least 70
- [ ] Type coverage target: 80%

## Phase 4: Strictness (Week 13+)
- [ ] Enable strict: true
- [ ] Enable noUncheckedIndexedAccess
- [ ] Burn down remaining $TSFixMe (target: <50)
- [ ] Remove allowJs: true
- [ ] Final type coverage target: 95%+

## Quality Gates
- [ ] All tests pass at each phase boundary
- [ ] Type coverage never decreases between PRs
- [ ] Zero new @ts-ignore (only @ts-expect-error)
- [ ] Contract tests pass for all API boundaries
```

---

*Research conducted March 2026. Sources verified against TypeScript 5.x documentation. All tools referenced are actively maintained as of research date.*
