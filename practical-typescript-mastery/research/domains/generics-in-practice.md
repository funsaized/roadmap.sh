# Generics in Practice

## Overview

This domain covers the practical use of TypeScript generics — the language feature that enables writing reusable, type-safe code that works across multiple data types while preserving type information. Generics are often cited as the hardest part of TypeScript to master, but the difficulty usually comes from over-abstraction rather than inherent complexity. This research focuses on practical proficiency: writing generic functions with appropriate constraints, understanding inference behavior, recognizing variance implications, and knowing when generics help versus when they hurt.

**Prerequisites from prior domains:**
- D-1: Type system fundamentals (union types, intersection types, type narrowing)
- D-3: Type modeling patterns (discriminated unions, mapped types, conditional types)

**Feeds into downstream domains:**
- D-6: TypeScript in React (generic component props, hooks with generics)
- D-7: TypeScript in Node.js/Backend (generic repository patterns, middleware typing)
- D-12: Team Practices and Anti-Patterns (generic complexity governance)

---

## Key Concepts

### 1. Generic Type Parameters
A type variable (conventionally `T`, `U`, `K`, `V`) that acts as a placeholder for a type specified later. Generics allow functions, classes, interfaces, and type aliases to operate on multiple types without losing type information.

```typescript
function identity<T>(arg: T): T { return arg; }
```

### 2. Generic Constraints (`extends`)
Limiting what types a generic parameter can accept using the `extends` keyword. Constraints ensure generic code can safely access specific properties or methods.

```typescript
function getLength<T extends { length: number }>(item: T): number {
  return item.length;
}
```

**Key patterns:**
- Constraining by shape: `T extends { id: string }`
- Constraining by another parameter: `K extends keyof T`
- Constraining by union: `T extends string | number`

### 3. Generic Default Parameters
Assigning a fallback type when no explicit type argument is provided and inference cannot determine the type. Defaults make generic APIs more ergonomic for common cases.

```typescript
interface ApiResponse<T = unknown> {
  data: T;
  status: number;
}
```

**Rules:** Required parameters before defaults. Inference from arguments takes priority over defaults.

### 4. Type Inference with Generics
TypeScript's ability to automatically deduce generic type arguments from the values passed to a function. Good generic design maximizes inference so callers rarely need to specify type arguments explicitly.

```typescript
// T inferred as "hello" (string literal type)
const result = identity("hello");
```

### 5. Common Inference Failures and Fixes

**Failure: Widening to union types** — When TypeScript infers a generic as a union of possible types rather than narrowing to a specific one. Fix: use function overloads or conditional types.

**Failure: Callback argument inference** — TypeScript can struggle to infer generics passed through callback functions. Fix: explicitly annotate the callback parameter or restructure the API.

**Failure: Nested generics resolving to `unknown`** — Deep generic nesting can cause inference to give up. Fix: introduce intermediate helper functions or explicit type arguments.

**Failure: Object property inference** — When an object with function properties is passed to a generic, TypeScript may default to the constraint instead of the inferred type. Fix: use `satisfies` operator or split the call.

**General fixes:**
- Provide explicit type arguments at the call site
- Use helper/builder functions to guide inference
- Simplify generic signatures (fewer type parameters)
- Use `as const` to preserve literal types

### 6. Variance (Covariance, Contravariance, Invariance, Bivariance)

Variance describes how subtyping relationships between simple types (e.g., `Dog extends Animal`) translate to subtyping relationships between generic types (e.g., `Box<Dog>` vs `Box<Animal>`).

**Covariance (output positions):** If `Dog extends Animal`, then `Producer<Dog>` is assignable to `Producer<Animal>`. Applies to return types and readonly properties. Safe because you only read values out.

**Contravariance (input positions):** If `Dog extends Animal`, then `Consumer<Animal>` is assignable to `Consumer<Dog>`. Applies to function parameters (with `strictFunctionTypes`). Safe because a handler of any Animal can certainly handle a Dog.

