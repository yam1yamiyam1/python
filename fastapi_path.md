# FastAPI Mastery Curriculum

## AI Drill Generation Reference

---

## HOW TO USE THIS FILE

This file is a **living reference for an AI assistant** to generate coding drills.

### Standard prompt — next drill:

> "Generate drill [N] from the FastAPI Mastery Curriculum. Follow the drill format exactly."

### Retention prompt — more drills on the same block:

> "I need [N] more drills on Block [X]. Same mechanic, different scenarios. Do not advance to the next block."

### The AI must follow these rules without exception:

1. Read the **Progress Tracker** first. That is the source of truth for where we are.
2. Introduce **exactly one new mechanic** per drill. Never combine two new things in one drill.
3. **Never reuse a scenario** that appears in the Scenario Bank's Used list or in the drill snapshot tables.
4. When generating retention drills (more drills on the same block): vary the scenario and add one **small twist** to the existing mechanic — do not introduce anything from the next block.
5. The **Drill Format** is mandatory and non-negotiable. Every field must be present.
6. Before writing the drill, the AI must internally state: "Current block is [X]. The one new mechanic I am introducing is [Y]. The scenario I am using is [Z]." This prevents drift.
7. Update the **Used Scenarios** list in the Scenario Bank after each drill.

---

## DRILL FORMAT

Every drill must follow this exact structure. No fields may be omitted.

```python
import asyncio  # noqa: F401
from typing import ...  # noqa: F401

async def run_drill_N():
    # =========================================================================
    # SCENARIO: [Memorable real-world name — must not repeat any used scenario]
    # =========================================================================
    # [2-3 sentence story context that makes the mechanic feel real]
    #
    # REQUIREMENTS:
    #
    # 1. A registry (or registries): REGISTRY_NAME = {}
    #
    # 2. [N] functions/hooks (you write these):
    #    - function_name(args) -> return_type
    #      - condition 1: behavior/raises
    #      - condition 2: behavior/raises
    #      - [note if async or sync]
    #
    # 3. [N] handler functions (you write these):
    #    - handler_name(args)
    #      - prints X, indented with two spaces
    #      - returns value or returns nothing
    #
    # 4. A decorator @register(param1, param2, ...)
    #    - what it does, how it stores data in REGISTRY
    #    - return func
    #
    # 5. Apply @register to handler_name:
    #    - exact parameters and values
    #
    # 6. An async/sync main_dispatch(args):
    #    - Stage 1: [description]
    #      - specific steps with conditions
    #    - Stage 2: [description]
    #      - specific steps with conditions
    #    - Stage 3: [description]
    #      - specific steps with conditions
    #
    # =========================================================================

    # --- YOUR CODE HERE ---

    # --- TESTS (do not modify) ---
    print("Test 1: ...")
    await dispatch(...)

    # =========================================================================
    # EXPECTED OUTPUT:
    # Test 1: ...
    #   [result]
    # =========================================================================


if __name__ == "__main__":
    asyncio.run(run_drill_N())
```

**Rules the AI must enforce on every single drill:**

- All logic lives inside `run_drill_N()` — no module-level state, ever
- Tests labeled `Test 1:`, `Test 2:`, etc. — no exceptions
- Handler output indented with exactly two spaces
- Expected output block always present, always complete, always accurate
- All imports must have `# noqa: F401` to prevent auto-removal on save
- No imports beyond what the drill actually uses
- **REQUIREMENTS section must follow this exact ordering:**
  1. Registries (e.g., `REGISTRY = {}`)
  2. Check/hook/middleware functions with full signatures and behavior
  3. Handler functions with full signatures and behavior
  4. Decorator definition
  5. Apply decorator(s) to handler(s) with exact parameters
  6. Main dispatch/engine function with numbered stages
- Minimum 4 tests per drill, covering: happy path, each failure mode, edge case

---

## PROGRESS TRACKER

```
Current Drill:     50
Current Phase:     2 — Routing Engine Internals
Current Block:     2B — Middleware + Dependency Fusion
Next Mechanic:     Prefix group isolation (sub-routers)
Completed Phases:  Phase 1 (complete)
```

Update this block after every drill session.

---

## PHASES & MECHANICS

---

### PHASE 1 — Registry & Dispatch Foundations

