# FastAPI Mastery Plan — Job-Focused

## Strategy
- Drills build mental models. Projects get you hired.
- One new concept per drill. Blank page. No hints.
- If you can't finish in 20 min, prerequisite is shaky — repeat it.
- **Apply after Project 1 ships — not after drill 200.**
- Track your times. Over 25 min = go back one drill.

---

## Revised Drill Map

| Range | Topic |
|---|---|
| 01–10 | Pydantic fundamentals ✅ |
| 11–20 | Async/Await fundamentals ✅ |
| 21–30 | Wrapper decorators ✅ |
| 31–40 | Registry decorators ✅ |
| 41–50 | Toy dispatch + toy middleware + toy DI ✅ |
| 51–60 | OOP decorators |
| 61–70 | Dynamic dispatch deep dive |
| 71–80 | First mixes (2 concepts) |
| 81–100 | Harder combos (3+ concepts) |
| 101–130 | Real FastAPI (core + auth + DB) → **Project 1** |
| 131–170 | Production hardening (testing + infra) → **Project 2** |
| 171–199 | Speed drills + synthesis |
| 200 | Final boss |

---

## Phase 1: Python Internals (Drills 51–100)

### OOP Decorators (51–60)
- `args[0]` is `self`
- read `self.state` inside decorator
- mutate `self.state` safely with `try/finally`
- same decorator on multiple methods with different rules
- `@wraps` — assert `__name__`, `__doc__`, `__wrapped__`
- sync + async branch via `inspect.iscoroutinefunction`
- log calls to `self.history` — reads and mutates instance state
- class-level registry — store unbound functions, bind via `args[0]`
- dispatch inside class + Pydantic + domain exception (`InvalidPayloadError`)
- final boss — async class, registry, dispatch, Pydantic, `@wraps`, `try/finally`, per-instance state

### Dynamic Dispatch (61–70)
- dispatch returns values — test the return path
- path params — `/users/{id}` pattern matching
- GET vs POST same path
- before/after hook points
- global error handler fallback
- route prefixes — `/api/v1/`
- async context manager — lifespan pattern
- dependency graph — one dep calls another
- response model — validate output with Pydantic
- final boss — mini HTTP router, all above combined

### First Mixes (71–80)
- Pydantic + OOP decorator
- async rate limiter with `asyncio.sleep`
- class-based router — registry + OOP + dispatch
- nested Pydantic models in dispatch
- parallel dependency resolution with `gather`
- custom exception hierarchy — base → domain → HTTP-mappable
- `contextvars` — request-scoped state without passing everywhere
- async queue — background task pattern
- semaphore inside decorator — concurrency limiter
- final boss — async class router, parallel deps, nested Pydantic, custom exceptions

### Harder Combos (81–100)
- `__init_subclass__` — auto-register subclasses
- descriptor protocol `__get__` — how bound methods actually work
- `__call__` on a class — callable class as decorator
- dataclasses vs Pydantic — when to use which
- `asyncio.Lock` inside class method decorator
- `asyncio.gather` with error isolation — one dep fails, others continue
- async generator — streaming response pattern
- middleware stack — ordered, each wraps the next (real ASGI shape)
- lifespan context manager — startup/shutdown state
- dependency override — test vs prod resolver
- 9 speed drills — all above, timed, no hints
- final boss — everything in one system

---

## Phase 2: Real FastAPI (Drills 101–140)
> **Start Project 1 at drill 101**

### Core FastAPI (101–110)
- `@app.get`, `uvicorn.run`, test with `httpx`
- path params + query params + type coercion
- request body with Pydantic model
- `response_model=` — validate output
- `HTTPException` + status codes
- `Depends()` — single injected dependency
- `Depends()` chained — one dep calls another
- `Depends()` with class — stateful dependency
- `BackgroundTasks` — fire and forget
- lifespan — startup/shutdown with `asynccontextmanager`

