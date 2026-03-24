# Knowledge Map — Practical TypeScript Mastery

## Overview

This knowledge map inventories **120 unique concepts** across 11 researched domains (D-1 through D-11), organized by domain with prerequisite links and difficulty ratings. Concepts that appear in multiple domains are listed once in their primary domain with cross-references noted.

---

## Section 1: Foundations (Beginner)

### Domain 1 — TypeScript Foundations and Type System Mental Model

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 1.1 | Structural Typing | Beginner | — | D-3 (branded types), D-5 (variance) |
| 1.2 | Type Erasure & Runtime Relationship | Beginner | — | D-4 (runtime boundaries) |
| 1.3 | Union Types | Beginner | — | D-3, D-5, D-6, D-7 |
| 1.4 | Intersection Types | Beginner | 1.3 | D-3, D-10 (perf) |
| 1.5 | Type Narrowing | Beginner | 1.3 | D-3, D-4, D-6 |
| 1.6 | Discriminated Unions | Beginner-Int | 1.3, 1.5 | D-3, D-6, D-7 |
| 1.7 | Literal Types & Literal Inference | Beginner | — | D-3 (template literals) |
| 1.8 | `as const` Assertion | Beginner | 1.7 | D-3, D-6 |
| 1.9 | Contextual Typing | Beginner | — | D-5 (generic inference) |
| 1.10 | Widening vs Narrowing | Beginner | 1.7, 1.9 | D-5 |
| 1.11 | Best Common Type Algorithm | Beginner | 1.3 | — |
| 1.12 | `type` vs `interface` Decision | Beginner | 1.3, 1.4 | D-10, D-12 |
| 1.13 | The `any` Type & `any` Leakage | Beginner | — | D-2, D-4, D-9 |
| 1.14 | Type Assertions (`as`) Dangers | Beginner | 1.13 | D-4 |
| 1.15 | Non-Null Assertion (`!`) | Beginner | — | D-2 |
| 1.16 | The `unknown` Type | Beginner | 1.13 | D-4, D-2 |
| 1.17 | The `never` Type | Beginner-Int | 1.6 | D-3, D-5 |

### Domain 2 — Strictness and Compiler Configuration

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 2.1 | `strict` Flag Family | Beginner-Int | D-1 | D-4, D-8 |
| 2.2 | `strictNullChecks` | Beginner-Int | 1.16 | D-4 |
| 2.3 | `noImplicitAny` | Beginner-Int | 1.13 | D-9 |
| 2.4 | `useUnknownInCatchVariables` | Beginner-Int | 1.16 | D-4 |
| 2.5 | `noUncheckedIndexedAccess` | Intermediate | 2.1 | D-4, D-6 |
| 2.6 | `exactOptionalPropertyTypes` | Intermediate | 2.1 | — |
| 2.7 | `noImplicitOverride` | Beginner-Int | 2.1 | — |
| 2.8 | Additional Safety Flags | Intermediate | 2.1 | — |
| 2.9 | Module Resolution (`NodeNext` vs `bundler`) | Intermediate | D-1 | D-7, D-11 |
| 2.10 | `verbatimModuleSyntax` | Intermediate | 2.9 | D-11 |
| 2.11 | `isolatedModules` | Intermediate | 2.9 | D-10 |
| 2.12 | `isolatedDeclarations` | Advanced | 2.11 | D-10 |
| 2.13 | Project References & `composite` | Intermediate | 2.9 | D-8, D-9, D-10 |
| 2.14 | Incremental Builds & `.tsbuildinfo` | Intermediate | 2.13 | D-8, D-10 |
| 2.15 | TSConfig Layering (`extends`) | Intermediate | 2.1, 2.9 | D-9 |
| 2.16 | Migration Strategy (Strict Ratchet) | Intermediate | 2.1 | D-9 |

---

## Section 2: Type System Depth (Intermediate)

