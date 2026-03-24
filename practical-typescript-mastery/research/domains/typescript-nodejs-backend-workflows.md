# TypeScript in Node.js and Backend Workflows

**Domain Level:** Intermediate-Advanced
**Estimated Total Time:** 18–25 hours
**Prerequisites:** D-1 (Foundations), D-2 (Strictness/Config), D-3 (Type Modeling), D-4 (Runtime Boundaries), D-5 (Generics)

---

## Overview

This domain covers how to leverage TypeScript's type system across the full backend stack in Node.js: typed route handlers, middleware augmentation via declaration merging, structured error envelopes, database type integration (Prisma, Drizzle), type-safe event systems, and end-to-end type sharing between frontend and backend. The focus is on practical patterns that reduce bugs, improve refactor confidence, and enforce contracts at compile time.

---

## Key Concepts

### 1. Typed Route Handlers
**What:** Defining request/response types for HTTP route handlers so that params, query, body, and reply are all type-checked at compile time.

**Framework approaches:**
- **Express:** Generic parameters on `Request<Params, ResBody, ReqBody, ReqQuery>`. Requires manual type annotation per handler.
- **Fastify:** Built-in generic route options (`{ Querystring, Params, Body, Reply }`). Type Providers (`@fastify/type-provider-typebox`, `fastify-type-provider-zod`) derive types from validation schemas automatically.
- **Hono:** Route chaining preserves full type inference. Zod integration via `@hono/zod-validator` provides both validation and type inference. RPC feature enables client-side type inference from server routes.
- **NestJS:** Controller decorators + DTOs with `class-validator` for runtime validation. TypeScript classes serve as both type definitions and validation schemas.

**Key tradeoff:** Manual type annotations (Express) vs. schema-derived types (Fastify/Hono type providers) vs. decorator-based (NestJS). Schema-derived approaches are strongly preferred for production because they provide both runtime validation and compile-time types from a single source.

**Relation to other concepts:** Builds on D-3 (type modeling for request/response shapes) and D-4 (runtime validation at boundaries).

### 2. Middleware Augmentation via Declaration Merging
**What:** Extending framework-provided types (e.g., Express `Request`) with custom properties added by middleware (auth user, locale, request ID).

**How it works:**
- Create a `.d.ts` file (e.g., `src/types/express/index.d.ts`)
- Use `declare module 'express-serve-static-core'` to merge new properties into the `Request` interface
- Properties should be optional (`?`) since middleware may not have run yet

**Important details:**
- Must augment `express-serve-static-core`, not just `express`
- The `.d.ts` file must be included in `tsconfig.json`'s `include` or `typeRoots`
- Fastify uses a similar pattern with `FastifyRequest` augmentation via declaration merging
- Hono uses typed `Context` with `c.set()`/`c.get()` for middleware data passing

**Common pitfalls:**
- Forgetting to make augmented properties optional (middleware ordering is not enforced by types)
- Augmenting the wrong module name
- Not including the declaration file in the TypeScript compilation

### 3. Error Envelope Patterns
**What:** A standardized, typed response structure for all API errors, enabling consistent client-side error handling.

**Core structure:**
```typescript
interface ApiError {
  statusCode: number;
  code: string;       // Machine-readable: "VALIDATION_FAILED", "NOT_FOUND"
  message: string;    // Human-readable summary
  details?: Array<{ field?: string; message: string }>;
  timestamp: string;
  path: string;
  traceId?: string;
}
```

**Implementation patterns:**
- Custom error class hierarchy extending `Error` with `statusCode` and `serialize()` method
- Discriminated union of error types on the client side using the `code` field
- Global error-handling middleware that catches custom errors and formats them
- RFC 9457 (Problem Details for HTTP APIs) as a standard format

**Relation to other concepts:** Uses discriminated unions (D-3) and runtime validation (D-4). The error type hierarchy is shared between frontend and backend via type sharing.

### 4. Database Type Integration
**What:** Ensuring that database queries, results, and domain models are all type-safe, with minimal drift between schema and TypeScript types.

