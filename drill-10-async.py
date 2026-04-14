import asyncio
import functools
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import products, users

os.system("cls")

# =============================================================================
# DRILL 10 — ASYNC / AWAIT
# =============================================================================
# HOW TO RUN:  python drill-10-async.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              No skipping — do them in order.
# =============================================================================

# NEW SYNTAX REFERENCE
# --------------------
# DEFINING AN ASYNC FUNCTION:
#   async def fetch(): ...          # just add async before def
#
# CALLING AN ASYNC FUNCTION:
#   result = await fetch()          # inside another async function
#   asyncio.run(fetch())            # at the top level (entry point)
#
# SLEEPING WITHOUT BLOCKING:
#   await asyncio.sleep(1)          # async version of time.sleep(1)
#   time.sleep(1)                   # ← WRONG in async — blocks everything
#
# RUNNING MULTIPLE TASKS AT ONCE:
#   results = await asyncio.gather(fn1(), fn2(), fn3())
#   # runs all three CONCURRENTLY, returns list of results in order
#
# CREATING TASKS (fire and don't wait):
#   task = asyncio.create_task(fn())    # starts fn, doesn't block
#   result = await task                 # wait for it later
#
# THE MENTAL MODEL:
#   Sync:  cook breakfast → wait → eat → shower → wait → leave
#   Async: start breakfast → start shower → breakfast done → eat → shower done → leave
#   Async doesn't make things faster on CPU work — it saves time on WAITING
#   (network calls, DB queries, file I/O). FastAPI is async because web
#   servers spend most time waiting for DB/network responses.
#
# IMPORTANT:
#   async def always returns a coroutine — calling it without await does nothing.
#   You MUST await it or wrap in asyncio.run().
#   await only works INSIDE an async function.


# =============================================================================
# SECTION A — BASIC ASYNC SYNTAX (1–15)
# =============================================================================


# 1. Write an async function `hello()` that prints "Hello, async world!".
#    Run it with asyncio.run(hello()).
async def hello():
    print("Hello, async world")


asyncio.run(hello())


# 2. Write an async function `get_name() -> str` that returns "Alice".
#    Write another async function `main()` that awaits get_name() and prints it.
#    Run main() with asyncio.run().
async def get_name() -> str:
    return "Alice"


async def main():
    data = await get_name()
    print(data)


asyncio.run(main())


# 3. Write an async function `delayed_hello(name: str)` that:
#    - prints "Starting..."
#    - awaits asyncio.sleep(0.5)
#    - prints f"Hello {name}!"
#    Run it. Notice it pauses half a second.
async def delayed_hello(name: str):
    print("Starting...")
    await asyncio.sleep(0.5)
    print(f"Hello {name}")


asyncio.run(delayed_hello("Alice"))
# 4. Write an async function `fetch_user(id: int) -> dict` that:
#    - awaits asyncio.sleep(0.1)  (simulates a DB call)
#    - returns the user from the users list matching that id
#    - returns None if not found
#    Write a main() that fetches user id=3 and prints their name.


async def fetch_user(id: int) -> dict | None:
    await asyncio.sleep(0.1)
    for u in users:
        if u["id"] == id:
            return u
    return None


async def main():
    print("Fetching user...")
    user = await fetch_user(3)

    if user:
        print(f"Found user: {user['name']}")
    else:
        print("User not found.")


if __name__ == "__main__":
    asyncio.run(main())


# 5. Write an async function `fetch_product(id: int) -> dict | None`
#    that simulates a 0.1s DB call and returns the matching product.
#    Write a main() that fetches product id=2 and prints its name and price.
async def fetch_product(id: int) -> dict | None:
    await asyncio.sleep(0.1)
    for p in products:
        if p["id"] == id:
            return p
    return None


async def main():
    print("Fetching product...")
    product = await fetch_product(2)
    if product:
        print(f"{product['name']} - ${product['price']:.2f}")
    else:
        print("Product not found.")


asyncio.run(main())


# 6. Write an async function `fetch_all_users() -> list[dict]`
#    that awaits asyncio.sleep(0.2) then returns the full users list.
#    Write main() that awaits it and prints all names.
async def fetch_all_users() -> list[dict]:
    await asyncio.sleep(0.2)
    return users


async def main():
    users = await fetch_all_users()
    print([u["name"] for u in users])


asyncio.run(main())


# 7. Write two async functions: `step_one()` and `step_two()`.
#    Each prints its name, sleeps 0.3s, then prints "done".
#    Write a main() that awaits them SEQUENTIALLY (one after the other).
#    Print total time. Expected: ~0.6s total.
#    Hint: start = time.time() before, print time.time() - start after.
def timer(fn):
    @functools.wraps(fn)
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await fn(*args, **kwargs)
        end = time.time()
        total_time = end - start
        print(f"Execution time for {fn.__name__}: {total_time:.4f} seconds")
        return result

    return wrapper