### Domain 3 — Type Modeling Patterns for Real Systems

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 3.1 | Discriminated Unions for State Workflows | Intermediate | 1.6 | D-6, D-7 |
| 3.2 | Exhaustiveness Checking (`assertNever`) | Intermediate | 1.17, 3.1 | D-6, D-7 |
| 3.3 | Branded (Opaque/Nominal) Types | Intermediate | 1.1 | D-4, D-7 |
| 3.4 | Built-in Utility Types | Intermediate | 1.3, 1.4 | D-6, D-7 |
| 3.5 | Mapped Types | Intermediate | 3.4 | D-5, D-6 |
| 3.6 | Key Remapping (`as` in mapped types) | Intermediate | 3.5 | D-7 |
| 3.7 | Conditional Types | Intermediate-Adv | 3.5 | D-5, D-10 |
| 3.8 | `infer` Keyword | Intermediate-Adv | 3.7 | D-5 |
| 3.9 | Template Literal Types | Intermediate | 1.7, 3.5 | D-7 |
| 3.10 | `satisfies` Operator | Intermediate | 1.7, 1.8 | D-6, D-11 |
| 3.11 | Readonly & Immutable Patterns | Intermediate | 3.4 | D-6 |
| 3.12 | Type Readability Design Principles | Intermediate | 3.1–3.9 | D-12 |

### Domain 4 — Runtime Boundaries and Data Validation

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 4.1 | Compile-Time vs Runtime Safety Boundary | Intermediate | 1.2, 1.16 | D-7 |
| 4.2 | Trust Boundaries & "Parse, Don't Validate" | Intermediate | 4.1 | D-7 |
| 4.3 | Safe Parsing with `unknown` | Intermediate | 1.16 | D-7 |
| 4.4 | User-Defined Type Guards (`is`) | Intermediate | 1.5 | D-7 |
| 4.5 | Assertion Functions (`asserts`) | Intermediate | 4.4 | D-7 |
| 4.6 | Zod Schema Validation | Intermediate | 4.1 | D-6, D-7 |
| 4.7 | Valibot (Lightweight Alternative) | Intermediate | 4.6 | — |
| 4.8 | ArkType & TypeBox (Awareness) | Intermediate | 4.6 | — |
| 4.9 | Standard Schema Specification | Intermediate | 4.6 | — |
| 4.10 | Schema-First vs Type-First Approach | Intermediate | 4.6 | D-7 |
| 4.11 | Deriving Types from Schemas | Intermediate | 4.6 | D-6, D-7 |
| 4.12 | Safe Error Handling in Validation | Intermediate | 4.6 | D-7 |
| 4.13 | Contract Testing (Pact, OpenAPI) | Intermediate-Adv | 4.10 | D-7, D-9 |
| 4.14 | Discriminated Union Validation | Intermediate | 3.1, 4.6 | D-7 |
| 4.15 | Recursive & Composable Schemas | Intermediate-Adv | 4.6 | — |

### Domain 5 — Generics in Practice

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 5.1 | Generic Type Parameters | Intermediate | D-1 | D-6, D-7 |
| 5.2 | Generic Constraints (`extends`) | Intermediate | 5.1 | D-6, D-7 |
| 5.3 | Generic Default Parameters | Intermediate | 5.1 | — |
| 5.4 | Type Inference with Generics | Intermediate | 1.9, 5.1 | D-6 |
| 5.5 | Common Inference Failures & Fixes | Intermediate | 5.4 | — |
| 5.6 | Variance (Co/Contra/In/Bi) | Intermediate-Adv | 5.1, 1.1 | D-11 |
| 5.7 | Explicit Variance Annotations (`in`/`out`) | Intermediate-Adv | 5.6 | D-11 |
| 5.8 | Golden Rule of Generics | Intermediate | 5.1 | D-12 |
| 5.9 | Over-Abstraction Anti-Patterns | Intermediate | 5.8 | D-12 |
| 5.10 | Generic Utility Patterns (Emitters, Repos) | Intermediate | 5.2 | D-6, D-7 |
| 5.11 | `keyof` with Generics | Intermediate | 5.2, 3.5 | D-6 |
| 5.12 | Generic Classes and Interfaces | Intermediate | 5.1 | D-7 |

---

## Section 3: Application Workflows (Intermediate-Advanced)

### Domain 6 — TypeScript in React and Frontend Workflows

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 6.1 | Props Modeling Patterns | Intermediate | D-1, D-3 | — |
| 6.2 | Discriminated Union Props | Intermediate | 3.1, 6.1 | — |
| 6.3 | Extending HTML Element Props | Intermediate | 3.4, 6.1 | — |
| 6.4 | Generic Components | Intermediate-Adv | 5.1, 6.1 | — |
| 6.5 | Custom Hooks with TypeScript | Intermediate | 5.1, 6.1 | — |
| 6.6 | Context API Typing | Intermediate | 6.1, 4.4 | — |
| 6.7 | Polymorphic Components (`as` prop) | Advanced | 5.2, 6.3 | — |
| 6.8 | Event Typing | Intermediate | 1.9, 6.1 | — |
| 6.9 | Ref Typing & Forwarding | Intermediate | 5.1, 6.1 | — |
| 6.10 | Component Composition Patterns | Intermediate-Adv | 6.1, 5.1 | — |
| 6.11 | End-to-End API-to-UI Type Safety | Advanced | 4.6, 6.5, D-7 | D-7 |
| 6.12 | React 19 TypeScript Considerations | Intermediate-Adv | 6.9 | D-11 |

