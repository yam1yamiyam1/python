import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import numbers

os.system("cls")

# =============================================================================
# DRILL 09 — DECORATORS
# =============================================================================
# HOW TO RUN:  python drill-09-decorators.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              No skipping — do them in order.
# =============================================================================

# NEW SYNTAX REFERENCE
# --------------------
# A decorator is a function that WRAPS another function.
# It lets you add behavior before/after a function without changing it.
#
# BASIC SHAPE:
#   def my_decorator(fn):
#       def wrapper(*args, **kwargs):
#           # do something BEFORE
#           result = fn(*args, **kwargs)   # call the original
#           # do something AFTER
#           return result
#       return wrapper                     # return the wrapper, NOT wrapper()
#
# APPLYING A DECORATOR:
#   @my_decorator
#   def greet(name):
#       return f"Hello {name}"
#
#   # The above is EXACTLY the same as:
#   def greet(name):
#       return f"Hello {name}"
#   greet = my_decorator(greet)    # ← this is what @ does under the hood
#
# PRESERVING FUNCTION IDENTITY:
#   from functools import wraps
#   def my_decorator(fn):
#       @wraps(fn)                         # keeps fn.__name__ and fn.__doc__
#       def wrapper(*args, **kwargs):
#           return fn(*args, **kwargs)
#       return wrapper
#
# DECORATOR WITH ARGUMENTS (factory pattern):
#   def repeat(times):                     # outer: takes config
#       def decorator(fn):                 # middle: takes the function
#           def wrapper(*args, **kwargs):  # inner: runs on each call
#               for _ in range(times):
#                   fn(*args, **kwargs)
#           return wrapper
#       return decorator
#
#   @repeat(3)
#   def say_hi():
#       print("hi")


# =============================================================================
# SECTION A — UNDERSTANDING THE PATTERN (1–15)
# =============================================================================


# 1. Write a decorator `shout` that uppercases the return value of any function.
#    Apply it to a function `greet(name)` that returns f"hello {name}".
#    Print greet("alice").  Expected: HELLO ALICE
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@shout
def greet(name):
    return f"hello {name}"


print(greet("alice"))


# 2. Write a decorator `log_call` that prints "Calling: {function name}"
#    BEFORE the function runs, then returns the result normally.
#    Hint: fn.__name__ gives you the function's name.
#    Apply it to a function `add(a, b)` that returns a + b.
#    Print add(3, 4).
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


print(add(3, 4))


# 3. Write a decorator `log_result` that prints "Result: {return value}"
#    AFTER the function runs. Apply it to multiply(a, b) that returns a * b.
#    Print multiply(5, 6).
def log_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@log_result
def multiply(a, b):
    return a * b


multiply(5, 6)


# 4. Combine both: write `log` that prints the function name AND the result.
#    Apply it to `subtract(a, b)`. Print subtract(10, 3).


