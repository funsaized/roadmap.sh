# Type Modeling Patterns for Real Systems

## Overview

This domain covers the practical type modeling patterns that let TypeScript developers encode business rules, prevent impossible states, and build expressive API surfaces — all at compile time with zero runtime overhead. These patterns sit at the core of "making illegal states unrepresentable" and form the foundation for advanced domain modeling in production systems.

**Prerequisites:** D-1 (Foundations — unions, narrowing, structural typing) and D-2 (Strictness — strict mode enabled, compiler options understood).

**Feeds into:** D-5 (Generics in Practice), D-6 (React/Frontend Workflows), D-7 (Backend Workflows), D-9 (Refactoring), D-11 (Modern Features), D-12 (Team Practices).

**Estimated total time:** 20–30 hours of focused study and applied practice.

---

## Key Concepts

### 1. Discriminated Unions for State Workflows

**What it is:** A union type where each member shares a common "discriminant" property with a unique literal value. TypeScript uses this discriminant to narrow the type in switch/if branches.

**Why it matters:** Eliminates the "bag of optionals" anti-pattern where you represent multiple states with a single interface full of optional properties. Forces you to handle every state explicitly.

**Core mechanics:**
- Discriminant property (usually `type`, `status`, or `kind`) with string literal values
- Type narrowing via switch statements or conditional checks
- Exhaustiveness checking using the `never` type in default branches
- Avoiding impossible states (e.g., an `ErrorState` cannot have `data`, a `LoadingState` cannot have `error`)

**Pattern:**
```typescript
type RequestState =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: User[] }
  | { status: 'error'; error: Error };
```

**Connections:** Builds on union types and narrowing from D-1. Essential for React state modeling (D-6) and backend workflow patterns (D-7).

### 2. Exhaustiveness Checking

**What it is:** A compile-time technique ensuring every variant of a discriminated union is handled. Uses the `never` type to catch unhandled cases.

**Pattern:**
```typescript
function assertNever(x: never): never {
  throw new Error(`Unexpected value: ${x}`);
}
```

**Why it matters:** When you add a new variant to a union, the compiler flags every switch/if that doesn't handle it — catching bugs at compile time rather than runtime.

### 3. Branded (Opaque/Nominal) Types

**What it is:** A technique to create nominally distinct types from structurally identical primitives. Prevents accidental interchange of values like `UserId` and `OrderId` even though both are strings.

**Implementation approaches (ranked by robustness):**

1. **Unique symbol pattern (recommended):**
```typescript
declare const UserIdBrand: unique symbol;
type UserId = string & { readonly [UserIdBrand]: typeof UserIdBrand };
```

2. **Object literal brand:**
```typescript
type OrderId = number & { readonly __brand: 'OrderId' };
```

3. **Zod `.brand()` for schema-integrated branding**

**Key properties:**
- Zero runtime overhead (brands are erased at compile time)
- Requires constructor/factory functions to create branded values
- Cannot be accidentally bypassed without explicit `as` assertion

**Use cases:** IDs, units of measurement, validated strings (emails, URLs), boundary-safe values.

**Connections:** Pairs naturally with runtime validation (D-4) and API boundary patterns (D-7).

### 4. Built-in Utility Types

**What they are:** TypeScript ships with utility types that transform existing types. These are the workhorses of API surface design.

**Essential utility types:**
- `Partial<T>` — makes all properties optional
- `Required<T>` — makes all properties required
- `Readonly<T>` — makes all properties readonly
- `Pick<T, K>` — selects a subset of properties
- `Omit<T, K>` — excludes specific properties
- `Record<K, V>` — creates an object type with keys K and values V
- `Extract<T, U>` / `Exclude<T, U>` — filter union members
- `NonNullable<T>` — removes null and undefined
- `ReturnType<T>` — extracts function return type
- `Parameters<T>` — extracts function parameter types as a tuple
- `Awaited<T>` — unwraps Promise types

**Practical patterns:**
- `Omit<User, 'id' | 'createdAt'>` for create DTOs
- `Pick<User, 'name' | 'email'>` for display components
- `Partial<User>` for patch/update operations
- `Readonly<Config>` for immutable configuration objects

### 5. Mapped Types

**What they are:** Types that iterate over the keys of another type and transform each property. The mechanism behind most utility types.

**Syntax:**
```typescript
type Transform<T> = {
  [K in keyof T]: SomeTransformation<T[K]>;
};
```

**Key capabilities:**
- Adding/removing `readonly` modifier (`+readonly` / `-readonly`)
- Adding/removing optional modifier (`+?` / `-?`)
- Key remapping with `as` clause (TypeScript 4.1+)
- Key filtering by returning `never` in the `as` clause
- Combining with conditional types for property-level transformations