@timer
async def step_one():
    print(f"Running: {step_one.__name__}")
    await asyncio.sleep(0.3)
    print(f"{step_one.__name__} is done")


@timer
async def step_two():
    print(f"Running: {step_two.__name__}")
    await asyncio.sleep(0.3)
    print(f"{step_two.__name__} is done")


async def main():
    await step_one()
    await step_two()


asyncio.run(main())


# 8. Now rewrite main() from drill 7 to run step_one() and step_two()
#    CONCURRENTLY using asyncio.gather().
#    Print total time. Expected: ~0.3s (both run at the same time).
async def main():
    await asyncio.gather(step_one(), step_two())


asyncio.run(main())


# 9. Write an async function `fetch_with_delay(name: str, delay: float) -> str`
#    that sleeps delay seconds then returns f"{name} ready".
#    Use asyncio.gather() to run these three at once:
#      fetch_with_delay("users", 0.3)
#      fetch_with_delay("products", 0.1)
#      fetch_with_delay("orders", 0.2)
#    Print all results. Total time should be ~0.3s not ~0.6s.
async def fetch_with_delay(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name} ready"


@timer
async def main():
    results = await asyncio.gather(
        fetch_with_delay("users", 0.3),
        fetch_with_delay("products", 0.1),
        fetch_with_delay("orders", 0.2),
    )
    for data in results:
        print(data)


asyncio.run(main())


# 10. Write an async function `safe_fetch(id: int) -> dict | None`
#     that wraps fetch_user() from drill 4 in a try/except.
#     If the user is not found, return None instead of raising.
#     Print safe_fetch(1) and safe_fetch(999).
async def safe_fetch(id: int) -> dict | None:
    try:
        user = await fetch_user(id)
        return user
    except Exception:
        return None


print(asyncio.run(safe_fetch(1)))
print(asyncio.run(safe_fetch(99)))

# 11. Write an async function `fetch_users_by_ids(ids: list[int]) -> list[dict]`
#     that fetches each user concurrently using asyncio.gather().
#     Print the names of users with ids [1, 3, 5, 7].
to_fetch = [1, 3, 5, 7]


async def fetch_users_by_ids(ids: list[int]) -> list[dict]:
    tasks = [safe_fetch(id) for id in ids]
    users = await asyncio.gather(*tasks)
    print([u["name"] for u in users if u])


asyncio.run(fetch_users_by_ids(to_fetch))


# 12. Write an async function `timed(label: str, coro)` that:
#     - records start time
#     - awaits the coroutine
#     - prints f"{label} took {elapsed:.3f}s"
#     - returns the result
#     NEW SYNTAX: coro is a coroutine object — just await it directly.
#     Use it: result = await timed("fetch users", fetch_all_users())
async def timed(label: str, coro):
    start_time = time.time()
    result = await coro
    end_time = time.time()
    elapsed = end_time - start_time
    print(f"{label} took {elapsed:.3f}s")
    return result


async def main():
    user_list = await timed("fetch users", fetch_all_users())
    print(user_list)


asyncio.run(main())


# 13. Write an async generator `count_up(n: int)`:
#     NEW SYNTAX:
#       async def count_up(n: int):
#           for i in range(n):
#               await asyncio.sleep(0.05)
#               yield i                     # async generator — use yield
#
#     Consume it with:
#       async for value in count_up(5):
#           print(value)
async def count_up(n: int):
    for i in range(n):
        await asyncio.sleep(0.05)
        yield i


async def run_generator():
    async for value in count_up(5):
        print(value)


asyncio.run(run_generator())

# 14. Write an async function `first_done(coros: list) -> any`
#     that returns the result of whichever coroutine finishes first.
#     NEW SYNTAX:
#       done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
#       for task in pending:
#           task.cancel()
#       result = done.pop().result()
#     Hint: wrap each coro in asyncio.create_task() first.
#     Test with fetch_with_delay("a", 0.3) and fetch_with_delay("b", 0.1).
#     Expected result: "b ready".

# 15. Write a main() that fetches ALL users AND ALL products concurrently,
#     then prints a summary: "Loaded {n} users and {m} products".
#     Use asyncio.gather(fetch_all_users(), fetch_all_products()).
#     Write fetch_all_products() first (same shape as fetch_all_users).


# =============================================================================
# SECTION B — ASYNC PATTERNS IN FASTAPI STYLE (16–30)
# =============================================================================

