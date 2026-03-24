# Cross-References — How Domains Relate and Reinforce Each Other

## Overview

This document maps the connections between domains, identifying reinforcement patterns, shared concepts, and integration points. These cross-references help learners understand how skills compound and where to revisit earlier concepts with deeper understanding.

---

## Cross-Domain Concept Bridges

### 1. Discriminated Unions (Bridge: D-1 → D-3 → D-4 → D-6 → D-7)

The single most cross-cutting pattern in the roadmap:
- **D-1:** Introduced as a union type pattern with type narrowing
- **D-3:** Applied to domain modeling (state machines, workflow states)
- **D-4:** Used in Zod's `z.discriminatedUnion()` for runtime validation
- **D-6:** Models React component props (mutually exclusive variants) and reducer actions
- **D-7:** Structures error envelopes, event payloads, and API responses

**Reinforcement:** Each domain deepens understanding. A developer who first learns discriminated unions in D-1 will recognize them as the natural pattern for state management in D-6 and error handling in D-7.

### 2. Type Erasure → Runtime Validation (Bridge: D-1 → D-4 → D-6 → D-7)

The fundamental insight that types disappear at runtime threads through the entire roadmap:
- **D-1:** Conceptual understanding of erasure
- **D-4:** Direct consequence — must validate at trust boundaries
- **D-6:** Frontend API response validation (Zod + TanStack Query)
- **D-7:** Backend request body validation (Zod middleware)

### 3. Generics (Bridge: D-5 → D-3 → D-6 → D-7)

Generic type parameters are the enabling mechanism for reusable type patterns:
- **D-5:** Core generic mechanics — constraints, inference, variance
- **D-3:** Generics power mapped types, conditional types, utility types
- **D-6:** Generic React components (`<List<T>>`), generic hooks (`useFetch<T>`)
- **D-7:** Generic repositories, typed event emitters, type providers

### 4. Project References (Bridge: D-2 → D-8 → D-9 → D-10)

The structural foundation for scaling TypeScript:
- **D-2:** Configuration — `composite`, `references`, `tsc --build`
- **D-8:** Tooling integration — CI with `tsc --build`, editor performance
- **D-9:** Monorepo migration patterns — package extraction, boundary enforcement
- **D-10:** Build graph optimization — incremental builds, cache-aware CI

### 5. Schema Validation (Bridge: D-4 → D-6 → D-7)

Zod (and alternatives) appear in three major application contexts:
- **D-4:** Core validation concepts, schema-first philosophy
- **D-6:** Form validation (React Hook Form + zodResolver), API response parsing
- **D-7:** Request body validation middleware, environment config validation

### 6. `any` Elimination (Bridge: D-1 → D-2 → D-9 → D-8)

Tracking and eliminating `any` is both a learning journey and a migration metric:
- **D-1:** Understanding why `any` is dangerous (leakage, false confidence)
- **D-2:** Strict flags that surface `any` (`noImplicitAny`)
- **D-9:** `any` debt tracking, `$TSFixMe` patterns, burndown metrics
- **D-8:** Type coverage tools, CI gates, Knip for dead code

---

## Domain Reinforcement Matrix

| Domain | Reinforces Understanding Of | By Providing |
|--------|---------------------------|--------------|
| D-2 (Strictness) | D-1 (any, unknown, nulls) | Compiler-enforced boundaries for concepts learned conceptually |
| D-3 (Modeling) | D-1 (unions, intersections) | Real-world application of foundational type constructs |
| D-4 (Boundaries) | D-1 (erasure), D-3 (discriminated unions) | Runtime manifestation of compile-time concepts |
| D-5 (Generics) | D-3 (mapped/conditional types) | Parameterized versions of static patterns |
| D-6 (React) | D-3, D-4, D-5 | Application-context for modeling, validation, and generics |
| D-7 (Backend) | D-3, D-4, D-5 | Server-context for the same patterns |
| D-8 (Tooling) | D-2 (config), D-1 (type system) | Automated enforcement of manual practices |
| D-9 (Migration) | D-2 (strictness), D-8 (tooling) | Progressive application of strictness using tooling |
| D-10 (Performance) | D-2 (config), D-3 (type patterns) | Performance consequences of configuration and pattern choices |
| D-11 (Features) | D-2, D-3 | New language features that simplify existing patterns |

---

## Feedback Loops Between Domains

### Loop 1: Model → Validate → Apply
```
D-3 (Model types) → D-4 (Validate at boundaries) → D-6/D-7 (Use in apps)
       ↑                                                      |
       └──────────── Refine models based on app needs ────────┘
```

### Loop 2: Configure → Check → Optimize
```
D-2 (Configure strictness) → D-8 (Enforce in CI) → D-10 (Optimize for speed)
       ↑                                                      |
       └─────── Adjust config based on perf constraints ──────┘
```

### Loop 3: Write → Migrate → Govern
```
D-1/D-3 (Write typed code) → D-9 (Migrate legacy code) → D-12 (Govern quality)
       ↑                                                         |
       └────────── Apply governance to new code ─────────────────┘
```

---

## When to Revisit Earlier Domains

| After Completing | Revisit | Why |
|-----------------|---------|-----|
| D-3 (Modeling) | D-1 (Foundations) | Deepens understanding of unions, narrowing with real modeling context |
| D-5 (Generics) | D-3 (Modeling) | Can now parameterize mapped/conditional types learned earlier |
| D-6 or D-7 (Apps) | D-4 (Boundaries) | Validation patterns become clearer with application context |
| D-9 (Migration) | D-2 (Strictness) | Strictness ratcheting is the endgame of migration |
| D-10 (Performance) | D-3, D-5 | Expensive type patterns become identifiable with diagnostic tools |
| D-11 (Features) | D-2, D-3 | New features often simplify or replace earlier patterns |

---

## Integration Scenarios

These scenarios span multiple domains and serve as practical integration exercises:

### Scenario 1: Type-Safe API Endpoint (D-3 + D-4 + D-7)
Define a domain model with discriminated unions, validate requests with Zod, return typed error envelopes.

### Scenario 2: React Feature with API Integration (D-3 + D-4 + D-5 + D-6)
Model state with discriminated unions, validate API responses with Zod, build generic hooks, render with typed components.

### Scenario 3: Monorepo Migration (D-2 + D-8 + D-9 + D-10)
Configure project references, set up CI with type coverage gates, migrate JS packages incrementally, optimize build performance.

### Scenario 4: Full-Stack Type Safety (D-4 + D-6 + D-7)
Share types between frontend and backend via tRPC or shared packages, validate at boundaries, maintain compile-time contracts.

### Scenario 5: Performance Investigation (D-2 + D-3 + D-10)
Use `generateTrace` to find expensive types, refactor using simpler patterns from D-3, measure improvement with BAM method.