**Key remapping patterns:**
```typescript
// Prefix keys with "on" and capitalize
type Handlers<T> = {
  [K in keyof T as `on${Capitalize<string & K>}`]: (value: T[K]) => void;
};

// Filter to only string properties
type StringProps<T> = {
  [K in keyof T as T[K] extends string ? K : never]: T[K];
};
```

**Connections:** Foundation for template literal type patterns. Used heavily in framework type definitions (D-6, D-7).

### 6. Conditional Types

**What they are:** Types that select between two branches based on a type-level condition, using `extends` as the test.

**Syntax:** `T extends U ? TrueType : FalseType`

**Key mechanics:**
- Distribution over unions: conditional types applied to union types distribute across each member
- `infer` keyword: captures part of a type pattern for use in the true branch
- Nested conditionals for multi-branch logic (use sparingly)

**Essential `infer` patterns:**
- Extract return type: `T extends (...args: any[]) => infer R ? R : never`
- Extract promise value: `T extends Promise<infer U> ? U : T`
- Extract array element: `T extends (infer U)[] ? U : T`
- Extract function parameters: `T extends (...args: infer P) => any ? P : never`

**When to use vs. avoid:**
- USE when building reusable type utilities that need to adapt to input types
- AVOID deep conditional chains (>2–3 levels) that become unreadable
- AVOID when a simple union or overload would suffice

**Connections:** Powers many built-in utility types. Essential for generic abstractions (D-5). Can cause performance issues if overused (D-10).

### 7. Template Literal Types

**What they are:** Types that use backtick syntax to construct string types from other string literal types. Introduced in TypeScript 4.1.

**Core capabilities:**
- String concatenation at the type level
- Cross-product of string unions (each combination is generated)
- Intrinsic string manipulation: `Uppercase`, `Lowercase`, `Capitalize`, `Uncapitalize`
- Pattern matching with `infer` to extract parts of string types

**Practical patterns:**

**Route keys:**
```typescript
type ApiVersion = 'v1' | 'v2';
type Resource = 'users' | 'orders';
type Route = `/api/${ApiVersion}/${Resource}`;
// "/api/v1/users" | "/api/v1/orders" | "/api/v2/users" | "/api/v2/orders"
```

**Event names:**
```typescript
type Entity = 'user' | 'order';
type Action = 'created' | 'updated' | 'deleted';
type DomainEvent = `${Entity}.${Action}`;
// "user.created" | "user.updated" | ... (6 total)
```

**Feature flags:**
```typescript
type Feature = 'darkMode' | 'betaSearch';
type FeatureFlag = `feature.${Feature}.enabled`;
```

**Route parameter extraction:**
```typescript
type ExtractParams<T extends string> =
  T extends `${string}:${infer Param}/${infer Rest}`
    ? Param | ExtractParams<Rest>
    : T extends `${string}:${infer Param}`
    ? Param
    : never;
```

**Connections:** Combines with mapped types for powerful key remapping. Used in routing libraries, event systems, and API clients (D-6, D-7).

### 8. The `satisfies` Operator

**What it is:** TypeScript 4.9 introduced `satisfies` to validate that a value conforms to a type without widening its inferred type.

**Why it matters for type modeling:**
```typescript
const routes = {
  home: '/',
  about: '/about',
  user: '/user/:id',
} satisfies Record<string, string>;
// Type is preserved as { home: "/"; about: "/about"; user: "/user/:id" }
// NOT widened to Record<string, string>
```

**Use cases:** Configuration objects, lookup tables, enum-like constants where you want both type checking AND narrow inference.

### 9. Readonly and Immutable Patterns

**What it is:** Using `Readonly<T>`, `ReadonlyArray<T>`, `as const`, and deep readonly patterns to prevent mutation at the type level.

**Key patterns:**
- `as const` for literal inference on objects and arrays
- `Readonly<T>` for shallow immutability
- Deep readonly via recursive mapped types or libraries
- `ReadonlyMap` and `ReadonlySet` for collection immutability

### 10. Designing Types for Readability

**What it is:** Principles for keeping type definitions understandable by the team, avoiding over-engineering.

**Guidelines:**
- Name types after domain concepts, not implementation details
- Prefer discriminated unions over deeply nested generics
- Use intermediate type aliases to break complex types into readable steps
- Document non-obvious type patterns with comments
- Keep conditional type nesting to 2–3 levels max
- Use `satisfies` over `as` for value-level type checking

---

## Decision Framework: When to Use Each Pattern

