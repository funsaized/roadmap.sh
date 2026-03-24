# TypeScript in React and Frontend Workflows

## Overview

This domain covers the practical integration of TypeScript with React for building type-safe, maintainable frontend applications. It spans props modeling, generic hooks, context typing, polymorphic components, event/ref typing, component composition patterns, and end-to-end API-to-UI type safety. Building on foundations from D-1 (type system), D-3 (type modeling patterns), D-4 (runtime boundaries), and D-5 (generics), this domain applies those concepts specifically to React's component model and ecosystem.

**Difficulty Level:** Intermediate-Advanced  
**Estimated Total Time:** 18-25 hours  
**Prerequisites:** D-1 (Foundations), D-3 (Type Modeling), D-4 (Runtime Boundaries), D-5 (Generics)

---

## Key Concepts

### 1. Props Modeling Patterns

**What it is:** Defining the shape of data and callbacks that flow into React components using TypeScript types and interfaces.

**Core patterns:**
- **Basic props with `interface` or `type`:** Define component contracts with required and optional properties. Convention: `ComponentNameProps`.
- **Optional props with defaults:** Use `?` for optional props and destructuring defaults for type-safe fallbacks.
- **Discriminated union props:** Model mutually exclusive prop combinations (e.g., a button that's either a submit button with `onSubmit` or a link with `href`). Prevents impossible states.
- **Extending HTML element props:** Use `React.ComponentProps<'element'>` or `React.ComponentPropsWithoutRef<'element'>` to inherit all native attributes when wrapping HTML elements.
- **Utility types for props transformation:** `Pick`, `Omit`, `Partial`, `Required` to derive props from existing types. `PropsWithChildren<P>` for components accepting children.
- **`children` typing:** `React.ReactNode` for general children, `React.ReactElement` for single element, render function patterns for typed children.
- **Spreading and forwarding props:** Use rest/spread with proper typing to pass remaining props to underlying elements.

**Relation to other concepts:** Foundation for all other React TypeScript patterns. Discriminated unions and utility types come from D-3.

### 2. Generic Components

**What it is:** Components parameterized by a type variable, enabling reuse across different data shapes while maintaining type safety.

**Key patterns:**
- **Generic list/table components:** `<List<T> items={T[]} renderItem={(item: T) => ReactNode}>` — the consumer specifies `T` and gets full inference.
- **Generic select/dropdown components:** Type the options and selected value generically.
- **Constrained generics:** `<T extends { id: string }>` to require certain properties on the generic type.
- **Inference from props:** TypeScript infers `T` from the data passed, so explicit type arguments are often unnecessary.

**Relation:** Builds directly on D-5 (Generics in Practice). Critical for design system components.

### 3. Custom Hooks with TypeScript

**What it is:** Extracting reusable stateful logic into hooks with proper type signatures.

**Key patterns:**
- **Typed return values:** Return tuples (`[value, setter]` with `as const` for literal tuple types) or objects (named properties for clarity).
- **Generic hooks:** `useFetch<T>(url)`, `useForm<T>(initialValues)` — hooks parameterized by the data type they operate on.
- **Constrained generic hooks:** `useForm<T extends Record<string, any>>` — ensure the generic meets minimum shape requirements.
- **Typed parameters and callbacks:** Strongly type all inputs including callback functions using `Parameters<T>` and similar utility types.
- **Hook composition:** Building complex hooks from simpler typed hooks, maintaining type flow throughout.

**Relation:** Applies D-5 generics in hook context. Return type patterns connect to D-3 utility types.

### 4. Context API Typing

**What it is:** Creating type-safe React Context providers and consumers.

**Key patterns:**
- **Typed context creation:** `createContext<ContextType | null>(null)` with explicit type parameter.
- **Custom consumer hooks with runtime guards:** `useAuth()` that throws if used outside provider — narrows from `T | null` to `T`.
- **Provider component typing:** Type the `children` prop as `React.ReactNode`, type the value object to match the context type.
- **Reducer-based context:** Combine `useReducer` with typed action discriminated unions for complex state management in context.
- **Context + generics:** Create generic context factories for reusable patterns (e.g., a generic CRUD context).

**Relation:** Combines D-3 discriminated unions (for actions) with D-4 runtime boundary thinking (null checks as guards).

### 5. Polymorphic Components

**What it is:** Components that can render as different HTML elements or other React components while maintaining type safety for the rendered element's props.

**Key patterns:**
- **The `as` prop pattern:** Accept a generic `as` prop constrained to `React.ElementType`, then merge the component's own props with the element's props.
- **`React.ElementType` and `React.ComponentPropsWithoutRef<T>`:** Core utility types for building polymorphic components.
- **Prop collision prevention:** Use `Omit` to remove component's own prop keys from the element's props to prevent type conflicts.
- **Default element type:** `<T extends ElementType = 'button'>` — provide a sensible default when `as` is not specified.
- **With ref forwarding:** Combine polymorphic pattern with `forwardRef` for full flexibility, using `ComponentPropsWithRef<T>`.

**Relation:** Advanced application of D-5 generics. Common in design system libraries (Chakra UI, Radix, MUI).

### 6. Event Typing

**What it is:** Correctly typing React synthetic event handlers for compile-time safety and IDE autocompletion.

**Key event types:**
- `React.MouseEvent<HTMLButtonElement>` — click events
- `React.ChangeEvent<HTMLInputElement>` — input changes
- `React.FormEvent<HTMLFormElement>` — form submissions
- `React.KeyboardEvent<HTMLElement>` — keyboard events
- `React.FocusEvent<HTMLElement>` — focus/blur events
- `React.DragEvent<HTMLElement>` — drag and drop
- `React.SyntheticEvent<T>` — generic base type

**Patterns:**
- Inline handlers get automatic inference; extracted functions need explicit types.
- Custom event handler types for component APIs: `onSelect: (item: T) => void`.
- Hover over JSX event props to discover the correct type.

**Relation:** Practical application of D-1 type inference concepts in React context.

### 7. Ref Typing and Forwarding

**What it is:** Type-safe use of React refs for DOM access, imperative handles, and mutable values.

**Key patterns:**
- **`useRef<HTMLElement>(null)`:** Type the ref with the specific HTML element type. Returns `RefObject<HTMLElement | null>`.
- **Mutable refs:** `useRef<number>(0)` — returns `MutableRefObject<number>` for storing values without re-renders.
- **`forwardRef<RefType, PropsType>`:** Pass refs through components. First generic is the ref type, second is props.
- **`useImperativeHandle`:** Expose a custom interface through a ref instead of the raw DOM element. Define an interface for the handle.
- **React 19 changes:** `ref` is now a regular prop on function components, reducing the need for `forwardRef` in new code.

**Relation:** Combines D-1 generics with React-specific API patterns.

### 8. Component Composition Patterns

**What it is:** Structuring component hierarchies with strong typing for composition, slots, and render delegation.

**Key patterns:**
- **Compound components:** Parent + child components that share implicit state (e.g., `<Tabs>` + `<Tab>` + `<TabPanel>`). Type the shared context.
- **Render props:** Functions as children or props that receive typed data: `render: (data: T) => ReactNode`.
- **Higher-order components (HOCs):** Wrapper functions that add props. Type the injected props and the wrapped component's props separately. Less common in modern React but still found in legacy codebases.
- **Slot patterns:** Named render areas with typed slot props.

**Relation:** Composition patterns use generics (D-5) and discriminated unions (D-3).

### 9. End-to-End API-to-UI Type Safety

**What it is:** Maintaining type safety from API response through data layer to rendered components, eliminating type gaps.

**Key approaches:**
- **tRPC:** TypeScript Remote Procedure Call — infers types from backend procedures directly on the frontend. No code generation needed. Works best in monorepos where frontend and backend share a TypeScript codebase.
- **TanStack Query (React Query) with typed fetch:** Use generics on `useQuery<TData, TError>` to type the response. Combine with Zod for runtime validation at the boundary.
- **OpenAPI/Swagger code generation:** Generate TypeScript types and API clients from OpenAPI specs using tools like `openapi-typescript` or `orval`.
- **GraphQL with codegen:** `graphql-codegen` generates typed hooks and types from GraphQL schema and queries.
- **Zod schemas → types:** Define runtime validators with Zod, infer TypeScript types with `z.infer<typeof schema>`. Validate at the API boundary, trust types internally.

**Pattern (API → Zod → Hook → Component):**
1. Define Zod schema for API response
2. Create typed fetch function that validates with Zod
3. Wrap in a custom hook (or TanStack Query) with proper generics
4. Component receives fully typed data — no `any`, no unchecked access

**Relation:** Directly applies D-4 (Runtime Boundaries) concepts. Critical bridge between backend and frontend domains.

### 10. React 19 TypeScript Considerations

**What it is:** TypeScript patterns affected by React 19's changes.

**Key changes:**
- **`ref` as a regular prop:** Function components can accept `ref` directly without `forwardRef`. Simplifies ref forwarding patterns.
- **`use()` hook:** New hook for reading resources (promises, context) — needs proper typing for the resolved value.
- **Server Components:** Cannot use hooks or browser APIs. Props must be serializable. Affects how you structure types for server vs client components.
- **Actions and `useActionState`:** New patterns for form handling with typed action functions and state.
- **Updated `@types/react`:** React 19 types may differ from React 18. Migration involves updating type imports and handling breaking changes.

**Relation:** Connects to D-11 (Modern TypeScript Features) for keeping up with ecosystem changes.

---

## Learning Resources

### Online Courses

1. **React with TypeScript — Total TypeScript (Matt Pocock)**
   - URL: https://www.totaltypescript.com/tutorials/react-with-typescript
   - Platform: Total TypeScript
   - Cost: Free tutorial
   - Duration: ~4 hours
   - Difficulty: Intermediate
   - Covers: Props, hooks typing, component patterns, ComponentProps, event handlers
   - *Primary recommendation — most focused and up-to-date resource*

2. **Advanced React with TypeScript — Total TypeScript (Matt Pocock)**
   - URL: https://www.totaltypescript.com/workshops/advanced-react-with-typescript
   - Platform: Total TypeScript
   - Cost: Paid (part of Total TypeScript subscription)
   - Duration: ~8 hours
   - Difficulty: Advanced
   - Covers: Generic components, polymorphic components, type helpers, advanced hooks, context patterns

3. **React and TypeScript, v3 — Frontend Masters (Steve Kinney)**
   - URL: https://frontendmasters.com/courses/react-typescript/
   - Platform: Frontend Masters
   - Cost: Paid (subscription)
   - Duration: ~6 hours
   - Difficulty: Intermediate-Advanced
   - Covers: Hooks typing, reducers, Context API, polymorphic components, React 19 features
   - Course notes: https://stevekinney.com/courses/react-typescript

4. **React with TypeScript — Udemy (various instructors)**
   - URL: https://www.udemy.com/topic/react-typescript/
   - Platform: Udemy
   - Cost: Paid (frequently discounted)
   - Duration: Varies (8-20 hours)
   - Difficulty: Beginner-Intermediate

### Video Tutorials and Talks

5. **Matt Pocock's YouTube Channel — React TypeScript Tips**
   - URL: https://www.youtube.com/@maaborern
   - Platform: YouTube
   - Cost: Free
   - Highlights: Short, focused videos on specific React+TS patterns (ComponentProps, generics in hooks, discriminated union props)

6. **Jack Herrington — TypeScript/React Patterns**
   - URL: https://www.youtube.com/@jherr
   - Platform: YouTube
   - Cost: Free
   - Highlights: Practical patterns, tRPC tutorials, React 19 TypeScript coverage, advanced component patterns

7. **TkDodo (Dominik Dorfmeister) — Type-Safe React Query**
   - URL: https://tkdodo.eu/blog/type-safe-react-query
   - Platform: Blog
   - Cost: Free
   - Covers: Typing TanStack Query properly, generic query hooks, type inference patterns

### Books

8. **React and TypeScript — Carl Rippon (2023)**
   - Relevant chapters: Props patterns, hooks, context, forms, API integration
   - Difficulty: Intermediate
   - *Good structured walkthrough of React+TS patterns*

9. **Learning TypeScript — Josh Goldberg (O'Reilly, 2022)**
   - Relevant chapters: Generics, type operations (apply to React context)
   - Difficulty: Intermediate
   - *Foundational TypeScript knowledge that underpins React patterns*

### Documentation and References

10. **React Official Docs — TypeScript Guide**
    - URL: https://react.dev/learn/typescript
    - Covers: Props, hooks, DOM events, typing patterns with official React examples
    - *Primary source — must-read*

11. **React TypeScript Cheatsheet**
    - URL: https://react-typescript-cheatsheet.netlify.app/
    - GitHub: https://github.com/typescript-cheatsheets/react
    - Covers: Basic setup, advanced patterns, HOCs, render props, context, hooks, migration
    - Stars: 45k+ (actively maintained as of 2024)
    - *Essential reference — bookmark-worthy*

12. **TypeScript Handbook — JSX Section**
    - URL: https://www.typescriptlang.org/docs/handbook/jsx.html
    - Covers: How TypeScript processes JSX, intrinsic elements, value-based elements

13. **tRPC Documentation**
    - URL: https://trpc.io/docs
    - Covers: End-to-end type safety, React integration, TanStack Query adapter

14. **TanStack Query Documentation — TypeScript**
    - URL: https://tanstack.com/query/latest/docs/framework/react/typescript
    - Covers: Typing queries, mutations, query keys, generic patterns

### Interactive Exercises and Practice

15. **Total TypeScript — React Exercises**
    - URL: https://www.totaltypescript.com/tutorials/react-with-typescript
    - Format: Interactive coding exercises in the browser
    - Covers: Progressively harder React+TS challenges

16. **Type Challenges — React-Related**
    - URL: https://github.com/type-challenges/type-challenges
    - Format: Type-level puzzles (some applicable to React utility type patterns)
    - Difficulty: Medium-Hard

17. **React TypeScript Practice — Exercism**
    - URL: https://exercism.org/tracks/typescript
    - Format: Mentored exercises (TypeScript track, applicable patterns)

### GitHub Repositories and Open-Source Projects

18. **typescript-cheatsheets/react**
    - URL: https://github.com/typescript-cheatsheets/react
    - Stars: 45k+
    - *The canonical community resource for React+TS patterns*

19. **Radix UI Primitives**
    - URL: https://github.com/radix-ui/primitives
    - *Excellent example of polymorphic components, composition patterns, and typed component APIs in a production design system*

20. **Chakra UI**
    - URL: https://github.com/chakra-ui/chakra-ui
    - *Well-typed component library demonstrating the `as` prop polymorphic pattern at scale*

21. **TanStack Query Source**
    - URL: https://github.com/TanStack/query
    - *Study generic hook patterns and type inference in a widely-used library*

### Community Resources

22. **r/reactjs and r/typescript** — Reddit
    - URL: https://reddit.com/r/reactjs, https://reddit.com/r/typescript
    - Active communities for pattern discussion and troubleshooting

23. **Reactiflux Discord**
    - URL: https://www.reactiflux.com/
    - Active Discord server with TypeScript channels

---

## Learning Path

### Phase 1: Props and Component Basics (4-5 hours)
**Concepts:** Props modeling, optional props, defaults, children typing, extending HTML props, `ComponentProps`

1. Read React official TypeScript guide (https://react.dev/learn/typescript)
2. Work through Total TypeScript React tutorial — props sections
3. Reference React TypeScript Cheatsheet for patterns

**Milestone:** Build a small component library (Button, Card, Input) with properly typed props that extend native HTML attributes.

### Phase 2: Hooks and State Typing (3-4 hours)
**Concepts:** useState typing, useReducer with discriminated union actions, custom hooks, generic hooks, typed return values

1. Total TypeScript React tutorial — hooks sections
2. Build a `useFetch<T>` hook and a `useForm<T>` hook
3. Type a useReducer with action discriminated unions

**Milestone:** Create 3 custom hooks (useFetch, useLocalStorage, useDebounce) with full generic typing and proper return types.

### Phase 3: Context and State Management (2-3 hours)
**Concepts:** Context creation with typed defaults, custom consumer hooks with null guards, reducer-based context, provider typing

1. Build an AuthContext with typed provider and consumer hook
2. Build a ThemeContext with useReducer for state transitions
3. Study the context patterns in React TypeScript Cheatsheet

**Milestone:** Implement a complete auth flow with typed context (login/logout/user state) where consuming components have zero `any` types.

### Phase 4: Advanced Component Patterns (4-5 hours)
**Concepts:** Polymorphic components, generic components, compound components, render props, forwardRef, useImperativeHandle

1. Build a polymorphic `Box` component with the `as` prop pattern
2. Build a generic `<DataTable<T>>` component
3. Build a compound `<Tabs>` component (Tabs + Tab + TabPanel)
4. Study Radix UI source code for real-world examples

**Milestone:** Create a mini design system with polymorphic Button, generic List, and compound Accordion components.

### Phase 5: Event and Ref Typing (2-3 hours)
**Concepts:** Synthetic event types, extracted event handlers, ref typing, forwardRef, useImperativeHandle, React 19 ref changes

1. Type a complex form with multiple input types and event handlers
2. Build a component with forwardRef and useImperativeHandle
3. Understand React 19's ref-as-prop simplification

**Milestone:** Build a form component library where all events are properly typed and refs work for focus management.

### Phase 6: End-to-End API-to-UI Type Safety (3-5 hours)
**Concepts:** Zod schema → type inference, typed fetch, TanStack Query generics, tRPC overview, OpenAPI codegen

1. Build an API integration: Zod schema → validated fetch → typed hook → typed component
2. Set up TanStack Query with proper generic typing
3. (Optional) Explore tRPC for a fullstack TypeScript project

**Milestone:** Build a complete feature (e.g., user list with search/filter) where types flow from API schema definition through to rendered UI components with zero type gaps.

---

## Practical Exercises

### Exercise 1: Typed Component Library (Beginner)
Build a small component library with:
- `Button` extending `<button>` props with `variant` and `size`
- `Input` extending `<input>` props with `label` and `error`
- `Card` with `title`, `children`, and optional `footer` render prop
- All components use `ComponentProps` to inherit HTML attributes

### Exercise 2: Generic Data Components (Intermediate)
Build:
- `<DataTable<T>>` — generic table with typed columns and row data
- `<Select<T>>` — generic select with typed options and onChange
- `<Autocomplete<T>>` — generic autocomplete with typed suggestions

### Exercise 3: Typed State Management (Intermediate)
Implement a shopping cart:
- Cart context with typed state and discriminated union actions
- useReducer with `ADD_ITEM | REMOVE_ITEM | UPDATE_QUANTITY | CLEAR` actions
- Custom `useCart()` hook with null guard
- CartProvider with properly typed children

### Exercise 4: Polymorphic Design System (Advanced)
Build a polymorphic component system:
- Base `Box` component with `as` prop supporting any HTML element
- `Button` extending Box with button-specific props
- `Link` extending Box with anchor-specific props
- Ensure TypeScript errors when passing invalid props for the rendered element

### Exercise 5: Full API-to-UI Pipeline (Advanced)
Build a user management feature:
1. Define Zod schemas for User, CreateUserInput, UpdateUserInput
2. Create typed API client functions with Zod validation
3. Build TanStack Query hooks: `useUsers()`, `useUser(id)`, `useCreateUser()`
4. Build UI components that consume the hooks with full type safety
5. Demonstrate that changing the Zod schema propagates type errors to the UI

### Exercise 6: React 19 Patterns (Advanced)
Refactor existing components for React 19:
- Remove `forwardRef` wrappers, use `ref` as a regular prop
- Implement a form with `useActionState` and typed actions
- Create Server Component types (serializable props only)

---

## Connections to Other Domains

### Depends On
- **D-1 (Foundations):** Structural typing, unions, inference, narrowing — all used constantly in React typing
- **D-3 (Type Modeling):** Discriminated unions for props and actions, utility types for props transformation, branded types for IDs
- **D-4 (Runtime Boundaries):** Zod validation at API boundaries, schema-to-type derivation, `unknown` handling
- **D-5 (Generics):** Generic components, generic hooks, constrained generics in component APIs

### Feeds Into
- **D-7 (Backend Workflows):** End-to-end type sharing strategies, tRPC patterns work across frontend and backend
- **D-12 (Team Practices):** Component API design standards, when to use advanced patterns vs simple props

### Cross-Cutting
- **D-2 (Strictness):** Strict mode catches more React typing issues; `noUncheckedIndexedAccess` affects array rendering patterns
- **D-8 (Tooling):** VS Code IntelliSense for React props, ESLint rules for hooks, testing typed components
- **D-9 (Refactoring):** Rename safety for props, migration from PropTypes to TypeScript, migrating class components to typed function components

---

## Source Freshness Notes

- React 19 was released December 2024. Patterns for `ref` as prop, `use()` hook, and Server Components are current.
- TanStack Query v5 is current (2024). Typing patterns documented here reflect v5.
- tRPC v11 is current (2024-2025). The React Query adapter approach is the recommended integration.
- `@types/react` v19 aligns with React 19. Some patterns (especially `forwardRef`) differ from React 18.
- The React TypeScript Cheatsheet was last updated November 2024.
- Total TypeScript content is continuously updated by Matt Pocock (2024-2025).
- Steve Kinney's Frontend Masters course covers React 19 patterns (2024).
