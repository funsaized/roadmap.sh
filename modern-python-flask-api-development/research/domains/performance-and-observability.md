# Performance and Observability

## Overview

This domain covers the techniques and tools needed to make Flask APIs fast, reliable, and transparent in production. It spans multi-layer caching strategies, database query profiling, distributed tracing with OpenTelemetry, metrics collection with Prometheus, load testing methodologies, and application profiling. Mastery here is essential for running production-grade Flask services and is a prerequisite for D-13 (Advanced Architectural Patterns).

**Prerequisites:** D-9 (Background Tasks and Async Patterns), D-11 (Deployment and Infrastructure)

---

## Key Concepts

### 1. Multi-Layer Caching

- **Application-level caching (Flask-Caching):** Using the `@cache.cached()` and `@cache.memoize()` decorators to cache view responses and function results. Supports multiple backends (simple in-memory, Redis, Memcached).
- **In-memory caching:** Fast, process-local caching using `functools.lru_cache` or custom dictionary-based caches. Best for single-instance deployments or hot data that changes rarely.
- **Distributed caching with Redis/Memcached:** Shared cache across multiple application instances. Redis provides persistence options, pub/sub for invalidation, and data structure support beyond simple key-value.
- **HTTP caching:** Using `Cache-Control`, `ETag`, and `Last-Modified` headers to enable browser and CDN caching. Reduces server load for cacheable responses.
- **Cache invalidation strategies:** Time-based TTL, event-driven invalidation, cache tags for group invalidation, write-through vs. write-behind patterns.
- **Cache key design:** Building deterministic cache keys from request parameters, user context, and query strings. Avoiding cache collisions and key bloat.

### 2. Database Query Profiling

- **SQLAlchemy query logging:** Using `SQLALCHEMY_ECHO=True` or `SQLALCHEMY_RECORD_QUERIES=True` to log all executed SQL statements with timing.
- **Slow query detection:** Using `get_recorded_queries()` with duration thresholds to identify queries exceeding acceptable response times.
- **N+1 query problem:** Detecting and fixing with eager loading strategies (`joinedload()`, `selectinload()`, `contains_eager()`).
- **EXPLAIN ANALYZE:** Using database-native query plan analysis to understand index usage, sequential scans, and join strategies.
- **Connection pooling tuning:** Configuring `SQLALCHEMY_POOL_SIZE` and `SQLALCHEMY_MAX_OVERFLOW` for optimal connection reuse under load.
- **Profiling tools:** SQLTap, SQLAlchemy-Easy-Profile, and Flask-DebugToolbar for development-time query analysis.

### 3. OpenTelemetry Tracing

- **Three pillars of observability:** Traces, metrics, and logs — and how OpenTelemetry unifies them under a single framework.
- **Automatic instrumentation:** Using `FlaskInstrumentor().instrument_app(app)` to automatically create spans for every HTTP request with method, path, status code, and duration.
- **Zero-code instrumentation:** Using `opentelemetry-instrument` CLI agent to instrument without code changes via monkey-patching.
- **Manual instrumentation:** Creating custom spans for business-critical operations, database calls, or external service interactions.
- **Distributed context propagation:** How trace context (W3C TraceContext) flows across service boundaries in microservice architectures.
- **Exporters:** Sending telemetry data to backends like Jaeger, Zipkin, Grafana Tempo, or any OTLP-compatible collector.
- **SQLAlchemy instrumentation:** Using `opentelemetry-instrumentation-sqlalchemy` to trace database queries within the same trace context.

### 4. Prometheus Metrics

- **Metric types:** Counters (monotonically increasing), Gauges (arbitrary values), Histograms (bucketed distributions), and Summaries (quantile calculations).
- **prometheus-flask-exporter:** Automatically exposing a `/metrics` endpoint with request count, duration histograms, and error rates.
- **Custom metrics:** Defining application-specific counters, gauges, and histograms for business KPIs (e.g., orders processed, cache hit rate).
- **PromQL:** Querying time-series data for dashboards and alerting (rate, histogram_quantile, increase, etc.).
- **Multiprocess mode:** Handling metrics aggregation when running with Gunicorn workers using `PROMETHEUS_MULTIPROC_DIR`.
- **Grafana dashboards:** Visualizing Prometheus metrics with pre-built and custom dashboards.
- **Alerting:** Setting up Alertmanager rules for SLO-based alerts (e.g., p99 latency > 500ms, error rate > 1%).

### 5. Load Testing

