# Tooling, Editor Ergonomics, and Developer Feedback Loops

## Overview

This domain covers the tooling ecosystem that makes TypeScript productive in practice: fast type-checking in CI, editor integration, typed linting, type-level testing, type coverage measurement, and incremental build strategies. Mastering this domain transforms TypeScript from "a language you write" into "a system that actively prevents mistakes and accelerates delivery."

**Prerequisites:** D-1 (Foundations), D-2 (Strictness and Compiler Configuration)
**Feeds into:** D-9 (Refactoring and Legacy Migration), D-10 (Performance and Build Engineering), D-12 (Team Practices and Governance)

**Difficulty Level:** Intermediate
**Estimated Total Time:** 15-20 hours

---

## Key Concepts

### 1. `tsc --noEmit` as a CI Type-Checking Gate

**What it is:** Running the TypeScript compiler without producing output files, purely to validate type correctness. This separates type-checking from JavaScript emission, allowing faster transpilers (esbuild, SWC) to handle the build while `tsc` ensures type safety.

**Why it matters:** Makes type-checking a fast, independent CI step. Teams can parallelize type-checking and building, catching type errors before merge without slowing down artifact generation.

**Key configuration:**
- `"noEmit": true` in tsconfig or via CLI flag
- Combine with `"skipLibCheck": true` for faster runs
- `"isolatedModules": true` when using external transpilers
- Add as a `"typecheck": "tsc --noEmit"` script in package.json

**Relation to other concepts:** Foundation for CI pipeline design; feeds into incremental builds and project references.

### 2. Incremental Builds and `.tsbuildinfo`

**What it is:** TypeScript's mechanism for caching compilation state between runs. When `"incremental": true` is set, TypeScript generates a `.tsbuildinfo` file storing the dependency graph and file hashes, so subsequent builds only reprocess changed files.

**Why it matters:** Dramatically reduces build times for large projects, both locally and in CI (when `.tsbuildinfo` is cached between runs).

**Key details:**
- Enabled automatically when `"composite": true` is set
- `.tsbuildinfo` file location configurable via `"tsBuildInfoFile"`
- Safe to delete; will be regenerated on next build
- Cache these files in CI for faster subsequent runs

**Relation to other concepts:** Prerequisite for project references; directly impacts CI pipeline speed.

### 3. Project References and `tsc --build`

**What it is:** A TypeScript feature for structuring large codebases (especially monorepos) into interconnected sub-projects. Each sub-project has its own `tsconfig.json` with `"composite": true`, and a root config lists `"references"` to sub-projects.

**Why it matters:** Enables partial rebuilds — only changed packages and their dependents are recompiled. Enforces module boundaries and prevents circular dependencies.

**Key details:**
- Compile with `tsc --build` (or `tsc -b`) instead of plain `tsc`
- Implicitly enables `"incremental"` and `"declaration"`
- Works with monorepo tools (Turborepo, Nx) for parallelization and caching
- `"declarationMap": true` enables cross-project "Go to Definition" in editors

**Relation to other concepts:** Builds on incremental builds; essential for D-10 (Performance and Build Engineering).

### 4. typescript-eslint Typed Linting

**What it is:** ESLint rules that leverage TypeScript's type information for deeper code analysis than syntax-only linting. Enabled via `@typescript-eslint/parser` with type-aware rule configurations.

**Why it matters:** Catches bugs that neither `tsc` nor basic ESLint rules can detect, such as floating promises, unsafe type assertions, unnecessary conditions, and incorrect await usage.

**Key components:**
- **`parserOptions.projectService`** (stable in v8, July 2024): Uses the same TypeScript APIs as VS Code; auto-finds nearest `tsconfig.json`; eliminates need for `tsconfig.eslint.json`
- **Performance considerations:** ~25% of lint time on type-aware parsing, ~70% on running rules; avoid `eslint-plugin-prettier` (runs Prettier per-file in ESLint)
- **Key typed rules:** `@typescript-eslint/no-floating-promises`, `@typescript-eslint/no-misused-promises`, `@typescript-eslint/strict-boolean-expressions`, `@typescript-eslint/no-unnecessary-condition`, `@typescript-eslint/await-thenable`
- **Profiling:** Use `TIMING=1 npx eslint .` to identify slow rules

**Relation to other concepts:** Depends on tsconfig setup; feeds into CI pipeline design and team governance practices.

### 5. VS Code TypeScript Editor Features

**What it is:** VS Code's built-in TypeScript language service provides rich editing features powered by the same compiler that runs `tsc`.