def log(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper


@log
def subtract(a, b):
    return a - b


subtract(10, 3)


# 5. Write a decorator `timer` that prints how long a function takes to run.
#    Use time.time() before and after. Already imported at the top.
#    Apply it to a function `slow_sum(nums)` that sums a list with a loop.
#    Print slow_sum(numbers).
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(result)
        print(f"Execution time for {func.__name__}: {duration:.4f} seconds")
        return result

    return wrapper


@timer
def slow_sums(nums):
    total = 0
    for num in nums:
        total += num
    return total


slow_sums(nums=numbers)
# 6. Write a decorator `validate_positive` that raises a ValueError
#    if the first argument is negative or zero.
#    Apply it to `square_root(n)` that returns n ** 0.5.
#    Print square_root(9). Then try square_root(-4) inside a try/except.

# 7. Write a decorator `clamp_result` that clamps the return value between 0 and 100.
#    Apply it to `scale(n)` that returns n * 10.
#    Print scale(5) → 50, scale(15) → 100, scale(-3) → 0.

# 8. Write a decorator `nullable` that returns None if the first argument is None,
#    otherwise calls the function normally.
#    Apply it to `get_upper(s)` that returns s.upper().
#    Print get_upper("hello") and get_upper(None).

# 9. Write a decorator `retry(times)` — a decorator FACTORY — that retries a
#    function up to `times` times if it raises an Exception, then re-raises.
#    Hint: use a loop, catch Exception, re-raise after the loop.
#    NEW SYNTAX:
#      def retry(times):
#          def decorator(fn):
#              def wrapper(*args, **kwargs):
#                  for i in range(times):
#                      try:
#                          return fn(*args, **kwargs)
#                      except Exception as e:
#                          last = e
#                  raise last
#              return wrapper
#          return decorator
#
#    Test it: make a function that fails twice then succeeds using a counter.
#    counter = {"n": 0}
#    @retry(3)
#    def flaky():
#        counter["n"] += 1
#        if counter["n"] < 3:
#            raise ValueError("not yet")
#        return "ok"
#    Print flaky().

# 10. Write a decorator `default_on_error` that catches any Exception
#     and returns a default value instead. Make it accept the default as an arg.
#     @default_on_error(default=0)
#     def risky(n):
#         return 100 // n
#     Print risky(5) → 20, risky(0) → 0.

# 11. Write a decorator `count_calls` that tracks how many times a function
#     has been called. Store the count on the wrapper function itself.
#     Hint: wrapper.calls = 0, then wrapper.calls += 1 inside wrapper.
#     Apply to `ping()` that returns "pong".
#     Call ping() 5 times. Print ping.calls.

# 12. Write a decorator `memoize` that caches results so the same inputs
#     are never computed twice.
#     Hint: cache = {}  inside the decorator (not wrapper).
#            key = args  (tuples are hashable)
#            if key in cache: return cache[key]
#     Apply to `slow_double(n)` that prints "computing..." then returns n * 2.
#     Call slow_double(5) twice — "computing..." should only print once.

# 13. Write a decorator `require_auth` that checks if a `user` dict has
#     role == "admin". If not, raise a PermissionError("Access denied").
#     The decorated function always takes `user` as its first argument.
#     Apply to `delete_user(user, target_name)` that prints f"Deleted {target_name}".
#     Test with users[0] (admin) and users[1] (non-admin) in a try/except.

# 14. Write a decorator `deprecated` that prints a warning
#     "WARNING: {fn.__name__} is deprecated" before calling the function.
#     Apply it to `old_format(user)` that returns user["name"].
#     Print old_format(users[0]).

# 15. Stack two decorators on one function. Apply BOTH `log` (from drill 4)
#     and `timer` (from drill 5) to a function `process(nums)` that returns sum(nums).
#     Print process(numbers).
#     NOTE: decorators apply bottom-up — the one closest to the function runs first.
#     @log
#     @timer
#     def process(nums): ...


# =============================================================================
# SECTION B — functools.wraps AND IDENTITY (16–25)
# =============================================================================

# NEW SYNTAX — read before starting:
# -----------------------------------
# Without @wraps, decorators clobber your function's name and docstring.
#
#   def my_dec(fn):
#       def wrapper(*args, **kwargs):
#           return fn(*args, **kwargs)
#       return wrapper
#
#   @my_dec
#   def greet(): "Says hello"
#
#   print(greet.__name__)   # "wrapper"  ← WRONG
#   print(greet.__doc__)    # None       ← WRONG
#
# Fix with @wraps:
#   from functools import wraps
#   def my_dec(fn):
#       @wraps(fn)
#       def wrapper(*args, **kwargs):
#           return fn(*args, **kwargs)
#       return wrapper
#
#   print(greet.__name__)   # "greet"   ← correct
#   print(greet.__doc__)    # "Says hello" ← correct


# 16. Write a decorator `preserve` using @wraps that does nothing but
#     preserves the function's identity. Apply it to:
#     def describe_user(user): "Returns user description"
#     Print describe_user.__name__ and describe_user.__doc__.

# 17. Rewrite your `log_call` from drill 2 using @wraps. Apply it to a
#     new function `get_price(product)` that returns product["price"].
#     Print get_price.__name__ — should be "get_price" not "wrapper".

# 18. Rewrite `timer` from drill 5 using @wraps.
#     Apply it to `sum_salaries(users)` that returns sum of all salaries.
#     Print sum_salaries.__name__ and the result.

# 19. Write `debug` decorator using @wraps that prints:
#     ">>> {fn_name}({args}, {kwargs})" before calling and
#     "<<< {fn_name} returned {result}" after.
#     Apply to `format_salary(user, currency="$")` that returns f"{currency}{user['salary']}".
#     Print format_salary(users[0]) and format_salary(users[1], currency="€").

# 20. Write `enforce_types` decorator that checks if all positional arguments
#     match the function's annotations using fn.__annotations__.
#     If any arg doesn't match its annotated type, raise a TypeError.
#     Hint:
#       import inspect
#       params = list(inspect.signature(fn).parameters.keys())
#       for i, (param, arg) in enumerate(zip(params, args)):
#           expected = fn.__annotations__.get(param)
#           if expected and not isinstance(arg, expected):
#               raise TypeError(...)
#     Apply to:
#       def multiply(a: int, b: int) -> int: return a * b
#     Print multiply(3, 4). Then try multiply("3", 4) in a try/except.


# =============================================================================
# SECTION C — DECORATOR FACTORIES (21–35)
# =============================================================================

# 21. Write `repeat(n)` decorator factory that calls the function n times.
#     @repeat(3)
#     def say(msg): print(msg)
#     say("hello")  → prints "hello" three times.

# 22. Write `prefix(text)` factory that prepends text to the return value.
#     @prefix(">>> ")
#     def status(user): return user["name"]
#     Print status(users[0]).  Expected: >>> Alice

# 23. Write `suffix(text)` factory that appends text to the return value.
#     @suffix(" ✓")
#     def confirm(msg): return msg
#     Print confirm("Saved").  Expected: Saved ✓

# 24. Write `limit(max_calls)` factory that raises a RuntimeError
#     after the function has been called more than max_calls times.
#     @limit(3)
#     def fetch(): return "data"
#     Call fetch() 3 times. Then call it once more in a try/except.

# 25. Write `validate_str(min_len, max_len)` factory that validates
#     the first string argument is between min_len and max_len characters.
#     Raise ValueError if not.
#     @validate_str(3, 20)
#     def set_username(name): return f"Username set: {name}"
#     Print set_username("Alice"). Try set_username("Al") in a try/except.

# 26. Write `clamp_arg(min_val, max_val)` factory that clamps the first
#     numeric argument before passing it to the function.
#     @clamp_arg(0, 100)
#     def set_volume(level): return f"Volume: {level}"
#     Print set_volume(50), set_volume(200), set_volume(-10).

# 27. Write `tag(html_tag)` factory that wraps the return value in an HTML tag.
#     @tag("h1")
#     def heading(text): return text
#     Print heading("Welcome").  Expected: <h1>Welcome</h1>
#     Apply @tag("li") to a function item(text) that returns text.
#     Print item("First").

# 28. Write `role_required(role)` factory that checks user["role"] == role.
#     The decorated function always takes user as its first argument.
#     @role_required("admin")
#     def admin_dashboard(user): return f"Welcome {user['name']}"
#     Print admin_dashboard(users[0]) — should work.
#     Try admin_dashboard(users[1]) in a try/except — should raise PermissionError.

# 29. Write `rate_limit(calls_per_second)` factory that raises RuntimeError
#     if the function is called faster than calls_per_second.
#     Use time.time() to track last call time.
#     Hint: store last call time on wrapper: wrapper.last_call = 0.0
#     @rate_limit(1)
#     def fetch_data(): return "data"
#     Print fetch_data(). Then immediately call it again in a try/except.

# 30. Write `transform_result(fn_transform)` factory that applies fn_transform
#     to the return value.
#     @transform_result(lambda x: x.upper())
#     def get_role(user): return user["role"]
#     Print get_role(users[0]).  Expected: ADMIN

# 31. Write `inject(key, value)` factory that injects a keyword argument
#     into every call automatically.
#     @inject("currency", "$")
#     def price_tag(amount, currency="€"): return f"{currency}{amount}"
#     Print price_tag(99) — should use "$" even though default is "€".

# 32. Stack @prefix("STATUS: ") and @suffix(" [OK]") on:
#     def ping(host): return host
#     Print ping("localhost").  Expected: STATUS: localhost [OK]
#     Remember: bottom decorator applies first.

# 33. Write `maybe(default)` factory — if the function raises any Exception,
#     return default instead.
#     @maybe(default=-1)
#     def divide(a, b): return a // b
#     Print divide(10, 2) → 5 and divide(10, 0) → -1.

# 34. Write `log_calls_to(storage: list)` factory that appends a call record
#     dict to storage on every call.
#     Record shape: {"fn": fn.__name__, "args": args, "kwargs": kwargs}
#     call_log = []
#     @log_calls_to(call_log)
#     def process(user): return user["name"]
#     Call process on every user. Print call_log.

# 35. Write `once` decorator (no arguments) that ensures a function only
#     runs ONCE — subsequent calls return the first result without re-running.
#     @once
#     def initialize(): print("Initializing..."); return "ready"
#     Call initialize() 3 times. Print each return value.
#     Expected: "Initializing..." prints once. All calls return "ready".


# =============================================================================
# SECTION D — DECORATING CLASSES AND METHODS (36–50)
# =============================================================================

# NEW SYNTAX — read before starting:
# ------------------------------------
# You can decorate class methods too. The wrapper still needs to accept self.
#
#   def log_method(fn):
#       @wraps(fn)
#       def wrapper(self, *args, **kwargs):
#           print(f"Calling {fn.__name__}")
#           return fn(self, *args, **kwargs)
#       return wrapper
#
#   class User:
#       @log_method
#       def greet(self): return f"Hi {self.name}"
#
# You can also decorate entire classes:
#
#   def add_repr(cls):
#       def __repr__(self):
#           fields = {k: v for k, v in self.__dict__.items()}
#           return f"{cls.__name__}({fields})"
#       cls.__repr__ = __repr__
#       return cls
#
#   @add_repr
#   class Product: ...

# 36. Write a method decorator `log_method` that prints
#     "Calling {cls_name}.{method_name}" before the method runs.
#     Hint: use self.__class__.__name__ inside wrapper.
#     Apply to a User class with a greet() method. Print greet for users[0].

# 37. Write a method decorator `validate_self` that raises ValueError
#     if self.name is empty or None before running the method.
#     Apply to a display() method in User. Test with a user with no name.

# 38. Write a method decorator `returns_copy` that deep-copies the return value
#     so callers can't mutate internal state.
#     import copy — use copy.deepcopy(result).
#     Apply to to_dict() in User. Mutate the returned dict and confirm
#     the original object is unchanged.

# 39. Write a class decorator `add_str` that adds a __str__ method to any class
#     that doesn't have one. The __str__ should return "{ClassName}({__dict__})".
#     Apply it to a bare class:
#       @add_str
#       class Config:
#           def __init__(self, host, port):
#               self.host = host
#               self.port = port
#     Print Config("localhost", 8080).

# 40. Write a class decorator `frozen` that prevents setting new attributes
#     after __init__ by overriding __setattr__.
#     Hint:
#       def frozen(cls):
#           original_init = cls.__init__
#           def new_init(self, *args, **kwargs):
#               original_init(self, *args, **kwargs)
#               self.__dict__["_frozen"] = True
#           def new_setattr(self, key, value):
#               if self.__dict__.get("_frozen") and key not in self.__dict__:
#                   raise AttributeError(f"Cannot add attribute '{key}'")
#               object.__setattr__(self, key, value)
#           cls.__init__ = new_init
#           cls.__setattr__ = new_setattr
#           return cls
#     Apply to User. Try user.nickname = "ace" in a try/except.

# 41. Write a class decorator `singleton` that ensures only one instance
#     of the class ever exists. Subsequent instantiations return the first.
#     Hint: store the instance on the class: cls._instance = None
#       @singleton
#       class Config:
#           def __init__(self, debug=False):
#               self.debug = debug
#     a = Config(debug=True)
#     b = Config(debug=False)
#     Print a is b  → True.  Print a.debug → True (first instance wins).

# 42. Write a class decorator `auto_repr` that generates __repr__ from __init__
#     parameter names and instance __dict__.
#     Apply to Product. Print repr(Product(**products[0])).

# 43. Write a method decorator `cache_property` that acts like @property
#     but caches the result after first access.
#     Hint: store on the instance: self.__dict__[fn.__name__] = result
#     Apply to an `initials` property on User that prints "computing..." then
#     returns the first letter of the name.
#     Access alice.initials twice — "computing..." should only print once.

# 44. Recreate Python's built-in @property from scratch (call it @myproperty).
#     It should work as a descriptor — implement __get__.
#     NEW SYNTAX:
#       class myproperty:
#           def __init__(self, fn):
#               self.fn = fn
#           def __get__(self, obj, objtype=None):
#               if obj is None:
#                   return self
#               return self.fn(obj)
#     Apply it to a `full_label` attribute on User: f"{name} — {role}".
#     Print alice.full_label.

# 45. Write a decorator `route(method, path)` that simulates FastAPI's
#     @app.get("/users") pattern. It should:
#     - store method and path on the function: fn.method, fn.path
#     - print "Registered: {METHOD} {path}" when the decorator is applied
#     - otherwise call the function normally
#
#     Apply it like this:
#       @route("GET", "/users")
#       def get_users(): return users
#
#       @route("POST", "/users")
#       def create_user(user): return user
#
#     Print get_users() and get_users.path and get_users.method.
#     This is the exact pattern FastAPI uses — @app.get("/users") is
#     a decorator factory that registers your function as a route handler.