| Pattern | Use When | Avoid When |
|---------|----------|------------|
| Discriminated unions | Modeling finite states, workflows, API responses | Only 2 simple variants (boolean may suffice) |
| Branded types | Multiple same-primitive IDs, units, validated strings | Single use, no confusion risk |
| Utility types (Pick/Omit) | Deriving API DTOs from domain types | Type has <3 properties (just write it) |
| Mapped types | Systematic transformation of all properties | One-off transformation (use Pick/Omit) |
| Conditional types | Reusable type utilities, generic abstractions | Simple cases where overloads work |
| Template literal types | Route keys, event names, feature flags, string patterns | Small, fixed sets (use plain union) |
| `satisfies` | Config objects, lookup tables, constants | Already using explicit type annotations |

**Rule of thumb:** If a teammate can't understand your type in 30 seconds, simplify it. Readability > cleverness.

---

## Learning Resources

### Official Documentation (Primary Sources)

1. **TypeScript Handbook — Narrowing**
   - URL: https://www.typescriptlang.org/docs/handbook/2/narrowing.html
   - Covers: Discriminated unions, type guards, exhaustiveness checking
   - Type: Documentation | Free | Updated with each TS release

2. **TypeScript Handbook — Mapped Types**
   - URL: https://www.typescriptlang.org/docs/handbook/2/mapped-types.html
   - Covers: Mapped type syntax, key remapping, modifier manipulation
   - Type: Documentation | Free

3. **TypeScript Handbook — Conditional Types**
   - URL: https://www.typescriptlang.org/docs/handbook/2/conditional-types.html
   - Covers: Conditional types, `infer`, distributive behavior
   - Type: Documentation | Free

4. **TypeScript Handbook — Template Literal Types**
   - URL: https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html
   - Covers: Template literal syntax, intrinsic string manipulation types
   - Type: Documentation | Free

5. **TypeScript Handbook — Utility Types Reference**
   - URL: https://www.typescriptlang.org/docs/handbook/utility-types.html
   - Covers: All built-in utility types with examples
   - Type: Documentation | Free

### Online Courses

6. **Total TypeScript — Type Transformations Workshop** (Matt Pocock)
   - URL: https://www.totaltypescript.com/workshops/type-transformations
   - Platform: Total TypeScript
   - Covers: 50+ exercises on unions, mapped types, conditional types, template literals
   - Duration: ~8–10 hours | Difficulty: Intermediate | Paid

7. **Total TypeScript — Advanced Patterns Workshop** (Matt Pocock)
   - URL: https://www.totaltypescript.com/workshops/advanced-typescript-patterns
   - Platform: Total TypeScript
   - Covers: Branded types, type predicates, advanced discriminated union patterns
   - Duration: ~6–8 hours | Difficulty: Advanced | Paid

8. **Execute Program — Advanced TypeScript**
   - URL: https://www.executeprogram.com/courses/advanced-typescript
   - Platform: Execute Program
   - Covers: Mapped types, conditional types, template literal types with spaced-repetition exercises
   - Duration: ~10 hours | Difficulty: Intermediate | Paid (free trial)

9. **Type-Level TypeScript** (Gabriel Vergnaud)
   - URL: https://type-level-typescript.com/
   - Platform: Self-hosted course
   - Covers: Type-level programming from basics to advanced, including all patterns in this domain
   - Duration: ~15 hours | Difficulty: Intermediate–Advanced | Free + Paid tiers

### Videos and Conference Talks

10. **"Discriminated Unions Are a Dev's Best Friend"** (Matt Pocock)
    - URL: https://www.totaltypescript.com/discriminated-unions-are-a-devs-best-friend
    - Covers: Practical discriminated union patterns with real examples
    - Duration: ~15 min | Free

11. **"Branded Types in TypeScript"** (Matt Pocock / Total TypeScript)
    - URL: https://www.totaltypescript.com/workshops/advanced-typescript-patterns/branded-types/what-is-a-branded-type
    - Covers: Branded type implementation patterns, use cases
    - Duration: ~20 min | Part of paid workshop (preview free)

12. **"Mapped Types in TypeScript"** (Dr. Axel Rauschmayer / 2ality)
    - URL: https://2ality.com/2025/02/mapped-types-typescript.html
    - Covers: Comprehensive mapped types guide with key remapping
    - Type: Long-form article | Free | Published Feb 2025

### Books

