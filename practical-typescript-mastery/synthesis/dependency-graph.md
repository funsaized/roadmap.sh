# Dependency Graph — Practical TypeScript Mastery

## Overview

This document defines the complete prerequisite dependency graph at both the domain level and the concept level. Edges are directional: `A → B` means "A is a prerequisite for B."

---

## Domain-Level Dependencies

```
D-1 (Foundations)
├── → D-2 (Strictness)
├── → D-3 (Type Modeling)
├── → D-4 (Runtime Boundaries)
├── → D-5 (Generics)
├── → D-6 (React/Frontend)
├── → D-7 (Backend)
├── → D-8 (Tooling)
├── → D-9 (Refactoring)
└── → D-11 (Modern Features)

D-2 (Strictness)
├── → D-3 (Type Modeling)
├── → D-4 (Runtime Boundaries)
├── → D-7 (Backend)
├── → D-8 (Tooling)
├── → D-9 (Refactoring)
├── → D-10 (Performance)
└── → D-11 (Modern Features)

D-3 (Type Modeling)
├── → D-5 (Generics)
├── → D-6 (React/Frontend)
├── → D-7 (Backend)
├── → D-9 (Refactoring)
├── → D-11 (Modern Features)
└── → D-12 (Team Practices)

D-4 (Runtime Boundaries)
├── → D-6 (React/Frontend)
├── → D-7 (Backend)
└── → D-9 (Refactoring)

D-5 (Generics)
├── → D-6 (React/Frontend)
├── → D-7 (Backend)
└── → D-12 (Team Practices)

D-8 (Tooling)
├── → D-9 (Refactoring)
├── → D-10 (Performance)
└── → D-12 (Team Practices)

D-9 (Refactoring)
├── → D-10 (Performance)
└── → D-12 (Team Practices)
```

### Domain Dependency Layers

```
Layer 0 (Foundation):    D-1
Layer 1 (Core Config):   D-2
Layer 2 (Modeling):      D-3, D-4, D-5
Layer 3 (Application):   D-6, D-7, D-8
Layer 4 (Scale):         D-9, D-11
Layer 5 (Optimization):  D-10
Layer 6 (Governance):    D-12
```

---

## Critical Concept-Level Dependencies

### Foundation Chain (Must complete in order)
```
Structural Typing (1.1)
  → Union Types (1.3) → Type Narrowing (1.5) → Discriminated Unions (1.6)
  → never Type (1.17) → Exhaustiveness Checking (3.2)

Type Erasure (1.2) → Compile-Time vs Runtime Boundary (4.1)
  → Trust Boundaries (4.2) → Schema Validation (4.6)

any Type (1.13) → unknown Type (1.16) → Safe Parsing (4.3)
```

### Strictness Chain
```
strict Flag Family (2.1)
  → noUncheckedIndexedAccess (2.5)
  → exactOptionalPropertyTypes (2.6)

Module Resolution (2.9) → verbatimModuleSyntax (2.10) → isolatedModules (2.11)
  → isolatedDeclarations (2.12)

Project References (2.13) → Incremental Builds (2.14)
  → Build Graph Optimization (10.6)
```

### Type Modeling Chain
```
Union Types (1.3) → Discriminated Unions (3.1)
  → State Workflow Modeling → React State (6.2, 6.6)
                            → Backend Events (7.6)

Utility Types (3.4) → Mapped Types (3.5) → Key Remapping (3.6)
  → Conditional Types (3.7) → infer Keyword (3.8)

Literal Types (1.7) → Template Literal Types (3.9)
  → Route/Event Name Typing (7.6)
```

### Generics Chain
```
Generic Parameters (5.1) → Constraints (5.2)
  → keyof with Generics (5.11) → Generic Utility Patterns (5.10)

Generic Inference (5.4) → Inference Failures (5.5)
  → Golden Rule (5.8) → Over-Abstraction (5.9)

Variance (5.6) → Explicit Annotations (5.7)
```

### Application Chains

**Frontend:**
```
Props Modeling (6.1) → Generic Components (6.4) → Polymorphic Components (6.7)
Props Modeling (6.1) → Custom Hooks (6.5) → E2E Type Safety (6.11)
Context API (6.6) → Compound Components (6.10)
```

**Backend:**
```
Typed Routes (7.1) → Middleware Augmentation (7.2)
Typed Routes (7.1) → Error Envelopes (7.3)
Typed Routes (7.1) → DB Integration (7.4, 7.5)
Generic Events (5.10) → Typed Event Systems (7.6)
Schema Validation (4.6) → tRPC/E2E Sharing (7.7)
```

### Tooling Chain
```
tsc --noEmit (8.1) → CI Pipeline Design (8.12) → Cache-Aware CI (10.7)
Typed Linting (8.4) → projectService (8.5)
Type Coverage (8.10) → any Debt Tracking (9.4)
Dead Code Detection (8.11) → Dead Code Elimination (9.13)
```

### Migration Chain
```
allowJs/checkJs (9.2) → Incremental Migration (9.1) → Strict Ratchet (2.16)
ts-migrate (9.5) → ts-morph (9.6)
Contract Tests (9.7) → Safe Refactoring (9.9)
Type Coverage (8.10) → any Burndown (9.4)
```

### Performance Chain
```
generateTrace (10.1) → analyze-trace (10.3) → Hot Files (10.5)
Expensive Types (10.4) → Mitigation Strategies
Project References (10.6) → Incremental Builds → Cache-Aware CI (10.7)
Emit Separation (10.8) → isolatedDeclarations (10.9)
Benchmarking (10.12) → Performance Budgets
```

---

## Circular Dependency Check

No circular dependencies exist in this graph. All edges are acyclic. The topological sort ordering matches the learning plan sequence (D-1 through D-12).

---

## Minimum Prerequisite Paths

### Path to "Can write production TypeScript safely" (Critical Path)
D-1 (15h) → D-2 (10h) → D-3 (15h) → D-4 (12h) → D-5 (10h)
**Total: ~62 hours**

### Path to "Can build fullstack apps with type safety"
Critical Path + D-6 (15h) + D-7 (15h) + D-8 (10h)
**Total: ~102 hours**

### Path to "Can lead TypeScript migration and optimization"
Full Path + D-9 (20h) + D-10 (12h) + D-11 (15h)
**Total: ~149 hours**