**Why it matters:** The editor is where developers spend most time. Mastering its TypeScript features directly reduces debugging time and improves refactoring confidence.

**Key features:**
- **Inlay hints:** Inline annotations showing inferred types, parameter names, return types. Configurable per category (`editor.inlayHints.enabled`). Interactive — Ctrl/Cmd+click navigates to definitions.
- **Go to Definition / Go to Type Definition:** Navigate to source or type declarations. Works across project references with `declarationMap`.
- **Rename Symbol (F2):** Type-safe rename across entire project, including imports and re-exports.
- **Quick Fixes:** Lightbulb suggestions for auto-imports, missing return types, implementing interfaces, adding missing properties.
- **Diagnostics panel (Ctrl+Shift+M):** Aggregated errors/warnings from `tsc`, prefixed with `[ts]`.
- **Organize Imports:** Auto-remove unused imports and sort remaining ones.
- **Extract to type/interface/function:** Refactoring actions for extracting repeated patterns.
- **TypeScript version selector:** Switch between workspace and bundled TS versions (bottom-right status bar).

**Key settings to configure:**
```json
{
  "typescript.preferences.importModuleSpecifier": "non-relative",
  "typescript.inlayHints.parameterNames.enabled": "literals",
  "typescript.inlayHints.variableTypes.enabled": true,
  "typescript.inlayHints.functionLikeReturnTypes.enabled": true,
  "editor.codeActionsOnSave": { "source.organizeImports": "explicit" }
}
```

**Relation to other concepts:** Directly uses the tsconfig and project references configuration; complemented by typed linting for additional diagnostics.

### 6. Type-Level Testing

**What it is:** Writing tests that verify type behavior at compile time — ensuring types accept correct values, reject incorrect ones, and produce expected output types. These tests run via `tsc` (not at runtime).

**Why it matters:** Critical for library authors and anyone maintaining shared type utilities. Prevents type regressions during refactoring. Catches cases where types silently become `any` or overly broad.

**Key tools:**

- **Vitest `expectTypeOf`** (recommended for projects already using Vitest): Built-in type testing via `expectTypeOf()` API. Tests in `*.test-d.ts` files. Analyzed statically by `tsc`.
  ```typescript
  import { expectTypeOf } from 'vitest'
  expectTypeOf(parseUser(raw)).toEqualTypeOf<User>()
  expectTypeOf<string>().not.toEqualTypeOf<number>()
  ```

- **expect-type** (standalone): The library bundled into Vitest. Can be used independently with any test runner. Operates purely at compile time.

- **tsd**: Specialized for testing `.d.ts` declaration files. Provides `expectType`, `expectError`, `expectAssignable`. Best for library authors publishing type definitions.

- **`@ts-expect-error`**: Basic but effective — asserts that the next line produces a TypeScript error. Useful for negative test cases.
  ```typescript
  // @ts-expect-error - string not assignable to number
  const x: number = "hello"
  ```

**Relation to other concepts:** Depends on understanding of type system (D-1, D-3); feeds into refactoring confidence (D-9) and team governance (D-12).

### 7. Type Coverage Tools

**What it is:** Tools that measure how completely a codebase is typed — specifically, what percentage of identifiers have explicit or inferred types vs. falling back to `any`.

**Why it matters:** Provides a quantitative metric for tracking migration progress (JS→TS) and enforcing type quality standards. Can be gated in CI to prevent regression.

**Key tools:**

- **type-coverage** (CLI): Calculates percentage of typed identifiers. Configurable threshold for CI gating. `npx type-coverage --detail --strict` shows each untyped identifier.

- **typescript-coverage-report**: Generates HTML reports from type-coverage data. Visual dashboard showing coverage per file. Inspired by Flow's coverage reporting.

- **Knip** (dead code detection): Comprehensive tool for finding unused files, exports, dependencies, and types. Successor to ts-prune (now maintenance-mode). Plugin support for 80+ frameworks. Essential for codebase hygiene.

- **ts-prune** (maintenance mode): Finds unused exports. Knip is the recommended replacement for new projects.

**Relation to other concepts:** Feeds into migration tracking (D-9) and team governance metrics (D-12).

### 8. CI Pipeline Design for TypeScript

**What it is:** Structuring CI workflows to maximize type safety feedback while minimizing pipeline duration.

**Why it matters:** Fast CI feedback loops encourage developers to keep types strict. Slow CI creates pressure to weaken type checks.

**Key patterns:**

