# Strictness and Compiler Configuration for Production Quality

## Overview

This domain covers the practical configuration of TypeScript's compiler for production-grade projects. It spans from enabling the `strict` flag family through adopting additional safety options, choosing correct module resolution strategies for modern stacks, leveraging project references for monorepo builds, and designing a tsconfig layering strategy that scales across teams and packages.

**Difficulty Level:** Beginner-Intermediate  
**Estimated Total Time:** 15–20 hours  
**Prerequisites:** D-1 (TypeScript Foundations and Type System Mental Model)  
**Downstream Dependencies:** D-3 (Type Modeling), D-4 (Runtime Boundaries), D-7 (Backend Workflows), D-8 (Tooling), D-9 (Refactoring), D-10 (Performance), D-11 (Modern Features)

---

## Key Concepts

### 1. The `strict` Flag Family

**What it is:** `"strict": true` is a meta-flag that enables eight individual strict-mode compiler options simultaneously. It is the single most impactful configuration change for code quality.

**Individual flags enabled by `strict: true`:**

| Flag | What It Does |
|------|-------------|
| `alwaysStrict` | Parses files in ECMAScript strict mode; emits `"use strict"` |
| `strictNullChecks` | Makes `null` and `undefined` distinct types, not assignable to everything |
| `strictBindCallApply` | Type-checks `bind`, `call`, and `apply` method arguments |
| `strictFunctionTypes` | Enforces contravariant function parameter checking |
| `strictPropertyInitialization` | Requires class properties to be initialized in constructor or at declaration |
| `noImplicitAny` | Errors when TypeScript cannot infer a type and would fall back to `any` |
| `noImplicitThis` | Errors when `this` has an implicit `any` type |
| `useUnknownInCatchVariables` | Types catch clause variables as `unknown` instead of `any` |

**Before/After Example — `strictNullChecks`:**

```typescript
// WITHOUT strictNullChecks — compiles but crashes at runtime
function getLength(arr?: string[]) {
  return arr.length; // No error! But arr could be undefined → runtime crash
}

// WITH strictNullChecks — caught at compile time
function getLength(arr?: string[]) {
  return arr.length; // Error: Object is possibly 'undefined'
}
// Fix:
function getLength(arr?: string[]) {
  return arr?.length ?? 0;
}
```

**Before/After Example — `noImplicitAny`:**

```typescript
// WITHOUT noImplicitAny — silent any leakage
function process(data) { // 'data' implicitly has 'any' type
  return data.foo.bar; // No type safety at all
}

// WITH noImplicitAny — forces annotation
function process(data: { foo: { bar: string } }) {
  return data.foo.bar; // Fully typed
}
```

**Before/After Example — `useUnknownInCatchVariables`:**

```typescript
// WITHOUT — catch variable is 'any', no safety
try { ... } catch (err) {
  console.log(err.message); // No error, but err might not have .message
}

// WITH — catch variable is 'unknown', must narrow
try { ... } catch (err) {
  if (err instanceof Error) {
    console.log(err.message); // Safe
  }
}
```

**Relationship to other concepts:** This is the foundation. All other safety flags build on top of `strict: true`. Module resolution and project references are orthogonal but combined in the same tsconfig file.

---

### 2. Additional Safety Flags (Beyond `strict`)

These flags are NOT enabled by `strict: true` but are highly recommended for production codebases. They should be adopted incrementally.

#### `noUncheckedIndexedAccess`
Adds `| undefined` to any indexed access (array elements, object index signatures). Prevents the most common source of "Cannot read properties of undefined" runtime errors.

**Before/After:**
```typescript
// WITHOUT
const users: string[] = [];
const first = users[0]; // Type: string — WRONG, it's undefined!
first.toUpperCase(); // Runtime crash

// WITH
const users: string[] = [];
const first = users[0]; // Type: string | undefined — CORRECT
first?.toUpperCase(); // Must handle undefined
```

**Adoption note:** This flag generates many new errors in existing codebases. Adopt after `strict: true` is stable. Use optional chaining (`?.`) and nullish coalescing (`??`) to fix.

#### `exactOptionalPropertyTypes`
Distinguishes between "property is absent" and "property is explicitly `undefined`." With this flag, `prop?: T` means the property can be omitted OR present with type `T`, but cannot be explicitly set to `undefined` unless `| undefined` is in the type.

