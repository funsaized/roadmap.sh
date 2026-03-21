# Knowledge Map: Modern Python Flask API Development

## Overview

This knowledge map catalogs **78 unique concepts** across 12 domains (D-1 through D-12, with D-13 as capstone), organized by difficulty progression. Concepts that appear across multiple domains are deduplicated and cross-referenced.

---

## Section 1: Foundations (Beginner)

### Domain 1: Python Foundations for Web Development

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-1 | Virtual Environments (venv) | Isolated Python environments for dependency management | — |
| C-2 | Package Management (pip) | Installing and managing Python packages | C-1 |
| C-3 | Dependency Locking (pip-tools) | Reproducible builds with pinned dependencies | C-2 |
| C-4 | Modern Package Management (Poetry/uv) | All-in-one dependency management with lockfiles | C-2 |
| C-5 | pyproject.toml | Modern Python project configuration standard | C-2 |
| C-6 | Type Hints and typing Module | Static type annotations for Python code | — |
| C-7 | Static Type Checking (mypy) | Compile-time type verification | C-6 |
| C-8 | First-Class Functions & Closures | Functions as objects, variable capture in inner functions | — |
| C-9 | Decorators | Function wrapping for cross-cutting behavior | C-8 |
| C-10 | Context Managers | Setup/teardown with `with` statement | — |
| C-11 | Python Project Structure | Package layout and module organization conventions | C-5 |
| C-12 | Environment Variable Configuration | Externalizing config with dotenv/decouple | — |

### Domain 2: HTTP and REST Fundamentals

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-13 | HTTP Protocol Basics | Request/response cycle, URLs, HTTP messages | — |
| C-14 | HTTP Methods | GET, POST, PUT, PATCH, DELETE and their semantics | C-13 |
| C-15 | HTTP Status Codes | 1xx–5xx categories and common codes for APIs | C-13 |
| C-16 | HTTP Headers | Request/response metadata, content negotiation | C-13 |
| C-17 | Idempotency and Safety | Method properties for reliable API design | C-14 |
| C-18 | REST Architectural Constraints | Client-server, statelessness, cacheability, uniform interface, HATEOAS | C-13 |
| C-19 | JSON Data Format | Structure, types, Python json module integration | — |
| C-20 | API Design Principles | Resource-based URLs, naming conventions, versioning basics | C-14, C-18 |

---

## Section 2: Flask Core (Beginner–Intermediate)

### Domain 3: Flask Core Fundamentals

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-21 | Flask Application Object | Central app instance, configuration, route registration | C-11, C-13 |
| C-22 | Application Factory Pattern | `create_app()` for configurable app creation | C-21, C-12 |
| C-23 | Routing and URL Rules | URL-to-view mapping, variable rules, converters | C-21, C-14 |
| C-24 | Blueprints | Modular application organization with URL prefixing | C-22, C-23 |
| C-25 | Application Context | `current_app`, `g` proxy objects for app-level data | C-22 |
| C-26 | Request Context | `request`, `session` proxy objects for request-level data | C-25 |
| C-27 | Configuration Management | `app.config`, config classes, environment-based loading | C-22, C-12 |
| C-28 | Flask CLI and Click | Custom commands, command groups, Click integration | C-22 |
| C-29 | Extension Initialization Pattern | Two-phase `init_app()` for factory compatibility | C-22 |
| C-30 | WSGI Basics | Flask as WSGI app, development server limitations | C-21 |
| C-31 | Error Handling Basics | `@errorhandler`, `abort()`, custom error pages | C-23 |

---

## Section 3: API Development (Intermediate)

### Domain 4: Request Handling and Data Validation

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-32 | Flask Request Object | `request.args`, `.json`, `.form`, `.files`, `.headers` | C-26 |
| C-33 | Marshmallow Validation | Schema-based serialization, deserialization, field validators | C-32, C-6 |
| C-34 | Pydantic Validation | Type-hint-based validation with BaseModel | C-32, C-6 |
| C-35 | Webargs Library | Request argument parsing from multiple locations | C-33 |
| C-36 | Flask-Smorest Integration | Marshmallow + webargs + auto-OpenAPI documentation | C-33, C-35, C-24 |
| C-37 | Structured Error Handling | Custom exceptions, consistent JSON error format, ValidationError handling | C-31, C-33 |
| C-38 | Request Hooks | `before_request`, `after_request`, `teardown_request`, `g` object | C-26 |
| C-39 | File Upload Handling | `request.files`, `secure_filename`, size limits | C-32 |

