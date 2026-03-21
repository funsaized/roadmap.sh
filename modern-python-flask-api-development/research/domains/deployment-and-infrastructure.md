# Deployment and Infrastructure

## Overview

This domain covers everything needed to take a Flask API from development to production: WSGI application servers, Docker containerization, reverse proxying with Nginx, structured logging, the 12-Factor App methodology, cloud deployment strategies, and CI/CD pipelines. It builds on Flask core fundamentals (D-3) and testing knowledge (D-8), and feeds into Performance and Observability (D-12).

---

## Key Concepts

### 1. WSGI Servers (Gunicorn)
Flask's built-in development server is single-threaded and unsuitable for production. Gunicorn (Green Unicorn) is a pre-fork WSGI HTTP server that manages multiple worker processes to handle concurrent requests.

- **Worker processes**: Independent OS processes, each with their own Python interpreter. Recommended formula: `(2 × CPU_cores) + 1`.
- **Threads (gthread worker class)**: Each worker can spawn threads for I/O-bound workloads. Typically 2–4 threads per worker.
- **Worker classes**: `sync` (default, one request at a time), `gthread` (threaded), `gevent`/`eventlet` (async, for long-polling or WebSockets).
- **Configuration file**: Use a `gunicorn.conf.py` for centralized settings (bind address, workers, timeout, max-requests, logging).
- **Graceful shutdown**: Gunicorn handles SIGTERM for zero-downtime deploys.
- **max-requests / max-requests-jitter**: Restart workers periodically to mitigate memory leaks.

### 2. Docker Containerization
Docker packages your Flask app and all dependencies into a portable, reproducible container image.

- **Dockerfile best practices**: Use slim base images (`python:3.12-slim`), copy `requirements.txt` first for layer caching, run as non-root user, use `.dockerignore`.
- **Multi-stage builds**: Separate build-time dependencies from runtime to reduce image size and attack surface.
- **Docker Compose**: Define multi-service stacks (app, database, Redis, Nginx) in `docker-compose.yml`.
- **Volume mounts**: Persist data (database files, uploads) across container restarts.
- **Environment variables**: Pass configuration at runtime via `--env-file` or compose `environment:` block.
- **Health checks**: Docker `HEALTHCHECK` instruction to monitor container health.

### 3. Nginx Reverse Proxy
Nginx sits in front of Gunicorn, handling tasks the application server shouldn't.