**Goal:** Build everything a framework does internally — by hand.

**Status: COMPLETE (Drills 1–50)**

#### Block 1A — Basic Registries

- Key-value registry (`ROUTES = {}`)
- `@register` decorator stores handler + metadata
- `dispatch(name, ...)` looks up and calls handler
- Sync handlers only

#### Block 1B — Check Functions (Guards)

- Check functions: sync, raise `ValueError` on failure
- `dispatch` runs checks before calling handler
- First failure stops immediately
- Checks passed as a `dict` → resolved into `**kwargs`

#### Block 1C — Async Handlers

- Handlers become `async def`
- `dispatch` becomes `async def`
- Check functions remain sync (not awaited)
- Handler is awaited

#### Block 1D — Pydantic Validation Layer

- Raw `dict` payload validated into a Pydantic model before checks
- `ValidationError` caught separately → "Invalid data"
- `ValueError` from checks caught → "Check Error: ..."
- Validated object passed into check functions (not raw dict)

#### Block 1E — Middleware Lists

- Checks restructured as a `list` of hooks (not a `dict`)
- Hooks receive the validated model, return nothing, raise on failure
- `dispatch` loops the list in order

#### Block 1F — Async Dependencies

- Dependencies are `async` functions that take a token and return real objects
- `dispatch` awaits each dependency
- Results collected into `resolved` dict → `**resolved` passed to handler
- `ValueError` from a dependency → "Access Denied: ..."

#### Block 1G — Full Fusion (Drills 48–50)

- All three stages in one dispatch:
  - Stage 1: Pydantic validation
  - Stage 2: Middleware list (sync hooks)
  - Stage 3: Async dependencies
- Each stage has its own error message
- Handler receives `**resolved` from dependencies only

**Drills 46–50 snapshot:**
| Drill | Scenario | New Mechanic |
|-------|----------|--------------|
| 46 | Gym | Dict-checks + async handlers |
| 47 | Online Checkout | Pydantic validation before checks |
| 48 | Concert Venue | Middleware as list (no return value) |
| 49 | Hospital | Async dependencies, awaited per dep |
| 50 | Airport | All three stages fused (validation + middleware + deps) |

---

### PHASE 2 — Routing Engine Internals

**Goal:** Build the pieces of a real HTTP router from scratch.

**Status: IN PROGRESS**

#### Block 2A — Return Values & Data Flow ✅ (introduced in drill 46+)

- Handlers return data instead of printing
- `dispatch` returns the result up the stack
- Tests assert on return values, not stdout

#### Block 2B — Middleware + Dependency Fusion ← CURRENT

- Before/after hooks on the dispatch engine itself (not per-route)
- Global `before_request` list runs before any route
- Global `after_request` list runs after any route, receives the result
- Per-route middleware and deps still work underneath

**Upcoming drills in 2B:**

- Drill 51: Add `before_request` hooks to the dispatch engine
- Drill 52: Add `after_request` hooks, pass result through
- Drill 53: Combine before + after + per-route middleware in one engine

#### Block 2C — Path Pattern Matching

- Route paths contain placeholders: `/users/{id}`
- Compiler converts path string → regex
- `dispatch` receives a raw URL string, extracts `{param}` values
- Extracted values passed as `**kwargs` to handler

**Mechanics to cover:**

- `re.compile` from path template
- Named capture groups: `(?P<id>[^/]+)`
- No match → 404
- Match → extract kwargs → pass to handler

#### Block 2D — Multi-Verb Routing

- Same path registered under different HTTP methods: GET, POST, PUT
- Registry key becomes `(method, path)` tuple
- `dispatch(method, path, ...)` hits the right handler
- Wrong method on valid path → 405 Method Not Allowed

#### Block 2E — Prefix Groups (Sub-Routers)

- A sub-router is a mini registry with its own prefix (e.g., `/api/v1`)
- Sub-router mounted onto main router
- `dispatch` on main router resolves prefix + path

#### Block 2F — Lifespan Events

- `startup()` and `shutdown()` async hooks on the engine
- Startup runs once before any dispatch
- Shutdown runs once at the end
- Simulated with `asynccontextmanager`

#### Block 2G — Chained Dependencies

