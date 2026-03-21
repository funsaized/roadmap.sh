# Background Tasks and Async Patterns

## Overview

This domain covers asynchronous task processing and background job management in Flask applications. As Flask is a WSGI framework, handling long-running operations within the request-response cycle blocks workers and degrades user experience. This domain teaches how to offload work to background task queues (primarily Celery), leverage Flask's async view support (since Flask 2.0), implement retry and failure handling strategies, and track task results. These patterns are essential prerequisites for D-12 (Performance and Observability) and D-13 (Advanced Architectural Patterns).

**Prerequisites from completed domains:** D-5 (Database Integration — understanding ORM sessions in task context), D-6 (Authentication — securing task-triggering endpoints).

---

## Key Concepts

### 1. Message Broker Architecture
The foundational pattern for background tasks: a **producer** (Flask app) sends messages to a **broker** (Redis or RabbitMQ), which holds them until a **worker** (Celery process) picks them up for execution. This decouples task submission from task execution.

### 2. Celery Fundamentals
- **Celery Application**: The central object that coordinates task registration, broker connection, and worker configuration
- **Tasks**: Python functions decorated with `@celery.task` or `@shared_task` that run asynchronously in worker processes
- **Workers**: Separate processes that consume tasks from the broker queue and execute them
- **Beat Scheduler**: A Celery process that sends periodic tasks at configured intervals (cron-like scheduling)

### 3. Flask-Celery Integration
- **Application Factory Pattern**: Creating a `celery_init_app()` function that initializes Celery with Flask's config and wraps task execution in Flask's application context via a custom `FlaskTask` class
- **`shared_task` Decorator**: Preferred over `@celery_app.task` when using the factory pattern — avoids circular imports and accesses the "current app"
- **Application Context in Tasks**: Tasks run in separate processes without Flask's app context; the `FlaskTask` wrapper ensures `app.app_context()` is available for database access, config, etc.
- **`make_celery.py`**: Entry point file for the `celery` CLI to locate the Celery app when using the factory pattern

### 4. Message Brokers
- **Redis**: Simple to set up, commonly used for both broker and result backend, suitable for small-to-medium workloads
- **RabbitMQ**: More robust with advanced routing, clustering, and delivery guarantees — ideal for large-scale deployments
- **Broker selection criteria**: Throughput, persistence, routing complexity, operational familiarity

### 5. Result Backends and Task Tracking
- **Result Backend**: Storage system (Redis, PostgreSQL via SQLAlchemy, Memcached) where Celery persists task state and return values
- **`AsyncResult`**: Object returned by `.delay()` that provides task status (`PENDING`, `STARTED`, `SUCCESS`, `FAILURE`, `RETRY`) and result retrieval
- **Custom Progress States**: Using `self.update_state(state='PROGRESS', meta={'current': 50, 'total': 100})` for granular progress reporting
- **`result_expires`**: Configuration to auto-clean old results from the backend

### 6. Task Invocation Patterns
- **`.delay(*args)`**: Simple shortcut for sending tasks to the broker
- **`.apply_async()`**: Full control over execution — countdown, eta, queue routing, retry policy, expiration
- **Canvas Primitives**: `chain()` (sequential), `group()` (parallel), `chord()` (parallel + callback), `starmap()` for complex workflows

### 7. Retry Strategies
- **Manual Retry**: `self.retry(exc=exc, countdown=60, max_retries=5)` inside try-except blocks
- **Automatic Retry**: `autoretry_for=(ConnectionError, TimeoutError)` in the decorator
- **Exponential Backoff**: `retry_backoff=True` (delays: 1s, 2s, 4s, 8s...) with optional `retry_backoff_max`
- **Jitter**: `retry_jitter=True` adds randomness to prevent thundering herd on simultaneous retries

### 8. Failure Handling and Reliability
- **Idempotency**: Designing tasks that produce the same result regardless of how many times they execute — critical for safe retries
- **Late Acknowledgment (`acks_late=True`)**: Task is ACK'd only after completion, so crashed workers don't lose tasks
- **Time Limits**: `soft_time_limit` raises `SoftTimeLimitExceeded` for graceful cleanup; `time_limit` force-kills
- **Dead Letter Queues**: Broker-level mechanism to capture unprocessable messages for inspection
- **Error Tracking Integration**: Sentry, Datadog, or custom alerting for task failures

