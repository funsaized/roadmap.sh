# Visual Layout Specification — Modern Python Flask API Development Roadmap

## Overview

A vertical-flow interactive roadmap inspired by roadmap.sh, rendering 104 nodes (100 content + 4 checkpoint) across 5 major sections with 15 sub-sections. The layout uses a 1400px-wide canvas with nodes arranged in up to 4 columns per sub-section row, flowing top-to-bottom through progressive difficulty levels.

## Layout Dimensions

| Property | Value |
|----------|-------|
| Total Width | 1400px |
| Total Height | ~4610px |
| Node Width | 260px |
| Node Height | 56px (regular), 72px (expandable) |
| Column Count | 4 max |
| Section Gap | 80px |
| Node Gap | 20px vertical, 30px horizontal |

## Color Scheme

### Difficulty Colors
- **Beginner** (#4CAF50): Green background (#E8F5E9), green border
- **Intermediate** (#2196F3): Blue background (#E3F2FD), blue border
- **Advanced** (#FF9800): Orange background (#FFF3E0), orange border
- **Expert** (#F44336): Red background (#FFEBEE), red border

### Special Node Styles
- **Milestone** (★): Gold badge, 3px border, trophy icon (🏆)
- **Optional**: Dashed border, 80% opacity
- **Checkpoint** (✓): Purple background (#F3E5F5), purple border (#9C27B0), 3px border

## Section Layout (Top to Bottom)

```
┌──────────────────────────────────────────────────────────────────────┐
│  SECTION 1: FOUNDATIONS (beginner, ~35h)                             │
│  ┌─ Package & Environment ──────────────────────────────────────┐    │
│  │  [venv] → [pip] → [pip-tools]  [Poetry/uv]  [pyproject.toml]│    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Python Language ────────────────────────────────────────────┐    │
│  │  [Type Hints] → [mypy]   [Functions] → [Decorators★] [CtxMgr]│   │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Project Setup ──────────────────────────────────────────────┐    │
│  │  [Project Structure]  [Env Vars]                              │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ HTTP & REST ────────────────────────────────────────────────┐    │
│  │  [HTTP Basics] → [Methods] → [Idempotency]                   │    │
│  │               → [Status Codes]  [Headers]                     │    │
│  │               → [REST★] → [API Design]                        │    │
│  │  [JSON]                                                       │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ╔══════════════════════════════════════════════════════════════╗    │
│  ║  ✓ Python & HTTP Foundations Complete                        ║    │
│  ╚══════════════════════════════════════════════════════════════╝    │
├──────────────────────────────────────────────────────────────────────┤
│  SECTION 2: FLASK CORE (beginner→intermediate, ~23h)                 │
│  ┌─ App Basics ─────────────────────────────────────────────────┐    │
│  │  [Flask App] → [Factory★] → [Routing]  [WSGI]               │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Organization ──────────────────────────────────────────────┐    │
│  │  [Blueprints★]  [Extensions]  [Error Handling]               │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Contexts & Config ─────────────────────────────────────────┐    │
│  │  [App Context] → [Req Context]  [Config Mgmt]  [CLI/Click]  │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ╔══════════════════════════════════════════════════════════════╗    │
│  ║  ✓ Flask Core Mastery                                        ║    │
│  ╚══════════════════════════════════════════════════════════════╝    │
├──────────────────────────────────────────────────────────────────────┤
│  SECTION 3: API DEVELOPMENT (intermediate, ~112h)                    │
│  ┌─ Request Handling ──────────────────────────────────────────┐    │
│  │  [Request Obj] → [Marshmallow★] → [Webargs] → [Smorest★]   │    │
│  │               → [Pydantic]                                    │    │
│  │  [Error Handling] [Req Hooks] [File Upload]                   │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Database ──────────────────────────────────────────────────┐    │
│  │  [SQLAlchemy] → [Models] → [Relations] → [Lazy] → [N+1★]   │    │
│  │             → [Sessions]  [Queries] → [Pagination] [Filter]  │    │
│  │             → [Pool]      [Migrations★]                       │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Authentication ────────────────────────────────────────────┐    │
│  │  [Passwords] [JWT★] → [Token Lifecycle] [OAuth] [API Keys]  │    │
│  │              [RBAC★] [CSRF]                                   │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ API Design ────────────────────────────────────────────────┐    │
│  │  [OpenAPI] → [Swagger/ReDoc] [RESTX] [Versioning]           │    │
│  │  [Pagination] [Filtering] [HATEOAS]                          │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Testing ───────────────────────────────────────────────────┐    │
│  │  [Test Client] → [Pytest★] → [DB Isolation] [Mocking]       │    │
│  │                            → [Coverage]                       │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ╔══════════════════════════════════════════════════════════════╗    │
│  ║  ✓ API Development Proficiency                               ║    │
│  ╚══════════════════════════════════════════════════════════════╝    │
├──────────────────────────────────────────────────────────────────────┤
│  SECTION 4: PRODUCTION ENGINEERING (advanced, ~90h)                  │
│  ┌─ Background Tasks ─────────────────────────────────────────┐    │
│  │  [Broker Arch] → [Celery★] → [Canvas] [Retry]  [Async]     │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Security ──────────────────────────────────────────────────┐    │
│  │  [OWASP★] [CORS] [Rate Limit] [Sec Headers] [Secrets] [Scan]│    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Deployment ────────────────────────────────────────────────┐    │
│  │  [Gunicorn] → [Docker★] → [Nginx]  [12-Factor]              │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Observability ─────────────────────────────────────────────┐    │
│  │  [Logging] → [OTel] [Prometheus]                              │    │
│  │  [CI/CD★] → [Cloud Deploy] [Load Test]                       │    │
│  │  [Caching] [DB Profiling] [App Profiling]                     │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ╔══════════════════════════════════════════════════════════════╗    │
│  ║  ✓ Production-Ready Engineer                                 ║    │
│  ╚══════════════════════════════════════════════════════════════╝    │
├──────────────────────────────────────────────────────────────────────┤
│  SECTION 5: ARCHITECTURE (expert, ~50h)                              │
│  ┌─ Design Patterns ──────────────────────────────────────────┐    │
│  │  [Service Layer] → [Repository] → [DI] → [Hex/Clean Arch]  │    │
│  └──────────────────────────────────────────────────────────────┘    │
│  ┌─ Advanced Architecture ─────────────────────────────────────┐    │
│  │  [DDD★] → [Event-Driven] → [Microservices★] → [Circuit Brk]│    │
│  │  [GraphQL]                                                    │    │
│  └──────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────┘
```

## Interactive Behavior

### Node Click → Detail Panel
- Slides in from right (400px wide)
- Shows: title, description, key concepts (tags), estimated hours
- Resources listed by type, recommended first
- Each resource has badges: difficulty, format, cost, time

### Progress Tracking
- Each node has a checkbox (persisted to localStorage)
- Section headers show "X of Y complete" progress bar
- Top banner shows overall "X% complete"
- Nodes with incomplete prerequisites show lock icon and reduced opacity

### Edge Rendering
- SVG connector lines between prerequisite and dependent nodes
- Straight lines for vertically adjacent nodes
- L-shaped paths for nodes in different columns
- Arrow heads on dependent end
- Color matches source node difficulty

## File Outputs

| File | Purpose |
|------|---------|
| `layout-spec.md` | This document — visual design specification |
| `roadmap-final.json` | Complete renderable data with coordinates, colors, styles, resources |