**Invariance (both positions):** When a type parameter appears in both input and output positions, no subtyping relationship exists. Mutable containers should be invariant.

**Bivariance (TypeScript's historical compromise):** Method parameters were historically bivariant. The `strictFunctionTypes` flag fixes this for function-typed properties but not for method shorthand syntax.

### 7. Explicit Variance Annotations (`in` / `out`, TypeScript 4.7+)

TypeScript 4.7 introduced `in` and `out` modifiers for generic type parameters to explicitly declare variance intent:

```typescript
interface Producer<out T> { get(): T; }       // covariant
interface Consumer<in T> { accept(v: T): void; } // contravariant
interface Mutable<in out T> { get(): T; set(v: T): void; } // invariant
```

Benefits: clearer intent, faster type-checking in large codebases, compiler-enforced variance correctness.

### 8. The Golden Rule of Generics

From Dan Vanderkam's *Effective TypeScript*: **A type parameter should appear at least twice in a function signature.** If it only appears once, it's not relating multiple values and is probably unnecessary.

```typescript
// BAD: T appears only once — just use string
function greet<T extends string>(name: T): void { ... }

// GOOD: T relates input to output
function first<T>(arr: T[]): T | undefined { return arr[0]; }
```

### 9. Over-Abstraction Anti-Patterns

Common signs of over-engineered generics:
- **Single-use generics** — Generic used in exactly one place
- **"Single-letter soup"** — `<T, U, V, W, X>` with no descriptive names
- **"Do-everything type"** — One type parameter representing input, output, and state
- **Unnecessary wrapping** — `MyWrapper<T>` that adds no value over `T` itself
- **Generic where union suffices** — Using `<T extends A | B>` when `param: A | B` would work

**When generics help:** Libraries/utilities consumed with many different types, relating input types to output types, building type-safe APIs with inference.

**When generics hurt:** One-off functions, types that don't relate multiple values, situations where concrete types or simple unions are clearer.

### 10. Generic Utility Patterns

Practical patterns that appear frequently in production TypeScript:

- **Generic data fetching:** `async function fetchData<T>(url: string): Promise<T>`
- **Generic repository/CRUD:** `interface Repository<T> { find(id: string): T; save(entity: T): void; }`
- **Generic event emitters:** `class EventEmitter<Events extends Record<string, any>> { emit<K extends keyof Events>(event: K, payload: Events[K]): void; }`
- **Generic builder/factory:** Functions that return configured instances with preserved types
- **Constrained identity (passthrough) functions:** For inference guidance, e.g., `defineConfig<T extends Config>(config: T): T`

### 11. `keyof` with Generics

Combining `keyof` with generic constraints to create type-safe property access:

```typescript
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}
```

This pattern is foundational for typed object utilities and appears throughout TypeScript's built-in utility types (`Pick`, `Omit`, `Record`).

### 12. The `infer` Keyword in Conditional Types

Used within conditional types to extract/unpack types from generic structures:

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type ElementType<T> = T extends (infer E)[] ? E : never;
```

Understanding `infer` is essential for building custom utility types and for reading library type definitions.

### 13. Generic Classes and Interfaces

Applying generics to class and interface definitions for reusable data structures:

```typescript
class Stack<T> {
  private items: T[] = [];
  push(item: T): void { this.items.push(item); }
  pop(): T | undefined { return this.items.pop(); }
}
```

---

## Learning Resources

### Online Courses

1. **Total TypeScript — TypeScript Generics Workshop** (Matt Pocock)
   - URL: https://www.totaltypescript.com/workshops/typescript-generics
   - Platform: Total TypeScript
   - Duration: ~4-6 hours (dozens of exercises)
   - Difficulty: Intermediate
   - Cost: Paid (part of TypeScript Pro bundle)
   - Why: The single best focused course on generics. Exercise-driven, covers constraints, inference, and real-world patterns.

2. **Execute Program — Advanced TypeScript (Generics & Constraints)**
   - URL: https://www.executeprogram.com/courses/advanced-typescript
   - Platform: Execute Program
   - Duration: ~3-4 hours (spaced repetition format)
   - Difficulty: Intermediate
   - Cost: Paid subscription
   - Why: Interactive, spaced-repetition approach ensures retention. Covers keyof constraints, conditional types with generics.

3. **DevChallenges — TypeScript Generics**
   - URL: https://devchallenges.io/learn/3-javascript/typescript-generics
   - Platform: DevChallenges
   - Duration: ~1-2 hours
   - Difficulty: Beginner-Intermediate
   - Cost: Free
   - Why: Accessible interactive introduction with hands-on challenges.

### Video Tutorials

4. **Matt Pocock — "TypeScript Generics in 3 Easy Patterns"** (YouTube)
   - URL: https://www.totaltypescript.com/typescript-generics-in-three-easy-patterns
   - Duration: ~15 minutes
   - Difficulty: Beginner-Intermediate
   - Why: Breaks generics into three mental models — passing types to types, passing types to functions, inferring from arguments.

5. **Matt Pocock — "Generics: When You Know and When to Use Them"** (YouTube)
   - URL: https://www.youtube.com/watch?v=lMfGp29Ht8c
   - Duration: ~12 minutes
   - Difficulty: Intermediate
   - Why: Focuses specifically on when generics help vs. hurt, addressing over-abstraction.

6. **Dmitri Pavlutin — "Covariance and Contravariance in TypeScript"**
   - URL: https://dmitripavlutin.com/typescript-covariance-contravariance/
   - Format: Written tutorial with diagrams
   - Difficulty: Intermediate-Advanced
   - Why: Clearest practical explanation of variance with TypeScript-specific examples.

### Books

7. **Effective TypeScript, 2nd Edition** — Dan Vanderkam
   - Publisher: O'Reilly, 2024
   - Relevant: Chapter 6 "Generics and Type-Level Programming"
   - Difficulty: Intermediate-Advanced
   - Why: Contains the "Golden Rule of Generics" and practical items on constraining generics, inference, and avoiding over-abstraction. The most practical generics guidance in book form.

8. **Programming TypeScript** — Boris Cherny
   - Publisher: O'Reilly, 2019
   - Relevant: Chapter 4 "Functions" (generics section), Chapter 6 "Advanced Types"
   - Difficulty: Intermediate
   - Why: Thorough treatment of generic functions, classes, and interfaces with clear examples. Good companion to the handbook.

### Documentation and Reference

9. **TypeScript Handbook — Generics**
   - URL: https://www.typescriptlang.org/docs/handbook/2/generics.html
   - Why: Official reference covering syntax, constraints, generic classes, and generic interfaces. Start here for canonical documentation.

10. **TypeScript Handbook — Guidelines for Writing Good Generic Functions**
    - URL: https://www.typescriptlang.org/docs/handbook/2/functions.html#guidelines-for-writing-good-generic-functions
    - Why: Official guidelines including "push type parameters down," "use fewer type parameters," and "type parameters should appear twice."

11. **Dan Vanderkam — "The Golden Rule of Generics"** (Blog)
    - URL: https://effectivetypescript.com/2020/08/12/generics-golden-rule/
    - Why: Definitive article on when generics are justified, with concrete before/after examples.

12. **Semver-TS — Variance in TypeScript** (Appendix C)
    - URL: https://www.semver-ts.org/appendices/c-variance-in-typescript.html
    - Why: Practical reference on variance implications for library authors, explains how variance affects SemVer compatibility.

### Interactive Exercises

13. **type-challenges** (GitHub)
    - URL: https://github.com/type-challenges/type-challenges
    - Format: 170+ type-level challenges (Easy → Extreme)
    - Difficulty: Beginner-Expert
    - Why: The definitive practice ground for TypeScript types. Many challenges involve generics, `infer`, constraints, and mapped types. Filter by difficulty for progressive learning.

14. **TypeScript Playground**
    - URL: https://www.typescriptlang.org/play
    - Why: Essential for experimenting with generics. Use the "Examples" dropdown for built-in generic examples.

15. **Exercism — TypeScript Track**
    - URL: https://exercism.org/tracks/typescript
    - Format: Mentored exercises
    - Difficulty: Beginner-Advanced
    - Why: Practical coding exercises where generics naturally arise in solutions. Community mentoring provides feedback.

### GitHub Repositories

16. **type-challenges Solutions Guide**
    - URL: https://ghaiklor.github.io/type-challenges-solutions/en/
    - Why: Detailed solutions and explanations for type-challenges, excellent for learning generic patterns when stuck.

17. **mattcfox/typescript-challenges**
    - URL: https://github.com/mattcfox/typescript-challenges
    - Why: Focused specifically on writing effective generics (not just type-level puzzles). Green (Easy) and Blue (Medium) categories.

### Community Resources

18. **r/typescript** (Reddit)
    - URL: https://www.reddit.com/r/typescript/
    - Why: Active community. Searching for "generics" surfaces real-world questions and expert answers.

19. **TypeScript Discord**
    - URL: https://discord.gg/typescript
    - Why: Real-time help with generic type errors and inference issues.

20. **Stack Overflow — TypeScript Generics Tag**
    - URL: https://stackoverflow.com/questions/tagged/typescript-generics
    - Why: Thousands of real-world generics questions with solutions. Excellent for learning from others' inference failures.

---

## Learning Path

### Phase 1: Generic Foundations (3-4 hours)
**Concepts:** Generic type parameters, basic syntax, generic functions, generic interfaces and classes

1. Read the TypeScript Handbook Generics page
2. Watch Matt Pocock's "Generics in 3 Easy Patterns"
3. Practice: Write 5 generic functions (identity, first-element, wrap, pair, reverse-pair)
4. **Milestone:** Can write a generic function that preserves input types in its return type

### Phase 2: Constraints and Inference (4-5 hours)
**Concepts:** Generic constraints with `extends`, `keyof` constraints, default type parameters, inference mechanics

1. Read TypeScript Handbook "Guidelines for Writing Good Generic Functions"
2. Read Dan Vanderkam's "Golden Rule of Generics" blog post
3. Study built-in utility types (`Pick`, `Omit`, `Partial`, `Record`) — understand how they use constraints
4. Practice: Implement simplified versions of `Pick`, `Omit`, and `Record`
5. **Milestone:** Can explain why a generic constraint is needed and write `K extends keyof T` patterns fluently

### Phase 3: Inference Failures and Debugging (3-4 hours)
**Concepts:** Common inference failures, fixes (explicit type args, helper functions, `satisfies`), the `infer` keyword

1. Work through 5 type-challenges (Easy level) involving generics
2. Read Stack Overflow's top generic inference questions
3. Practice: Take 3 real-world inference failures, diagnose them, apply fixes
4. **Milestone:** Can diagnose why TypeScript inferred `unknown` or a union and apply the appropriate fix

### Phase 4: Variance (2-3 hours)
**Concepts:** Covariance, contravariance, invariance, bivariance, `in`/`out` annotations, `strictFunctionTypes`

1. Read Dmitri Pavlutin's covariance/contravariance article
2. Read Semver-TS Appendix C on variance
3. Practice: Create Producer<T>, Consumer<T>, and Mutable<T> interfaces and test assignability
4. **Milestone:** Can predict whether a generic type is covariant, contravariant, or invariant and explain why

### Phase 5: Over-Abstraction and Design Judgment (2-3 hours)
**Concepts:** Golden Rule, when generics help vs. hurt, refactoring generic code, reading library generics

1. Read Effective TypeScript Chapter 6
2. Watch Matt Pocock's "When to Use Generics" video
3. Practice: Review 3 open-source libraries' generic APIs, identify good and bad patterns
4. **Milestone:** Can audit generic code and decide whether to simplify or keep it

### Phase 6: Advanced Practice (4-6 hours)
**Concepts:** Generic utility patterns, generic event systems, generic builders, complex real-world generics

1. Work through 10 type-challenges (Medium level)
2. Complete Total TypeScript Generics workshop exercises (or equivalent)
3. Build a mini-project: type-safe event emitter or generic form validator
4. **Milestone:** Can design and implement generic APIs that provide excellent inference for consumers

**Total estimated time: 18-25 hours**

---

## Practical Exercises

### Exercise 1: Generic Data Access (Beginner)
Build a type-safe `pluck` function that extracts a property from an array of objects:
```typescript
function pluck<T, K extends keyof T>(items: T[], key: K): T[K][]
// pluck([{name: "Alice", age: 30}], "name") → ["Alice"] (typed as string[])
```

### Exercise 2: Generic API Response Wrapper (Beginner-Intermediate)
Create a generic `ApiResult<T>` type with success/error variants and helper functions:
```typescript
type ApiResult<T> = { ok: true; data: T } | { ok: false; error: string };
function mapResult<T, U>(result: ApiResult<T>, fn: (data: T) => U): ApiResult<U>;
```

### Exercise 3: Type-Safe Event Emitter (Intermediate)
Build an event emitter where event names and payload types are constrained:
```typescript
class TypedEmitter<Events extends Record<string, any>> {
  on<K extends keyof Events>(event: K, handler: (payload: Events[K]) => void): void;
  emit<K extends keyof Events>(event: K, payload: Events[K]): void;
}
```

### Exercise 4: Generic Builder Pattern (Intermediate)
Create a form builder where field types accumulate as fields are added:
```typescript
const form = createForm()
  .field("name", z.string())
  .field("age", z.number())
  .build();
// form.values should be typed as { name: string; age: number }
```

### Exercise 5: Implement Utility Types (Intermediate)
Implement these from scratch using generics, mapped types, and conditional types:
- `MyPick<T, K>`
- `MyOmit<T, K>`
- `MyReturnType<T>`
- `MyPartial<T>`
- `DeepReadonly<T>`

### Exercise 6: Variance Exploration (Intermediate-Advanced)
Create interfaces demonstrating each variance kind, predict assignability, and verify in the TypeScript Playground:
- `ReadonlyBox<T>` (covariant)
- `WriteOnlyBox<T>` (contravariant)
- `MutableBox<T>` (invariant)
- Add explicit `in`/`out` annotations and observe compiler behavior

### Exercise 7: Fix Inference Failures (Intermediate-Advanced)
Given 5 code snippets where TypeScript inference fails (returns `unknown`, widens to union, etc.), diagnose and fix each:
- Callback argument inference failure
- Nested generic defaulting to constraint
- Union widening in generic parameter
- Missing constraint causing property access error
- Over-generic function that should use concrete types

### Exercise 8: Generic Middleware Chain (Advanced)
Build a type-safe middleware pipeline where each middleware can transform the context type:
```typescript
type Middleware<In, Out> = (ctx: In) => Out;
function pipe<A, B>(m1: Middleware<A, B>): Middleware<A, B>;
function pipe<A, B, C>(m1: Middleware<A, B>, m2: Middleware<B, C>): Middleware<A, C>;
// ... support up to N middlewares with proper type inference
```

---

## Connections to Other Domains

- **D-6 (React):** Generic components (`<Select<T>>`, `<Table<T>>`), generic hooks (`useState<T>`, custom hooks with inference), generic context providers
- **D-7 (Node.js/Backend):** Generic repository patterns, typed middleware, generic API route handlers, generic ORM patterns
- **D-3 (Type Modeling):** Generics build on mapped types and conditional types — this domain teaches how to parameterize those patterns
- **D-12 (Team Practices):** Generic complexity governance, when to reject PRs with over-engineered generics, team conventions for generic naming and constraints