### 9. Flask Async Views (Flask 2.0+)
- **Installation**: `pip install "Flask[async]"` installs `asgiref` dependency
- **Usage**: Define routes with `async def` and use `await` for non-blocking I/O
- **How it works**: Flask runs async views in a sub-thread with its own asyncio event loop
- **Limitations**: Still WSGI — each request ties up one worker; doesn't increase overall concurrency; `asyncio.create_task()` background tasks may be cancelled when view completes
- **When to use**: Multiple concurrent I/O calls within a single request (e.g., `asyncio.gather()` for parallel API calls)
- **When NOT to use**: CPU-bound work, true background tasks (use Celery instead)

### 10. Alternative Task Queue Systems
- **RQ (Redis Queue)**: Lightweight, Redis-only, simpler API — good for small projects
- **Huey**: Minimal Redis-based task queue with built-in scheduling
- **Dramatiq**: Fast, modern alternative focusing on simplicity and reliability
- **APScheduler / Flask-APScheduler**: In-process scheduler for periodic tasks (no separate broker needed)

### 11. Monitoring and Observability
- **Flower**: Web-based real-time monitoring dashboard for Celery workers and tasks
- **Celery CLI Inspection**: `celery inspect active`, `celery inspect stats`, `celery inspect registered`
- **Prometheus + Grafana**: Metrics collection and visualization for production monitoring
- **Queue Length Monitoring**: Detecting backlogs and scaling workers accordingly

### 12. Production Best Practices
- **Pass IDs, not objects**: Send primary keys to tasks, let tasks fetch data from DB
- **Keep tasks short**: Break complex work into smaller chained tasks
- **Multiple queues**: Separate critical tasks from bulk processing
- **Worker management**: `worker_max_tasks_per_child` to prevent memory leaks; autoscaling with `--autoscale`
- **Graceful shutdown**: `SIGTERM` handling during deployments
- **Backwards-compatible task signatures**: Default values for new arguments during rolling deploys

### Concept Relationships
- Message Broker Architecture → underpins Celery Fundamentals → enables Flask-Celery Integration
- Result Backends → enables Task Tracking → feeds into Monitoring
- Retry Strategies + Failure Handling → together ensure Reliability
- Flask Async Views are complementary to (not a replacement for) Celery task queues
- Canvas Primitives build on basic Task Invocation patterns for complex workflows

### Cross-Domain Prerequisites
- **For D-12 (Performance and Observability)**: Monitoring patterns, Flower/Prometheus integration, queue optimization
- **For D-13 (Advanced Architectural Patterns)**: Canvas workflows, event-driven architecture, CQRS with task queues

---

## Learning Resources

### Official Documentation
1. **Flask — Background Tasks with Celery** — Official Flask documentation pattern for Celery integration, including factory pattern setup and `FlaskTask` wrapper.
   - URL: https://flask.palletsprojects.com/en/stable/patterns/celery/
   - Type: Documentation | Free | Difficulty: Intermediate

2. **Flask — Async/Await Support** — Official docs on using async views in Flask 2.0+.
   - URL: https://flask.palletsprojects.com/en/stable/async-await/
   - Type: Documentation | Free | Difficulty: Intermediate

3. **Celery User Guide — Tasks** — Comprehensive reference for task definition, retry configuration, states, and best practices.
   - URL: https://docs.celeryq.dev/en/main/userguide/tasks.html
   - Type: Documentation | Free | Difficulty: Intermediate–Advanced

4. **Celery User Guide — Canvas (Workflows)** — Documentation on chains, groups, chords, and other workflow primitives.
   - URL: https://docs.celeryq.dev/en/main/userguide/canvas.html
   - Type: Documentation | Free | Difficulty: Advanced

5. **Celery Configuration Reference** — Complete configuration options for brokers, backends, workers, and task behavior.
   - URL: https://docs.celeryq.dev/en/main/userguide/configuration.html
   - Type: Documentation | Free | Difficulty: Intermediate–Advanced

### Online Courses
6. **The Definitive Guide to Celery and Flask** — TestDriven.io
   - URL: https://testdriven.io/courses/flask-celery/
   - Platform: TestDriven.io | Paid (~$40) | Estimated Duration: 8–10 hours
   - Covers: Docker containerization, WebSocket support, periodic tasks, multiple queues, retries, Flower monitoring, testing with pytest. Updated for Flask 3.0.3 and Celery 5.4.0.
   - Difficulty: Intermediate–Advanced

7. **Asynchronous Tasks with Flask and Celery** — TestDriven.io (free tutorial)
   - URL: https://testdriven.io/blog/flask-and-celery/
   - Platform: TestDriven.io | Free | Estimated Duration: 2–3 hours
   - Covers: Basic integration, Docker + Redis, background processes, Flower monitoring, testing.
   - Difficulty: Intermediate