### Domain 7 — TypeScript in Node.js and Backend Workflows

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 7.1 | Typed Route Handlers | Intermediate | D-3, D-4 | — |
| 7.2 | Middleware Augmentation (Declaration Merging) | Intermediate | 7.1 | — |
| 7.3 | Error Envelope Patterns | Intermediate | 3.1, 7.1 | D-6 |
| 7.4 | Database Type Integration (Prisma) | Intermediate-Adv | 3.4, 7.1 | — |
| 7.5 | Database Type Integration (Drizzle) | Intermediate-Adv | 3.4, 7.1 | — |
| 7.6 | Typed Event Systems | Intermediate-Adv | 5.10, 3.9 | — |
| 7.7 | End-to-End Type Sharing (tRPC) | Advanced | 5.1, 4.6 | D-6 |
| 7.8 | End-to-End Type Sharing (Hono RPC) | Advanced | 7.7 | — |
| 7.9 | Node.js Module Configuration | Intermediate | 2.9 | — |
| 7.10 | Testing Backend TypeScript | Intermediate | 7.1 | D-8 |

---

## Section 4: Tooling and Operations (Intermediate-Advanced)

### Domain 8 — Tooling, Editor Ergonomics, and Developer Feedback Loops

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 8.1 | `tsc --noEmit` as CI Gate | Intermediate | 2.1 | D-10 |
| 8.2 | Incremental Builds & `.tsbuildinfo` | Intermediate | 2.14 | D-10 |
| 8.3 | Project References & `tsc --build` | Intermediate | 2.13 | D-10 |
| 8.4 | typescript-eslint Typed Linting | Intermediate | 2.1 | D-12 |
| 8.5 | `parserOptions.projectService` | Intermediate | 8.4 | — |
| 8.6 | VS Code TypeScript Features | Intermediate | D-1 | — |
| 8.7 | Inlay Hints Configuration | Beginner-Int | 8.6 | — |
| 8.8 | Rename Symbol & Refactoring Actions | Intermediate | 8.6 | D-9 |
| 8.9 | Type-Level Testing (expectTypeOf, tsd) | Intermediate-Adv | D-3 | D-9 |
| 8.10 | Type Coverage Tools (type-coverage) | Intermediate | D-1 | D-9 |
| 8.11 | Dead Code Detection (Knip) | Intermediate | — | D-9 |
| 8.12 | CI Pipeline Design for TypeScript | Intermediate | 8.1, 8.4 | D-10 |
| 8.13 | Testing Stack Integration (Vitest/Jest) | Intermediate | — | — |

---

## Section 5: Scale and Migration (Advanced)

### Domain 9 — Refactoring and Legacy Migration

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 9.1 | Incremental JS-to-TS Migration | Advanced | D-2, D-8 | — |
| 9.2 | `allowJs` and `checkJs` | Intermediate | 2.1 | — |
| 9.3 | `@ts-ignore` vs `@ts-expect-error` | Intermediate | — | — |
| 9.4 | `any` Debt Tracking & Burndown | Advanced | 1.13, 8.10 | — |
| 9.5 | Codemod Tools (ts-migrate, jscodeshift) | Advanced | — | — |
| 9.6 | ts-morph for Type-Aware Refactoring | Advanced | 9.5 | — |
| 9.7 | Contract Tests as Safety Nets | Advanced | 4.13 | — |
| 9.8 | Monorepo Migration Patterns | Advanced | 2.13 | D-10 |
| 9.9 | Safe Large Refactoring (Strangler Fig) | Advanced | 9.1 | — |
| 9.10 | Declaration Files & Type Stubs | Intermediate | D-1 | — |
| 9.11 | JSDoc-Based Typing (Pre-Migration) | Intermediate | 9.2 | — |
| 9.12 | Codemod-Assisted Compiler Upgrades | Advanced | 9.5 | D-11 |
| 9.13 | Dead Code Elimination | Intermediate | 8.11 | — |

