# Runtime Boundaries and Data Validation

## Overview

This domain covers the critical gap between TypeScript's compile-time type system and runtime reality. TypeScript types are erased at compilation — they provide zero runtime guarantees. Every boundary where external data enters your application (API responses, user input, database results, config files, message queues) is a trust boundary that requires explicit runtime validation.

Mastering this domain means understanding *where* compile-time safety ends, *how* to validate data at runtime without duplicating type definitions, and *which* tools and patterns give you both safety and developer velocity.

**Prerequisites:** D-1 (type system fundamentals, narrowing, discriminated unions), D-2 (strict configuration, `useUnknownInCatchVariables`)

**Feeds into:** D-5 (generics in validation schemas), D-6 (React form validation, frontend data fetching), D-7 (backend request/response validation, middleware), D-9 (migration — adding validation to unvalidated codebases)

---

## Key Concepts

### 1. Compile-Time vs Runtime Type Safety Boundary

**What it is:** TypeScript's type annotations exist only at compile time. After transpilation, all type information is erased — JavaScript has no knowledge of your interfaces, type aliases, or generics. This means `as User` does not validate anything at runtime; it just tells the compiler to trust you.

**Why it matters:** Any data crossing a trust boundary (network, file system, user input, inter-process communication) has type `unknown` in reality, regardless of what your TypeScript annotations say. Failing to validate at these boundaries is the #1 source of "impossible" runtime bugs in TypeScript codebases.

**Key insight:** Treat type assertions (`as`) as red flags at trust boundaries. They are compile-time lies when applied to unvalidated external data.

### 2. Trust Boundaries and the "Parse, Don't Validate" Philosophy

**What it is:** A trust boundary is any point where data enters your system from an external source. The "parse, don't validate" philosophy (coined by Alexis King) means transforming unstructured `unknown` data into typed, validated data in a single step — rather than checking properties individually and hoping you covered everything.

**Key boundaries in typical applications:**
- HTTP request/response bodies
- Query parameters and URL path segments
- Form submissions
- Database query results
- Environment variables and configuration
- Message queue payloads
- Third-party SDK responses
- File reads (JSON, YAML, CSV)
- WebSocket messages
- localStorage/sessionStorage

**Pattern:** Validate once at the boundary, then trust the types downstream. This creates a "validated zone" inside your application where types can be trusted.

### 3. The `unknown` Type and Safe Parsing

**What it is:** `unknown` is TypeScript's type-safe alternative to `any`. Unlike `any`, you cannot perform any operations on an `unknown` value without first narrowing it through type checks.

**Safe parsing pattern:**
```typescript
// UNSAFE: trusting external data
const user = JSON.parse(response) as User; // No runtime check!

// SAFE: parsing through unknown
const data: unknown = JSON.parse(response);
// Now must narrow before use
```

**Relationship to `useUnknownInCatchVariables`:** With this tsconfig flag (covered in D-2), catch clause variables are typed as `unknown` instead of `any`, forcing you to validate error shapes before accessing properties.

### 4. Type Guards (Built-in and User-Defined)

**What it is:** Type guards are runtime expressions that narrow a value's type within a conditional block. TypeScript recognizes several built-in patterns and allows custom user-defined type predicates.

**Built-in type guards:**
- `typeof x === 'string'` — narrows primitives
- `x instanceof MyClass` — narrows class instances
- `'property' in obj` — narrows by property existence
- Truthiness checks — narrows away `null`/`undefined`
- Equality checks — narrows literal types

**User-defined type predicates:** Functions with return type `value is Type` that perform custom runtime checks and inform the compiler of the narrowed type.

```typescript
function isUser(value: unknown): value is User {
  return (
    typeof value === 'object' &&
    value !== null &&
    'id' in value &&
    typeof (value as any).id === 'number' &&
    'name' in value &&
    typeof (value as any).name === 'string'
  );
}
```

**Critical caveat:** TypeScript *trusts* your type predicate. If your runtime check is incomplete or wrong, the compiler won't catch it. This is why schema validation libraries are preferred for complex shapes — they generate correct validation logic automatically.

### 5. Assertion Functions

**What it is:** Functions with return type `asserts value is Type` that throw on invalid data and narrow the type in the calling scope after the call.

```typescript
function assertUser(value: unknown): asserts value is User {
  if (!isUser(value)) {
    throw new Error('Invalid user data');
  }
}

// After this call, data is narrowed to User
assertUser(data);
console.log(data.name); // OK — TypeScript knows it's User
```