- **Parallel stages:** Run `tsc --noEmit`, ESLint (typed), and tests concurrently
- **GitHub Actions example:**
  ```yaml
  jobs:
    typecheck:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-node@v4
        - run: npm ci
        - run: npm run typecheck
    lint:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-node@v4
        - run: npm ci
        - run: npm run lint
    test:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-node@v4
        - run: npm ci
        - run: npm run test
  ```
- **Cache strategies:** Cache `node_modules` and `.tsbuildinfo` files between runs
- **Monorepo optimization:** Use Turborepo/Nx to only typecheck affected packages
- **Type coverage gate:** Add `npx type-coverage --at-least 95` as a CI step

**Relation to other concepts:** Integrates all other concepts into a cohesive workflow.

### 9. Testing Stack Integration with TypeScript

**What it is:** Configuring test frameworks (Vitest, Jest) for strong type safety in test code itself, not just the code under test.

**Why it matters:** Test code is production code — it should benefit from TypeScript's type checking. Typed test helpers catch configuration errors and incorrect mock setups at compile time.

**Key considerations:**
- **Vitest:** First-class TypeScript support, no separate config needed, uses Vite's transform pipeline
- **Jest with ts-jest:** Requires `ts-jest` transformer configuration; `@types/jest` for type definitions
- **Type-safe mocks:** Use `vi.fn<Parameters<typeof fn>, ReturnType<typeof fn>>()` pattern
- **Separate tsconfig for tests:** Include test files, may relax certain strict options for test ergonomics

---

## Learning Resources

### Official Documentation (Primary Sources)

1. **TypeScript Handbook — Compiler Options Reference**
   - URL: https://www.typescriptlang.org/docs/handbook/compiler-options.html
   - Covers: All compiler flags including `noEmit`, `incremental`, `composite`, `skipLibCheck`
   - Type: Documentation | Free | Updated with each TS release

2. **TypeScript — Project References**
   - URL: https://www.typescriptlang.org/docs/handbook/project-references.html
   - Covers: Composite projects, `tsc --build`, solution-style tsconfigs
   - Type: Documentation | Free | Foundational reference

3. **typescript-eslint — Getting Started with Typed Linting**
   - URL: https://typescript-eslint.io/getting-started/typed-linting/
   - Covers: Setting up typed linting, projectService, configuration
   - Type: Documentation | Free | Updated for v8

4. **typescript-eslint — Typed Linting Performance Troubleshooting**
   - URL: https://typescript-eslint.io/troubleshooting/typed-linting/performance/
   - Covers: Diagnosing slow linting, TIMING profiling, common bottlenecks
   - Type: Documentation | Free

5. **typescript-eslint — Project Service Blog Post**
   - URL: https://typescript-eslint.io/blog/project-service/
   - Covers: How projectService works, migration from parserOptions.project
   - Type: Blog/Documentation | Free | 2024

6. **VS Code — TypeScript Editing Features**
   - URL: https://code.visualstudio.com/docs/typescript/typescript-editing
   - Covers: IntelliSense, inlay hints, refactoring, code navigation, diagnostics
   - Type: Documentation | Free

7. **VS Code — TypeScript Debugging**
   - URL: https://code.visualstudio.com/docs/typescript/typescript-debugging
   - Covers: Source map configuration, launch.json setup, breakpoint debugging
   - Type: Documentation | Free

8. **Vitest — Testing Types**
   - URL: https://vitest.dev/guide/testing-types
   - Covers: `expectTypeOf` API, `*.test-d.ts` files, type assertion patterns
   - Type: Documentation | Free

### Books

9. **Effective TypeScript (2nd Edition)** by Dan Vanderkam
   - Relevant chapters: Items on compiler configuration, editor integration, type coverage
   - Difficulty: Intermediate
   - Note: Dan Vanderkam authored the blog post introducing Knip for TypeScript type coverage
   - URL: https://effectivetypescript.com/

10. **Total TypeScript Essentials** by Matt Pocock
    - URL: https://www.totaltypescript.com/books/total-typescript-essentials
    - Relevant chapters: "TypeScript in the Development Pipeline" — covers tsc setup, CI integration, editor configuration
    - Difficulty: Beginner-Intermediate
    - Free online book

### Video Content

11. **Matt Pocock — Total TypeScript YouTube Channel**
    - URL: https://www.youtube.com/@maaborern (Total TypeScript)
    - Covers: Short, focused TypeScript tips including tooling, editor features, and configuration
    - Type: Video | Free | Ongoing series

12. **typescript-eslint v8 announcement / typed linting deep dive**
    - URL: https://typescript-eslint.io/blog/announcing-typescript-eslint-v8/
    - Covers: New features in v8, projectService, configuration changes
    - Type: Blog post | Free | July 2024