- **Locust:** Python-based load testing tool where user behavior is defined as Python code. Supports distributed testing, web UI for real-time monitoring, and easy CI/CD integration.
- **k6:** JavaScript-based load testing tool by Grafana Labs. Supports complex scenarios, thresholds, and cloud execution.
- **Test types:** Smoke tests, load tests, stress tests, spike tests, soak tests — each serving different validation purposes.
- **Metrics to measure:** Requests per second (RPS), response time percentiles (p50, p95, p99), error rate, throughput, and concurrent user capacity.
- **Realistic test design:** Modeling actual user behavior with weighted tasks, think times, and sequential flows rather than simple endpoint hammering.
- **CI/CD integration:** Running performance regression tests as part of the deployment pipeline with pass/fail thresholds.

### 6. Application Profiling

- **cProfile / Werkzeug ProfilerMiddleware:** Built-in deterministic profiling that traces every function call. Best for development and identifying CPU-bound bottlenecks.
- **py-spy:** Sampling profiler that attaches to running Python processes without restart or code changes. Generates flame graphs for visual bottleneck analysis. Suitable for production use with minimal overhead.
- **Flame graphs:** Visual representation of call stacks showing where time is spent. Wide bars indicate hot paths.
- **SnakeViz:** Browser-based viewer for cProfile `.prof` output files, providing interactive sunburst and icicle visualizations.
- **Memory profiling:** Using `memory_profiler` or `tracemalloc` to detect memory leaks and excessive allocations.
- **GC tuning:** Understanding Python's garbage collector behavior and its impact on latency spikes.

### Concept Relationships

```
Caching ←→ Query Profiling (cache what's slow)
    ↓
Load Testing → reveals bottlenecks → Profiling (cProfile, py-spy)
    ↓
OTel Tracing + Prometheus Metrics → ongoing production observability
    ↓
Grafana Dashboards + Alerting → operational awareness
```

### Prerequisites for Other Domains

- All concepts in this domain feed into **D-13: Advanced Architectural Patterns**, where performance-aware design decisions (caching layers, observability-driven development) become architectural concerns.

---

## Learning Resources

### Online Courses

1. **"Monitoring and Observability with OpenTelemetry" — Udemy**
   - URL: https://www.udemy.com/topic/opentelemetry/
   - Platform: Udemy
   - Duration: ~4-6 hours
   - Difficulty: Intermediate
   - Cost: Paid (~$15-30 on sale)

2. **"Pluralsight: Optimizing Flask Applications with Caching and Middleware" — Pluralsight Lab**
   - URL: https://www.pluralsight.com/labs/codeLabs/guided-optimizing-flask-applications-with-caching-and-middleware
   - Platform: Pluralsight
   - Duration: ~2 hours (hands-on lab)
   - Difficulty: Intermediate
   - Cost: Pluralsight subscription

3. **"Performance Testing in Python: A Step-by-Step Guide with Flask" — Code Like a Girl**
   - URL: https://code.likeagirl.io/performance-testing-in-python-a-step-by-step-guide-with-flask-e5a56f99513d
   - Platform: Medium (free)
   - Duration: ~1 hour reading
   - Difficulty: Intermediate

### Video Tutorials and Conference Talks

4. **"Prometheus Monitoring Flask Application" — YouTube**
   - URL: https://www.youtube.com/watch?v=WnKqDmb2E10
   - Duration: ~20 minutes
   - Difficulty: Beginner-Intermediate

5. **"Load Testing Your API Using Locust" — Nordic APIs**
   - URL: https://nordicapis.com/load-testing-your-api-using-locust/
   - Type: Written tutorial with examples
   - Difficulty: Intermediate

6. **"Load Testing with Locust" — YouTube (Locust official)**
   - URL: https://www.youtube.com/watch?v=bUEYe6AqlXE
   - Duration: ~15 minutes
   - Difficulty: Beginner

### Books

7. **"Cloud-Native Observability with OpenTelemetry" — Alex Boten (Packt, 2022)**
   - Relevant chapters: Ch. 9 (Flask instrumentation library), plus chapters on traces, metrics, and log correlation
   - Difficulty: Intermediate-Advanced
   - URL: https://subscription.packtpub.com/book/cloud-and-networking/9781801077705/9/ch09lvl1sec49/flask-library-instrumentor