**Before/After:**
```typescript
interface Config {
  theme?: "dark" | "light";
}

// WITHOUT — both are allowed
const a: Config = { theme: undefined }; // OK but semantically wrong
const b: Config = {}; // OK

// WITH — explicit undefined is an error
const a: Config = { theme: undefined }; // Error!
const b: Config = {}; // OK
// To allow undefined: theme?: "dark" | "light" | undefined
```

#### `noImplicitOverride`
Requires the `override` keyword when a subclass method overrides a base class method. Catches accidental overrides and renames.

#### `noFallthroughCasesInSwitch`
Reports errors for switch cases that fall through without `break`, `return`, or `throw`.

#### `noPropertyAccessFromIndexSignature`
Forces bracket notation (`obj["key"]`) when accessing properties from index signatures, making it clear the property may not exist.

#### `noImplicitReturns`
Ensures all code paths in a function return a value when a return type is specified.

**Recommended Adoption Order:**
1. `strict: true` (the foundation — adopt first)
2. `noUncheckedIndexedAccess` (highest ROI additional flag)
3. `noImplicitOverride` (low noise, easy to adopt)
4. `noFallthroughCasesInSwitch` (low noise)
5. `noImplicitReturns` (moderate noise)
6. `exactOptionalPropertyTypes` (highest noise — adopt last)
7. `noPropertyAccessFromIndexSignature` (optional, depends on team preference)

---

### 3. Module Resolution for Modern Stacks

**Core distinction:** `module` controls what JavaScript module syntax TypeScript emits. `moduleResolution` controls how TypeScript finds files referenced by imports.

#### `moduleResolution: "NodeNext"`
- Mirrors Node.js's native ESM + CJS resolution algorithm
- **Requires explicit file extensions** in relative imports (e.g., `import { foo } from './utils.js'`)
- Understands `package.json` `exports` and `imports` fields
- Best for: Node.js applications, libraries targeting Node.js
- Paired with `module: "NodeNext"`

#### `moduleResolution: "bundler"`
- Designed for webpack, Rollup, Vite, esbuild workflows
- Does NOT require file extensions in imports
- Supports `package.json` `exports` and `imports`
- Paired with `module: "esnext"` or `module: "preserve"`
- Best for: Frontend apps, apps using bundlers
- **Caution:** Code configured with `bundler` resolution may not work in Node.js without a bundler

#### Decision Matrix

| Scenario | `module` | `moduleResolution` |
|----------|----------|--------------------|
| Node.js app (no bundler) | `"NodeNext"` | `"NodeNext"` |
| Frontend app with bundler | `"esnext"` or `"preserve"` | `"bundler"` |
| Library for npm (Node.js consumers) | `"NodeNext"` | `"NodeNext"` |
| Library for npm (bundler consumers) | `"NodeNext"` | `"NodeNext"` |
| Next.js / Remix / Vite app | `"esnext"` or `"preserve"` | `"bundler"` |

#### Related Module Options

- **`verbatimModuleSyntax`** (TS 5.0+): Preserves import/export statements as written. Forces use of `import type` for type-only imports. Replaces deprecated `importsNotUsedAsValues` and `preserveValueImports`. **Highly recommended for all projects.**
- **`isolatedModules`**: Ensures each file can be transpiled independently. Required for esbuild, SWC, Babel workflows. Prevents use of `const enum` across files and namespace merging.
- **`isolatedDeclarations`** (TS 5.5+): Ensures `.d.ts` files can be generated without full type-checking. Requires explicit return type annotations on exports. Important for library authors and large monorepos.
- **`esModuleInterop`**: Fixes default import compatibility between CJS and ESM.
- **`moduleDetection: "force"`**: Treats all files as modules. Prevents "cannot redeclare block-scoped variable" errors.

#### ESM/CJS Interoperability

Key concepts for library authors:
- `.mjs` / `.cjs` file extensions for explicit module format
- `package.json` `"type": "module"` or `"type": "commonjs"`
- `package.json` `"exports"` field for conditional exports (ESM vs CJS entry points)
- Dual-package publishing strategies

---

