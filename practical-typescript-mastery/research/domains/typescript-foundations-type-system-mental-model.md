# TypeScript Foundations and Type System Mental Model

## Overview

This domain covers the foundational concepts every TypeScript practitioner must internalize to be productive. It is the prerequisite for all other domains in the roadmap. The focus is on building accurate mental models of how TypeScript's type system works — structural typing, type erasure, inference behavior, and the core type constructs (unions, intersections, narrowing, discriminated unions). It also covers the practical decision of `type` vs `interface` and documents the most common traps that erode type safety (`any` leakage, `as` casts, non-null assertions).

**Estimated total time: 15–25 hours**

**Prerequisites for other domains:** This domain is a direct prerequisite for D-2 (Strictness), D-3 (Type Modeling), D-4 (Runtime Boundaries), D-5 (Generics), D-6 (Frontend), D-7 (Backend), D-8 (Tooling), D-9 (Refactoring), D-11 (Modern Features).

---

## Key Concepts

### 1. Structural Typing (Duck Typing)
- **What it is:** TypeScript determines type compatibility by comparing the *shape* (properties and methods) of types, not their names or declarations. Two types with the same structure are compatible even if declared separately.
- **Why it matters:** This is the single most important mental model shift from nominally-typed languages (Java, C#). It explains why TypeScript allows substitutions that might seem surprising, and why excess property checking only applies to object literals.
- **Practical impact:** Enables flexible API design, but can lead to accidental compatibility. Understanding structural typing is essential for designing branded/opaque types (D-3).

### 2. Type Erasure and Runtime Relationship
- **What it is:** All TypeScript type annotations are removed during compilation. The emitted JavaScript contains zero type information. Type annotations never change runtime behavior.
- **Why it matters:** Developers must understand that TypeScript provides *compile-time* safety only. You cannot use `instanceof` with interfaces or type aliases. Runtime validation requires separate mechanisms (D-4).
- **Practical impact:** Informs decisions about where runtime validation is needed (API boundaries, user input, database results). Directly prerequisite for D-4 (Runtime Boundaries).

### 3. Union Types
- **What it is:** A type that represents a value that can be one of several types, written with `|` (e.g., `string | number`). Only properties/methods common to all members are accessible without narrowing.
- **Why it matters:** Unions are the primary tool for modeling "either/or" scenarios — API responses that succeed or fail, values that might be absent, polymorphic data.
- **Relationship:** Unions work hand-in-hand with narrowing and discriminated unions.

### 4. Intersection Types
- **What it is:** A type that combines multiple types into one using `&`. The resulting type has all properties from all constituent types.
- **Why it matters:** Used for composing types (e.g., combining a base entity with audit fields), extending type aliases, and creating mixin patterns.
- **Relationship:** Intersection is the `type` alias equivalent of `interface extends`. Understanding the difference matters for D-3 and performance (D-10).

### 5. Type Narrowing
- **What it is:** The process by which TypeScript refines a broader type to a more specific type within a code block, using control flow analysis and type guards.
- **Type guards include:** `typeof`, `instanceof`, `in` operator, truthiness checks, equality checks, custom type predicate functions (`value is Type`).
- **Why it matters:** Narrowing is how you *safely* work with union types. Without narrowing, unions are practically unusable.
- **Practical impact:** The quality of your narrowing directly determines how much you need unsafe escape hatches (`as`, `!`).

### 6. Discriminated Unions (Tagged Unions)
- **What it is:** A pattern where union members share a common literal property (the "discriminant" or "tag") that TypeScript uses for exhaustive narrowing via `switch` or `if` checks.
- **Why it matters:** This is the most important type modeling pattern for real-world state machines, API responses, event systems, and workflow states. Enables exhaustiveness checking.
- **Relationship:** Builds on unions + narrowing. Prerequisite for D-3 (domain modeling) and D-6/D-7 (frontend/backend state).

### 7. Literal Types and Literal Inference
- **What it is:** TypeScript can infer exact literal values as types (e.g., `"loading"` instead of `string`). `const` declarations infer literal types; `let` declarations widen to the base type.
- **Why it matters:** Literal types power discriminated unions, string enums, and template literal types (D-3). Understanding widening vs. literal inference prevents common bugs.
- **`as const` assertion:** Freezes inference to literal types for objects and arrays. Essential tool.

### 8. Type Inference — Contextual Typing
- **What it is:** TypeScript infers parameter types of callbacks and expressions from the surrounding context (e.g., `addEventListener` provides the event type to the callback parameter automatically).
- **Why it matters:** Reduces boilerplate. Understanding when contextual typing applies vs. when explicit annotations are needed improves coding speed and prevents unnecessary annotations.

### 9. Type Inference — Widening vs. Narrowing
- **What it is:** *Widening* generalizes a literal type to its base primitive (`"hello"` → `string` for `let`). *Narrowing* refines a broad type to a specific one via control flow.
- **Why it matters:** Widening is the source of many "why doesn't this work?" moments. Understanding when TypeScript widens and how to prevent it (`as const`, explicit annotations) is a daily productivity skill.

### 10. Best Common Type Algorithm
- **What it is:** When TypeScript infers a type from an array or expression with mixed types, it selects the "best common type" — the type compatible with all candidates. If no common type exists, it infers a union.
- **Why it matters:** Explains unexpected inferred types in arrays and ternary expressions. Practical for understanding why `[1, "hello"]` becomes `(string | number)[]`.

### 11. `type` Aliases vs. `interface` Declarations
- **What it is:** Two ways to define named types in TypeScript with overlapping but distinct capabilities.
- **Key differences:**
  - `interface` supports declaration merging; `type` does not
  - `type` can alias primitives, unions, tuples, mapped types; `interface` cannot
  - `interface extends` is slightly more performant and produces clearer errors than `type` with `&`
  - `interface` is the idiomatic choice for object shapes and class contracts
  - `type` is required for unions, tuples, and advanced type manipulation
- **Practical guidance:** Use `interface` for object shapes/APIs by default. Use `type` for unions, tuples, function types, and computed types. Be consistent within a codebase.

### 12. The `any` Type and `any` Leakage
- **What it is:** `any` disables type checking entirely for a value. It propagates: if a function returns `any`, everything downstream loses type safety.
- **Why it matters:** `any` is the #1 source of false confidence in TypeScript codebases. It silently defeats the type system. Common sources: untyped dependencies, `JSON.parse()`, error catch clauses.
- **Alternatives:** `unknown` (safe), generics, explicit type annotations.
- **Detection:** ESLint rules (`@typescript-eslint/no-explicit-any`, `@typescript-eslint/no-unsafe-*`).

### 13. Type Assertions (`as`) and Their Dangers
- **What it is:** `value as Type` tells the compiler to treat a value as a different type. It performs no runtime check — it is purely a compile-time override.
- **Why it matters:** Overuse of `as` bypasses TypeScript's safety guarantees. It should be a last resort, not a first response to type errors. Common misuse: `as any` to silence errors.
- **Safe alternatives:** Type guards, validation functions, proper narrowing, redesigning types.

### 14. Non-Null Assertion Operator (`!`)
- **What it is:** `value!` tells TypeScript "this value is definitely not null/undefined." No runtime check is performed.
- **Why it matters:** Leads to `TypeError: Cannot read properties of undefined` at runtime when the assertion is wrong. Undermines `strictNullChecks`.
- **Safe alternatives:** Optional chaining (`?.`), nullish coalescing (`??`), explicit null checks, assertion functions.

### 15. The `unknown` Type
- **What it is:** A type-safe alternative to `any`. Values typed as `unknown` cannot be used without first narrowing them via type guards.
- **Why it matters:** The correct type for "I don't know what this is yet" scenarios (API responses, catch clause errors, deserialized data). Prerequisite for D-4 (Runtime Boundaries).

### 16. The `never` Type
- **What it is:** Represents values that never occur — unreachable code, exhaustive switch defaults, functions that always throw.
- **Why it matters:** Used for exhaustiveness checking in discriminated unions. If a `switch` doesn't handle all cases, the default branch won't accept `never`, causing a compile error.

---

## Learning Resources

### Official Documentation (Primary Sources)

1. **TypeScript Handbook — The Basics**
   - URL: https://www.typescriptlang.org/docs/handbook/2/basic-types.html
   - Covers: Type annotations, type erasure, structural typing fundamentals
   - Freshness: Continuously updated, current for TS 5.x
   - Type: Documentation

2. **TypeScript Handbook — Everyday Types**
   - URL: https://www.typescriptlang.org/docs/handbook/2/everyday-types.html
   - Covers: Primitives, arrays, unions, type aliases, interfaces, literal types, `any`/`unknown`
   - Type: Documentation

3. **TypeScript Handbook — Narrowing**
   - URL: https://www.typescriptlang.org/docs/handbook/2/narrowing.html
   - Covers: typeof guards, truthiness narrowing, equality narrowing, `in` operator, `instanceof`, type predicates, discriminated unions, exhaustiveness checking with `never`
   - Type: Documentation

4. **TypeScript Handbook — Type Inference**
   - URL: https://www.typescriptlang.org/docs/handbook/type-inference.html
   - Covers: Best common type, contextual typing
   - Type: Documentation

5. **TypeScript Handbook — Unions and Intersection Types**
   - URL: https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html
   - Covers: Union types, intersection types, discriminating unions
   - Type: Documentation

6. **TypeScript Playground — Widening and Narrowing Example**
   - URL: https://www.typescriptlang.org/play/typescript/language/type-widening-and-narrowing.ts.html
   - Covers: Interactive demonstration of widening vs narrowing behavior
   - Type: Interactive exercise

### Books

7. **Effective TypeScript, 2nd Edition** — Dan Vanderkam (O'Reilly, 2024)
   - Relevant chapters: Items 1–12 (Understanding TypeScript's type system), Items on structural typing, type inference, narrowing
   - Difficulty: Beginner–Intermediate
   - Why: The gold standard practical TypeScript book. Updated for TS 5. Item-based format makes it easy to apply immediately.
   - URL: https://effectivetypescript.com/

8. **Programming TypeScript** — Boris Cherny (O'Reilly, 2019)
   - Relevant chapters: Ch 3 (All About Types), Ch 6 (Advanced Types)
   - Difficulty: Beginner–Intermediate
   - Why: Excellent foundational explanations of the type system mechanics. Older but still accurate for core concepts.

9. **Learning TypeScript** — Josh Goldberg (O'Reilly, 2022)
   - Relevant chapters: Ch 1–5 (Type System basics, Unions and Narrowing)
   - Difficulty: Beginner
   - Why: Approachable introduction with exercises
   - URL: https://www.learningtypescript.com/

### Online Courses and Tutorials

10. **Total TypeScript — Beginner's TypeScript Tutorial** (Free)
    - URL: https://www.totaltypescript.com/tutorials/beginners-typescript
    - Platform: Total TypeScript (Matt Pocock)
    - Duration: ~3 hours
    - Covers: Core TypeScript concepts with editor-first exercises
    - Why: Matt Pocock is the most effective TypeScript educator currently active. Interactive exercise format.

11. **Total TypeScript — Type Transformations Workshop** (Paid)
    - URL: https://www.totaltypescript.com/workshops/type-transformations
    - Platform: Total TypeScript
    - Duration: ~5 hours
    - Covers: Inference, unions, narrowing, template literals, mapped types
    - Why: Deep dive into exactly the topics in this domain

12. **TypeScript for JavaScript Developers** (Free)
    - URL: https://learntypescript.dev/
    - Platform: Carl Rippon
    - Duration: Self-paced
    - Covers: Type system, narrowing, compiler options, with quizzes
    - Why: Specifically targets JS developers transitioning to TS

13. **Learn TypeScript — freeCodeCamp Full Course** (Free)
    - URL: https://www.youtube.com/watch?v=30LWjhZzg50
    - Platform: YouTube / freeCodeCamp
    - Duration: ~5 hours
    - Covers: Comprehensive beginner-to-intermediate TypeScript
    - Why: Free, comprehensive, well-structured

14. **Codecademy — Learn TypeScript** (Free tier available)
    - URL: https://www.codecademy.com/learn/learn-typescript
    - Platform: Codecademy
    - Duration: ~10 hours
    - Covers: TypeScript fundamentals, functions, complex types
    - Why: Interactive, hands-on exercises in-browser

### Interactive Exercises and Practice

15. **TypeScript Exercises**
    - URL: https://typescript-exercises.github.io/
    - GitHub: https://github.com/typescript-exercises/typescript-exercises
    - Covers: Progressive exercises from basic typing to advanced type manipulation. Key rule: no `any` allowed.
    - Difficulty: Beginner → Intermediate
    - Why: Forces correct typing habits from day one

16. **Type Challenges**
    - URL: https://tsch.js.org/
    - GitHub: https://github.com/type-challenges/type-challenges
    - Covers: Pure type-level challenges (easy → extreme difficulty)
    - Difficulty: Beginner → Expert
    - Why: The definitive practice ground for type system mastery. Start with "easy" and "medium" for this domain.

17. **Exercism TypeScript Track**
    - URL: https://exercism.org/tracks/typescript
    - Covers: ~100+ exercises covering TypeScript fundamentals through real-world problems
    - Difficulty: Beginner → Advanced
    - Why: Mentored feedback available, real coding problems

18. **Learning TypeScript Projects**
    - URL: https://github.com/LearningTypeScript/projects
    - Covers: Hands-on projects organized by difficulty (Appetizers → Entrees → Desserts)
    - Why: Companion to "Learning TypeScript" book, real-world application

### Video Content

19. **TypeScript Course for Beginners — Academind (Maximilian Schwarzmüller)**
    - URL: https://www.youtube.com/watch?v=BwuLxPH8IDs
    - Duration: ~15 hours
    - Covers: Comprehensive TypeScript fundamentals
    - Why: Well-produced, thorough, free on YouTube

20. **No BS TS — Jack Herrington**
    - URL: https://www.youtube.com/playlist?list=PLNqp92_EXZBJYFrpEzdO2EapvU0GOJ09n
    - Covers: Practical TypeScript concepts in short, focused videos
    - Why: Concise, practical, covers narrowing, generics, and real patterns

### Community Resources

21. **r/typescript** — Reddit
    - URL: https://www.reddit.com/r/typescript/
    - Active community for TypeScript questions, patterns, and discussions

22. **TypeScript Discord**
    - URL: https://discord.gg/typescript
    - Official TypeScript community Discord server

23. **Stack Overflow — TypeScript tag**
    - URL: https://stackoverflow.com/questions/tagged/typescript
    - Massive Q&A archive for TypeScript issues

---

## Learning Path

### Phase 1: TypeScript–JavaScript Relationship (3–4 hours)
**Concepts:** Structural typing, type erasure, runtime relationship
**Activities:**
1. Read TypeScript Handbook — The Basics
2. Understand that types are erased: write TypeScript, inspect emitted JavaScript
3. Experiment in TypeScript Playground with structural compatibility examples
**Milestone:** Can explain to a colleague why you cannot use `instanceof` with a TypeScript interface, and why two separately declared types with the same shape are compatible.

### Phase 2: Core Type Constructs (4–6 hours)
**Concepts:** Union types, intersection types, literal types, `as const`
**Activities:**
1. Read TypeScript Handbook — Everyday Types
2. Read TypeScript Handbook — Unions and Intersection Types
3. Complete TypeScript Exercises (exercises 1–5)
4. Practice: Model an API response as `Success | Error` union
**Milestone:** Can write union types, intersection types, and use `as const` for literal inference without looking at docs.

### Phase 3: Narrowing and Discriminated Unions (4–6 hours)
**Concepts:** Type guards (typeof, instanceof, in, truthiness, equality), type predicates, discriminated unions, exhaustiveness checking with `never`
**Activities:**
1. Read TypeScript Handbook — Narrowing (full page)
2. Watch Matt Pocock's narrowing videos (Total TypeScript)
3. Complete TypeScript Exercises (exercises 6–10)
4. Implement a state machine with discriminated unions (e.g., HTTP request lifecycle: idle → loading → success → error)
5. Implement exhaustiveness checking with `never` in a switch statement
**Milestone:** Can write a discriminated union with exhaustive switch handling. Can write a custom type predicate function.

### Phase 4: Type Inference Deep Dive (2–3 hours)
**Concepts:** Contextual typing, widening vs narrowing, best common type
**Activities:**
1. Read TypeScript Handbook — Type Inference
2. Explore Playground example on widening/narrowing
3. Experiment: observe how `let` vs `const` affects inferred types, how callback parameters get contextual types
4. Read Effective TypeScript Items 3 ("Understand That Code Generation Is Independent of Types") and 7 ("Think of Types as Sets of Values")
**Milestone:** Can predict what TypeScript will infer for a given expression. Can use `as const` and explicit annotations to control inference.

### Phase 5: type vs interface and Common Traps (2–4 hours)
**Concepts:** `type` vs `interface` decision framework, `any` leakage, `as` casts, non-null assertions, `unknown` as safe alternative
**Activities:**
1. Read Matt Pocock's "Type vs Interface" article: https://www.totaltypescript.com/type-vs-interface-which-should-you-use
2. Read Effective TypeScript items on `any` (Items 43–46 in 2nd edition)
3. Audit a real codebase for `any` usage — count occurrences, trace how `any` propagates
4. Practice replacing `as` assertions with proper narrowing
5. Practice replacing `!` with optional chaining and null checks
**Milestone:** Has a clear personal/team guideline for `type` vs `interface`. Can identify `any` leakage in code review. Never uses `as any` as a first resort.

---

## Practical Exercises

### Exercise 1: Structural Typing Explorer
Create two interfaces `Dog` and `Cat` with overlapping shapes. Demonstrate that a function accepting `Dog` can receive a value typed as `Cat` if the shapes are compatible. Then add a unique property to break compatibility. Observe compiler behavior.

### Exercise 2: Type Erasure Proof
Write a TypeScript function with type annotations. Compile it and examine the emitted JavaScript. Attempt to do a runtime type check on an interface — observe that it's impossible. Implement a runtime type guard as the solution.

### Exercise 3: Union Type API Response
Model an API response as a discriminated union:
```typescript
type ApiResponse<T> =
  | { status: "success"; data: T }
  | { status: "error"; error: string; code: number }
  | { status: "loading" };
```
Write a function that handles all cases with exhaustive narrowing. Add a new status and see the compiler catch the unhandled case.

### Exercise 4: Narrowing Gauntlet
Given a value of type `string | number | boolean | null | undefined | { name: string }`, write a function that narrows it using every available technique: `typeof`, truthiness, equality, `in` operator, and type predicates. Each branch should access type-specific operations.

### Exercise 5: Widening vs Literal Inference
Demonstrate the difference between `let x = "hello"` (widened to `string`) and `const x = "hello"` (literal `"hello"`). Show how `as const` affects object and array inference. Create a scenario where widening causes a type error and fix it.

### Exercise 6: any Leakage Audit
Take a small TypeScript project (or create one) with intentional `any` usage. Trace how `any` propagates through function calls, assignments, and return values. Replace every `any` with `unknown` and proper type guards. Compare the safety before and after.

### Exercise 7: State Machine with Discriminated Unions
Model a document editing workflow:
- Draft → Review → Approved → Published
- Draft → Review → Rejected → Draft (revision)
Each state has different available actions and data. Implement with discriminated unions and ensure exhaustive handling.

### Exercise 8: type vs interface Comparison
Implement the same data model using both `type` and `interface`. Test declaration merging with `interface`. Attempt union types with `interface` (observe the limitation). Use intersections with `type` to achieve extension. Document which approach you'd choose for each use case and why.

---

## Connections to Other Domains

| Concept | Used in Domain |
|---------|---------------|
| Structural typing | D-3 (Branded types are a workaround for structural compatibility) |
| Type erasure | D-4 (Runtime boundaries need explicit validation because types are erased) |
| Unions & narrowing | D-3, D-5, D-6, D-7 (Pervasive pattern in all modeling and application code) |
| Discriminated unions | D-3 (State modeling), D-6 (React state), D-7 (Backend event systems) |
| Inference & widening | D-2 (Strict config affects inference), D-5 (Generic inference) |
| type vs interface | D-3 (Complex type modeling), D-12 (Team conventions) |
| any/unknown | D-2 (Strict flags), D-4 (Runtime validation), D-9 (Migration from JS) |
| never | D-3 (Exhaustiveness), D-5 (Conditional types) |

---

## Source Freshness Notes
- TypeScript Handbook: Continuously updated, accurate for TS 5.x (verified March 2026)
- Effective TypeScript 2nd Ed: Published June 2024, covers TS 5.x
- Total TypeScript courses: Actively maintained as of 2025
- TypeScript Exercises: Last updated 2024, exercises still relevant
- Type Challenges: Actively maintained, 40k+ GitHub stars