13. **Effective TypeScript, 2nd Edition** (Dan Vanderkam, O'Reilly 2024)
    - Relevant chapters: Chapter 6 (Generics and Type-Level Programming), Item 50 (Conditional Types vs Overloads)
    - Difficulty: Intermediate–Advanced
    - Notes: Authoritative, practical, updated for modern TypeScript

14. **Programming TypeScript** (Boris Cherny, O'Reilly 2019)
    - Relevant chapters: Chapter 6 (Advanced Types — conditional, mapped, branded types)
    - Difficulty: Intermediate
    - Notes: Foundational reference; some patterns slightly dated but concepts remain valid

15. **Learning TypeScript** (Josh Goldberg, O'Reilly 2022)
    - URL: https://www.learningtypescript.com/
    - Relevant chapters: Chapters on unions, type operations
    - Includes branded types article: https://www.learningtypescript.com/articles/branded-types
    - Difficulty: Beginner–Intermediate

### Interactive Exercises

16. **Type Challenges** (GitHub)
    - URL: https://github.com/type-challenges/type-challenges
    - Covers: 200+ type-level challenges from easy to extreme, including mapped types, conditional types, template literals
    - Format: Solve in TypeScript Playground or VS Code
    - Difficulty: Easy → Extreme | Free
    - Recommended challenges for this domain: Pick, Readonly, TupleToObject, First, Length, Exclude, Awaited, If, Concat, Push, Unshift (easy); Deep Readonly, Chainable Options, Last, Pop, Promise.all, Trim, Capitalize, Replace (medium)

17. **TypeScript Playground**
    - URL: https://www.typescriptlang.org/play
    - Use for: Experimenting with all patterns in this domain interactively
    - Free

18. **Codewars — TypeScript Type-Level Challenges**
    - URL: https://www.codewars.com/collections/ts-type-level-challenges
    - Format: Kata-style challenges | Free

### GitHub Repositories

19. **type-challenges/type-challenges**
    - URL: https://github.com/type-challenges/type-challenges
    - Stars: 45k+ | Active
    - Use for: Practicing mapped types, conditional types, template literal types

20. **type-challenges solutions by ghaiklor**
    - URL: https://ghaiklor.github.io/type-challenges-solutions/en/
    - Use for: Studying solutions and explanations after attempting challenges

### Community Resources

21. **r/typescript** (Reddit)
    - URL: https://www.reddit.com/r/typescript/
    - Use for: Discussing type modeling patterns, getting feedback on complex types

22. **TypeScript Discord**
    - URL: https://discord.gg/typescript
    - Use for: Real-time help with type modeling questions

23. **Stack Overflow — TypeScript Tags**
    - URL: https://stackoverflow.com/questions/tagged/typescript+mapped-types
    - URL: https://stackoverflow.com/questions/tagged/typescript+conditional-types
    - Use for: Finding solutions to specific type modeling problems

---

## Learning Path

### Phase 1: Discriminated Unions and State Modeling (4–5 hours)

**Concepts:** Discriminated unions, discriminant properties, type narrowing in switch/if, exhaustiveness checking with `never`, `assertNever` helper.

**Activities:**
1. Read TypeScript Handbook — Narrowing (discriminated unions section)
2. Watch Matt Pocock's "Discriminated Unions Are a Dev's Best Friend"
3. Practice: Model a shopping cart state machine (empty → hasItems → checkout → paid → shipped)
4. Practice: Model an HTTP request lifecycle (idle → loading → success → error → retrying)
5. Implement exhaustive switch handler with `assertNever`

**Milestone:** Can model any finite-state workflow with discriminated unions and handle all states exhaustively.

### Phase 2: Utility Types and Mapped Types (5–7 hours)

**Concepts:** Built-in utility types (Pick, Omit, Partial, Required, Readonly, Record, Extract, Exclude), custom mapped types, modifier manipulation (+/- readonly, +/- optional), key remapping with `as`.

**Activities:**
1. Read TypeScript Handbook — Mapped Types
2. Read TypeScript Handbook — Utility Types Reference
3. Study how Pick and Omit are implemented internally
4. Practice: Create DTOs from domain types (CreateUserDto, UpdateUserDto, UserSummary)
5. Practice: Build a `DeepPartial<T>` and `DeepReadonly<T>` type
6. Practice: Use key remapping to create event handler types from a data model
7. Complete Type Challenges: Pick, Readonly, TupleToObject, Omit (easy/medium)

**Milestone:** Can derive any API surface type from a domain model using utility and mapped types.

### Phase 3: Branded Types (3–4 hours)

**Concepts:** Nominal vs structural typing, unique symbol brand pattern, object literal brand pattern, factory functions for branded values, combining brands with runtime validation.

**Activities:**
1. Read the branded types article on learningtypescript.com
2. Read egghead.io branded types guide
3. Practice: Create branded types for UserId, OrderId, Email, and PositiveNumber
4. Practice: Build factory functions that validate and brand in one step
5. Practice: Integrate branded types into a domain model (Order with OrderId, UserId references)

**Milestone:** Can prevent ID/unit mix-ups across an entire codebase using branded types.

### Phase 4: Conditional Types and `infer` (4–6 hours)

**Concepts:** Conditional type syntax, `extends` as type-level predicate, `infer` keyword for type extraction, distributive conditional types, recursive conditional types.

**Activities:**
1. Read TypeScript Handbook — Conditional Types
2. Study implementations of ReturnType, Parameters, Awaited
3. Practice: Build UnwrapPromise, ArrayElement, FunctionReturnType from scratch
4. Practice: Create a `DeepAwaited<T>` recursive unwrapper
5. Complete Type Challenges: If, Awaited, ReturnType (easy/medium)
6. Advanced: Build a type that extracts all string-valued properties from an object

**Milestone:** Can build reusable type utilities using conditional types and `infer` without creating unreadable chains.

### Phase 5: Template Literal Types (3–4 hours)

**Concepts:** Template literal syntax at type level, cross-product of string unions, intrinsic string manipulation (Capitalize, Uppercase, etc.), pattern matching with `infer` in template literals, combining with mapped types.

**Activities:**
1. Read TypeScript Handbook — Template Literal Types
2. Practice: Create type-safe event name system (`entity.action` pattern)
3. Practice: Build type-safe route definitions with parameter extraction
4. Practice: Create feature flag types with `feature.${name}.enabled` pattern
5. Complete Type Challenges: Capitalize, Replace, Trim (medium)

**Milestone:** Can enforce string format constraints (routes, events, config keys) at compile time.

### Phase 6: Integration and Decision-Making (2–3 hours)

**Concepts:** `satisfies` operator, combining patterns, readability guidelines, when NOT to use advanced types, pattern selection decision framework.

**Activities:**
1. Review the decision framework table above
2. Practice: Refactor a real-world codebase module using appropriate patterns
3. Practice: Code review exercise — identify over-engineered vs under-typed code
4. Build a mini domain model combining discriminated unions + branded types + mapped types

**Milestone:** Can select the right type modeling pattern for any given situation and justify the choice.

---

## Practical Exercises

### Exercise 1: State Machine for Order Processing (Beginner)
Model an e-commerce order lifecycle: `draft → submitted → processing → shipped → delivered → cancelled`. Each state has different available data (draft has items, shipped has trackingNumber, cancelled has reason). Implement a `processOrder` function with exhaustive handling.

### Exercise 2: Type-Safe API DTOs (Intermediate)
Given a `User` domain type with 10+ properties, derive: `CreateUserRequest` (omit id, timestamps), `UpdateUserRequest` (partial, omit id), `UserSummary` (pick name, email, avatar), `UserListItem` (pick id, name, lastActive). All derived from a single source type.

### Exercise 3: Branded ID System (Intermediate)
Create a branded ID system for a multi-entity app (User, Order, Product, Comment). Build factory functions, ensure IDs can't be swapped, and create a generic `findById` function that's type-safe per entity.

### Exercise 4: Event System with Template Literals (Advanced)
Build a typed event emitter where event names follow `domain.entity.action` format. The emitter's `on` and `emit` methods should enforce valid event names AND correctly typed payloads per event.

### Exercise 5: Form State Machine (Advanced)
Model a multi-step form wizard with discriminated unions. Each step has different fields. Build types that enforce: step transitions are valid, form data accumulates across steps, final submission has all required fields. Combine with `satisfies` for step configuration.

### Exercise 6: API Response Transformer (Advanced)
Build a generic `ApiResponse<T>` type that wraps any data type. Create mapped type utilities to: make all nested dates into strings (for JSON serialization), strip internal-only fields, add pagination metadata. Chain these transformations.

---

## Connections to Other Domains

- **D-4 (Runtime Boundaries):** Branded types need runtime validation at boundaries. Schema libraries (Zod) can produce branded types.
- **D-5 (Generics):** Conditional types and mapped types are the building blocks of generic abstractions.
- **D-6 (React/Frontend):** Discriminated unions for component props, mapped types for form state, template literals for route typing.
- **D-7 (Backend):** Branded types for entity IDs, utility types for request/response DTOs, template literal types for event systems.
- **D-9 (Refactoring):** Type modeling patterns enable safe refactoring — changing a discriminated union forces updates everywhere.
- **D-11 (Modern Features):** `satisfies` (4.9), key remapping (4.1), template literal types (4.1) are relatively recent additions.
- **D-12 (Team Practices):** Decision framework for when to use each pattern; readability guidelines prevent type-level over-engineering.