### Domain 5: Database Integration and ORMs

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-40 | SQLAlchemy Core vs ORM | Two-layer architecture, Flask-SQLAlchemy wrapper | C-29 |
| C-41 | Model Definition | `db.Model`, column types, constraints, indexes | C-40 |
| C-42 | Relationship Types | One-to-many, many-to-many, one-to-one, self-referential | C-41 |
| C-43 | Lazy Loading Strategies | select, joined, subquery, selectin, dynamic, raise | C-42 |
| C-44 | N+1 Query Problem and Eager Loading | Detection and fixes with joinedload/selectinload | C-43 |
| C-45 | Query Construction and Filtering | filter(), filter_by(), order_by(), pagination | C-41 |
| C-46 | Session and Transaction Management | add, commit, rollback, flush, scoped sessions, savepoints | C-40 |
| C-47 | Database Migrations (Alembic/Flask-Migrate) | Schema versioning, upgrade/downgrade workflow | C-41 |
| C-48 | Connection Pooling | Pool size, overflow, recycle configuration | C-40 |

### Domain 6: Authentication and Authorization

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-49 | Password Hashing | bcrypt, Argon2, PBKDF2, Werkzeug security helpers | C-41 |
| C-50 | JWT Authentication | Token structure, Flask-JWT-Extended, access/refresh tokens | C-38, C-37 |
| C-51 | Token Lifecycle Management | Refresh, rotation, blocklisting, fresh tokens, reuse detection | C-50 |
| C-52 | OAuth 2.0 and OpenID Connect | Authorization flows, Authlib, social login | C-50 |
| C-53 | API Key Authentication | Generation, hashed storage, validation decorators | C-38 |
| C-54 | Role-Based Access Control (RBAC) | User-Role-Permission models, custom decorators, JWT claims | C-50, C-42 |
| C-55 | CSRF Protection | Token-based protection for cookie auth, SameSite cookies | C-50 |

### Domain 7: API Design and Documentation

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-56 | OpenAPI Specification | Standardized API description format (OAS 3.1) | C-20 |
| C-57 | Swagger UI and ReDoc | Interactive documentation renderers | C-56 |
| C-58 | Flask-RESTX | Namespaces, models, auto-Swagger generation | C-24, C-56 |
| C-59 | Pagination Strategies | Offset-based, cursor-based, keyset pagination | C-45 |
| C-60 | Filtering and Sorting | Query parameter-based data filtering with field whitelisting | C-45 |
| C-61 | API Versioning | URI, header, query param, content negotiation strategies | C-24, C-56 |
| C-62 | HATEOAS and Hypermedia | Response links for API discoverability | C-18 |

### Domain 8: Testing Flask APIs

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-63 | Flask Test Client | `app.test_client()` for simulated HTTP requests | C-22 |
| C-64 | Pytest Fixtures and conftest.py | Setup/teardown, scopes, shared fixtures | C-63 |
| C-65 | Test Database Isolation | In-memory SQLite, transactional rollback, Factory Boy | C-64, C-46 |
| C-66 | Mocking External Services | unittest.mock, responses library, requests-mock | C-64 |
| C-67 | Coverage Measurement | pytest-cov, branch coverage, CI integration | C-64 |

---

## Section 4: Production Engineering (Advanced)

### Domain 9: Background Tasks and Async Patterns

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-68 | Message Broker Architecture | Producer-broker-worker pattern with Redis/RabbitMQ | C-25 |
| C-69 | Celery Fundamentals | Tasks, workers, Beat scheduler, Flask integration | C-68, C-22 |
| C-70 | Task Invocation and Canvas | delay(), apply_async(), chain, group, chord | C-69 |
| C-71 | Retry and Failure Handling | Exponential backoff, jitter, idempotency, acks_late, time limits | C-69 |
| C-72 | Flask Async Views | async def routes with asyncio (Flask 2.0+) | C-23 |

### Domain 10: Security Hardening

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-73 | OWASP API Security Top 10 | Framework for understanding API-specific security risks | C-54, C-37 |
| C-74 | CORS Configuration | Flask-CORS, origin whitelisting, preflight handling | C-16, C-55 |
| C-75 | Rate Limiting | Flask-Limiter, strategies, keying, Redis backend | C-38, C-53 |
| C-76 | Security Headers | Flask-Talisman, HSTS, CSP, X-Content-Type-Options | C-16 |
| C-77 | Secret Management | dotenv, platform env vars, HashiCorp Vault | C-12, C-27 |
| C-78 | Dependency Vulnerability Scanning | pip-audit, Bandit (SAST), Safety, CI integration | C-3 |