- Dependency B takes the resolved output of Dependency A as input
- Engine resolves the dependency graph in order
- Circular dependency → raise at registration time

#### Block 2H — Egress Filtering

- Handler returns a dict
- Engine passes it through an output schema (Pydantic)
- Fields not in the schema are stripped before returning
- "Private" fields never reach the caller

---

### PHASE 3 — FastAPI Native (Framework Layer)

**Goal:** Everything you built manually, now using FastAPI's actual tools.

**Status: NOT STARTED**

#### Block 3A — Native Parameter Binding

- `Path(...)`, `Query(...)`, `Body(...)` in real FastAPI routes
- Combining all three in a single route
- Response models with `response_model=`

#### Block 3B — Settings & Config

- `pydantic-settings` with `BaseSettings`
- Env vars loaded and type-coerced on startup
- App crashes on boot if required fields missing

#### Block 3C — Database Layer (SQLModel)

- Models as both Pydantic schemas and DB tables
- Async sessions with `AsyncSession`
- Basic CRUD operations

#### Block 3D — Dependency Injection (Depends)

- `Depends()` for DB session lifecycle
- Nested dependencies: `Depends(get_user)` inside `Depends(get_current_user)`
- Dependency yields (generator pattern)

#### Block 3E — Alembic Migrations

- Alembic wired to SQLModel metadata
- `env.py` configured
- `alembic revision --autogenerate` workflow
- `upgrade` and `downgrade` scripts

#### Block 3F — JWT Auth

- Password hashing with `passlib`
- Token issuance: `python-jose` or `PyJWT`
- `exp` claim, secret key signing
- `/token` route returns access token

#### Block 3G — RBAC Authorization

- `Depends(get_current_user)` extracts token from `Authorization` header
- User roles checked inside dependency
- 403 if role insufficient
- Route-level role annotation

#### Block 3H — WebSockets

- `@app.websocket("/ws")` endpoint
- Token validated on handshake
- Continuous message streaming
- Proper `WebSocketDisconnect` handling

#### Block 3I — Background Tasks & Task Queues

- `BackgroundTasks` for lightweight fire-and-forget
- Celery or Arq for heavy workloads
- Clear separation: which jobs go where and why

---

### PHASE 4 — Production Hardening

**Goal:** Make the system observable, testable, deployable.

**Status: NOT STARTED**

#### Block 4A — Testing (pytest + httpx)

- `pytest-asyncio` setup
- `AsyncClient` with `app` mounted
- DB fixture: create tables → run test → drop tables
- `dependency_overrides` to swap real DB for in-memory

#### Block 4B — Structured Logging

- `structlog` replacing all `print` calls
- JSON output format
- Log fields: `event`, `level`, `timestamp`, trace ID

#### Block 4C — Request Tracing Middleware

- ASGI middleware reads `X-Request-ID` header
- Generates UUID if missing
- Injects into `structlog` context for all logs in that request
- Appends to response headers

#### Block 4D — Global Exception Handling

- `@app.exception_handler(Exception)` catches everything
- Raw tracebacks never exposed to clients
- Structured JSON error response: `{error, message, request_id}`

#### Block 4E — Docker

- Multi-stage `Dockerfile`: build stage + runtime stage
- Non-root user
- Minimal final image size
- `.dockerignore`

#### Block 4F — Docker Compose

- `docker-compose.yml` with: app, PostgreSQL, Redis
- Health checks on DB before app starts
- Volume for DB persistence
- Env vars via `.env` file

#### Block 4G — CI Pipeline

- `.github/workflows/ci.yml`
- Steps: `ruff` format check → `mypy` type check → `pytest`
- Fails fast on first broken step
- Runs on push and pull request

#### Block 4H — Deployment

- Deploy to Railway, Render, or Fly.io
- Staging vs production environment separation
- Secrets managed via platform env vars (never in repo)

---

## RULES OF PROGRESSION

1. **Sandbox First:** Never use a framework feature until you've built it manually in a drill. FastAPI's `Depends` only after building your own dependency resolver.

2. **No Print Assertions:** From Phase 2 onwards, tests must use `assert` statements, not eyeball-the-output. Drills may still print for human readability, but assertions are required.

3. **Blank Page Only:** Capstone drills (end of each phase) are built from scratch. No copying previous drills. No boilerplate. Every connection wired by hand.

