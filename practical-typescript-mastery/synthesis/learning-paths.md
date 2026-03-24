# Learning Paths — Practical TypeScript Mastery

## Overview

Four distinct learning paths through the roadmap, each targeting different goals and time budgets. All paths share the same foundation (D-1) and build upward through the dependency graph.

---

## Path 1: Quick Start (40-50 hours)

**Goal:** Practical TypeScript competence for immediate productivity gains. First wins within 10-15 hours.

**Target:** Developer who wants to stop fighting TypeScript and start leveraging it.

### Sequence

| Phase | Domain | Focus | Hours | Cumulative |
|-------|--------|-------|-------|-----------|
| 1 | D-1 | Core type system: unions, narrowing, discriminated unions, `any` vs `unknown` | 12-15 | 15 |
| 2 | D-2 | Enable `strict: true`, understand `noUncheckedIndexedAccess`, module resolution basics | 8-10 | 25 |
| 3 | D-3 | Discriminated unions for state, utility types (Pick/Omit/Partial), branded types intro | 10-12 | 37 |
| 4 | D-4 | Zod basics, schema-first validation at one API boundary | 6-8 | 45 |
| 5 | D-8 | `tsc --noEmit` in CI, VS Code essentials, typed linting basics | 5-6 | 50 |

### Key Resources
- R-11 Total TypeScript Beginner Tutorial (free)
- R-8 Effective TypeScript — Items 1-20
- R-39 TSConfig Cheat Sheet
- R-15 Total TypeScript Zod Tutorial (free)
- R-18 TypeScript Exercises

### Milestones
- **Hour 5:** Can explain structural typing and type erasure
- **Hour 12:** Can model API response with discriminated union + exhaustive handling
- **Hour 20:** Project configured with `strict: true` and `noUncheckedIndexedAccess`
- **Hour 35:** Can derive API DTOs from domain types using utility types
- **Hour 45:** One API boundary validated with Zod
- **Hour 50:** CI pipeline runs `tsc --noEmit` and typed ESLint

---

## Path 2: Standard (100-130 hours)

**Goal:** Full practical TypeScript proficiency for day-to-day development across frontend and backend.

**Target:** Developer building fullstack TypeScript applications who wants confidence in types, refactoring, and team conventions.

### Sequence

| Phase | Domain | Focus | Hours | Cumulative |
|-------|--------|-------|-------|-----------|
| 1 | D-1 | Complete foundations | 15-20 | 20 |
| 2 | D-2 | Full strictness + module resolution + project references | 12-15 | 35 |
| 3 | D-3 | All type modeling patterns | 15-20 | 55 |
| 4 | D-4 | Runtime boundaries, Zod/Valibot, contract testing intro | 12-15 | 70 |
| 5 | D-5 | Generics: constraints, inference, variance, golden rule | 12-15 | 85 |
| 6 | D-6 or D-7 | Choose frontend OR backend depth | 15-18 | 103 |
| 7 | D-8 | Full tooling: typed linting, type testing, CI pipelines | 10-12 | 115 |
| 8 | D-11 | Modern features awareness, upgrade playbook | 8-10 | 125 |

### Key Resources
- All Tier 1 resources from catalog
- R-12, R-13 Total TypeScript workshops (Type Transformations + Generics)
- R-14 or R-22 (React or Fastify depending on track)
- R-17 Type Challenges (easy + medium)

### Milestones
- **Hour 20:** Type system mental model solidified
- **Hour 55:** Can model any business domain with appropriate type patterns
- **Hour 70:** All API boundaries validated; schema-first pattern established
- **Hour 85:** Generic APIs designed with proper inference
- **Hour 115:** CI pipeline with type-checking, typed linting, type tests
- **Hour 125:** Can evaluate and adopt new TS features

---

## Path 3: Comprehensive (150-190 hours)

**Goal:** Complete mastery of all domains. Can lead TypeScript adoption, migration, and optimization for a team.

**Target:** Tech lead or senior developer responsible for TypeScript strategy.

### Sequence

| Phase | Domain | Focus | Hours | Cumulative |
|-------|--------|-------|-------|-----------|
| 1 | D-1 | Complete foundations | 15-20 | 20 |
| 2 | D-2 | Full strictness + module resolution + project references + layering | 15-18 | 38 |
| 3 | D-3 | All modeling patterns + readability principles | 18-22 | 60 |
| 4 | D-4 | Full runtime boundaries + contract testing | 18-22 | 82 |
| 5 | D-5 | Complete generics including variance and over-abstraction | 15-18 | 100 |
| 6 | D-6 | React/frontend workflows | 15-18 | 118 |
| 7 | D-7 | Backend workflows | 15-18 | 136 |
| 8 | D-8 | Full tooling mastery | 12-15 | 151 |
| 9 | D-9 | Refactoring and migration | 15-18 | 169 |
| 10 | D-11 | Modern features + upgrade management | 12-15 | 184 |

### Key Resources
- All Tier 1 and Tier 2 resources
- R-34 Execute Program
- R-35 Type-Level TypeScript
- R-46 TypeScript Migration to Modules case study
- R-47, R-54 Performance optimization resources

---

## Path 4: Expert (190-220 hours)

**Goal:** Mastery-level depth across all domains including performance engineering, migration at scale, and governance. Can architect TypeScript strategy for a large organization.

**Target:** Principal engineer or platform team lead.

### Sequence

Includes everything from Comprehensive, plus:

| Phase | Domain | Focus | Hours | Cumulative |
|-------|--------|-------|-------|-----------|
| 1-10 | D-1–D-9,D-11 | Comprehensive path | 150-184 | 184 |
| 11 | D-10 | Performance diagnostics, build engineering, benchmarking | 15-18 | 202 |
| 12 | D-12 | Team governance, anti-patterns, type quality standards | 8-10 | 212 |
| 13 | Capstone | Cross-domain integration project | 8-10 | 222 |

### Additional Resources
- R-4 TypeScript Performance Wiki (deep study)
- R-47 Gel optimization case study
- R-53 Anders Hejlsberg 10x Faster TypeScript talk
- R-58, R-59 ts-migrate + ts-morph (hands-on)

### Expert Milestones
- **Hour 202:** Can diagnose and fix type-check performance bottlenecks using `generateTrace`
- **Hour 212:** Can establish team type quality standards and review heuristics
- **Hour 222:** Completed a cross-domain capstone integrating migration, performance, and governance

---

## Path Comparison

| Aspect | Quick Start | Standard | Comprehensive | Expert |
|--------|------------|----------|---------------|--------|
| Hours | 40-50 | 100-130 | 150-190 | 190-220 |
| Domains | 5 | 8 | 10 | 11+ |
| First Win | Hour 12 | Hour 12 | Hour 12 | Hour 12 |
| Can Lead Migration | No | Partial | Yes | Yes |
| Can Optimize Builds | No | No | Partial | Yes |
| Can Set Team Standards | No | Partial | Yes | Yes |
| Recommended For | IC dev | Senior dev | Tech lead | Principal/Platform |

---

## Suggested Electives

After completing any path, explore based on role:

- **Frontend specialist:** D-6 deep dive → Polymorphic components, design system typing
- **Backend specialist:** D-7 deep dive → Prisma/Drizzle patterns, event-driven typing
- **Platform engineer:** D-10 deep dive → Build graph optimization, CI caching, TS 7 preparation
- **Migration lead:** D-9 deep dive → Codemod authoring, contract testing at scale