**Use case:** Useful for guard clauses at function entry points, especially in middleware or handler functions.

### 6. Schema Validation Libraries

**What it is:** Libraries that let you define data schemas using a TypeScript-friendly API and automatically infer static types from those schemas, providing both runtime validation and compile-time types from a single definition.

**Major libraries (2024-2025 landscape):**

| Library | Bundle Size | Performance | Maturity | Key Strength |
|---------|-------------|-------------|----------|--------------|
| **Zod** | ~15KB (full), ~5KB (mini) | Fast (v4 JIT) | Very mature, 38K+ stars | Ecosystem, DX, features |
| **Valibot** | ~1.4KB | Fast | Growing, 7.7K stars | Minimal bundle, tree-shaking |
| **ArkType** | Medium | Very fast | Alpha/beta | TS-native syntax |
| **TypeBox** | Small | Very fast | Mature | JSON Schema compatible |
| **io-ts** | Medium | Moderate | Mature | FP-oriented, encoding/decoding |
| **Yup** | Medium | Moderate | Mature | Form validation heritage |
| **Effect Schema** | Part of Effect | Fast | Growing | Effect ecosystem integration |

**Zod** is the ecosystem default — supported by tRPC, React Hook Form, Drizzle, Hono, Next.js server actions, and virtually every TypeScript framework. Zod v4 (2025) brought major performance improvements via JIT compilation.

**Valibot** excels when bundle size is critical (edge functions, mobile web, Cloudflare Workers). Its modular functional API enables aggressive tree-shaking.

**ArkType** offers TypeScript-native syntax (`'string>=2'`) and focuses on runtime-static type fidelity, but is less mature.

### 7. Standard Schema Specification

**What it is:** A v1.0 specification (2025) co-authored by the creators of Zod, Valibot, and ArkType that defines a common interface (`StandardSchemaV1`) for TypeScript validation libraries. Framework authors can target Standard Schema instead of individual libraries, enabling interoperability.

**Practical impact:** You can swap validation libraries without rewriting framework integration code. Supported by Zod v3.24+, Valibot v1.0+, ArkType v2.0+.

**URL:** https://standardschema.dev/

### 8. Schema-First vs Type-First Approaches

**Schema-first (types derived from schemas):**
```typescript
// Define schema → infer type
const UserSchema = z.object({
  id: z.number(),
  name: z.string(),
  email: z.string().email(),
});
type User = z.infer<typeof UserSchema>; // Type derived from schema
```

**Pros:** Single source of truth, runtime + compile-time from one definition, schemas can express constraints types cannot (email format, min/max).
**Cons:** Schema DSL learning curve, all types coupled to validation library.

**Type-first (schemas derived from types):**
```typescript
// Define type → generate schema/validation
interface User {
  id: number;
  name: string;
  email: string;
}
// Use tools like typia, ts-auto-guard, or typescript-json-schema
// to generate runtime validators from the type
```

**Pros:** Types remain plain TypeScript, no library coupling.
**Cons:** Requires build step or code generation, harder to express runtime constraints (email format, ranges).

**External-schema-first (types from external specification):**
- OpenAPI/Swagger → generate TypeScript types + validation
- GraphQL SDL → codegen types
- Protocol Buffers → generate types
- JSON Schema → `json-schema-to-typescript`

**Pros:** Language-agnostic contracts, useful for public APIs and polyglot systems.
**Cons:** Extra build tooling, potential drift between spec and code.

**Recommendation:** For most TypeScript projects, schema-first with Zod/Valibot is the practical default. Use external-schema-first when you have a pre-existing API specification or cross-language requirements.

### 9. Deriving Types from Schemas and Schemas from Types

**Types from schemas (most common):**
- `z.infer<typeof schema>` (Zod)
- `v.InferOutput<typeof schema>` (Valibot)
- `type MyType = typeof schema.infer` (ArkType)

**Schemas from types:**
- `typia` — generates validation code from TypeScript types at compile time
- `typescript-json-schema` — extracts JSON Schema from TypeScript interfaces
- `ts-auto-guard` — generates type guard functions from interfaces

**Key tradeoff:** Schema-first gives you richer runtime validation (regex, ranges, custom refinements) but couples your types to a library. Type-first keeps types pure but limits runtime constraint expressiveness.

### 10. Safe Error Handling in Validation

**What it is:** Validation can fail, and how you handle failures matters for both safety and developer experience.