# NEW SYNTAX — read before starting:
# ------------------------------------
# In FastAPI, your route handlers are async functions.
# You don't call asyncio.run() yourself — FastAPI does that.
# You just write:
#
#   @app.get("/users")
#   async def get_users():
#       users = await db.fetch_all("SELECT * FROM users")
#       return users
#
# For now we simulate the DB with async functions and asyncio.sleep().
# The pattern is identical to what you'll write in real FastAPI routes.
#
# SIMULATED DB LAYER:
#   async def db_get_all(table: list) -> list:
#       await asyncio.sleep(0.1)   # simulate query time
#       return table
#
#   async def db_get_one(table: list, id: int) -> dict | None:
#       await asyncio.sleep(0.05)
#       return next((item for item in table if item["id"] == id), None)

# 16. Write the two simulated DB functions above: db_get_all and db_get_one.
#     Write a main() that uses them to fetch all users and then user id=2.
#     Print results.

# 17. Simulate a GET /users route handler:
#     async def route_get_users() -> list[dict]:
#         return await db_get_all(users)
#     Write main() that calls it and prints all names.

# 18. Simulate a GET /users/{id} route handler:
#     async def route_get_user(id: int) -> dict | None:
#         user = await db_get_one(users, id)
#         if user is None:
#             raise ValueError(f"User {id} not found")
#         return user
#     Write main() that fetches id=4 (success) and id=99 (caught exception).

# 19. Simulate a POST /users route (create):
#     async def route_create_user(new_user: dict) -> dict:
#         await asyncio.sleep(0.05)   # simulate insert
#         return {"id": len(users) + 1, **new_user}
#     Write main() that creates {"name": "Yuan", "age": 25, "role": "user"}.
#     Print the returned dict.

# 20. Simulate a DELETE /users/{id} route:
#     async def route_delete_user(id: int) -> dict:
#         user = await db_get_one(users, id)
#         if user is None:
#             raise ValueError("Not found")
#         return {"deleted": True, "user": user}
#     Write main() and test with id=1 and id=99.

# 21. Simulate a GET /products route and GET /products/{id} route.
#     Run both in a single main() using gather.
#     Print "Found {n} products" and the name of product id=3.

# 22. Write an async function `get_user_orders(user_id: int) -> list[dict]`
#     that fetches orders where userId == user_id.
#     Simulate a 0.1s delay. Print orders for user_id=1.

# 23. Write an async function `get_user_with_orders(user_id: int) -> dict`
#     that fetches the user AND their orders CONCURRENTLY using gather(),
#     then returns {"user": user, "orders": orders_list}.
#     Print the result for user_id=1.

# 24. Write an async function `get_dashboard() -> dict`
#     that fetches users, products, and orders ALL concurrently,
#     then returns:
#       {
#         "total_users": int,
#         "total_products": int,
#         "total_orders": int,
#         "total_revenue": int   (sum of all order totals)
#       }
#     Print it.

# 25. Write an async function `search_users(query: str) -> list[dict]`
#     that simulates a search (0.1s delay) and returns users whose name
#     contains query (case-insensitive). Print search_users("a").

# 26. Write an async function `bulk_create_users(new_users: list[dict]) -> list[dict]`
#     that creates each user concurrently (simulate 0.05s per insert with gather).
#     Returns list of created dicts with generated ids.
#     Test with 3 new users. Print results.

# 27. Write an async function `paginate(table: list, page: int, size: int) -> dict`
#     that simulates pagination with a 0.05s delay and returns:
#       {"data": [...], "page": page, "size": size, "total": len(table)}
#     Print paginate(users, 1, 3) and paginate(users, 2, 3).

# 28. Write an async context manager `db_connection()`:
#     NEW SYNTAX:
#       from contextlib import asynccontextmanager
#       @asynccontextmanager
#       async def db_connection():
#           print("DB connected")
#           yield {"connected": True}   # the "connection" object
#           print("DB disconnected")
#
#     Use it:
#       async with db_connection() as conn:
#           print(conn)
#     This is how FastAPI manages DB sessions in real apps.

# 29. Write an async function `with_timeout(coro, seconds: float)`
#     that cancels the coroutine if it takes longer than seconds.
#     NEW SYNTAX:
#       try:
#           result = await asyncio.wait_for(coro, timeout=seconds)
#           return result
#       except asyncio.TimeoutError:
#           return None
#     Test: with_timeout(fetch_with_delay("slow", 1.0), 0.3) → None
#           with_timeout(fetch_with_delay("fast", 0.1), 0.3) → "fast ready"

# 30. Write a complete simulated FastAPI-style app as async functions:
#     - db_get_all / db_get_one (from drill 16)
#     - route_get_users()
#     - route_get_user(id)
#     - route_create_user(data)
#     - route_delete_user(id)
#     Write a main() that runs this sequence:
#       1. GET all users → print count
#       2. GET user id=3 → print name
#       3. POST new user Yuan → print returned dict
#       4. DELETE user id=2 → print confirmation
#     Run everything concurrently where possible, sequentially where order matters.
#     This is the closest thing to a real FastAPI app without the framework.