### Interactive Exercises and Tools

13. **tsd — Type Definition Testing Tool**
    - URL: https://github.com/tsdjs/tsd
    - Covers: Testing `.d.ts` files with `expectType`, `expectError`, `expectAssignable`
    - Type: Tool/GitHub repo | Free | 3.5k+ stars

14. **expect-type**
    - URL: https://github.com/mmkal/expect-type
    - Covers: Compile-time type assertions, bundled in Vitest
    - Type: Tool/GitHub repo | Free

15. **Knip — Dead Code Detector**
    - URL: https://knip.dev/
    - Covers: Unused files, exports, dependencies, types detection
    - Type: Tool | Free | Actively maintained, 80+ framework plugins

16. **type-coverage**
    - URL: https://github.com/nicolo-ribaudo/type-coverage (originally https://github.com/nicolo-ribaudo/type-coverage)
    - npm: `npx type-coverage`
    - Covers: Type coverage percentage, CI threshold gating
    - Type: Tool | Free

17. **typescript-coverage-report**
    - URL: https://github.com/alexcanessa/typescript-coverage-report
    - Covers: HTML reports for type coverage visualization
    - Type: Tool | Free

### Courses

18. **Total TypeScript — Pro Essentials Workshop**
    - URL: https://www.totaltypescript.com/
    - Covers: TypeScript configuration, tooling setup, editor integration as part of broader curriculum
    - Type: Online course | Paid | ~10 hours relevant content
    - Platform: totaltypescript.com

19. **CircleCI Blog — Enforce Type Safety with TypeScript Checks Before Deployments**
    - URL: https://circleci.com/blog/enforce-type-safety-with-typescript-checks-before-deployments/
    - Covers: Practical CI setup with tsc --noEmit
    - Type: Tutorial/Blog | Free

### Community Resources

20. **r/typescript subreddit**
    - URL: https://www.reddit.com/r/typescript/
    - Active community for TypeScript tooling discussions, performance troubleshooting

21. **TypeScript Discord**
    - URL: https://discord.gg/typescript
    - Official TypeScript community with channels for tooling and editor questions

### GitHub Repositories to Study

22. **typescript-eslint monorepo**
    - URL: https://github.com/typescript-eslint/typescript-eslint
    - Why: Study how a large TypeScript project configures its own linting, project references, and CI

23. **Turborepo examples**
    - URL: https://github.com/vercel/turborepo/tree/main/examples
    - Why: Reference implementations for monorepo TypeScript builds with caching

---

## Learning Path

### Phase 1: CI Type-Checking Foundations (3-4 hours)

**Concepts:** `tsc --noEmit`, CI pipeline setup, parallel stages
**Activities:**
1. Set up `"typecheck": "tsc --noEmit"` in a project
2. Configure a GitHub Actions workflow with parallel typecheck/lint/test jobs
3. Measure and compare CI times with and without `skipLibCheck`
4. Add type-checking as a pre-commit hook using lint-staged

**Milestone:** Working CI pipeline that catches type errors before merge

### Phase 2: Incremental Builds and Project References (3-4 hours)

**Concepts:** `.tsbuildinfo`, `incremental`, `composite`, `tsc --build`, project references
**Activities:**
1. Enable incremental builds in a single-package project; observe `.tsbuildinfo` generation
2. Split a medium project into 2-3 sub-projects with project references
3. Configure CI caching for `.tsbuildinfo` files
4. Measure rebuild times with and without incremental compilation

**Milestone:** Monorepo-style project with sub-second incremental rebuilds

### Phase 3: typescript-eslint Typed Linting (3-4 hours)

**Concepts:** Typed rules, projectService, performance profiling, rule selection
**Activities:**
1. Configure typescript-eslint with `parserOptions.projectService`
2. Enable key typed rules: `no-floating-promises`, `no-misused-promises`, `strict-boolean-expressions`
3. Run `TIMING=1 npx eslint .` to profile rule performance
4. Compare linting speed with and without typed rules; optimize configuration
5. Integrate typed linting into CI pipeline

**Milestone:** Typed ESLint rules running in CI catching real bugs, with acceptable performance

### Phase 4: VS Code Mastery (2-3 hours)

**Concepts:** Inlay hints, diagnostics, refactoring actions, workspace settings
**Activities:**
1. Configure inlay hints for parameter names and return types
2. Practice Rename Symbol (F2) across a multi-file project
3. Use "Go to Type Definition" vs "Go to Definition" to understand the difference
4. Set up workspace-specific TypeScript settings (`.vscode/settings.json`)
5. Learn keyboard shortcuts for Quick Fix, Organize Imports, and Problems panel