**Patterns:**
- **Result types:** Zod's `.safeParse()` returns `{ success: true, data: T } | { success: false, error: ZodError }` — no thrown exceptions, explicit error handling
- **Thrown errors:** `.parse()` throws on invalid data — simpler but requires try/catch
- **Custom error formatting:** Zod's `.format()`, Valibot's `flatten()` for human-readable errors
- **Error aggregation:** Collecting all validation errors vs failing fast on first error

### 11. Contract Testing and Type-Safe API Clients

**What it is:** Ensuring that API consumers and producers agree on data shapes, enforced through automated tests that verify contracts at boundaries.

**Approaches:**

**End-to-end type sharing (tRPC):**
- Server defines procedures with input/output schemas
- Client automatically infers types from the server router
- Compile-time contract enforcement — mismatches caught by `tsc`
- Best for internal TypeScript-to-TypeScript communication

**Consumer-Driven Contract (CDC) Testing (Pact):**
- Consumers define expectations about provider behavior
- Provider verifies it meets consumer expectations
- Language-agnostic — works across polyglot microservices
- Tool: https://docs.pact.io/

**OpenAPI-based contracts:**
- Define API spec in OpenAPI/Swagger format
- Generate type-safe clients (openapi-typescript, orval)
- Validate responses against spec in tests
- Good for public APIs and cross-team boundaries

**Schema-validated API clients:**
- Wrap `fetch` with schema validation on responses
- Parse API responses through Zod schemas before use
- Catches API drift at runtime instead of trusting response shapes

### 12. Validation in Practice: Common Application Patterns

**HTTP request validation (backend):**
```typescript
// Express/Fastify middleware pattern
const createUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
});

app.post('/users', (req, res) => {
  const result = createUserSchema.safeParse(req.body);
  if (!result.success) {
    return res.status(400).json({ errors: result.error.flatten() });
  }
  // result.data is typed as { name: string; email: string }
  createUser(result.data);
});
```

**API response validation (frontend):**
```typescript
const UserResponseSchema = z.object({
  id: z.number(),
  name: z.string(),
});

async function fetchUser(id: number) {
  const response = await fetch(`/api/users/${id}`);
  const data: unknown = await response.json();
  return UserResponseSchema.parse(data); // Throws if API changed
}
```

**Environment variable validation:**
```typescript
const EnvSchema = z.object({
  DATABASE_URL: z.string().url(),
  PORT: z.coerce.number().default(3000),
  NODE_ENV: z.enum(['development', 'production', 'test']),
});

export const env = EnvSchema.parse(process.env);
```

**Form validation (React):**
```typescript
// With React Hook Form + Zod
const formSchema = z.object({
  username: z.string().min(3).max(20),
  password: z.string().min(8),
});

const { register, handleSubmit } = useForm({
  resolver: zodResolver(formSchema),
});
```

### 13. Discriminated Union Validation

**What it is:** Validating data that can be one of several shapes, distinguished by a discriminant field. Builds on discriminated unions from D-3.

```typescript
const EventSchema = z.discriminatedUnion('type', [
  z.object({ type: z.literal('click'), x: z.number(), y: z.number() }),
  z.object({ type: z.literal('keypress'), key: z.string() }),
  z.object({ type: z.literal('scroll'), delta: z.number() }),
]);

type Event = z.infer<typeof EventSchema>;
// Automatically creates discriminated union type
```

### 14. Recursive and Composable Schemas

**What it is:** Building complex validation schemas from smaller, reusable pieces, including self-referential (recursive) schemas.

```typescript
// Composable
const AddressSchema = z.object({ street: z.string(), city: z.string() });
const PersonSchema = z.object({
  name: z.string(),
  address: AddressSchema,
});

// Recursive (e.g., tree structures)
const CategorySchema: z.ZodType<Category> = z.lazy(() =>
  z.object({
    name: z.string(),
    children: z.array(CategorySchema),
  })
);
```

---

## Learning Resources

### Official Documentation and References

1. **TypeScript Handbook — Narrowing**
   - URL: https://www.typescriptlang.org/docs/handbook/2/narrowing.html
   - Covers type guards, type predicates, discriminated unions, and the `never` type for exhaustive checks
   - Primary source, always current with latest TS version

2. **TypeScript Handbook — Type Guards and Differentiating Types**
   - URL: https://www.typescriptlang.org/docs/handbook/advanced-types.html
   - Covers `typeof`, `instanceof`, `in` operator, and user-defined type guards
   - Primary source