### 4. Project References and Incremental Builds

**Project references** allow breaking a large TypeScript codebase into smaller, independently compilable units. Essential for monorepos.

#### Key Configuration

```json
// packages/shared/tsconfig.json
{
  "compilerOptions": {
    "composite": true,       // Required for referenced projects
    "declaration": true,     // Generates .d.ts files
    "declarationMap": true,  // Enables go-to-definition into source
    "outDir": "./dist"
  },
  "include": ["src/**/*.ts"]
}

// packages/api/tsconfig.json
{
  "compilerOptions": {
    "composite": true,
    "outDir": "./dist"
  },
  "references": [
    { "path": "../shared" }  // Declares dependency
  ],
  "include": ["src/**/*.ts"]
}

// Root tsconfig.json (orchestrator)
{
  "files": [],
  "references": [
    { "path": "packages/shared" },
    { "path": "packages/api" },
    { "path": "packages/web" }
  ]
}
```

#### How `tsc --build` Works
1. Reads the dependency graph from `references`
2. Determines which projects are out-of-date using `.tsbuildinfo` files
3. Builds only changed projects in correct dependency order
4. Generates `.d.ts` files that downstream projects consume

#### Key Flags
- **`composite: true`**: Required for any project that is referenced. Implicitly enables `declaration` and `incremental`.
- **`incremental: true`**: Generates `.tsbuildinfo` cache files for faster subsequent builds. Implied by `composite`.
- **`tsBuildInfoFile`**: Custom location for the `.tsbuildinfo` file.
- **`declarationMap: true`**: Generates source maps for `.d.ts` files, enabling IDE go-to-definition to jump to source instead of declarations.
- **`disableReferencedProjectLoad`**: Prevents loading all referenced projects at startup (useful for very large monorepos).