- **Reverse proxying**: Forward requests to Gunicorn via `proxy_pass`.
- **Static file serving**: Serve CSS/JS/images directly from Nginx, bypassing the application.
- **SSL/TLS termination**: Handle HTTPS with certificates (Let's Encrypt / Certbot).
- **Load balancing**: Distribute traffic across multiple Gunicorn instances.
- **Rate limiting and buffering**: Protect the application from abuse and slow clients.
- **Headers**: Forward `X-Forwarded-For`, `X-Forwarded-Proto`, `Host` to the app for correct request context.

### 4. Structured Logging
Production apps need machine-parseable, searchable logs instead of unstructured text.

- **JSON logging**: Use `structlog` or `python-json-logger` to emit JSON log entries.
- **Log levels**: DEBUG, INFO, WARNING, ERROR, CRITICAL — use consistently; avoid DEBUG in production.
- **Log to stdout**: In containerized environments, write to stdout and let the platform collect logs (12-Factor principle).
- **Request context**: Include request ID, method, URL, response status, duration in every log line.
- **Correlation IDs**: Trace a single request across services using a unique ID.
- **Log aggregation**: Ship logs to ELK Stack (Elasticsearch/Logstash/Kibana), Datadog, or cloud-native services.

### 5. 12-Factor App Methodology
A set of 12 principles for building portable, scalable SaaS applications. Applied to Flask:

1. **Codebase**: One repo, many deploys (dev/staging/prod from same codebase).
2. **Dependencies**: Declare in `requirements.txt` or `pyproject.toml`; isolate with virtualenvs.
3. **Config**: Store secrets and environment-specific values in environment variables, not code. Use `python-dotenv` for local dev.
4. **Backing services**: Treat databases, caches, queues as attached resources swappable via URLs.
5. **Build, release, run**: Strict separation — Docker enforces this naturally.
6. **Processes**: Stateless processes; store session/state in backing services (Redis, DB).
7. **Port binding**: Export HTTP via port binding (Gunicorn binds to a port).
8. **Concurrency**: Scale horizontally by adding processes, not making one process bigger.
9. **Disposability**: Fast startup, graceful shutdown (SIGTERM handling).
10. **Dev/prod parity**: Docker ensures identical environments everywhere.
11. **Logs**: Treat as event streams to stdout.
12. **Admin processes**: Run migrations, scripts as one-off processes in the same environment.

### 6. Cloud Deployment Strategies
Options for hosting Flask applications in production:

- **VPS / IaaS**: AWS EC2, DigitalOcean Droplets, Linode — full control, manual setup.
- **PaaS**: Heroku, Render, Railway, PythonAnywhere — managed deployment, less infrastructure management.
- **Container services**: AWS ECS/Fargate, Google Cloud Run, Azure Container Apps — run Docker containers without managing servers.
- **Serverless**: AWS Lambda + API Gateway (via Zappa or Mangum) — pay-per-request, auto-scaling.
- **Kubernetes**: For large-scale orchestration — pods, services, deployments, Helm charts.

### 7. CI/CD Pipelines
Automate testing, building, and deployment on every code change.

- **GitHub Actions**: Define workflows in `.github/workflows/*.yml` — lint, test, build Docker image, push to registry, deploy.
- **Pipeline stages**: Checkout → Install deps → Lint → Test → Build image → Push to registry → Deploy.
- **Container registries**: Docker Hub, GitHub Container Registry (ghcr.io), AWS ECR, Google Artifact Registry.
- **Secrets management**: Store credentials as GitHub Secrets, never in code.
- **Deployment strategies**: Rolling updates, blue-green deployment, canary releases.
- **GitLab CI/CD, Jenkins**: Alternative pipeline tools with similar concepts.

### 8. Process Management
Keep your application running reliably in production.

- **systemd**: Linux service manager for running Gunicorn as a system service.
- **Supervisor**: Process control system for managing and monitoring processes.
- **Docker restart policies**: `restart: unless-stopped` or `restart: always` in Docker Compose.
- **Health checks**: Application-level `/health` endpoints, Docker HEALTHCHECK, load balancer health probes.

### 9. WSGI Entry Point and Application Factory
The bridge between your Flask app and the WSGI server.

- **`wsgi.py`**: Entry point that imports and creates the Flask application instance.
- **Application factory pattern**: `create_app()` function for configurable app creation (essential for testability and multiple configurations).

---

## Concept Relationships

```
Application Factory (wsgi.py)
    └── Gunicorn (WSGI server)
            └── Nginx (reverse proxy)
                    └── Cloud Platform / Docker Host
                            └── CI/CD Pipeline (automated deployment)

12-Factor App ──── informs ──── all of the above
Structured Logging ──── integrates with ──── Gunicorn + Flask + Log Aggregation
Docker ──── containerizes ──── Flask + Gunicorn stack
Docker Compose ──── orchestrates ──── App + DB + Nginx + Workers
```

### Prerequisites for Other Domains
- **D-12 (Performance and Observability)**: Requires deployment infrastructure knowledge, logging, and container setup to implement monitoring, APM, and performance profiling.

---

## Learning Resources

### Online Courses

1. **Pluralsight: Flask: Deploy and Scale Applications** (Paid)
   - URL: https://www.pluralsight.com/courses/flask-deploy-scale-applications
   - Covers: Docker, WSGI servers, CI/CD, cloud platforms (AWS, GCP, Azure)
   - Updated: June 2025
   - Duration: ~2-3 hours
   - Level: Intermediate–Advanced

2. **Udemy: Python REST APIs with Flask, Docker, MongoDB, and AWS DevOps** (Paid)
   - URL: https://www.udemy.com/course/python-rest-apis-with-flask-docker-mongodb-and-aws-devops/
   - Covers: Flask REST APIs, Docker deployment, AWS EC2
   - Updated: October 2024
   - Duration: ~10 hours
   - Level: Intermediate

3. **TestDriven.io: Dockerizing Flask with Postgres, Gunicorn, and Nginx** (Free tutorial)
   - URL: https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/
   - Covers: Complete Docker setup for Flask with production stack
   - Level: Intermediate
   - Highly recommended — step-by-step production setup

### Video Tutorials

4. **DigitalOcean: How To Serve Flask Applications with Gunicorn and Nginx on Ubuntu 22.04** (Free)
   - URL: https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-22-04
   - Covers: systemd, Gunicorn, Nginx setup on bare Linux
   - Level: Intermediate

5. **YouTube: Deploy Flask App on Render (2024)** (Free)
   - URL: https://www.youtube.com/watch?v=ojArD6nLXKg
   - Covers: PaaS deployment, free tier hosting
   - Level: Beginner–Intermediate

6. **YouTube: Deploy Flask on Azure App Service (2024)** (Free)
   - URL: https://www.youtube.com/watch?v=bTpSDZioCUY
   - Covers: Azure cloud deployment
   - Level: Intermediate

### Books

7. **The Flask Mega-Tutorial by Miguel Grinberg** (Online / Book)
   - URL: https://learn.miguelgrinberg.com/product/flask-mega-tutorial
   - Relevant: Chapter 17 (Linux), Chapter 18 (Heroku), Chapter 19 (Docker)
   - Level: Intermediate
   - The canonical Flask deployment reference

8. **Flask Web Development, 2nd Edition by Miguel Grinberg** (O'Reilly)
   - Chapter 17: Deployment options
   - Level: Intermediate
   - Covers traditional and cloud-based deployment

9. **Mastering Flask Web and API Development (Packt, 2024)**
   - URL: https://www.packtpub.com/en-us/product/mastering-flask-web-and-api-development-9781837633227
   - Chapter 11: Deploying Flask Applications (Gunicorn, uWSGI, Docker, Kubernetes, Nginx)
   - Level: Advanced

### Documentation and References

10. **Flask Official Docs: Deploying to Production**
    - URL: https://flask.palletsprojects.com/en/stable/deploying/
    - Covers: Gunicorn, Waitress, mod_wsgi, uWSGI deployment guides

11. **Gunicorn Official Documentation**
    - URL: https://docs.gunicorn.org/en/stable/
    - Settings reference: https://docs.gunicorn.org/en/stable/settings.html

12. **12factor.net — The Twelve-Factor App**
    - URL: https://12factor.net/
    - The original methodology document — essential reading

13. **Docker Official Documentation**
    - URL: https://docs.docker.com/
    - Dockerfile reference, Compose file reference, best practices

14. **Nginx Documentation**
    - URL: https://nginx.org/en/docs/
    - Reverse proxy, load balancing, SSL configuration

15. **Flask Logging Documentation**
    - URL: https://flask.palletsprojects.com/en/stable/logging/
    - Configuring Flask's app.logger

16. **structlog Documentation**
    - URL: https://www.structlog.org/en/stable/
    - Best practices for structured logging in Python

### Interactive Exercises and Labs

17. **Docker Getting Started Tutorial (Official)**
    - URL: https://docs.docker.com/get-started/
    - Hands-on introduction to Docker concepts

18. **Play with Docker (Docker Labs)**
    - URL: https://labs.play-with-docker.com/
    - Free browser-based Docker environment for practice

19. **KodeKloud: 12-Factor App Course**
    - URL: https://kodekloud.com/blog/12-factor-app/
    - Interactive explanation of each factor

### GitHub Repositories

20. **nickjj/docker-flask-example**
    - URL: https://github.com/nickjj/docker-flask-example
    - Production-ready Flask + Docker Compose setup with best practices since 2014
    - Includes: Gunicorn, PostgreSQL, Redis, Celery, static asset management

21. **testdrivenio/flask-on-docker**
    - URL: https://github.com/testdrivenio/flask-on-docker
    - Companion repo for the TestDriven.io tutorial
    - Includes: Nginx, Gunicorn, PostgreSQL in Docker

22. **flask-env by brettlangdon**
    - URL: https://github.com/brettlangdon/flask-env
    - Environment-based Flask configuration helper (12-Factor pattern)

### Community Resources

23. **r/flask subreddit**
    - URL: https://www.reddit.com/r/flask/
    - Active community for Flask deployment questions

24. **r/devops subreddit**
    - URL: https://www.reddit.com/r/devops/
    - CI/CD, Docker, infrastructure discussions

25. **Better Stack: Gunicorn Explained**
    - URL: https://betterstack.com/community/guides/scaling-python/gunicorn-explained/
    - Deep dive into Gunicorn architecture and tuning

---

## Learning Path

### Phase 1: WSGI Servers and Application Serving (3–4 hours)
1. Understand WSGI protocol and why Flask's dev server is insufficient
2. Install and configure Gunicorn with a Flask app
3. Learn worker/thread configuration and tuning
4. Create a `gunicorn.conf.py` configuration file
5. **Milestone**: Successfully serve a Flask app with Gunicorn, test with `curl`

### Phase 2: Docker Containerization (4–6 hours)
1. Learn Docker fundamentals (images, containers, Dockerfiles)
2. Write a Dockerfile for a Flask + Gunicorn application
3. Use `.dockerignore` and multi-stage builds
4. Learn Docker Compose for multi-service stacks (app + database)
5. **Milestone**: Run your Flask API in Docker with `docker compose up`

### Phase 3: Nginx Reverse Proxy (3–4 hours)
1. Understand reverse proxy architecture
2. Configure Nginx to proxy requests to Gunicorn
3. Set up static file serving through Nginx
4. Configure SSL/TLS with Let's Encrypt
5. Add Nginx to your Docker Compose stack
6. **Milestone**: Full Nginx → Gunicorn → Flask stack running in Docker

### Phase 4: 12-Factor App Principles (2–3 hours)
1. Read 12factor.net (the complete methodology)
2. Refactor your Flask app to use environment variables for all config
3. Implement stateless processes (move session storage to Redis)
4. Set up proper log streaming to stdout
5. **Milestone**: Your app passes a 12-Factor checklist review

### Phase 5: Structured Logging (2–3 hours)
1. Configure Python's logging module for Flask
2. Set up JSON logging with `structlog` or `python-json-logger`
3. Add request IDs and correlation IDs
4. Configure Gunicorn access log format
5. **Milestone**: All application logs output as structured JSON to stdout

### Phase 6: CI/CD Pipelines (4–5 hours)
1. Set up GitHub Actions workflow for your Flask project
2. Add linting (flake8/ruff) and testing (pytest) steps
3. Build and push Docker images to a container registry
4. Add automated deployment to a staging environment
5. **Milestone**: Every push to main triggers automated test → build → deploy

### Phase 7: Cloud Deployment (3–5 hours)
1. Deploy to a PaaS (Render or Railway) for quick wins
2. Deploy to a VPS (DigitalOcean/AWS EC2) with full Nginx + Gunicorn + Docker stack
3. Explore container services (AWS ECS, Google Cloud Run)
4. **Milestone**: Your Flask API is publicly accessible with HTTPS

**Total estimated time: 21–30 hours**

---

## Practical Exercises

### Exercise 1: Basic Gunicorn Deployment (Beginner)
Take your Flask API from the testing domain (D-8) and serve it with Gunicorn. Experiment with different worker counts and measure response times using `ab` (Apache Bench) or `wrk`.

### Exercise 2: Dockerize Your Flask API (Intermediate)
Write a Dockerfile and `docker-compose.yml` that runs your Flask API with Gunicorn, PostgreSQL, and Redis. Use environment variables for all configuration. Ensure the image is under 200MB using slim base images.

### Exercise 3: Full Production Stack (Intermediate)
Add Nginx as a reverse proxy to your Docker Compose setup. Configure SSL with self-signed certificates (or Let's Encrypt if on a public server). Serve static files directly through Nginx.

### Exercise 4: 12-Factor Audit (Intermediate)
Audit your Flask application against all 12 factors. Create a checklist and fix any violations. Pay special attention to config (env vars), logs (stdout), and statelessness.

### Exercise 5: Structured Logging Implementation (Intermediate)
Replace all `print()` and basic logging with `structlog`. Add request ID middleware that generates a UUID per request and includes it in every log line. Test that logs are valid JSON.

### Exercise 6: CI/CD Pipeline (Advanced)
Create a GitHub Actions workflow that: (1) runs linting with ruff, (2) runs pytest, (3) builds a Docker image, (4) pushes to GitHub Container Registry, (5) deploys to a staging server via SSH. Add branch protection rules requiring CI to pass.

### Exercise 7: Blue-Green Deployment (Advanced)
Implement a blue-green deployment strategy using Docker Compose. Run two versions of your app simultaneously, switch Nginx upstream to the new version, verify it works, then tear down the old version.

### Exercise 8: Cloud Deployment Project (Advanced)
Deploy your complete Flask API stack to AWS (EC2 + RDS + ElastiCache) or equivalent. Set up proper security groups, use managed database services, configure CloudWatch or equivalent for log aggregation.

---

## Connections to Other Domains

- **D-3 (Flask Core)**: Application factory pattern (`create_app()`) is essential for the WSGI entry point
- **D-8 (Testing)**: CI/CD pipelines automate test execution; Docker ensures test environment consistency
- **D-9 (Background Tasks)**: Celery workers need their own process management in Docker Compose
- **D-10 (Security)**: SSL/TLS configuration, secrets management, non-root containers
- **D-12 (Performance and Observability)**: This domain provides the infrastructure foundation; D-12 adds APM, metrics, and monitoring on top
- **D-13 (Advanced Patterns)**: Microservice deployment, service discovery, orchestration build on deployment fundamentals