### Domain 10 — Performance and Build Engineering

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 10.1 | `--generateTrace` Performance Diagnostics | Advanced | D-2 | — |
| 10.2 | `--extendedDiagnostics` | Intermediate-Adv | 10.1 | — |
| 10.3 | `@typescript/analyze-trace` Tool | Advanced | 10.1 | — |
| 10.4 | Expensive Type Patterns | Advanced | D-3, D-5 | — |
| 10.5 | Hot Files Identification | Advanced | 10.1 | — |
| 10.6 | Build Graph with Project References | Advanced | 2.13 | — |
| 10.7 | Cache-Aware CI Pipelines | Advanced | 8.12, 10.6 | — |
| 10.8 | Emit Separation (SWC/esbuild + tsc) | Advanced | 2.11 | — |
| 10.9 | `isolatedDeclarations` for Parallel Emit | Advanced | 2.12 | — |
| 10.10 | `skipLibCheck` Optimization | Intermediate | 2.1 | — |
| 10.11 | Monorepo Build Orchestration (Turborepo/Nx) | Advanced | 10.6 | — |
| 10.12 | Benchmarking Methodology (BAM Method) | Advanced | 10.1, 10.2 | — |
| 10.13 | Project Corsa / TypeScript 7 (Go Rewrite) | Awareness | — | D-11 |

---

## Section 6: Modern Features and Governance (Advanced-Expert)

### Domain 11 — Modern TypeScript Features and Upgrade Management

| # | Concept | Difficulty | Prerequisites | Cross-refs |
|---|---------|-----------|---------------|------------|
| 11.1 | TypeScript Release Cadence | Intermediate | — | — |
| 11.2 | TS 5.0 Key Features (Decorators, `const` params, `bundler`) | Intermediate | D-2 | — |
| 11.3 | `using` Declarations (5.2) | Intermediate | D-1 | — |
| 11.4 | `NoInfer<T>` (5.4) | Intermediate-Adv | D-5 | — |
| 11.5 | Inferred Type Predicates (5.5) | Intermediate | 4.4 | — |
| 11.6 | `--isolatedDeclarations` (5.5) | Advanced | 2.12 | D-10 |
| 11.7 | Iterator Helpers (5.6) | Intermediate | D-1 | — |
| 11.8 | `--noCheck` (5.6) | Intermediate | D-2 | D-10 |
| 11.9 | `--erasableSyntaxOnly` (5.8) | Intermediate | D-2 | — |
| 11.10 | TS 6.0 Bridge Release | Advanced | D-2 | — |
| 11.11 | TS 7.0 (Project Corsa) | Awareness | — | D-10 |
| 11.12 | Feature Evaluation Framework | Intermediate | — | D-12 |
| 11.13 | Upgrade Playbook | Advanced | 11.1 | D-9 |
| 11.14 | Breaking Change Management | Advanced | 11.13 | — |
| 11.15 | Team Communication for Upgrades | Intermediate | 11.12 | D-12 |
| 11.16 | Version Pinning & Dependency Coordination | Intermediate | — | — |

### Domain 12 — Team Practices, Governance, and Anti-Patterns (NOT YET RESEARCHED)

*Note: D-12 research has not been completed. The following concepts are referenced from other domains but not fully elaborated:*

- Code review heuristics for type quality
- "Type quality" standards definition
- When NOT to use advanced types
- Shared type utilities governance
- Anti-pattern catalog
- Generic complexity governance

---

## Total Concept Count: 120 unique concepts across 11 domains

## Cross-Cutting Themes

These themes thread across multiple domains:

1. **Runtime Boundary Safety** — D-1 (erasure), D-2 (strict flags), D-4 (validation), D-6 (API fetching), D-7 (request validation)
2. **Before/After Examples** — Present in D-1, D-2, D-3, D-4, D-9
3. **Incremental Adoption** — D-2 (strictness ratchet), D-9 (JS→TS migration), D-11 (feature adoption)
4. **Type Error Diagnosis** — D-1 (narrowing), D-5 (inference failures), D-10 (performance traces)
5. **Production Readiness** — D-2 (strict config), D-4 (validation), D-7 (error envelopes), D-8 (CI gates)
6. **Monorepo and Scale** — D-2 (project refs), D-8 (build optimization), D-9 (monorepo migration), D-10 (build engineering)