3. **Zod Official Documentation**
   - URL: https://zod.dev/
   - Comprehensive reference for the most widely used TypeScript validation library
   - Covers schemas, parsing, type inference, error handling, integrations
   - Updated for Zod v4

4. **Valibot Official Documentation**
   - URL: https://valibot.dev/
   - Modular validation library documentation with comparison guides
   - Includes thesis/research paper on design decisions: https://valibot.dev/thesis.pdf

5. **ArkType Official Documentation**
   - URL: https://arktype.io/
   - TypeScript-syntax-at-runtime validation library
   - Integrations documentation: https://arktype.io/docs/integrations

6. **Standard Schema Specification**
   - URL: https://standardschema.dev/
   - The interoperability standard for TypeScript validation libraries
   - Important for understanding library-agnostic validation patterns

7. **Pact Contract Testing Documentation**
   - URL: https://docs.pact.io/
   - Consumer-driven contract testing framework
   - Language-agnostic with TypeScript/JavaScript support

8. **tRPC Documentation**
   - URL: https://trpc.io/docs
   - End-to-end type-safe API framework
   - Shows how compile-time type sharing replaces traditional contract testing

### Books

9. **Effective TypeScript, 2nd Edition** — Dan Vanderkam (O'Reilly, 2024)
   - Item 74: "Know How to Reconstruct Types at Runtime" — covers Zod, JSON Schema generation, and choosing between schema-first and type-first approaches
   - Chapter 9: "Writing and Running Your Code" — runtime type reconstruction
   - Difficulty: Intermediate
   - URL: https://effectivetypescript.com/

10. **Programming TypeScript** — Boris Cherny (O'Reilly, 2019)
    - Chapter on type guards and runtime type checking patterns
    - Foundational but some patterns pre-date modern validation libraries
    - Difficulty: Intermediate

### Video Tutorials and Courses

11. **Total TypeScript — Zod Tutorial (Free, Interactive)**
    - URL: https://www.totaltypescript.com/tutorials/zod
    - Platform: Total TypeScript
    - Hands-on exercises with short videos, solve problems in browser
    - Duration: ~2-3 hours
    - Difficulty: Beginner-Intermediate

12. **Frontend Masters — Fullstack TypeScript v2 (Zod Intro excerpt)**
    - URL: https://www.youtube.com/watch?v=GOsFM_kIU78
    - Speaker: Steve Kinney
    - Covers Zod fundamentals, performance, lazy recursion, JSON schemas
    - Duration: ~30 min (excerpt)
    - Full course: https://stevekinney.com/courses/full-stack-typescript

13. **Zod Validation Tutorial for Beginners (Full Course)**
    - URL: https://www.youtube.com/watch?v=IcyjtsAdKRs
    - Duration: ~40 minutes
    - Covers installation, schema creation, error handling, React/Next.js integration
    - Published: March 2025

14. **TypeScript and Zod Tutorial with React Hook Form — Dave Gray**
    - URL: Available on Dave Gray's YouTube channel
    - Covers Zod schemas, type inference, fetching/parsing data, zodResolver integration
    - Practical frontend validation focus

15. **Matt Pocock — Zod and TypeScript Tips (YouTube)**
    - Channel: Matt Pocock / Total TypeScript
    - Various short-form videos on Zod patterns, type inference, and validation
    - URL: https://www.youtube.com/@maaboroshi (Total TypeScript channel)

### Interactive Exercises and Practice

16. **Total TypeScript — Zod Interactive Tutorial**
    - URL: https://www.totaltypescript.com/tutorials/zod
    - Browser-based exercises with instant feedback
    - Free

17. **Execute Program — Advanced TypeScript (Validating Data Manually)**
    - URL: https://www.executeprogram.com/courses/advanced-typescript
    - Covers manual validation patterns and type predicate tips
    - Spaced-repetition format
    - Paid subscription

18. **TypeScript Playground**
    - URL: https://www.typescriptlang.org/play
    - Practice type guards, assertion functions, and narrowing patterns
    - Free, instant feedback

### GitHub Repositories and Open-Source Projects

19. **Zod Repository**
    - URL: https://github.com/colinhacks/zod
    - 38K+ stars, study source code and examples
    - Excellent README with comprehensive examples

20. **Valibot Repository**
    - URL: https://github.com/fabian-hiller/valibot
    - 7.7K stars, modular architecture worth studying
    - Comparison guide in docs

21. **tRPC Repository**
    - URL: https://github.com/trpc/trpc
    - Study how end-to-end type safety works in practice
    - Example apps in the repo

22. **Standard Schema Repository**
    - URL: https://github.com/standard-schema/standard-schema
    - The specification itself — small, well-documented

23. **openapi-typescript**
    - URL: https://github.com/openapi-ts/openapi-typescript
    - Generate TypeScript types from OpenAPI specs
    - Demonstrates external-schema-first approach

### Articles and Blog Posts

24. **Dan Vanderkam — "Know How to Reconstruct Types at Runtime"**
    - URL: https://effectivetypescript.com/2024/10/31/runtime-types/
    - Blog companion to Effective TypeScript Item 74
    - Excellent overview of schema-first vs type-first tradeoffs

25. **Alexis King — "Parse, Don't Validate" (Foundational)**
    - URL: https://lexi-lambda.github.io/blog/2019/11/05/parse-don-t-validate/
    - The seminal article on the parsing philosophy
    - Written for Haskell but the principle applies universally to TypeScript

26. **LogRocket — "Methods for TypeScript Runtime Type Checking"**
    - URL: https://blog.logrocket.com/methods-for-typescript-runtime-type-checking/
    - Practical survey of runtime validation approaches
    - Updated regularly

27. **Valibot Comparison Guide**
    - URL: https://valibot.dev/guides/comparison/
    - Detailed feature/performance comparison of validation libraries
    - Maintained by Valibot author

### Community Resources

28. **r/typescript (Reddit)**
    - URL: https://www.reddit.com/r/typescript/
    - Active discussions on validation library choices and patterns

29. **TypeScript Discord**
    - URL: https://discord.gg/typescript
    - Channels for validation, type-safety, and library discussions

---

## Learning Path

### Phase 1: Foundations (4-6 hours)

**Cluster: Understanding the Boundary Problem**
1. Compile-time erasure and why types don't protect at runtime (~1 hr)
2. Trust boundaries — identifying where validation is needed (~1 hr)
3. The `unknown` type vs `any` — safe default for external data (~1 hr)

**Milestone:** Can explain to a colleague why `as User` on a `fetch` response is unsafe and what to do instead.

**Resources:** TypeScript Handbook (Narrowing), Effective TypeScript Item 74 blog post

### Phase 2: Manual Validation Patterns (3-4 hours)

**Cluster: Type Guards and Assertion Functions**
4. Built-in type guards (`typeof`, `instanceof`, `in`) (~1 hr)
5. User-defined type predicates (`value is Type`) (~1.5 hr)
6. Assertion functions (`asserts value is Type`) (~1 hr)

**Milestone:** Can write a correct, comprehensive type guard for a nested object shape and use it to narrow `unknown` data.

**Resources:** TypeScript Handbook, Execute Program exercises

### Phase 3: Schema Validation Libraries (6-8 hours)

**Cluster: Learning Zod (Primary Library)**
7. Zod fundamentals — schema definition, parsing, type inference (~2 hr)
8. Complex schemas — objects, arrays, unions, discriminated unions, recursion (~2 hr)
9. Error handling — `.safeParse()`, error formatting, custom error messages (~1 hr)
10. Refinements and transforms — custom validation logic, data transformation (~1 hr)

**Cluster: Library Landscape**
11. Valibot — modular API, tree-shaking, when to choose over Zod (~1 hr)
12. ArkType, TypeBox, io-ts — awareness-level understanding (~1 hr)
13. Standard Schema — what it means for library interoperability (~0.5 hr)

**Milestone:** Can define Zod schemas for a real API contract (request + response), infer types, validate data, and handle errors gracefully.

**Resources:** Total TypeScript Zod tutorial, Zod docs, Valibot docs

### Phase 4: Schema Architecture Decisions (3-4 hours)

**Cluster: Schema-First vs Type-First**
14. Schema-first approach — schemas as source of truth, `z.infer` pattern (~1 hr)
15. Type-first approach — `typia`, code generation, tradeoffs (~1 hr)
16. External-schema-first — OpenAPI codegen, GraphQL codegen (~1 hr)
17. Choosing the right approach for your project (~0.5 hr)

**Milestone:** Can articulate when to use schema-first (most cases), type-first (minimal validation needs), or external-schema-first (cross-language APIs) with concrete justification.

**Resources:** Effective TypeScript, Dan Vanderkam blog post, openapi-typescript docs

### Phase 5: Application Patterns (4-5 hours)

**Cluster: Validation in Real Applications**
18. Backend request validation patterns (Express/Fastify middleware) (~1.5 hr)
19. Frontend API response validation (~1 hr)
20. Form validation with React Hook Form + Zod (~1 hr)
21. Environment variable and config validation (~0.5 hr)
22. Database result validation and drift detection (~1 hr)

**Milestone:** Can implement validation at every trust boundary in a fullstack TypeScript application.

### Phase 6: Contract Testing (3-4 hours)

**Cluster: Ensuring API Contracts Hold**
23. tRPC — end-to-end type safety as implicit contract testing (~1.5 hr)
24. Consumer-driven contracts with Pact (~1 hr)
25. OpenAPI-based contract validation (~1 hr)
26. Schema-validated API clients (wrapping fetch with Zod) (~0.5 hr)

**Milestone:** Can set up automated contract verification between a TypeScript API and its consumers.

**Resources:** tRPC docs, Pact docs, openapi-typescript

**Total estimated time: 23-31 hours**

---

## Practical Exercises

### Exercise 1: The Unsafe-to-Safe Refactor (Beginner, 1 hr)
Take a function that uses `as` assertions on `fetch` response data:
```typescript
async function getUsers(): Promise<User[]> {
  const res = await fetch('/api/users');
  return (await res.json()) as User[];
}
```
Refactor it to:
1. Type the response as `unknown`
2. Define a Zod schema for `User`
3. Parse through the schema with proper error handling
4. Infer the `User` type from the schema

### Exercise 2: Environment Config Validator (Beginner, 1 hr)
Build a validated environment config module:
- Define schemas for all environment variables
- Use `z.coerce` for string-to-number conversion
- Provide sensible defaults with `.default()`
- Make the module fail fast at startup if config is invalid
- Export the validated, typed config object

### Exercise 3: API Boundary Validation Middleware (Intermediate, 2 hr)
Build a generic Express/Fastify middleware that:
- Accepts a Zod schema for request body, query params, and path params
- Validates all three and returns structured 400 errors
- Attaches validated, typed data to the request object
- Handles nested validation errors with proper error messages

### Exercise 4: Full-Stack Contract (Intermediate, 3 hr)
Build a shared validation layer for a frontend + backend:
- Define shared schemas in a `packages/schemas` directory
- Backend uses schemas for request validation
- Frontend uses same schemas for form validation (React Hook Form + zodResolver)
- Frontend uses schemas to validate API responses
- Demonstrate that changing a schema field breaks both frontend and backend at compile time

### Exercise 5: Schema-First API Client (Intermediate, 2 hr)
Build a type-safe API client wrapper:
- Define response schemas for each API endpoint
- Create a `typedFetch` function that validates responses through schemas
- Handle validation failures gracefully (log, fallback, or throw)
- Compare DX with raw `fetch` + `as`

### Exercise 6: Consumer-Driven Contract Test (Advanced, 3 hr)
Set up a Pact contract test between a TypeScript API and consumer:
- Consumer defines expected interactions
- Provider verifies against consumer contracts
- Integrate into CI pipeline
- Demonstrate catching a breaking change before deployment

### Exercise 7: Migration — Adding Validation to an Unvalidated Codebase (Advanced, 2 hr)
Given a codebase with `any` types and `as` assertions at API boundaries:
- Audit all trust boundaries
- Prioritize which boundaries to validate first (risk-based)
- Incrementally add Zod schemas without breaking existing code
- Track validation coverage as a metric

---

## Connections to Other Domains

- **D-1 (Foundations):** Understanding narrowing and discriminated unions is prerequisite for type guards and discriminated union validation schemas
- **D-2 (Strictness):** `useUnknownInCatchVariables` and `strict` mode force you to handle `unknown` properly; strictness makes validation more natural
- **D-3 (Type Modeling):** Branded types from D-3 can be combined with validation (e.g., `z.string().transform(val => val as BrandedId)`)
- **D-5 (Generics):** Generic schemas, generic validation middleware, and reusable schema patterns build on generics knowledge
- **D-6 (React):** Form validation (React Hook Form + Zod), data fetching validation, and component prop validation
- **D-7 (Backend):** Request/response validation middleware, database result parsing, event payload validation
- **D-9 (Migration):** Adding validation to legacy codebases is a key migration pattern
- **D-12 (Team Practices):** Establishing validation standards, deciding when validation is required, schema review in PRs