8. **Async Views in Flask** — TestDriven.io (free tutorial)
   - URL: https://testdriven.io/blog/flask-async/
   - Platform: TestDriven.io | Free | Estimated Duration: 1–2 hours
   - Covers: Flask async/await support, performance considerations, when to use async vs task queues.
   - Difficulty: Intermediate

### Video Tutorials and Conference Talks
9. **"Mixing reliability with Celery for delicious async tasks"** — Flávio Juvenal, DjangoCon US 2023
   - URL: https://www.youtube.com/watch?v=VuONiF99Oqc
   - Duration: ~30 min | Difficulty: Advanced
   - Focus: Production reliability patterns, failure handling, real-world Celery usage

10. **"Intro to Celery: Development and Productionizing"** — YouTube (Jan 2025)
    - URL: https://www.youtube.com/watch?v=VRHVEporra0
    - Duration: ~45 min | Difficulty: Beginner–Intermediate
    - Focus: From local development to GKE deployment

11. **"Getting Started With Celery: Asynchronous Tasks in Python"** — YouTube (Mar 2025)
    - URL: https://www.youtube.com/watch?v=c8WgtttXu5w
    - Duration: ~30 min | Difficulty: Beginner
    - Focus: First steps with Celery for background tasks

### Books
12. **"Flask Web Development" by Miguel Grinberg** — O'Reilly, 2nd Edition
    - Relevant: Chapter on background tasks, email sending with Celery
    - Companion repo with Celery: https://github.com/miguelgrinberg/flasky-with-celery
    - Difficulty: Intermediate

13. **"Architecture Patterns with Python" by Harry Percival & Bob Gregory** — O'Reilly, 2020
    - Relevant: Chapters on event-driven architecture, message buses, and async patterns applicable to task queue design
    - Difficulty: Advanced

### Blog Posts and Articles
14. **"Celery Best Practices: A Practical Approach"** — Azat Khashtamov
    - URL: https://khashtamov.com/en/celery-best-practices-practical-approach/
    - Covers: Idempotency, task design, monitoring, production tips

15. **"Celery Best Practices"** — Deni Bertović
    - URL: https://denibertovic.com/posts/celery-best-practices/
    - Classic reference on task design patterns

16. **"5 Tips for Writing Production-Ready Celery Tasks"** — Wolt Engineering
    - URL: https://careers.wolt.com/en/blog/tech/5-tips-for-writing-production-ready-celery-tasks
    - Focus: Real-world production patterns from a high-scale company

17. **"Celery Tasks Checklist"** — DevChecklists
    - URL: https://devchecklists.com/en/checklist/celery-tasks-checklist
    - Quick reference checklist for task implementation

18. **"The Ultimate Guide to Celery in Python"** — Deepnote
    - URL: https://deepnote.com/blog/ultimate-guide-to-celery-library-in-python
    - Comprehensive guide covering architecture, best practices, and scaling

### GitHub Repositories
19. **miguelgrinberg/flask-celery-example** — Example Flask app with Celery for async email and progress tracking
    - URL: https://github.com/miguelgrinberg/flask-celery-example
    - Good for: Seeing a complete, working Flask+Celery integration

20. **celery/celery** — Celery source code and examples
    - URL: https://github.com/celery/celery
    - Good for: Understanding internals, reading example configurations

21. **mher/flower** — Real-time Celery monitoring tool
    - URL: https://github.com/mher/flower
    - Good for: Learning monitoring setup, studying the project's architecture

### Community Resources
22. **r/flask** and **r/Python** — Reddit communities with active Celery + Flask discussions
    - URL: https://www.reddit.com/r/flask/ and https://www.reddit.com/r/Python/
23. **Full Stack Python — Task Queues** — Curated overview of Python task queue options
    - URL: https://www.fullstackpython.com/task-queues.html
24. **Stack Overflow — [celery] tag** — Large Q&A archive for Celery troubleshooting
    - URL: https://stackoverflow.com/questions/tagged/celery

---

## Learning Path