**Prisma ORM approach:**
- Schema-first: `schema.prisma` → `prisma generate` → auto-generated TypeScript client with full type inference
- Generated types for all CRUD operations, including `CreateInput`, `UpdateInput`, `WhereInput`
- Derive application-specific types using `Pick`, `Omit`, `Partial` from generated types
- Prisma Migrate for schema evolution
- `prisma-standalone-types` for sharing types without the full client dependency

**Drizzle ORM approach:**
- Code-first: Define schema in TypeScript files using Drizzle's table builders
- Types inferred directly from schema definitions (no code generation step)
- SQL-first philosophy: thin typed layer over SQL, developer controls the queries
- Lightweight, no external dependencies, good for serverless
- Drizzle Kit CLI for migrations

**Key pattern — Repository pattern:**
- Abstract database access behind typed interfaces
- Domain types may differ from ORM-generated types (decouple persistence from domain)
- Enables testing with mock repositories

**Drift control:**
- Generated types stay in sync via CI checks (`prisma generate` + `tsc --noEmit`)
- For Drizzle, schema IS TypeScript, so drift is impossible within the same codebase

### 5. Typed Event Systems
**What:** Making Node.js event-driven patterns type-safe by constraining event names and payload types at compile time.

**Core pattern — Event Map:**
```typescript
interface AppEvents {
  userCreated: [{ userId: string; email: string }];
  orderPlaced: [{ orderId: string; total: number }];
  notification: [{ type: string; message: string }];
}
```

**Implementation approaches:**
- **Custom TypedEventEmitter:** Wrapper around Node.js `EventEmitter` using generics and `keyof` to enforce event name and payload types
- **`typed-emitter` package:** Zero-runtime-cost typings-only solution for typed events
- **`@types/node` generics (2024+):** Recent `@types/node` updates add generic support to `EventEmitter` directly
- **Framework-specific:** NestJS event-driven module, Fastify hooks with typed payloads

**Benefits:** Catches typos in event names, enforces correct payload shapes, enables IDE autocompletion for events.

**Versioned event contracts:** For event-driven systems, define versioned payload types and use discriminated unions for backward-compatible evolution.

### 6. End-to-End Type Sharing
**What:** Sharing types between frontend and backend so that API contracts are enforced at compile time across the full stack.

**Approaches (from most to least integrated):**

1. **tRPC** — Zero-schema RPC framework. Backend procedures automatically infer types on the frontend via TypeScript's type inference. No code generation. Best for monorepo setups. v11 (March 2025) adds SSE subscriptions.

2. **Hono RPC** — Similar to tRPC but built into Hono. Route chaining preserves types; `hc` client infers types from server routes.

3. **Shared type packages** — Extract shared interfaces/types into a package consumed by both frontend and backend. Works with any framework. Requires careful versioning.

4. **OpenAPI/Swagger code generation** — Generate typed clients from OpenAPI specs. Works for REST APIs and multi-language consumers. Tools: `openapi-typescript`, `orval`, `swagger-typescript-api`.

5. **GraphQL code generation** — `graphql-codegen` generates typed hooks/queries from GraphQL schema. Good for GraphQL APIs.

**Monorepo considerations:**
- Shared types package with project references
- tRPC or Hono RPC for internal APIs (zero-cost type sharing)
- OpenAPI codegen for public/external APIs

### 7. Node.js Module Configuration for TypeScript
**What:** Correctly configuring `module` and `moduleResolution` in tsconfig for Node.js backends.

- `"module": "NodeNext"` + `"moduleResolution": "NodeNext"` for native ESM/CJS interop
- Understanding `.mts`/`.cts` extensions and `package.json` `"type": "module"`
- Import assertions and JSON imports
- Dual-package publishing for libraries

### 8. Testing Backend TypeScript Code
**What:** Type-safe testing patterns for backend services.

- Typed test utilities with `vitest` or `jest` (typed mocks, typed assertions)
- Supertest with typed response expectations
- Contract testing with shared types or OpenAPI specs
- Type-level tests for API contracts (using `tsd` or `expect-type`)

---

## Learning Resources

### Documentation (Primary Sources)