### Domain 11: Deployment and Infrastructure

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-79 | WSGI Servers (Gunicorn) | Worker processes, threading, configuration | C-30 |
| C-80 | Docker Containerization | Dockerfiles, multi-stage builds, Docker Compose | C-79 |
| C-81 | Nginx Reverse Proxy | Proxying, static files, SSL termination, load balancing | C-80 |
| C-82 | 12-Factor App Methodology | Principles for portable, scalable applications | C-77, C-27 |
| C-83 | Structured Logging | JSON logs, correlation IDs, log aggregation | C-80 |
| C-84 | CI/CD Pipelines | GitHub Actions, automated test/build/deploy workflows | C-67, C-80 |
| C-85 | Cloud Deployment Strategies | PaaS, IaaS, container services, serverless, Kubernetes | C-80, C-81 |

### Domain 12: Performance and Observability

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-86 | Multi-Layer Caching | Flask-Caching, Redis, HTTP caching headers, invalidation | C-48, C-69 |
| C-87 | Database Query Profiling | SQLALCHEMY_ECHO, slow query detection, EXPLAIN ANALYZE | C-44, C-48 |
| C-88 | OpenTelemetry Tracing | Auto/manual instrumentation, distributed context, exporters | C-83 |
| C-89 | Prometheus Metrics | Counters, gauges, histograms, Grafana dashboards, alerting | C-83 |
| C-90 | Load Testing | Locust, k6, test types, CI integration | C-84 |
| C-91 | Application Profiling | cProfile, py-spy, flame graphs, memory profiling | C-79 |

---

## Section 5: Architecture (Expert)

### Domain 13: Advanced Architectural Patterns

| ID | Concept | Description | Prerequisites |
|----|---------|-------------|---------------|
| C-92 | Service Layer Pattern | Business logic separation from route handlers | C-24, C-46 |
| C-93 | Repository Pattern | Data access abstraction behind clean interfaces | C-40, C-92 |
| C-94 | Dependency Injection | IoC containers, provider types, request scoping | C-92, C-93 |
| C-95 | Domain-Driven Design | Entities, value objects, aggregates, bounded contexts | C-92 |
| C-96 | Event-Driven Architecture | Domain events, event bus, CQRS, event sourcing | C-95, C-69 |
| C-97 | GraphQL with Flask | Strawberry/Ariadne, resolvers, DataLoader, subscriptions | C-92 |
| C-98 | Microservice Decomposition | Bounded context extraction, API gateway, service discovery | C-95, C-96, C-85 |
| C-99 | Circuit Breaker Pattern | Resilience pattern for inter-service calls (pybreaker) | C-98 |
| C-100 | Hexagonal/Clean Architecture | Ports and adapters, dependency rule, layered structure | C-92, C-93, C-94 |

---

## Cross-Domain Concept Appearances

The following concepts appear meaningfully across multiple domains and have been unified:

| Concept | Primary Domain | Also Appears In |
|---------|---------------|-----------------|
| Decorators | D-1 | D-3 (routing), D-6 (auth), D-7 (API docs), D-10 (rate limiting) |
| Type Hints | D-1 | D-4 (Pydantic), D-5 (model typing), D-7 (OpenAPI) |
| Context Managers | D-1 | D-3 (app/request context), D-5 (sessions), D-8 (test fixtures) |
| Error Handling | D-3 | D-4 (validation errors), D-6 (auth errors), D-10 (security errors) |
| Configuration | D-1/D-3 | D-5 (DB URI), D-10 (secrets), D-11 (12-Factor) |
| Request Hooks | D-4 | D-6 (auth middleware), D-10 (rate limiting), D-12 (tracing) |
| N+1 Problem | D-5 | D-12 (query profiling), D-13 (GraphQL DataLoader) |
| Input Validation | D-4 | D-10 (sanitization), D-6 (auth input) |
| Application Factory | D-3 | D-8 (test instances), D-11 (WSGI entry), D-9 (Celery init) |
| Logging | D-11 | D-12 (observability), D-9 (task monitoring) |