### Phase 1: Foundations (3–4 hours)
**Concepts:** Message broker architecture, Celery fundamentals, Redis as broker
**Activities:**
1. Read Flask's official Celery pattern docs (#1)
2. Watch "Getting Started With Celery" video (#11)
3. Set up Redis locally (Docker) and create a minimal Celery app

**Milestone:** Can define a simple task, send it via `.delay()`, and see it execute in a Celery worker.

### Phase 2: Flask Integration (3–4 hours)
**Concepts:** Flask-Celery integration, application factory pattern, app context in tasks, `shared_task`
**Activities:**
1. Follow the TestDriven.io free tutorial (#7)
2. Study `miguelgrinberg/flask-celery-example` repo (#19)
3. Build a Flask app with Celery using the factory pattern and `make_celery.py`

**Milestone:** Flask API endpoint triggers Celery task; task accesses Flask app context (e.g., database).

### Phase 3: Result Tracking and Async Views (3–4 hours)
**Concepts:** Result backends, `AsyncResult`, custom progress states, Flask async views
**Activities:**
1. Read Celery result backend docs and configure Redis result backend
2. Implement a `/task-status/<id>` endpoint with progress reporting
3. Read Flask async/await docs (#2) and TestDriven.io async tutorial (#8)
4. Create async views for parallel I/O calls

**Milestone:** Can poll task status with progress percentage; understand when to use async views vs. Celery.

### Phase 4: Retry and Failure Handling (3–4 hours)
**Concepts:** Manual/automatic retries, exponential backoff, jitter, idempotency, time limits, `acks_late`
**Activities:**
1. Read Celery Tasks user guide section on retries (#3)
2. Study the Wolt blog post (#16) and Celery best practices posts (#14, #15)
3. Implement tasks with `autoretry_for`, backoff, and time limits
4. Simulate failures and verify retry behavior

**Milestone:** Tasks retry with exponential backoff on transient errors; hard failures are logged and don't block the queue.

### Phase 5: Advanced Patterns and Production (4–5 hours)
**Concepts:** Canvas workflows, Beat scheduler, multiple queues, monitoring, production best practices
**Activities:**
1. Read Canvas documentation (#4) and implement a chain + chord workflow
2. Set up Celery Beat for periodic tasks
3. Configure multiple queues with dedicated workers
4. Install and explore Flower (#21) for monitoring
5. Review the DevChecklists checklist (#17)

**Milestone:** Running a production-like setup with periodic tasks, prioritized queues, monitoring dashboard, and robust error handling.

**Total estimated time: 16–21 hours**

---

## Practical Exercises

### Exercise 1: Email Queue (Beginner)
Build a Flask API with a `/send-email` endpoint that queues an email-sending task via Celery + Redis. The endpoint returns immediately with a task ID. Implement a `/status/<id>` endpoint to check delivery status.

### Exercise 2: Image Processing Pipeline (Intermediate)
Create an image upload endpoint that triggers a Celery task to resize images into multiple sizes (thumbnail, medium, large). Use `self.update_state()` to report progress. Implement retry logic for storage failures.

### Exercise 3: Report Generator with Progress (Intermediate)
Build a report generation system where a Flask endpoint triggers a long-running Celery task that queries a database, processes data, and generates a PDF. Implement progress tracking with custom states and a polling endpoint.

### Exercise 4: Retry Strategy Lab (Intermediate)
Create a task that calls an unreliable external API. Implement:
- Automatic retry with exponential backoff and jitter
- `soft_time_limit` with graceful cleanup
- `acks_late` for crash recovery
- Sentry-style error logging on final failure
Test by simulating random failures.

### Exercise 5: Multi-Step Order Processing (Advanced)
Implement an e-commerce order processing pipeline using Celery Canvas:
- `chain(validate_order, charge_payment, update_inventory, send_confirmation)`
- Use `chord` for parallel tasks (e.g., notify warehouse + send email)
- Implement compensating transactions on failure (e.g., refund if inventory update fails)
- Set up Celery Beat for daily order summary reports
- Monitor everything with Flower

### Exercise 6: Async vs. Celery Comparison (Intermediate)
Build two versions of the same endpoint — one using Flask async views with `asyncio.gather()` for parallel API calls, and one using Celery tasks. Benchmark response times and understand the trade-offs. Document when each approach is appropriate.

---

## Connections to Other Domains

- **D-5 (Database Integration)**: Tasks need database access — understanding SQLAlchemy session management in task context is critical
- **D-6 (Authentication)**: Task-triggering endpoints need proper auth; tasks may need to act on behalf of users
- **D-8 (Testing)**: Testing Celery tasks requires `CELERY_ALWAYS_EAGER` or task mocking patterns
- **D-10 (Security Hardening)**: Securing broker connections, serializer safety (avoid pickle), input validation in tasks
- **D-11 (Deployment)**: Running Celery workers alongside Flask in production (Supervisor, Docker Compose, Kubernetes)
- **D-12 (Performance and Observability)**: Flower monitoring, Prometheus metrics, queue depth alerting
- **D-13 (Advanced Architectural Patterns)**: Event-driven architecture, CQRS patterns built on task queues