4. **One New Mechanic Per Drill:** Each drill introduces exactly one new concept. The rest of the drill is revision of what came before.

5. **Real Scenarios Only:** Every drill uses a named real-world scenario. No "FooHandler" or "test_function" names.

6. **Drill Density:** The default is one drill per mechanic. If a mechanic feels unsolid, ask for retention drills explicitly. A block is only considered complete when you can solve a cold drill (no notes, no reference) for that mechanic in under 15 minutes.

7. **Progress Tracker is always updated** after a session ends. If you forget to update it, tell the AI your current drill number at the start of the next session and it will recalibrate.

---

## SCENARIO BANK

**AI rule:** Never reuse a scenario from the Used list. Pick from Available. Move to Used after generating.

**Used (do not reuse):**
Gym, Online Checkout, Concert Venue, Hospital, Airport

**Available:**
Hotel, Bank, University, Courthouse, Restaurant, Shipping Port, Train Station, Pharmacy, Stock Exchange, Power Grid, Police Station, Embassy, Library, Immigration Checkpoint, Data Center, Space Station, Fire Station, Museum, Casino, Aquarium, Seaport, Nuclear Plant, City Hall, Unemployment Office, Customs Office, Blood Bank, Veterinary Clinic, Broadcast Studio, Satellite Control Room

---

## RETENTION DRILL RULES

When the user asks for more drills on the same block, the AI must:

1. **Keep the same core mechanic.** Do not introduce anything from the next block.
2. **Pick a fresh scenario** from the Available list.
3. **Add exactly one small twist** per retention drill — examples:
   - Add a second middleware hook with different logic
   - Add a second dependency with a different error condition
   - Add a new edge case test (empty string, None, boundary value)
   - Flip the order of stages and explain why it matters
   - Add an optional field to the Pydantic model with a default
4. **Do not add two twists at once.** One twist per retention drill, maximum.
5. Retention drills are numbered normally (drill 51, 52, etc.) — they are not separate.

---

## QUICK REFERENCE: KEY PATTERNS

### Registry + Decorator Pattern

```python
REGISTRY = {}

def register(name, checks: dict):
    def decorator(func):
        REGISTRY[name] = {"handler": func, "checks": checks}
        return func
    return decorator
```

### Three-Stage Dispatch (current pattern as of drill 50)

```python
async def dispatch(name, raw_payload, token):
    if name not in REGISTRY:
        print("404"); return
    route = REGISTRY[name]

    # Stage 1: Pydantic
    try:
        model = MyModel(**raw_payload)
    except ValidationError:
        print("Invalid data"); return

    # Stage 2: Middleware
    for hook in route["middleware"]:
        try:
            hook(model)
        except ValueError as e:
            print(f"Denied: {e}"); return

    # Stage 3: Async Dependencies
    resolved = {}
    for arg, dep in route["dependencies"].items():
        try:
            resolved[arg] = await dep(token)
        except ValueError as e:
            print(f"Denied: {e}"); return

    return await route["handler"](**resolved)
```

### Path Pattern Compiler (Phase 2C target)

```python
import re

def compile_path(path: str) -> re.Pattern:
    pattern = re.sub(r"\{(\w+)\}", r"(?P<\1>[^/]+)", path)
    return re.compile(f"^{pattern}$")
```

### Async Dependency with Yield (Phase 3D target)

```python
async def get_db():
    session = AsyncSession(engine)
    try:
        yield session
    finally:
        await session.close()
```

---

## GLOSSARY

| Term            | Meaning in this curriculum                                                     |
| --------------- | ------------------------------------------------------------------------------ |
| Registry        | A dict (`ROUTES = {}`) that maps names to handlers + metadata                  |
| Check function  | Sync function that raises `ValueError` on failure, returns a string on success |
| Middleware hook | Sync function that raises `ValueError` on failure, returns nothing             |
| Dependency      | Async function that takes a token and returns a real object                    |
| Resolved        | The dict built by running all dependencies, passed as `**kwargs` to handler    |
| Dispatch        | The central async function that runs all stages and calls the handler          |
| Stage           | One of: Pydantic validation, middleware loop, dependency loop                  |
| Handler         | The final async function that does the real work                               |