1. **Fastify TypeScript Reference**
   - URL: https://fastify.dev/docs/latest/Reference/TypeScript/
   - Covers: Generic route typing, type providers, declaration merging
   - Freshness: Actively maintained (v5.x, 2024-2025)

2. **Fastify Type Providers Documentation**
   - URL: https://fastify.dev/docs/latest/Reference/Type-Providers/
   - Covers: TypeBox, JSON Schema to TS, Zod type provider integration
   - Freshness: Current with Fastify v5

3. **Prisma TypeScript Documentation**
   - URL: https://www.prisma.io/typescript
   - Covers: Generated types, type-safe queries, utility type derivation
   - Freshness: Actively maintained (2024-2025)

4. **Drizzle ORM Documentation**
   - URL: https://orm.drizzle.team/docs/overview
   - Covers: Schema definition in TypeScript, type inference, migrations
   - Freshness: Actively maintained (2024-2025)

5. **tRPC Documentation**
   - URL: https://trpc.io/docs/
   - Covers: End-to-end type safety, procedures, middleware, subscriptions
   - Freshness: v11 released March 2025

6. **Hono Documentation — RPC**
   - URL: https://hono.dev/docs/guides/rpc
   - Covers: Type-safe RPC, client type inference, route chaining
   - Freshness: Actively maintained (2024-2025)

7. **NestJS Controllers Documentation**
   - URL: https://docs.nestjs.com/controllers
   - Covers: Typed controllers, DTOs, parameter decorators
   - Freshness: Current

8. **NestJS Exception Filters Documentation**
   - URL: https://docs.nestjs.com/exception-filters
   - Covers: Typed error handling, custom exception classes, global filters
   - Freshness: Current

9. **TypeScript Handbook — Declaration Merging**
   - URL: https://www.typescriptlang.org/docs/handbook/declaration-merging.html
   - Covers: Interface merging, module augmentation (foundation for middleware typing)
   - Freshness: Evergreen reference

10. **Node.js TypeScript Documentation**
    - URL: https://nodejs.org/en/learn/getting-started/nodejs-with-typescript
    - Covers: Running TypeScript with Node.js, module configuration
    - Freshness: Updated for current Node.js LTS

### Online Courses

11. **Microservices with NodeJS, React, Typescript and Kubernetes** (Udemy)
    - URL: https://www.udemy.com/course/microservices-with-node-js-and-react/
    - Duration: ~90 hours (select backend sections: ~20 hours)
    - Level: Intermediate-Advanced
    - Cost: Paid (~$15-20 on sale)
    - Covers: Typed Express services, event-driven architecture, error handling patterns

12. **The Complete Node.js Backend Developer Bootcamp** (Udemy)
    - URL: https://www.udemy.com/course/express-typescript-nodejs-mongodb-more-the-real-path/
    - Duration: ~40 hours
    - Level: Intermediate
    - Cost: Paid
    - Covers: Express + TypeScript, NestJS, TypeORM, PostgreSQL, MongoDB

13. **Pluralsight Node.js Microservices: Advanced Topics and Best Practices**
    - URL: https://www.pluralsight.com/courses/nodejs-microservices-advanced-topics-best-practices
    - Duration: ~3 hours
    - Level: Advanced
    - Cost: Pluralsight subscription
    - Covers: Typed microservice patterns, scalability

### Video Tutorials and Talks

14. **Matt Pocock — Type-Safe Event Emitters in TypeScript** (typescript.tv)
    - URL: https://typescript.tv/hands-on/make-nodejs-eventemitter-type-safe/
    - Duration: ~15 min
    - Covers: Building a typed event emitter wrapper

15. **freeCodeCamp — Build Production-Ready Web Apps with Hono**
    - URL: https://www.freecodecamp.org/news/build-production-ready-web-apps-with-hono/
    - Covers: Full Hono tutorial with TypeScript, type-safe routing, RPC

16. **tRPC v11 Announcement Blog**
    - URL: https://trpc.io/blog/announcing-trpc-v11
    - Covers: Latest tRPC features, SSE subscriptions, migration guide

### Books