**Milestone:** Comfortable navigating and refactoring TypeScript code using editor features alone

### Phase 5: Type-Level Testing (2-3 hours)

**Concepts:** `expectTypeOf`, `@ts-expect-error`, tsd, test-d.ts files
**Activities:**
1. Write type tests for a utility type library using Vitest's `expectTypeOf`
2. Add `@ts-expect-error` tests for negative cases (values that should NOT type-check)
3. Set up tsd for testing exported type definitions
4. Add type tests to CI pipeline alongside runtime tests

**Milestone:** Type test suite that catches type regressions on every PR

### Phase 6: Type Coverage and Code Hygiene (2-3 hours)

**Concepts:** type-coverage, Knip, dead code detection, coverage thresholds
**Activities:**
1. Run `npx type-coverage --detail --strict` on a project; identify untyped areas
2. Generate an HTML coverage report with typescript-coverage-report
3. Set up Knip to find unused exports and dead code
4. Add type coverage threshold to CI (`type-coverage --at-least 90`)
5. Create a dashboard or tracking mechanism for type coverage over time

**Milestone:** Type coverage metric tracked in CI with a floor that prevents regression

---

## Practical Exercises

### Exercise 1: Build a Complete TypeScript CI Pipeline (Beginner)
**Goal:** Create a GitHub Actions workflow for a TypeScript project
**Tasks:**
- Parallel jobs: typecheck (`tsc --noEmit`), lint (typescript-eslint with typed rules), test (vitest)
- Cache `node_modules` and `.tsbuildinfo`
- Add type coverage threshold check
- Configure status checks to require all jobs pass before merge

### Exercise 2: Optimize a Slow Linting Setup (Intermediate)
**Goal:** Diagnose and fix performance issues in typed linting
**Tasks:**
- Start with a project using `parserOptions.project` pointing to tsconfig
- Profile with `TIMING=1`; identify the slowest rules
- Migrate to `parserOptions.projectService`
- Remove `eslint-plugin-prettier`; use Prettier separately
- Compare before/after timing; document the improvement

### Exercise 3: Add Type Testing to a Utility Library (Intermediate)
**Goal:** Write comprehensive type tests for shared type utilities
**Tasks:**
- Create a small utility library with `Pick`, `Omit` wrappers and branded types
- Write `expectTypeOf` tests verifying correct input/output types
- Write `@ts-expect-error` tests for invalid inputs
- Ensure type tests run in CI and fail on type regressions

### Exercise 4: Monorepo Build Optimization (Advanced)
**Goal:** Set up project references in a multi-package repository
**Tasks:**
- Structure 3 packages: `shared-types`, `api-server`, `web-client`
- Configure `composite: true` and project references
- Set up `tsc --build` with incremental compilation
- Integrate with Turborepo for cached, parallel builds
- Measure full rebuild vs incremental rebuild times

### Exercise 5: Type Coverage Improvement Sprint (Advanced)
**Goal:** Systematically improve type coverage from ~70% to ~95%
**Tasks:**
- Run type-coverage and generate baseline report
- Identify files with most `any` usage; categorize (intentional vs accidental)
- Create a burn-down plan with weekly targets
- Use Knip to remove dead code that inflates coverage denominator
- Set up CI gating at progressively higher thresholds

---

## Connections to Other Domains

| Domain | Connection |
|--------|-----------|
| D-1 (Foundations) | Understanding type inference is essential for interpreting inlay hints and type coverage reports |
| D-2 (Strictness) | Compiler configuration directly determines what `tsc --noEmit` checks and how strict linting rules behave |
| D-9 (Refactoring) | Type testing and coverage tools provide safety nets for large refactors; CI gates prevent regression |
| D-10 (Performance) | Incremental builds, project references, and build caching are the foundation of build performance optimization |
| D-12 (Team Practices) | Type coverage metrics, linting rule selection, and CI pipeline design are governance decisions that affect the whole team |

---

## Source Freshness Notes

- **typescript-eslint v8 / projectService:** Stable July 2024. Documentation current as of 2025.
- **Vitest type testing:** Stable feature, documented in current Vitest docs (v2.x+).
- **Knip:** Actively maintained (2024-2025), recommended over deprecated ts-prune.
- **TypeScript incremental/composite:** Stable since TS 3.4/3.0; documentation current.
- **VS Code TypeScript features:** Continuously updated with VS Code releases; docs reflect latest.
- **type-coverage:** Stable CLI tool; works with current TypeScript versions.