#### Benefits
- Faster rebuilds (only changed packages recompile)
- Enforced dependency boundaries (packages can't import from non-declared dependencies)
- Better IDE performance (loads only relevant project parts)
- Parallelizable builds (independent packages can build concurrently)

---

### 5. TSConfig Layering Strategy

A well-designed layering strategy reduces duplication, ensures consistency, and allows per-package customization.

#### The `extends` Property
- `compilerOptions` are **merged** (child overrides parent for same keys)
- `files`, `include`, `exclude` are **overwritten entirely** (not merged!)
- Relative paths resolve from the file that declares them, not from the base

#### Recommended Layer Architecture

```
monorepo/
├── tsconfig.base.json          # Shared compiler options
├── tsconfig.json               # Root orchestrator (references only)
├── packages/
│   ├── shared/
│   │   ├── tsconfig.json       # Extends base, adds composite + references
│   │   └── tsconfig.build.json # Build-specific (stricter, emit)
│   ├── api/
│   │   ├── tsconfig.json       # Extends base, Node.js specific
│   │   └── tsconfig.build.json
│   └── web/
│       ├── tsconfig.json       # Extends base, DOM + React specific
│       └── tsconfig.build.json
```

#### Template: Base Configuration

```json
// tsconfig.base.json — shared across all packages
{
  "compilerOptions": {
    // Strictness
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,

    // Module
    "moduleDetection": "force",
    "isolatedModules": true,
    "verbatimModuleSyntax": true,

    // Interop
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "allowJs": true,

    // Output
    "target": "es2022",
    "skipLibCheck": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  }
}
```

#### Template: Node.js Package

```json
// packages/api/tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "rootDir": "./src",
    "composite": true,
    "lib": ["es2022"]
  },
  "include": ["src/**/*.ts"],
  "exclude": ["**/*.test.ts", "**/*.spec.ts"],
  "references": [
    { "path": "../shared" }
  ]
}
```

#### Template: Frontend/React Package

```json
// packages/web/tsconfig.json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "module": "esnext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "noEmit": true,
    "lib": ["es2022", "dom", "dom.iterable"]
  },
  "include": ["src/**/*.ts", "src/**/*.tsx"],
  "references": [
    { "path": "../shared" }
  ]
}
```

#### Template: Test Configuration Override

```json
// packages/api/tsconfig.test.json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "composite": false,
    "noEmit": true,
    "rootDir": "."
  },
  "include": ["src/**/*.ts", "test/**/*.ts"]
}
```

#### Community Base Packages
- **`@tsconfig/bases`** (GitHub: [tsconfig/bases](https://github.com/tsconfig/bases)): Community-maintained presets for Node.js LTS, React, Next.js, Deno, Bun, etc.
- **`@total-typescript/tsconfig`** (GitHub: [total-typescript/tsconfig](https://github.com/total-typescript/tsconfig)): Matt Pocock's opinionated recommended config.

#### Debugging Configuration
- Run `tsc --showConfig` in any directory to see the fully resolved configuration after inheritance.
- Run `tsc --listFiles` to see which files TypeScript will process.

---

### 6. Migration Strategy for Existing Projects

For teams adopting strictness incrementally:

1. **Start with `strict: true`** on a new project or branch
2. Use `// @ts-expect-error` temporarily for known issues (NOT `// @ts-ignore`)
3. Track `@ts-expect-error` count as a metric — burn it down over sprints
4. **Incremental flag adoption** for legacy codebases:
   - Week 1–2: Enable `noImplicitAny` (usually the largest batch of errors)
   - Week 3–4: Enable `strictNullChecks` (second largest batch)
   - Week 5+: Enable remaining `strict` sub-flags one at a time
   - After `strict` is stable: Add `noUncheckedIndexedAccess`
5. Use `tsc --noEmit` in CI to catch regressions without affecting the build

---

## Learning Resources

### Documentation and Reference (Primary Sources)

1. **TSConfig Reference** — Official TypeScript documentation  
   URL: https://www.typescriptlang.org/tsconfig/  
   Coverage: Complete reference for every compiler option with examples  
   Freshness: Continuously updated with each TypeScript release  
   *This is the single most important reference for this domain.*

2. **TypeScript Handbook — Modules Theory**  
   URL: https://www.typescriptlang.org/docs/handbook/modules/theory.html  
   Coverage: Deep explanation of module resolution algorithms, ESM/CJS theory  
   Freshness: Updated for TS 5.x module resolution modes

3. **TypeScript Handbook — Choosing Compiler Options**  
   URL: https://www.typescriptlang.org/docs/handbook/modules/guides/choosing-compiler-options.html  
   Coverage: Decision guide for module and moduleResolution settings  
   Freshness: Current for TS 5.x

4. **TypeScript Project References Documentation**  
   URL: https://www.typescriptlang.org/docs/handbook/project-references.html  
   Coverage: Official guide to project references, composite, and tsc --build  
   Freshness: Stable, foundational reference

5. **TypeScript Handbook — tsconfig.json**  
   URL: https://www.typescriptlang.org/docs/handbook/tsconfig-json.html  
   Coverage: How tsconfig files work, extends, file inclusion  
   Freshness: Current

### Online Courses

6. **Total TypeScript — TypeScript Pro Essentials** (Matt Pocock)  
   URL: https://www.totaltypescript.com/workshops/typescript-pro-essentials  
   Platform: Total TypeScript  
   Cost: Paid (part of Pro subscription)  
   Relevant section: "Configuring TypeScript" module  
   Coverage: tsconfig options, module resolution, strict mode  
   Difficulty: Beginner-Intermediate  
   *Best-in-class for practical TypeScript configuration understanding.*

7. **Total TypeScript — Free Book: Essentials**  
   URL: https://www.totaltypescript.com/books/total-typescript-essentials/configuring-typescript  
   Platform: Total TypeScript (free)  
   Coverage: Configuration chapter with practical guidance  
   Difficulty: Beginner-Intermediate

8. **Learn TypeScript — Strictness Module**  
   URL: https://learntypescript.dev/11/l6-strictness/  
   Platform: learntypescript.dev  
   Cost: Free  
   Coverage: Interactive lessons on strict mode flags  
   Difficulty: Beginner

### Video Tutorials and Talks

9. **Matt Pocock — "TSConfig Cheat Sheet" (YouTube)**  
   URL: https://www.youtube.com/watch?v=bLch4GHjRcM  
   Duration: ~15 minutes  
   Coverage: Walkthrough of essential tsconfig options  
   Freshness: 2024

10. **Matt Pocock — "noUncheckedIndexedAccess" (Total TypeScript Tips)**  
    URL: https://www.totaltypescript.com/tips/make-accessing-objects-safer-by-enabling-nouncheckedindexedaccess-in-tsconfig  
    Format: Short video tip  
    Coverage: Why and how to enable this critical safety flag

11. **Theo Browne — "Stop Using TypeScript Without These Settings"**  
    URL: https://www.youtube.com/results?search_query=theo+typescript+strict+settings  
    Platform: YouTube  
    Coverage: Practical walkthrough of production tsconfig settings  
    Freshness: 2024

12. **BetterStack Guide — TypeScript Module Resolution**  
    URL: https://betterstack.com/community/guides/scaling-nodejs/typescript-module-resolution/  
    Format: Written tutorial with diagrams  
    Coverage: NodeNext vs bundler resolution, ESM/CJS interop  
    Freshness: 2024

### Books

13. **"Effective TypeScript" by Dan Vanderkam** (2nd Edition, 2024)  
    Publisher: O'Reilly  
    Relevant chapters: Items on compiler configuration, strict mode, type safety  
    Difficulty: Intermediate  
    *The 2nd edition was updated for TypeScript 5.x and modern module resolution.*

14. **"Programming TypeScript" by Boris Cherny**  
    Publisher: O'Reilly  
    Relevant chapters: Chapter on compiler options and project setup  
    Difficulty: Beginner-Intermediate

15. **"TypeScript in 50 Lessons" by Stefan Baumgartner**  
    Publisher: Smashing Magazine  
    Relevant sections: Configuration and strictness lessons  
    Difficulty: Beginner-Intermediate  
    URL: https://typescript-book.com/

### GitHub Repositories and Tools

16. **tsconfig/bases** — Community TSConfig presets  
    URL: https://github.com/tsconfig/bases  
    Stars: 3k+  
    What it demonstrates: Curated tsconfig presets for Node.js, React, Next.js, Deno, Bun  
    Usage: `npm install @tsconfig/strictest` then extend in your tsconfig

17. **total-typescript/tsconfig** — Matt Pocock's recommended config  
    URL: https://github.com/total-typescript/tsconfig  
    What it demonstrates: Opinionated production-ready tsconfig  
    Usage: `npm install @total-typescript/tsconfig` then extend

18. **Nx Monorepo** — TypeScript project references at scale  
    URL: https://nx.dev/blog/managing-ts-packages-in-monorepos  
    Coverage: How Nx manages TypeScript project references in large monorepos  
    Freshness: 2024

19. **Moonrepo Guide — TypeScript Project References**  
    URL: https://moonrepo.dev/docs/guides/javascript/typescript-project-refs  
    Coverage: Step-by-step guide to setting up project references  
    Freshness: 2024

### Articles and Guides

20. **Matt Pocock — "The TSConfig Cheat Sheet"**  
    URL: https://www.totaltypescript.com/tsconfig-cheat-sheet  
    Coverage: Concise recommendations for all essential tsconfig options  
    Freshness: Updated April 2024  
    *Start here for a quick overview before diving into official docs.*

21. **Dr. Axel Rauschmayer — "tsconfig.json"** (2ality)  
    URL: https://2ality.com/2025/01/tsconfig-json.html  
    Coverage: Deep technical explanation of tsconfig options  
    Freshness: January 2025

22. **BetterStack — "TypeScript strict Option"**  
    URL: https://betterstack.com/community/guides/scaling-nodejs/typescript-strict-option/  
    Coverage: Detailed walkthrough of strict mode and migration strategies  
    Freshness: 2024

23. **whatislove.dev — "The Strictest TypeScript Config"**  
    URL: https://whatislove.dev/articles/the-strictest-typescript-config/  
    Coverage: Maximum strictness configuration with all flags explained  
    Freshness: 2024

### Community Resources

24. **r/typescript** (Reddit)  
    URL: https://www.reddit.com/r/typescript/  
    Relevant threads on strict configuration, module resolution debates

25. **TypeScript Discord**  
    URL: https://discord.gg/typescript  
    Active community for configuration questions

26. **Stack Overflow — [typescript] [tsconfig]**  
    URL: https://stackoverflow.com/questions/tagged/typescript+tsconfig.json  
    Best for: Specific configuration problem-solving

---

## Learning Path

### Phase 1: Strict Mode Foundation (3–4 hours)
**Concepts:** `strict: true`, individual strict sub-flags, before/after examples  
**Activities:**
1. Read the TSConfig cheat sheet (https://www.totaltypescript.com/tsconfig-cheat-sheet) — 30 min
2. Read official TSConfig reference for strict-family flags — 1 hour
3. Exercise: Take an existing JS/TS project, enable `strict: true`, fix all errors — 2 hours

**Milestone:** Can explain what each strict sub-flag does and fix common errors it surfaces.

### Phase 2: Additional Safety Flags (2–3 hours)
**Concepts:** `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `noImplicitOverride`, `noFallthroughCasesInSwitch`  
**Activities:**
1. Read TSConfig reference for each additional flag — 1 hour
2. Exercise: Enable `noUncheckedIndexedAccess` in the same project, fix errors — 1.5 hours
3. Read the "Strictest TypeScript Config" article — 30 min

**Milestone:** Can configure and explain the full strictness ladder from `strict: true` through all additional flags.

### Phase 3: Module Resolution (3–4 hours)
**Concepts:** `module`, `moduleResolution`, NodeNext vs bundler, ESM/CJS interop, `verbatimModuleSyntax`, `isolatedModules`  
**Activities:**
1. Read official Modules Theory handbook page — 1 hour
2. Read official "Choosing Compiler Options" guide — 30 min
3. Read BetterStack module resolution guide — 45 min
4. Exercise: Set up a project with `module: "NodeNext"` and explicit file extensions — 1.5 hours
5. Exercise: Configure a frontend project with `moduleResolution: "bundler"` — 1 hour

**Milestone:** Can choose correct module/moduleResolution for any project type and explain ESM/CJS interop.

### Phase 4: Project References and Incremental Builds (3–4 hours)
**Concepts:** `composite`, `references`, `tsc --build`, `.tsbuildinfo`, `declaration`, `declarationMap`  
**Activities:**
1. Read official Project References documentation — 1 hour
2. Read Moonrepo or Nx guide on project references — 45 min
3. Exercise: Set up a 3-package monorepo with project references — 2 hours
4. Measure build times with and without incremental builds

**Milestone:** Can configure and build a multi-package monorepo using `tsc --build`.

### Phase 5: TSConfig Layering and Templates (2–3 hours)
**Concepts:** `extends`, layering patterns, base/package/test configs, `@tsconfig/bases`, `tsc --showConfig`  
**Activities:**
1. Read official extends documentation — 30 min
2. Review `@tsconfig/bases` and `@total-typescript/tsconfig` repos — 30 min
3. Exercise: Design a tsconfig layering strategy for the monorepo from Phase 4 — 1.5 hours
4. Verify with `tsc --showConfig` that inheritance resolves correctly

**Milestone:** Can design and debug a multi-layer tsconfig strategy for a real project.

---

## Practical Exercises

### Exercise 1: Strict Mode Audit (Beginner)
**Goal:** Enable `strict: true` in an existing project and fix all type errors.  
**Steps:**
1. Clone any open-source TS project that doesn't use strict mode
2. Enable `"strict": true` in tsconfig.json
3. Run `tsc --noEmit` and categorize errors by type
4. Fix all errors, documenting before/after patterns
5. **Success criteria:** Zero type errors with strict enabled

### Exercise 2: Safety Flag Ladder (Beginner-Intermediate)
**Goal:** Incrementally adopt additional safety flags.  
**Steps:**
1. Starting from a project with `strict: true`, add `noUncheckedIndexedAccess`
2. Fix all new errors using optional chaining and explicit checks
3. Add `noImplicitOverride`, `noFallthroughCasesInSwitch`, `noImplicitReturns`
4. Finally add `exactOptionalPropertyTypes`
5. Document the error count at each stage

### Exercise 3: Module Resolution Configuration (Intermediate)
**Goal:** Configure a dual-output library that works in both ESM and CJS.  
**Steps:**
1. Create a small TypeScript library with 3-4 exported functions
2. Configure `module: "NodeNext"`, `moduleResolution: "NodeNext"`
3. Set up `package.json` with `"exports"` field for ESM and CJS
4. Build and verify the library works when consumed by both ESM and CJS consumers
5. Enable `verbatimModuleSyntax` and fix any import issues

### Exercise 4: Monorepo with Project References (Intermediate)
**Goal:** Build a working monorepo with incremental builds.  
**Steps:**
1. Create a monorepo with 3 packages: `shared`, `api`, `web`
2. Configure `composite: true` and `references` in each package
3. Create a root `tsconfig.json` with all references
4. Create a `tsconfig.base.json` with shared compiler options
5. Run `tsc --build` and verify incremental builds work
6. Modify one file in `shared` and verify only `shared` + dependents rebuild
7. **Success criteria:** `tsc --build` completes in under 2 seconds for incremental rebuilds

### Exercise 5: TSConfig Layering (Intermediate)
**Goal:** Design a complete tsconfig layering strategy.  
**Steps:**
1. Using the monorepo from Exercise 4, create:
   - `tsconfig.base.json` (shared options)
   - Per-package `tsconfig.json` (extends base)
   - Per-package `tsconfig.build.json` (emit-specific)
   - Per-package `tsconfig.test.json` (test-specific)
2. Verify each configuration with `tsc --showConfig`
3. Set up CI to use `tsconfig.build.json` for builds and `tsconfig.json` for IDE
4. Document the layering strategy in a README

### Exercise 6: Migration Simulation (Advanced)
**Goal:** Practice migrating a non-strict codebase to full strictness.  
**Steps:**
1. Start with a project that has `strict: false` and uses `any` liberally
2. Create a migration plan with phases
3. Use `// @ts-expect-error` to temporarily suppress known issues
4. Track `@ts-expect-error` count as a burndown metric
5. Complete migration to `strict: true` + `noUncheckedIndexedAccess`
6. Document the migration playbook for team reuse

---

## Connections to Other Domains

- **→ D-3 (Type Modeling):** Strict configuration is prerequisite. Many type modeling patterns only work correctly with `strictNullChecks` and `strict` enabled.
- **→ D-4 (Runtime Boundaries):** `useUnknownInCatchVariables` and `noUncheckedIndexedAccess` directly affect runtime boundary patterns.
- **→ D-7 (Backend Workflows):** Module resolution (`NodeNext`) is essential for Node.js backend projects.
- **→ D-8 (Tooling):** `tsc --noEmit` in CI, incremental builds, and project references are core tooling topics.
- **→ D-9 (Refactoring):** Migration strategies from this domain feed directly into refactoring and legacy migration.
- **→ D-10 (Performance):** Project references, incremental builds, and `isolatedDeclarations` are performance optimization levers.
- **→ D-11 (Modern Features):** `verbatimModuleSyntax`, `isolatedDeclarations`, and new strict flags are tracked through TypeScript releases.

---

## TSConfig Templates Reference

### Minimal Strict App (no emit — using bundler/transpiler)
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "target": "es2022",
    "module": "preserve",
    "moduleResolution": "bundler",
    "noEmit": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "moduleDetection": "force",
    "lib": ["es2022", "dom", "dom.iterable"]
  }
}
```

### Node.js Application
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "target": "es2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "dist",
    "rootDir": "src",
    "sourceMap": true,
    "declaration": true,
    "isolatedModules": true,
    "verbatimModuleSyntax": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "lib": ["es2022"]
  },
  "include": ["src/**/*.ts"],
  "exclude": ["**/*.test.ts"]
}
```

### Library Package (monorepo)
```json
{
  "extends": "../../tsconfig.base.json",
  "compilerOptions": {
    "composite": true,
    "outDir": "dist",
    "rootDir": "src",
    "declaration": true,
    "declarationMap": true
  },
  "include": ["src/**/*.ts"]
}
```

### Maximum Strictness (all safety flags)
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "noFallthroughCasesInSwitch": true,
    "noImplicitReturns": true,
    "noPropertyAccessFromIndexSignature": true,
    "allowUnreachableCode": false,
    "allowUnusedLabels": false
  }
}
```

---

*Research conducted: March 2025. Sources verified against TypeScript 5.7/5.8 documentation. Module resolution guidance reflects Node.js 20+ LTS and modern bundler ecosystem.*