17. **"Programming TypeScript" by Boris Cherny** (O'Reilly, 2019)
    - Relevant chapters: Ch. 9 (Frontend/Backend Frameworks), Ch. 10 (Namespaces and Module Augmentation)
    - Level: Intermediate
    - Note: Foundational patterns still apply; some API examples dated

18. **"Effective TypeScript" by Dan Vanderkam** (O'Reilly, 2nd ed. 2024)
    - Relevant items: Items on type assertions, declaration files, module augmentation
    - Level: Intermediate-Advanced
    - Note: 2nd edition updated for TS 5.x

### GitHub Repositories

19. **fastify/fastify** — Reference implementation for typed routes
    - URL: https://github.com/fastify/fastify
    - Stars: 33k+ | What to study: `/types/` directory, type provider examples

20. **trpc/trpc** — End-to-end type-safe APIs
    - URL: https://github.com/trpc/trpc
    - Stars: 35k+ | What to study: Examples directory, middleware patterns

21. **drizzle-team/drizzle-orm** — Type-safe SQL ORM
    - URL: https://github.com/drizzle-team/drizzle-orm
    - Stars: 27k+ | What to study: Schema definitions, query builder types

22. **prisma/prisma** — Database toolkit with generated types
    - URL: https://github.com/prisma/prisma
    - Stars: 41k+ | What to study: Generated client types, example projects

23. **honojs/hono** — Ultrafast web framework with typed RPC
    - URL: https://github.com/honojs/hono
    - Stars: 22k+ | What to study: RPC examples, type inference patterns

24. **andywer/typed-emitter** — Zero-cost typed event emitter
    - URL: https://github.com/andywer/typed-emitter
    - Stars: 200+ | What to study: Type-only approach to event safety

### Interactive Exercises and Practice

25. **Exercism — TypeScript Track**
    - URL: https://exercism.org/tracks/typescript
    - Covers: General TypeScript practice; apply backend patterns to exercises
    - Format: Mentored exercises with community feedback

26. **TypeScript Playground**
    - URL: https://www.typescriptlang.org/play
    - Use for: Prototyping event maps, error envelopes, type providers quickly

### Community Resources

27. **r/typescript** (Reddit)
    - URL: https://www.reddit.com/r/typescript/
    - Active discussions on backend patterns, framework comparisons

28. **Fastify Discord**
    - URL: https://discord.gg/fastify
    - Active community for Fastify-specific TypeScript questions

29. **tRPC Discord**
    - URL: https://trpc.io/discord
    - Community support for tRPC patterns and issues

---

## Learning Path

### Phase 1: Typed Route Handlers (4–5 hours)
**Concepts:** Express generics, Fastify type providers, Hono route chaining, schema-derived types

1. Read Fastify TypeScript docs and Type Providers docs
2. Build a small CRUD API with Fastify + Zod type provider
3. Compare: rewrite one route in Express with manual types, then in Hono with RPC
4. **Milestone:** Can define a typed POST endpoint where body, params, query, and response are all type-checked from a single Zod schema

### Phase 2: Middleware Augmentation (2–3 hours)
**Concepts:** Declaration merging, module augmentation, Express `Request` extension, Fastify decorators

1. Read TypeScript Handbook on declaration merging
2. Implement auth middleware that adds `user` to Express `Request` via `.d.ts`
3. Do the same in Fastify using `decorateRequest` + type augmentation
4. **Milestone:** Can add typed custom properties to request objects and have IDE autocompletion work correctly

### Phase 3: Error Envelope Patterns (2–3 hours)
**Concepts:** Custom error classes, error serialization, global error middleware, discriminated unions for errors, RFC 9457

1. Define an `ApiError` interface and error class hierarchy
2. Build a global error-handling middleware
3. Implement client-side discriminated union handling for different error codes
4. **Milestone:** All API errors follow a consistent typed envelope; client code exhaustively handles error variants

### Phase 4: Database Type Integration (4–5 hours)
**Concepts:** Prisma generated types, Drizzle schema-as-types, repository pattern, type derivation, drift control

1. Set up Prisma with a small schema, explore generated types
2. Derive application-specific types (CreateInput, Response) from Prisma types
3. Set up Drizzle with the same schema, compare type inference approach
4. Implement a repository layer abstracting the ORM
5. **Milestone:** Database queries are fully type-safe; application types are derived from (not duplicating) database schema types

### Phase 5: Typed Event Systems (2–3 hours)
**Concepts:** Event map pattern, TypedEventEmitter, `typed-emitter`, versioned events

1. Build a custom TypedEventEmitter with generics
2. Use `typed-emitter` package as an alternative
3. Design a versioned event payload with backward compatibility
4. **Milestone:** All event emissions and listeners are type-checked; typos in event names cause compile errors

### Phase 6: End-to-End Type Sharing (4–6 hours)
**Concepts:** tRPC procedures, Hono RPC, shared type packages, OpenAPI codegen, monorepo type sharing

1. Build a small fullstack app with tRPC (server + client)
2. Verify that changing a server procedure signature breaks the client at compile time
3. Set up OpenAPI codegen for comparison (use `openapi-typescript`)
4. Extract shared types into a package for a non-tRPC setup
5. **Milestone:** Frontend code gets compile-time errors when backend API contracts change; can choose the right type-sharing strategy for different scenarios

---

## Practical Exercises

### Exercise 1: Typed REST API with Error Envelopes (Beginner)
Build a task management API with Fastify + Zod type provider:
- CRUD routes with fully typed request/response
- Custom error classes for NotFound, Validation, Unauthorized
- Global error middleware producing consistent envelopes
- Test with typed Supertest assertions

### Exercise 2: Middleware Chain with Augmented Types (Intermediate)
Build an Express API with:
- Auth middleware adding typed `user` to request
- Rate-limit middleware adding typed `rateLimit` info
- Request ID middleware adding `requestId`
- All augmented via declaration merging
- Downstream handlers access augmented properties with full type safety

### Exercise 3: Type-Safe Database Layer (Intermediate)
Build a user/post system:
- Define Prisma schema with User, Post, Comment models
- Generate and explore Prisma client types
- Create typed repository interfaces
- Derive API response types from Prisma types using utility types
- Add Drizzle as an alternative implementation of the same repository interface

### Exercise 4: Event-Driven Order System (Intermediate-Advanced)
Build an order processing system:
- Define typed event map: `orderCreated`, `paymentProcessed`, `orderShipped`, `orderDelivered`
- Implement TypedEventEmitter
- Handlers for each event with correct payload types
- Add a new event and verify existing handlers still compile
- Implement event versioning for the `orderCreated` payload

### Exercise 5: Full-Stack Type-Safe App (Advanced)
Build a complete notes app with:
- Backend: Fastify + Prisma + typed events
- Frontend: React (from D-6 knowledge)
- Type sharing via tRPC
- Error envelopes consumed on frontend with exhaustive matching
- Verify: rename a field on the server → frontend fails to compile
- Compare: swap tRPC for shared type package approach

---

## Connections to Other Domains

| Related Domain | Connection |
|---|---|
| D-1 Foundations | Structural typing enables typed route contracts; union types power error envelopes |
| D-2 Strictness | `strict`, `noUncheckedIndexedAccess` catch unsafe property access in handlers and DB results |
| D-3 Type Modeling | Discriminated unions for errors and events; branded types for IDs; mapped types for API responses |
| D-4 Runtime Boundaries | Zod/schema validation at API input boundaries; `unknown` for external data |
| D-5 Generics | TypedEventEmitter, type providers, repository patterns all use generics extensively |
| D-6 Frontend | Error envelopes consumed on frontend; type sharing connects to React data fetching |
| D-8 Tooling | `tsc --noEmit` in CI validates backend types; editor ergonomics for backend code |
| D-9 Refactoring | Repository pattern enables safe ORM swaps; typed events enable safe refactoring of event-driven systems |

---

## Version Notes

- **TypeScript 5.x** assumed throughout (5.3+ for best module resolution support)
- **Fastify v5** for type provider examples
- **Prisma 5.x / 6.x** for generated types (v7 changes output location)
- **Drizzle ORM 0.36+** for latest relational query support
- **tRPC v11** (March 2025) for SSE subscriptions
- **Hono v4** for RPC features
- **Node.js 20+ LTS** for ESM support and TypeScript runner

*Last updated: March 2025*