8. **"Flask Web Development" — Miguel Grinberg (O'Reilly, 2nd Edition)**
   - Relevant sections: Performance optimization, profiling, and deployment chapters
   - Difficulty: Intermediate

9. **"High Performance Python" — Micha Gorelick & Ian Ozsvald (O'Reilly, 2nd Edition, 2020)**
   - Relevant chapters: Profiling (cProfile, py-spy), memory optimization, concurrency
   - Difficulty: Advanced

### Documentation and Reference Materials

10. **Flask-Caching Official Documentation**
    - URL: https://flask-caching.readthedocs.io/en/latest/
    - Covers: All caching backends, decorators, configuration, and cache invalidation

11. **OpenTelemetry Python Getting Started Guide**
    - URL: https://opentelemetry.io/docs/languages/python/getting-started/
    - Covers: SDK setup, auto-instrumentation, exporters

12. **OpenTelemetry Flask Instrumentation Docs**
    - URL: https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/flask/flask.html
    - Covers: FlaskInstrumentor API, request/response hooks, custom spans

13. **OpenTelemetry Zero-Code Instrumentation for Python**
    - URL: https://opentelemetry.io/docs/zero-code/python/
    - Covers: Agent-based instrumentation without code changes

14. **prometheus-flask-exporter (PyPI)**
    - URL: https://pypi.org/project/prometheus-flask-exporter/
    - Covers: Setup, custom metrics, multiprocess support

15. **Locust Official Documentation**
    - URL: https://locust.io/
    - Covers: Test script authoring, distributed testing, web UI, CI integration

16. **Flask-SQLAlchemy Query Recording**
    - URL: https://flask-sqlalchemy.readthedocs.io/en/stable/record-queries/
    - Covers: SQLALCHEMY_RECORD_QUERIES, slow query logging

17. **Prometheus Querying Basics (PromQL)**
    - URL: https://prometheus.io/docs/prometheus/latest/querying/basics/
    - Covers: PromQL syntax, functions, aggregations

### Interactive Exercises and Practice

18. **Grafana Cloud Flask Metrics Collection Guide**
    - URL: https://grafana.com/docs/grafana-cloud/knowledge-graph/advanced-configuration/enable-prom-metrics-collection/application-frameworks/flask/
    - Type: Step-by-step hands-on tutorial
    - Difficulty: Intermediate

19. **Load Testing with Locust — Linode Guide**
    - URL: https://www.linode.com/docs/guides/load-testing-with-locust/
    - Type: Hands-on tutorial with cloud deployment
    - Difficulty: Intermediate

20. **BetterStack: Prometheus Python Metrics Guide**
    - URL: https://betterstack.com/community/guides/monitoring/prometheus-python-metrics/
    - Type: Step-by-step tutorial
    - Difficulty: Beginner-Intermediate

### GitHub Repositories

21. **opentelemetry-python-contrib (Flask instrumentation source)**
    - URL: https://github.com/open-telemetry/opentelemetry-python-contrib
    - What it demonstrates: Official Flask instrumentation implementation

22. **SigNoz OpenTelemetry Python Example (Flask + MongoDB)**
    - URL: https://github.com/SigNoz/opentelemetry-python-example
    - What it demonstrates: Complete Flask app with auto/manual tracing, custom metrics, logging

23. **highlight/otel-flask-example**
    - URL: https://github.com/highlight/otel-flask-example
    - What it demonstrates: Simple Flask app with logs, traces, and metrics forwarding

24. **sqlalchemy-easy-profile**
    - URL: https://github.com/dmvass/sqlalchemy-easy-profile
    - What it demonstrates: WSGI middleware for per-request query profiling

25. **prometheus-flask-exporter (source)**
    - URL: https://github.com/rycus86/prometheus-flask-exporter
    - What it demonstrates: Production-ready Prometheus integration for Flask

### Community Resources

- **r/flask** — https://www.reddit.com/r/flask/ — Active community for Flask questions
- **r/Python** — https://www.reddit.com/r/Python/ — OpenTelemetry and performance discussions
- **OpenTelemetry CNCF Slack** — https://cloud-native.slack.com — #opentelemetry-python channel
- **Locust GitHub Discussions** — https://github.com/locustio/locust/discussions
- **Grafana Community Forums** — https://community.grafana.com/

---

## Learning Path

### Phase 1: Application Profiling Fundamentals (3-4 hours)
1. Learn cProfile and Werkzeug ProfilerMiddleware basics
2. Practice profiling a Flask app endpoint
3. Install py-spy and generate flame graphs
4. Use SnakeViz to analyze .prof files

**Milestone:** Able to identify the slowest function in a Flask request handler using both cProfile and py-spy.

### Phase 2: Database Query Profiling (3-4 hours)
1. Enable SQLALCHEMY_RECORD_QUERIES and log slow queries
2. Detect and fix N+1 queries with eager loading
3. Use EXPLAIN ANALYZE on identified slow queries
4. Explore Flask-DebugToolbar and SQLTap

**Milestone:** Identify and fix an N+1 query problem in a Flask-SQLAlchemy app, reducing query count from N+1 to 2.

### Phase 3: Caching Strategies (4-5 hours)
1. Set up Flask-Caching with simple backend
2. Implement view caching and memoization
3. Switch to Redis backend for distributed caching
4. Build a multi-layer cache (in-memory + Redis)
5. Implement cache invalidation patterns
6. Add HTTP caching headers

**Milestone:** Demonstrate a 10x response time improvement on a database-heavy endpoint using caching.

### Phase 4: Prometheus Metrics (4-5 hours)
1. Install and configure prometheus-flask-exporter
2. Understand the four metric types
3. Create custom application metrics
4. Set up a local Prometheus server to scrape metrics
5. Build a Grafana dashboard
6. Handle multiprocess mode with Gunicorn
7. Write basic PromQL queries

**Milestone:** A working Grafana dashboard showing request rate, error rate, and latency percentiles for your Flask API.

### Phase 5: OpenTelemetry Tracing (5-6 hours)
1. Install OTel SDK and Flask instrumentation
2. Set up automatic instrumentation with FlaskInstrumentor
3. Try zero-code instrumentation with opentelemetry-instrument
4. Add manual spans for custom operations
5. Instrument SQLAlchemy queries
6. Export traces to Jaeger (local Docker instance)
7. Understand distributed context propagation

**Milestone:** View a complete distributed trace in Jaeger showing an HTTP request → custom business logic span → database query span.

### Phase 6: Load Testing (3-4 hours)
1. Install Locust and write a basic locustfile
2. Run load tests against your Flask API
3. Analyze results: RPS, latency percentiles, error rates
4. Design realistic test scenarios with weighted tasks
5. Run stress tests to find breaking points
6. Explore k6 as an alternative

**Milestone:** A load test report showing your API handles 100 concurrent users with p95 latency under 200ms.

### Phase 7: Integration and Production Readiness (3-4 hours)
1. Combine OTel tracing + Prometheus metrics in one Flask app
2. Correlate traces with logs
3. Set up alerting rules in Prometheus/Grafana
4. Add performance tests to CI/CD pipeline
5. Document SLOs for your API

**Milestone:** A production-ready Flask API with unified observability (traces + metrics + logs), automated load tests, and SLO-based alerting.

**Total estimated time: 25-32 hours**

---

## Practical Exercises

### Exercise 1: Profile and Optimize (Beginner)
Build a Flask API endpoint that queries a database with an intentional N+1 problem. Profile it with cProfile, identify the bottleneck, fix it with eager loading, and measure the improvement.

### Exercise 2: Multi-Layer Cache (Intermediate)
Implement a Flask API with a three-layer caching strategy: in-memory (lru_cache) → Redis → database. Add a `/cache-stats` endpoint showing hit/miss ratios at each layer. Implement cache invalidation on writes.

### Exercise 3: Full Observability Stack (Intermediate-Advanced)
Set up a Flask API with:
- OpenTelemetry auto-instrumentation sending traces to Jaeger
- Prometheus metrics via prometheus-flask-exporter
- Grafana dashboards for request rate, error rate, and latency
- Custom metrics for business operations
Deploy with Docker Compose (Flask + Redis + Postgres + Jaeger + Prometheus + Grafana).

### Exercise 4: Load Test Suite (Intermediate)
Write a comprehensive Locust test suite for a Flask API with:
- Multiple user types (authenticated/anonymous) with different behavior weights
- Sequential task flows (browse → search → add to cart → checkout)
- Performance thresholds that fail the test if p95 > 300ms
- HTML report generation

### Exercise 5: Production Performance Pipeline (Advanced)
Build a CI/CD pipeline that:
1. Deploys a Flask API to a staging environment
2. Runs automated load tests with Locust
3. Collects metrics from Prometheus
4. Fails the deployment if performance regressions are detected
5. Generates a performance comparison report (current vs. previous build)

---

## Connections to Other Domains

- **D-5 (Database Integration):** Query profiling and N+1 detection build directly on ORM knowledge
- **D-9 (Background Tasks):** Offloading heavy work to Celery is a key performance strategy; tracing spans across async task boundaries
- **D-11 (Deployment):** Prometheus/Grafana are part of the production infrastructure stack; load testing validates deployment capacity
- **D-13 (Advanced Architectural Patterns):** Performance-aware design (caching layers, circuit breakers, rate limiting) becomes architectural decision-making