### Auth (111–120)
- `OAuth2PasswordBearer` — extract token from header
- JWT decode — verify signature and expiry with `python-jose`
- current user dependency — token → User object
- role-based access — admin vs regular user
- refresh token pattern
- API key auth — header + query param
- `HTTPBasic` auth
- scopes — fine-grained permissions
- auth middleware — global vs per-route
- final boss — JWT + roles + scopes in one system

### Database (121–130)
- SQLAlchemy async setup — engine, session factory
- first table + Alembic migration
- CRUD — create, read, update, delete
- `get_db()` session as a dependency
- relationships — one-to-many, eager vs lazy load
- transactions — commit, rollback
- repository pattern — separate DB logic from routes
- pagination — limit/offset + cursor-based
- filters + search
- final boss — full CRUD API with auth + DB

---

## Phase 3: Production (Drills 131–170)
> **Start Project 2 at drill 141**

### Testing (131–140)
- `pytest` + `httpx.AsyncClient` — test FastAPI routes
- fixtures — test DB, test user, test token
- dependency override — swap real DB for test DB
- factory pattern for test data
- parametrized tests — one test, many cases
- mock external services with `respx`
- test auth flows end-to-end
- enforce 90%+ coverage
- load test with `locust` — find your bottleneck
- final boss — full test suite for drill 130 system

### Production Patterns (141–155)
- `pydantic-settings` — env vars, `.env` files
- structured logging with `structlog`
- request ID middleware — trace a request across logs
- rate limiting — token bucket with Redis
- Redis cache layer on expensive routes
- background workers with `arq`
- WebSockets — real-time updates
- file upload — stream to S3
- health check + readiness endpoint
- graceful shutdown — drain in-flight requests
- CORS — production config
- exception handler hierarchy — domain exceptions → HTTP
- OpenAPI customization — tags, descriptions, examples
- API versioning — `/v1/` prefix strategy
- final boss — production-ready API with all above

### Infrastructure (156–170)
- Docker — containerize the app
- Docker Compose — app + DB + Redis
- GitHub Actions — CI pipeline, run tests on push
- environment promotion — dev → staging → prod configs
- secrets management — never hardcode
- managed Postgres setup (Railway / Supabase)
- deploy to Railway / Render / Fly.io
- Nginx — reverse proxy, SSL termination
- horizontal scaling — gunicorn workers
- DB connection pooling — `asyncpg`
- Prometheus + Grafana — basic monitoring
- Sentry — error tracking integration
- zero-downtime deploy — blue/green basics
- DB backup + restore
- final boss — full deploy pipeline, monitored, tested, scaled

---

## Phase 4: Speed + Portfolio (171–200)

### Speed Drills (171–190)
- every concept from phases 1–3
- timed, no hints, blank page, under 15 minutes each

### Synthesis Projects (191–199)
- auth + CRUD API
- real-time chat with WebSockets
- background job queue system
- multi-tenant API with scoped DB access
- file upload + processing pipeline
- public API with rate limiting + API keys
- admin dashboard API
- microservice with inter-service auth
- full e-commerce API

### Drill 200 — Final Boss
- all 6 concepts + FastAPI + auth + DB + tests + Docker + deployed
- no hints, timed, blank page

---

## Projects (non-negotiable)

### Project 1 — after drill 80, build through 101–130
- FastAPI CRUD API
- users, posts, JWT auth
- deployed, live URL, GitHub README
- **start applying for jobs here**

### Project 2 — after drill 130, build through 131–170
- your choice of domain
- full test suite, Docker, deployed
- something you'd show in an interview without hesitation

---

## The Rules
- One new concept per drill
- Blank page, no hints
- Can't finish in 20 min → prerequisite is shaky, repeat it
- Every Phase 2+ drill gets a real `assert` or `pytest` — no print-and-eyeball
- Two projects on GitHub before applying — not drills, real APIs with live URLs
- **Apply after Project 1. Not after drill 200.**
