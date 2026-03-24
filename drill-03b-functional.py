import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from functools import reduce

from training_data import numbers, orders, products, students, users

# =============================================================================
# DRILL 03b — ADVANCED FUNCTIONAL PYTHON
# Lambdas · *args/**kwargs · Scope & Closures · Higher-Order Functions
# 100 Drills | Increasing Entropy
# =============================================================================
# HOW TO RUN:  python drill-03b-functional.py
# RULES:       Write your answer directly below each drill comment.
#              Every drill must print something to verify your answer.
#              Do them in order — each section builds on the last.
# =============================================================================


# =============================================================================
# QUICK REFERENCE
# =============================================================================
#
# LAMBDA
#   lambda x: x * 2                        # single arg
#   lambda x, y: x + y                     # multi arg
#   lambda x: "yes" if x > 0 else "no"    # ternary — only type of branch allowed
#   sorted(lst, key=lambda x: x["age"])    # as sort key
#
# *ARGS / **KWARGS
#   def fn(*args):       args is a TUPLE   → iterate with for
#   def fn(**kwargs):    kwargs is a DICT  → iterate with kwargs.items()
#   def fn(*args, **kwargs):               → accept anything
#   fn(*[1,2,3])         unpack list into positional args
#   fn(**{"a":1,"b":2})  unpack dict into keyword args
#
# GLOBAL / NONLOCAL
#   x = 0
#   def fn():
#       global x     ← required to WRITE to module-level variable
#       x += 1
#
#   def outer():
#       count = 0
#       def inner():
#           nonlocal count   ← required to WRITE to enclosing (not global) var
#           count += 1
#       return inner
#
# HIGHER-ORDER FUNCTIONS
#   map(func, iterable)      → lazy iterator, wrap in list() to see results
#   filter(func, iterable)   → lazy iterator, wrap in list()
#   sorted(lst, key=func)    → returns NEW sorted list
#   Functions are values — pass them, return them, store them in variables
#
# =============================================================================


# =============================================================================
# SECTION E — DEEP-DIVE LAMBDAS (E1–E25)
# WHY THIS SECTION: Lambdas are Python's arrow functions — but they are
# intentionally limited to ONE expression. This section trains your eye to
# recognize when a lambda is appropriate (short transforms, sort keys,
# filter predicates) vs when you need a full def. The drills go from
# simple math → data extraction → sorting → filtering → chaining.
# =============================================================================

# E1. WHY: Confirms you can assign a lambda to a variable just like JS const.
#     INPUT:  any number x
#     OUTPUT: x * x
#     Call it with 5. Print the result.
square = lambda x: x**2
print(square(5))

# E2. WHY: Repeats the assign-to-variable pattern with a different operation.
#     INPUT:  any number x
#     OUTPUT: x * x * x
#     Call it with 3. Print the result.
cube = lambda x: x**3
print(cube(3))

# E3. WHY: Shows that lambdas work with unary (single-arg) operations too.
#     INPUT:  any number x
#     OUTPUT: x with its sign flipped (7 → -7, -4 → 4)
#     Call it with 7 and -4. Print both.
negate = lambda x: -x
print(negate(7))
print(negate(-4))

# E4. WHY: Introduces multi-argument lambdas.
#     INPUT:  x (number), y (number)
#     OUTPUT: x + y
#     Call it with (10, 20). Print.
add = lambda x, y: x + y
print(add(10, 20))

# E5. WHY: Real-world math lambda with two named inputs.
#     INPUT:  x = the part, y = the whole (e.g. x=25, y=200)
#     OUTPUT: float — (x / y) * 100  →  12.5
#     Call it with (25, 200). Print.
percent = lambda x, y: x / y * 100
print(percent(25, 200))

# E6. WHY: Nested ternary — the most complex branch a lambda can handle.
#     "Clamping" a number to a range is a very common utility.
#     INPUT:  x = value to clamp, lo = minimum allowed, hi = maximum allowed
#     OUTPUT: lo if x is below range, hi if above, x itself if in range
#     Call it with (5, 0, 10) → 5, (-3, 0, 10) → 0, (15, 0, 10) → 10. Print all.
clamp = lambda x, lo, hi: lo if x < hi else (hi if x > hi else x)
print(clamp(5, 0, 10))
print(clamp(-3, 0, 10))
print(clamp(15, 0, 10))

# E7. WHY: Functions are first-class values — you can store them in a list
#     and call them by iterating. This is the foundation of pipelines.
#     INPUT:  ops is a list of lambdas, each takes one number
#     OUTPUT: three printed numbers — 4+1=5, 4*2=8, 4**2=16
ops = [lambda x: x + 1, lambda x: x * 2, lambda x: x**2]
for op in ops:
    print(op(4))

# E8. WHY: Lambdas work on dicts too — this pattern (extract one field)
#     is used constantly as a sort key or map transform.
#     INPUT:  x = any dict that has a "name" key  (e.g. a user dict)
#     OUTPUT: the string value of x["name"]
#     Call it on users[0]. Print.
get_name = lambda x: x["name"]
print(get_name(users[0]))

# E9. WHY: Same extraction pattern — applied to every item in a list.
#     INPUT:  x = a user dict  (must have "salary" key)
#     OUTPUT: the integer salary value
#     Call it on every user. Print each salary.
get_salary = lambda x: x["salary"]
for u in users:
    print(get_salary(u))

# E10. WHY: sorted() takes a `key=` function — this is the most common real
#      use of lambdas in Python. You never mutate the list; sorted() returns new.
#      INPUT:  users list, sorted in place by age (youngest first)
#      OUTPUT: user names printed youngest → oldest
#      Syntax: sorted(users, key=lambda u: u["age"])
for u in sorted(users, key=lambda u: u["age"]):
    print(u["name"])

# E11. WHY: reverse=True flips the sort — no minus sign trick needed like JS.
#      INPUT:  users list, sorted by salary highest → lowest
#      OUTPUT: "Alice - 72000" style lines, richest first
for u in sorted(users, key=lambda u: u["salary"], reverse=True):
    print(f"{u['name']} - {u['salary']}")

# E12. WHY: Same sorted() pattern applied to products.
#      INPUT:  products list, sorted by price lowest → highest
#      OUTPUT: "Iron Sword - 120" style lines
for p in sorted(products, key=lambda p: p["price"]):
    print(f"{p['name']} - {p['price']}")

# E13. WHY: Sorting orders by total — most expensive first.
#      INPUT:  orders list, sorted by total highest → lowest
#      OUTPUT: "Order #1 - $240" style lines
for o in sorted(orders, key=lambda o: o["total"], reverse=True):
    print(f"Order #{o['id']} - ${o['total']}")

# E14. WHY: Sorting by a numeric field on a different dataset.
#      INPUT:  students list, sorted by attendance highest → lowest
#      OUTPUT: "Noah - 99" style lines
for s in sorted(students, key=lambda s: s["attendance"], reverse=True):
    print(f"{s['name']} - {s['attendance']}")

# E15. WHY: Sorting strings alphabetically — Python compares strings
#      lexicographically by default, so this just works.
#      INPUT:  users list, sorted by name A → Z
#      OUTPUT: names printed in alphabetical order
for u in sorted(users, key=lambda u: u["name"]):
    print(u["name"])

# E16. WHY: Tuple key = multi-level sort. First sort by category A→Z,
#      then within each category sort by price low→high.
#      This is Python's equivalent of SQL ORDER BY category, price.
#      INPUT:  products list
#      OUTPUT: "Iron Sword weapon - $120" — grouped by category, price-ordered within
#      Hint: key=lambda p: (p["category"], p["price"])
for p in sorted(products, key=lambda p: (p["category"], p["price"])):
    print(f"{p['name']} {p['category']} - ${p['price']}")

# E17. WHY: filter() is the built-in equivalent of JS .filter().
#      It returns a lazy iterator — wrap in list() to get a real list.
#      INPUT:  users list + lambda that returns True for active users
#      OUTPUT: list of full user dicts where isActive == True
#      Print the names of results.
print(list(filter(lambda u: u["isActive"], users)))

# E18. WHY: filter() applied to products — same pattern, different data.
#      INPUT:  products list + lambda checking price < 100
#      OUTPUT: "Health Potion - $25" style lines for cheap products only
for p in list(filter(lambda p: p["price"] < 100, products)):
    print(f"{p['name']} - ${p['price']}")

# E19. WHY: filter() to select by string field value.
#      INPUT:  orders list + lambda checking status == "completed"
#      OUTPUT: list of "Order #X" strings for completed orders only
print(
    [
        f"Order #{o['id']}"
        for o in list(filter(lambda o: o["status"] == "completed", orders))
    ]
)

# E20. WHY: filter() on students — practicing the same mental model across
#      different datasets builds the pattern into muscle memory.
#      INPUT:  students list + lambda checking attendance > 85
#      OUTPUT: list of names of high-attendance students
print([s["name"] for s in list(filter(lambda s: s["attendance"] > 85, students))])

# E21. WHY: map() is the built-in equivalent of JS .map().
#      Like filter(), it returns a lazy iterator — wrap in list().
#      INPUT:  users list + lambda extracting the "name" field
#      OUTPUT: ["Alice", "Bob", "Carol", ...] — one name per user
print(list(map(lambda u: u["name"], users)))

# E22. WHY: map() to build formatted strings — common for display layers.
#      INPUT:  users list + lambda building a display string per user
#      OUTPUT: ["Alice - $72000", "Bob - $38000", ...] — one string per user
print(list(map(lambda u: f"{u['name']} - ${u['salary']}", users)))

# E23. WHY: map() on a plain list of numbers — same tool, simpler data.
#      INPUT:  numbers list + lambda doubling each value
#      OUTPUT: new list with each number doubled  [8, 16, 30, ...]
print(list(map(lambda n: n * 2, numbers)))

# E24. WHY: Chaining filter() inside map() — the outer map() transforms,
#      the inner filter() selects. Read inside-out: filter first, then map.
#      This is the Python equivalent of arr.filter(...).map(...) in JS.
#      INPUT:  users list, filtered to active + salary > 50000, then names extracted
#      OUTPUT: list of names of high-earning active users only
print(
    list(
        map(
            lambda u: u["name"],
            filter(lambda u: u["isActive"] and u["salary"] > 50000, users),
        )
    )
)

# E25. WHY: Nested ternary inside a lambda used as a map key.
#      This is the limit of what lambdas should do — any more complex and
#      you should switch to a def.
#      INPUT:  u = a user dict with a "salary" field
#      OUTPUT: "High" if salary > 70000, "Mid" if > 45000, "Low" otherwise
#      Apply with map() to produce "Alice - High" style strings. Print.
salary_bracket = lambda u: (
    "High" if u["salary"] > 70000 else ("Mid" if u["salary"] > 45000 else "Low")
)
print(list(map(lambda u: f"{u['name']} - {salary_bracket(u)}", users)))


# =============================================================================
# SECTION F — *ARGS AND **KWARGS (F1–F25)
# WHY THIS SECTION: *args and **kwargs let functions accept a variable number
# of inputs — like JS rest params (...args) but Python also has **kwargs for
# named arguments. This unlocks flexible APIs, utility functions, and
# the ability to forward arguments between functions (critical for HOFs).
# Rule of thumb: *args = "I don't know how many values" (tuple inside)
#                **kwargs = "I don't know which named fields" (dict inside)
# =============================================================================


# F1. WHY: The simplest *args use case — collect numbers, sum them.
#     Teaches that *args becomes a TUPLE you can pass directly to sum().
#     INPUT:  any number of integers passed as separate arguments
#     OUTPUT: their sum as a single integer
#     Call it with (1, 2, 3) → 6, then (10, 20, 30, 40) → 100. Print both.
def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))


# F2. WHY: *args with reduce() — since there's no built-in product(),
#     this shows how to fold a tuple with a lambda.
#     INPUT:  any number of integers
#     OUTPUT: their product (all multiplied together)  2*3*4 = 24
def multiply_all(*args):
    return reduce(lambda x, y: x * y, args)


print(multiply_all(2, 3, 4))


# F3. WHY: Index access on *args tuple. args[0] = first, args[-1] = last.
#     INPUT:  any number of values (at least 2)
#     OUTPUT: list [first_value, last_value]
def first_and_last(*args):
    return [args[0], args[-1]]


print(first_and_last(1, 9, 8, 744, 52))


# F4. WHY: len() works on the args tuple just like any sequence.
#     INPUT:  any number of arguments
#     OUTPUT: integer count of how many were passed
def count_args(*args):
    print(len(args))


count_args(1, 5, 4, 7, 8, 5)
count_args(1, 5, 4, 7, 8, 5, 5, 8, 7, 4)
count_args(1, 5, 4, 7, 8, 5, 5, 5, 2, 2, 4, 4, 7, 5, 5, 6)


# F5. WHY: Iterating over args with a list comprehension — same as iterating
#     any tuple. Shows you can mix types freely.
#     INPUT:  mixed types — int, str, float, bool, None
#     OUTPUT: list of type objects  [<class 'int'>, <class 'str'>, ...]
def print_types(*args):
    print([type(a) for a in args])


print_types(1, "hello", 3.14, True, None)


# F6. WHY: Real utility function — *args collects all numbers, built-ins
#     do the work. The key trick: stats(*numbers) UNPACKS the list into
#     individual arguments — the * outside the call spreads the list.
#     INPUT:  any number of numeric arguments (call with *numbers to unpack list)
#     OUTPUT: dict with keys count, sum, min, max, avg
def stats(*args):
    result = {
        "count": len(args),
        "sum": sum(args),
        "min": min(args),
        "max": max(args),
        "avg": sum(args) / len(args),
    }
    print(result)


# stats(*numbers) unpacks the list → stats(4, 8, 15, 16, 23, 42, ...)
# print(*numbers) also unpacks — prints all values space-separated
stats(*numbers)
print(*numbers)


# F7. WHY: *names is a tuple of strings — iterate with for, same as any tuple.
#     INPUT:  any number of name strings
#     OUTPUT: "Hello, {name}!" printed once per name
def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")


greet_all("Yuan", "Ann", "Gojo", "Sukuna")


# F8. WHY: str.join() works on any iterable — including the args tuple.
#     INPUT:  any number of word strings
#     OUTPUT: single string with all words joined by a space
def build_sentence(*words):
    print(" ".join(words))


build_sentence("Fuck", "you", "bitch", "ass", "nigga")


# F9. WHY: **kwargs lets you pass named HTML attributes without listing them all.
#     kwargs is a dict inside the function — iterate with .items() to get k, v pairs.
#     INPUT:  element = tag name string (e.g. "a")
#             **attr = any number of keyword args as HTML attributes
#     OUTPUT: HTML string like '<a href="https://example.com" class_="link">'
def tag(element, **attr):
    # Build a list: ["a", 'href="https://..."', 'class_="link"']
    # then join with spaces inside angle brackets
    string = [element]
    for k, v in attr.items():
        string.append(f'{k}="{v}"')
    print(f"<{' '.join(string)}>")


tag("a", href="https://example.com", class_="link")


# F10. WHY: **kwargs is literally just a dict — this drill shows that
#      returning kwargs directly gives you a plain dict.
#      INPUT:  any named keyword arguments
#      OUTPUT: dict with those same key-value pairs
#              create_user(name="Alice", age=32, role="admin")
#              → {"name": "Alice", "age": 32, "role": "admin"}
def create_user(**kwargs):
    # Building manually here to show it — could also just return kwargs directly
    user = {}
    for k, v in kwargs.items():
        user[k] = v
    print(user)


create_user(name="Alice", age=32, role="admin")


# F11. WHY: Logging pattern — **kwargs lets callers pass any fields they want
#      without you needing to define every possible parameter upfront.
#      INPUT:  any named keyword arguments
#      OUTPUT: each key=value pair printed on its own line
def log(**fields):
    for k, v in fields.items():
        print(f"{k}={v}")


log(event="login", user="Alice", ip="192.168.1.1")


# F12. WHY: {**user, **updates} is Python's spread merge — like JS {...user, ...updates}.
#      IMPORTANT: this function MUTATES the original user dict because
#      user_to_update = user just copies the reference, not the data.
#      A truly safe version would use {**user, **updates} and return a new dict.
#      INPUT:  user = existing user dict, **updates = fields to override
#      OUTPUT: the user dict with updated fields printed
def update_user(user, **updates):
    # NOTE: this mutates the original — see the comment above about the bug
    user_to_update = user
    for k, v in updates.items():
        user_to_update[k] = v
    print(user_to_update)


update_user(users[0], salary=99999, role="superadmin")


# F13. WHY: *dicts collects multiple dict arguments — dict.update() merges
#      later dicts over earlier ones. This is a variadic merge utility.
#      INPUT:  any number of dict arguments
#      OUTPUT: single merged dict (later keys override earlier)
def merge(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    print(result)


# NOTE: merge() is defined but never called here — the next 3 lines just
# print individual dicts for reference. Call merge(users[1], products[1]) to test.
print(users[1])
print(products[1])
print(students[1])


# F14. WHY: Mixing required positional args (a, b) with *args and **kwargs.
#      Rule: required args MUST come before *args in the signature.
#      INPUT:  a=1 (required), b=2 (required), then any extra positional + keyword args
#      OUTPUT: prints a, b, the extra args tuple (3,4,5), and kwargs dict {x,y}
def flexible(a, b, *args, **kwargs):
    print(a)  # first required arg
    print(b)  # second required arg
    print(args)  # tuple of anything extra: (3, 4, 5)
    print(kwargs)  # dict of named extras: {"x": "hello", "y": True}


flexible(1, 2, 3, 4, 5, x="hello", y=True)


# F15. WHY: Filtering kwargs by type — shows that kwargs is a normal dict
#      and you can apply any dict/list operation to it.
#      INPUT:  any keyword arguments of mixed types
#      OUTPUT: list of "key=value" strings for string-valued kwargs only
#              only_kwargs(name="Alice", age=32, role="admin", score=99)
#              → ["name=Alice", "role=admin"]  (age and score are not strings)
def only_kwargs(**kwargs):
    print([f"{k}={v}" for k, v in kwargs.items() if isinstance(v, str)])


only_kwargs(name="Alice", age=32, role="admin", score=99)


# F16. WHY: Combining a required positional arg with *args — here price is fixed,
#      but you can pass as many discount rates as you want.
#      Uses reduce() to apply discounts sequentially (each one builds on the last).
#      INPUT:  price = starting price (float/int)
#              *discount_rates = any number of rates as decimals (0.1 = 10% off)
#      OUTPUT: set containing the final discounted price  {72.0}
#              apply_discount(100, 0.1, 0.2) → 100 * 0.9 * 0.8 = 72.0
def apply_discount(price, *discount_rates):
    print({reduce(lambda final, d: final * (1 - d), discount_rates, price)})


apply_discount(100, 0.1, 0.2)


# F17. WHY: args[::2] is a slice taking every other element starting at 0 (keys).
#      args[1::2] takes every other element starting at 1 (values).
#      zip() pairs them up. dict() converts pairs to a dict.
#      INPUT:  even number of args — alternating key, value, key, value ...
#              zip_to_dict("name", "Alice", "age", 32)
#      OUTPUT: {"name": "Alice", "age": 32}
def zip_to_dict(*args):
    result = dict(zip(args[::2], args[1::2]))
    print(result)


zip_to_dict("name", "Alice", "age", 32)


# F18. WHY: *required collects the field names to check as a tuple.
#      Iterates through them and returns False the moment one is missing.
#      INPUT:  data = any dict, *required = field name strings to check
#      OUTPUT: True if ALL required keys exist in data, False if any missing
#              require_fields(users[0], "name", "salary", "nickname")
#              → False  (users[0] has no "nickname" key)
def require_fields(data: dict, *required):
    for r in required:
        if r not in data:
            return False
    return True


print(require_fields(users[0], "name", "salary", "nickname"))


# F19. WHY: **dict_literal unpacks a dict into keyword arguments at the call site.
#      This is the exact inverse of **kwargs — instead of collecting named args
#      into a dict, you're SPREADING a dict into named args.
#      INPUT:  show(name, age, role) — three required keyword args
#      OUTPUT: "Alice 32 admin" — the three values printed
def show(name, age, role):
    print(f"{name} {age} {role}")


# The ** before the dict spreads it — each key becomes a keyword argument
show(**{"name": users[0]["name"], "age": users[0]["age"], "role": users[0]["role"]})


# F20. WHY: {**item, **updates} is a non-mutating merge — creates a NEW dict
#      each time. This is the correct pattern from F12 (which had the mutation bug).
#      INPUT:  collection = list of dicts, **updates = fields to add/override on EVERY item
#      OUTPUT: new list where every dict has the update applied
#              batch_update(users, isActive=False) → all users with isActive=False
#              Original users list is NOT changed.
def batch_update(collection, **updates):
    new_collection = []
    for item in collection:
        new_item = {**item, **updates}  # spread both — updates wins on conflicts
        new_collection.append(new_item)
    return new_collection


print(batch_update(users, isActive=False))


# F21. WHY: *keys collects the grouping field names as a tuple.
#      When grouping by one key, the key is a plain value (e.g. "admin").
#      When grouping by multiple keys, the key is a tuple (e.g. ("admin", True)).
#      setdefault(key, []) creates an empty list if the key doesn't exist yet.
#      INPUT:  collection = list of dicts
#              *keys = one or more field name strings to group by
#      OUTPUT: prints group key + count for each group
#              group_by(users, "role") → Key: admin Count:2, Key: user Count:4 ...
#              group_by(users, "role", "isActive") → Key: ('admin', True) Count:2 ...
get_keys = lambda x, args: tuple(x[k] for k in args)


def group_by(collection, *keys):
    group = {}
    for item in collection:
        if len(keys) == 1:
            group_key = item[keys[0]]  # single key → plain value
        else:
            group_key = get_keys(item, keys)  # multiple keys → tuple
        group.setdefault(group_key, []).append(item)
    for key, items in group.items():
        print(f"Key: {key} Count:{len(items)}")


group_by(users, "role", "isActive")
group_by(orders, "status")


# F22. WHY: Returns a FUNCTION — not a value. The inner function closes over
#      `funcs` and applies them in sequence when called. This is a pipeline factory.
#      INPUT:  *funcs = any number of single-arg functions in order
#      OUTPUT: a new function that takes one value and passes it through all funcs
#              pipeline_args(lambda x: x*2, lambda x: x+10, lambda x: x**2)(3)
#              → step1: 3*2=6, step2: 6+10=16, step3: 16**2=256
def pipeline_args(*funcs):
    def inner(x):
        current_value = x
        for func in funcs:
            current_value = func(current_value)
        return current_value

    return inner


result = pipeline_args(lambda x: x * 2, lambda x: x + 10, lambda x: x**2)
print(result(1))


# F23. WHY: Manual partial application — "bake in" some arguments now,
#      supply the rest later. Like functools.partial but built by hand.
#      This is incomplete — inner() ignores new_args and returns nothing useful.
#      FIX: inner should accept *new_args and call func(*partial_args, *new_args)
#      INPUT:  func = any callable, *partial_args = args to pre-fill
#      OUTPUT: a new function that accepts remaining args and calls func with all of them
def partial_apply(func, *partial_args):
    def inner(*new_args):
        print(func(*partial_args, *new_args))

    return inner


add = lambda x, y: x + y
add5 = partial_apply(add, 5)
add5(2)


# F24. WHY: Returns a validator function that runs ALL rules against one value.
#      If any rule fails, the whole check fails. Like Promise.all() but for booleans.
#      INPUT:  *validators = single-arg lambdas that each return True/False
#      OUTPUT: a function that takes one value and returns True only if ALL pass
#              check = validate(lambda x: x > 0, lambda x: x < 100, lambda x: x % 2 == 0)
#              check(4)   → True   (4 > 0, 4 < 100, 4 % 2 == 0 — all pass)
#              check(101) → False  (101 > 100 — fails second rule)
def validate(*validators):
    def inner(value):
        print(all(func(value) for func in validators))

    return inner


check = validate(lambda x: x > 0, lambda x: x < 100, lambda x: x % 2 == 0)
check(2)
check(4)
check(101)


# F25. WHY: A dispatcher routes a key to its handler function — like a switch
#      statement but using a dict of lambdas. Common in event systems and CLIs.
#      INPUT:  **handlers = named lambdas (handler name → function)
#      OUTPUT: a function that takes (key, value) and calls handlers[key](value)
#              process("double", 5) → calls (lambda x: x*2)(5) → 10
#              process("upper", "hi") → calls str.upper("hi") → "HI"
def process_functions(**handlers):
    def inner(key, value):
        return handlers[key](value)

    return inner


process = process_functions(double=lambda x: x * 2, upper=lambda x: x.upper())
print(process("double", 5))
print(process("upper", "hi"))
# =============================================================================
# SECTION G — SCOPE & CLOSURES (G1–G25)
# WHY THIS SECTION: Closures are functions that remember the environment they
# were created in. This is exactly how React hooks work internally — useState
# is a closure over a value slot. `global` lets a function modify module-level
# state. `nonlocal` lets an inner function modify its enclosing function's state.
# The pattern: outer function creates state → inner function closes over it →
# outer returns inner → caller holds a function with private persistent state.
# =============================================================================

# G1. WHY: Without `global`, Python treats any assignment inside a function as
#     a LOCAL variable. `global x` tells Python "this x is the module-level one".
#     DEFINE:  counter = 0   (module level)
#              def increment():   (no args, no return — just mutates counter)
#     CALL:    increment() five times, then print(counter)
#     OUTPUT:  5
counter = 0


def increment():
    global counter
    counter += 1
    print(counter)


increment()
increment()
increment()
increment()
increment()

# G2. WHY: Same pattern applied to summing — shows global works for accumulation.
#     DEFINE:  total = 0   (module level)
#              def add_to_total(n):   n = any integer, no return — mutates total
#     CALL:    for n in numbers: add_to_total(n)   then print(total)
#     OUTPUT:  sum of all numbers in the list
total = 0


def add_to_total(n):
    global total
    total += n


for n in numbers:
    add_to_total(n)
print(total)

# G3. WHY: Shows EXACTLY what happens when you forget global.
#     Python sees `score -= 10` and thinks score is local — but it was never
#     assigned locally, so reading it before writing raises UnboundLocalError.
#     DEFINE:  score = 100   (module level)
#              def lose_points_broken():   no args, tries score -= 10 WITHOUT global
#              def lose_points_fixed():    no args, uses global score, does score -= 10
#     CALL:    wrap lose_points_broken() in try/except UnboundLocalError
#              print "UnboundLocalError caught — forgot global keyword"
#              then call lose_points_fixed() and print(score)
#     OUTPUT:  error message, then 90
score = 100


def lose_points_broken():
    try:
        score -= 10
    except UnboundLocalError:
        print("UnboundLocalError caught — forgot global keyword")


def lose_points_fixed():
    global score
    score -= 10
    print(score)


lose_points_broken()
lose_points_fixed()

# G4. WHY: Two separate global variables, two separate functions modifying them.
#     Shows that global is per-variable — you declare each one you want to modify.
#     DEFINE:  login_count = 0  /  logout_count = 0   (module level)
#              def login():    no args, no return — increments login_count
#              def logout():   no args, no return — increments logout_count
#     CALL:    login() x3, logout() x1, print both counts
#     OUTPUT:  login_count=3  logout_count=1
login_count = 0
logout_count = 0


def login():
    global login_count
    login_count += 1


def logout():
    global logout_count
    logout_count += 1


login()
login()
login()
logout()
print(login_count, logout_count)

# G5. WHY: Global dict as a simple cache — shows global works for mutable
#     objects too (dicts, lists). You still need `global` to reassign the name,
#     but dict[key]=value works WITHOUT global (mutation vs rebind).
#     DEFINE:  cache = {}   (module level)
#              def remember(key, value):   key=any string, value=any value, no return
#                  stores cache[key] = value  (no global needed — just mutation)
#     CALL:    remember("user", "Alice") / remember("role", "admin") / remember("id", 1)
#              then print(cache)
#     OUTPUT:  {"user": "Alice", "role": "admin", "id": 1}
cache = {}


def remember(key, value):
    cache[key] = value


remember("user", "Alice")
remember("role", "admin")
remember("id", 1)
print(cache)


# G6. Define make_counter()
#     outer var: count
#     inner fn:  increment — uses nonlocal, returns count
#     returns:   increment (the function, not the result)
#     NEW SYNTAX: nonlocal count
#     OUTPUT:    c() → 1, c() → 2, c() → 3
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        print(count)

    return increment


c = make_counter()
c()
c()
c()

# G7. Reuse make_counter() from G6.
#     vars: counter_a, counter_b
#     Call each a few times and show they don't share state.
#     OUTPUT:    counter_a() → 1, 2, 3 / counter_b() → 1, 2 (independent)
counter_a = make_counter()
counter_b = make_counter()
counter_a()
counter_a()
counter_a()
counter_b()
counter_b()


# G8. Define make_counter_from(start)
#     Same as G6 but count starts at `start` instead of 0.
#     vars: count, increment
#     OUTPUT:    make_counter_from(10)() → 11, 12, 13
def make_counter_from(start):
    count = start

    def increment():
        nonlocal count
        count += 1
        print(count)

    return increment


c10 = make_counter_from(10)
c10()
c10()
c10()


# G9. Define make_adder(n)
#     Returns a function that adds n to its input.
#     vars: add5, add10
#     OUTPUT:    add5(3) → 8 / add10(3) → 13
def make_adder(n):
    return lambda x: x + n


add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3))
print(add10(3))


# G10. Define make_multiplier(n)
#      Returns a function that multiplies its input by n.
#      vars: double, triple, quadruple
#      OUTPUT:    double(4) → 8 / triple(4) → 12 / quadruple(4) → 16
def make_multiplier(n):
    return lambda x: x * n


double = make_multiplier(2)
triple = make_multiplier(3)
quadruple = make_multiplier(4)
print(double(4))
print(triple(4))
print(quadruple(4))


# G11. Define make_power(exp)
#      Returns a function that raises its input to exp.
#      vars: square, cube
#      OUTPUT:    square(4) → 16 / cube(4) → 64
def make_power(exp):
    return lambda x: x**exp


square = make_power(2)
cube = make_power(3)
print(square(4))
print(cube(4))


# G12. Define make_between(lo, hi)
#      Returns a function that checks if a number is between lo and hi.
#      vars: is_teen, is_adult
#      OUTPUT:    is_teen(15) → True / is_teen(25) → False
def make_between(lo, hi):
    return lambda x: lo < x < hi


is_teen = make_between(13, 18)
is_adult = make_between(19, 40)
print(is_teen(15))
print(is_teen(25))
print(is_adult(18))
print(is_adult(39))


# G13. Define make_accumulator(initial=0)
#      outer var: total
#      inner fn:  add(n) — uses nonlocal, returns total
#      returns:   add
#      Test by feeding all order totals one by one.
#      OUTPUT:    acc(240) → 240 / acc(125) → 365 / acc(60) → 425...
def make_accumulator(initial=0):
    total = initial

    def add(n):
        nonlocal total
        total += n
        print(total)

    return add


acc = make_accumulator(0)
acc(240)
acc(125)
acc(60)


# G14. Define make_history()
#      outer var: history (list)
#      inner fn:  record(value) — appends, returns history
#      returns:   record
#      NOTE: no nonlocal needed — appending mutates the list, not reassigns it.
#      OUTPUT:    log('Alice') → ['Alice'] / log('Bob') → ['Alice', 'Bob']
def make_history():
    history = []

    def record(value):
        history.append(value)
        print(history)

    return record


log = make_history()
log("Alice")
log("Bob")


# G15.
#   fn:        make_once(func)
#   vars:      called (bool), result (any)
#   inner fn:  wrapper()
#   behavior:  make a function that runs func only on the first call,
#              then returns the same cached result every time after
#   call:      expensive = make_once(lambda: print("running...") or 42)
#              print(expensive())
#              print(expensive())
#              print(expensive())
#   output:    running...
#              42
#              42
#              42
def make_once(func):
    called = False
    result = 0

    def wrapper():
        nonlocal called, result
        if not called:
            result = func()
            called = True
        return result

    return wrapper


expensive = make_once(lambda: print("running...") or 42)
print(expensive())
print(expensive())
print(expensive())


# G16.
#   fn:       make_logger(prefix)
#   vars:     error, info
#   inner fn: log(message)
#   behavior: make a function that prints a prefixed message
#   call:     error = make_logger("ERROR")
#             info  = make_logger("INFO")
#             error("File not found")
#             info("Server started")
#   output:   ERROR: File not found
#             INFO: Server started
def make_logger(prefix):
    def log(message):
        print(f"{prefix}: {message}")

    return log


error = make_logger("ERROR")
info = make_logger("INFO")
error("File not found")
info("Server started")


# G17.
#   fn:       make_validator(min_val, max_val)
#   vars:     price_ok, age_ok
#   inner fn: validate(n)
#   behavior: make a function that checks if a number is within the given range
#   call:     price_ok = make_validator(0, 200)
#             age_ok   = make_validator(18, 60)
#             print(price_ok(120))
#             print(age_ok(22))
#             print(age_ok(10))
#   output:   True
#             True
#             False
def make_validator(min_val, max_val):
    def validate(n):
        print(min_val < n < max_val)

    return validate


price_ok = make_validator(0, 200)
age_ok = make_validator(18, 60)
price_ok(120)
age_ok(22)
age_ok(10)


# G18.
#   fn:        make_formatter(template)
#   vars:      fmt
#   inner fn:  fmt(data)
#   new syn:   template.format(**data)  unpacks dict keys as named args into placeholders
#   behavior:  make a function that fills a template string using a dict
#   call:      fmt = make_formatter("{name} earns ${salary}")
#              for u in users: print(fmt(u))
#   output:    Alice earns $72000
#              Bob earns $38000
#              ...
def make_formatter(template):
    def fmt(data):
        return template.format(**data)

    return fmt


fmt = make_formatter("{name} earns ${salary}")
for u in users:
    print(fmt(u))


# G19.
#   fn:       make_tax_calculator(rate)
#   vars:     tax_20, tax_30, tax_40
#   inner fn: calculate(salary)
#   behavior: make a function that calculates the tax amount from a salary
#             returns salary * rate  (the tax owed, not the take-home pay)
#   call:     tax_20 = make_tax_calculator(0.2)
#             for u in users: print(f"{u['name']}: {tax_20(u['salary'])}")
#   output:   Alice: 14400.0
#             Bob: 7600.0
#             ...
def make_tax_calculator(rate):
    def calculate(salary):
        return salary * rate

    return calculate


tax_20 = make_tax_calculator(0.2)
for u in users:
    print(f"{u['name']}: {tax_20(u['salary']):.2f}")

# G20.
#   vars:     fns (list), i (int loop var)
#   behavior: create 3 lambdas in a loop and store them in fns
#             write your prediction as a comment before running
#   call:     fns = []
#             for i in range(3):
#                 fns.append(lambda: i)
#             print(fns[0]())
#             print(fns[1]())
#             print(fns[2]())
#   output:   2
#             2
#             2
fns = []
for i in range(3):
    fns.append(lambda: i)

print(fns[0]())
print(fns[1]())
print(fns[2]())

# G21.
#   vars:    fns (list), i (int loop var)
#   new syn: lambda x=i: x
#   behavior: same as G20 but fix it so each lambda captures its own value of i
#   call:    fns = []
#            for i in range(3):
#                fns.append(lambda x=i: x)
#            print(fns[0]())
#            print(fns[1]())
#            print(fns[2]())
#   output:  0
#            1
#            2
fns = []
for i in range(3):
    fns.append(lambda x=i: x)
print(fns[0]())
print(fns[1]())
print(fns[2]())


# G22.
#   fn:       make_multiplier_list(factors)
#   vars:     result (list), f (loop var), multipliers
#   behavior: make a list of multiplier functions, one per factor
#             apply the G21 fix so each lambda captures its own f value
#   call:     multipliers = make_multiplier_list([2, 3, 5])
#             print(multipliers[0](10))
#             print(multipliers[1](10))
#             print(multipliers[2](10))
#   output:   20
#             30
#             50
def make_multiplier_list(factors):
    result = []
    for f in factors:
        result.append(lambda x, f=f: x * f)
    return result


multipliers = make_multiplier_list([2, 3, 5])
print(multipliers[0](10))
print(multipliers[1](10))
print(multipliers[2](10))


# G23.
#   fn:       make_pipeline(*funcs)
#   vars:     x (loop var reassigned each step), pipe, pipeline
#   inner fn: pipe(x)
#   behavior: make a function that passes a value through each func in sequence
#   call:     pipeline = make_pipeline(lambda x: x*2, lambda x: x+10, lambda x: x**2)
#             print(pipeline(3))
#   output:   256  (3*2=6 → 6+10=16 → 16**2=256)
def make_pipeline(*funcs):
    def pipe(x):
        current_x = x
        for f in funcs:
            current_x = f(current_x)
        print(current_x)

    return pipe


pipeline = make_pipeline(lambda x: x * 2, lambda x: x + 10, lambda x: x**2)
pipeline(3)


# G24.
#   fn:       make_retry(func, max_attempts=3)
#   vars:     flaky, safe
#   inner fn: wrapper()
#   behavior: make a function that calls func and retries if it raises an exception
#             returns "All attempts failed" if all attempts fail
#   call:     import random
#             def flaky():
#                 if random.random() < 0.7: raise ValueError("failed")
#                 return "success"
#             safe = make_retry(flaky, max_attempts=5)
#             print(safe())
#   output:   success   (or "All attempts failed" if unlucky)


def make_retry(func, max_attempts=3):
    def wrapper():
        attempts = 0
        while attempts < max_attempts:
            try:
                return func()
            except ValueError:
                attempts += 1

        return "All attempts failed"

    return wrapper


def flaky():
    if random.random() < 0.9:
        raise ValueError("failed")
    return "success"


safe = make_retry(flaky, max_attempts=5)
print(safe())


# G25.
#   fn:        make_bank_account(initial_balance=0)
#   vars:      balance (shared), account
#   inner fns: deposit(n), withdraw(n), get_balance()
#   behavior:  make a dict of 3 functions sharing one balance variable
#              deposit  — adds n, returns new balance
#              withdraw — subtracts n only if balance stays >= 0, returns balance
#              balance  — returns current balance, no change
#   call:      account = make_bank_account(100)
#              print(account["deposit"](50))
#              print(account["withdraw"](30))
#              print(account["withdraw"](200))
#              print(account["balance"]())
#   output:    150
#              120
#              120
#              120
def make_bank_account(initial_balance=0):
    balance = initial_balance

    def deposit(n):
        nonlocal balance
        balance += n
        return balance

    def withdraw(n):
        nonlocal balance

        if (balance - n) < 0:
            return "Insufficient balance"
        else:
            balance -= n
            return balance

    def get_balance():
        nonlocal balance
        return balance

    return {"deposit": deposit, "withdraw": withdraw, "balance": get_balance}


account = make_bank_account(100)
print(account["deposit"](50))
print(account["withdraw"](30))
print(account["withdraw"](200))
print(account["balance"]())
# =============================================================================
# SECTION H — HIGHER-ORDER FUNCTIONS & PIPELINES (H1–H24)
# WHY THIS SECTION: Higher-order functions (HOFs) take functions as arguments
# or return functions. map/filter/sorted are HOFs you already used in Section E.
# This section rebuilds them from scratch (so you understand them) then composes
# them into pipelines. This is the foundation of React's data-flow patterns,
# Redux middleware, and any ETL pipeline in backend Python.
# =============================================================================

# H1. map() to extract all user names from users.
#     OUTPUT:  ['Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace', 'Hank']
print(list(map(lambda x: x["name"], users)))

# H2. map() to format every product price as "$120.00".
#     OUTPUT:  ['$120.00', '$85.00', '$25.00', ...]
print(list(map(lambda x: f"{x['price']:.2f}", products)))

# H3. map() to build "Alice (admin) — $72000" for every user.
#     OUTPUT:  ['Alice (admin) — $72000', 'Bob (user) — $38000', ...]
print(list(map(lambda x: f"{x['name']} ({x['role']}) - ${x['salary']}", users)))

# H4. filter() to get active users. Print their names.
#     OUTPUT:  Alice / Carol / David / Frank / Grace
print(list(map(lambda x: x["name"], filter(lambda x: x["isActive"], users))))

# H5. filter() to get orders with total > 150. Print id + total.
#     OUTPUT:  Order #1 — $240 / Order #4 — $255 / ...
print(
    list(
        map(
            lambda x: f"Order #{x['id']} - ${x['total']}",
            filter(lambda x: x["total"] > 150, orders),
        )
    )
)

# H6. Chain filter() and map() in one expression.
#     filter active users → map to display strings. No temp variable.
#     OUTPUT:  ['Alice (admin) — $72000', 'Carol (moderator) — $51000', ...]
print(
    list(
        map(
            lambda x: f"{x['name']} ({x['role']}) - ${x['salary']}",
            filter(lambda x: x["isActive"], users),
        )
    )
)

# H7. sorted() + slice [:3] to get the top 3 earners. Print names.
#     vars: top3
#     OUTPUT:  David / Alice / Grace
print(list(map(lambda x: x["name"], sorted(users, key=lambda x: -x["salary"])[:3])))


# H8.
#   fn:       my_map(func, collection)
#   vars:     result (list), item (loop var)
#   behavior: apply func to every item and return a new list
#   call:     print(my_map(func that returns p["name"], products))
#   output:   ['Iron Sword', 'Steel Shield', 'Health Potion', ...]
def my_map(func, collection):
    return list(func(item) for item in collection)


print(my_map(lambda p: p["name"], products))


# H9.
#   fn:       my_filter(predicate, collection)
#   vars:     result (list), item (loop var), in_stock
#   behavior: keep only items where predicate returns True
#   call:     in_stock = my_filter(func that returns p["inStock"], products)
#             print([p["name"] for p in in_stock])
#   output:   ['Iron Sword', 'Steel Shield', 'Health Potion', ...]
def my_filter(predicate, collection):
    return list(item for item in collection if predicate(item))


in_stock = my_filter(lambda p: p["inStock"], products)
print(my_map(lambda p: p["name"], in_stock))


# H10.
#   fn:       my_reduce(func, collection, initial)
#   vars:     result (starts as initial, updated each step), item (loop var)
#   behavior: fold a list into one value by running func(result, item) each step
#   call:     print(my_reduce(func that adds o["total"] to acc, orders, 0))
#   output:   1085
def my_reduce(func, collection, initial):
    result = initial
    for item in collection:
        result = func(result, item)
    return result


print(my_reduce(lambda acc, o: acc + o["total"], orders, 0))

# H11.
#   vars:     winner (dict)
#   behavior: use my_reduce to find the user with the highest salary
#             initial = users[0]
#   call:     winner = my_reduce(func that returns whichever user has higher salary, users, users[0])
#             print(winner["name"])
#   output:   David
winner = my_reduce(
    lambda best, u: u if u["salary"] > best["salary"] else best, users, users[0]
)
print(winner["name"])


# H12.
#   fn:       apply_to_all(collection, *funcs)
#   behavior: apply every func to every item, returns a list of lists
#   call:     print(apply_to_all(users, func that gets name, func that gets salary))
#   output:   [['Alice', 72000], ['Bob', 38000], ...]
def apply_to_all(collection, *funcs):
    return [[func(item) for func in funcs] for item in collection]


print(apply_to_all(users, lambda u: u["name"], lambda u: u["salary"]))


# H13.
#   fn:       compose(f, g)
#   vars:     get_salary_str, get_upper_name
#   behavior: make a function where g runs first on input, then f runs on g's result
#             fn(x) = f(g(x))
#   call:     get_salary_str = compose(func that formats as "$n", func that gets salary)
#             get_upper_name = compose(func that uppercases, func that gets name)
#             print(get_salary_str(users[0]))
#             print(get_upper_name(users[0]))
#   output:   $72000
#             ALICE
def compose(f, g):
    def wrapper(x):
        return f(g(x))

    return wrapper


get_salary_str = compose(lambda x: f"${x}", lambda u: u["salary"])
get_upper_name = compose(str.upper, lambda u: u["name"])
print(get_salary_str(users[0]))
print(get_upper_name(users[0]))


# H14.
#   fn:       compose_all(*funcs)
#   vars:     get_after_tax
#   behavior: make a function that chains N functions — output of each feeds into next
#   call:     get_after_tax = compose_all(
#                 func that gets salary,
#                 func that multiplies by 0.8,
#                 func that formats as "$n"
#             )
#             for u in users: print(f"{u['name']}: {get_after_tax(u)}")
#   output:   Alice: $57600
#             Bob: $30400
#             ...
def compose_all(*funcs):
    def wrapper(x):
        for func in funcs:
            x = func(x)
        return x

    return wrapper


get_after_tax = compose_all(
    lambda u: u["salary"], lambda s: s * 0.8, lambda s: f"${round(s)}"
)
for u in users:
    print(f"{u['name']}: {get_after_tax(u)}")


# H15.
#   fn:       pipe(value, *funcs)
#   vars:     result
#   behavior: pass a value through each func in order and return the final result
#             like compose_all but you pass data in directly instead of getting a fn back
#   call:     result = pipe(users[0]["salary"], func * 0.8, func round, func format "$n")
#             print(result)
#   output:   $57600
def pipe(value, *funcs):
    for func in funcs:
        value = func(value)
    return value


result = pipe(
    users[0]["salary"], lambda x: x * 0.8, lambda x: round(x), lambda x: f"${x}"
)
print(result)


# H16.
#   fn:       group_by(collection, key_func)
#   vars:     result (dict), key (loop var), groups
#   new syn:  result.setdefault(key, [])  creates empty list for key if not there yet
#   behavior: group items into lists by the value returned from key_func
#   call:     groups = group_by(users, func that gets role)
#             for role, members in groups.items(): print(f"{role}: {len(members)}")
#   output:   admin: 2
#             user: 4
#             moderator: 2
def group_by(collection, key_func):
    result = {}
    for item in collection:
        result.setdefault(key_func(item), []).append(item)
    return result


groups = group_by(users, lambda x: x["role"])
print(list(f"{k}: {len(v)}" for k, v in groups.items()))


# H17.
#   fn:       flat_map(collection, func)
#   vars:     result (list), all_grades
#   new syn:  result.extend(other_list)  adds each element (not the list itself)
#   behavior: apply func to each item (func returns a list), flatten all into one list
#   call:     all_grades = flat_map(students, func that gets grades list)
#             print(all_grades)
#   output:   [88, 92, 79, 95, 84, 72, 68, 75, ...]
def flat_map(collection, func):
    return list(g for item in collection for g in func(item))


all_grades = flat_map(students, lambda x: x["grades"])
print(all_grades)


# H18.
#   fn:       zip_with(func, list_a, list_b)
#   new syn:  for a, b in zip(list_a, list_b)
#   behavior: pair up items from two lists and apply a two-arg func to each pair
#   call:     print(zip_with(func that builds "name — $total" string, users, orders))
#   output:   ['Alice — $240', 'Bob — $125', ...]
def zip_with(func, la, lb):
    return list(func(a, b) for a, b in zip(la, lb))


result = zip_with(lambda a, b: f"{a['name']} - ${b['total']}", users, orders)
print(result)


# H19.
#   fn:       partition(collection, predicate)
#   vars:     yes (list), no (list), active, inactive
#   behavior: split a list into two in one pass — matching and not matching
#             returns a tuple (yes, no)
#   call:     active, inactive = partition(users, func that checks isActive)
#             print([u["name"] for u in active])
#             print([u["name"] for u in inactive])
#   output:   ['Alice', 'Carol', 'David', 'Frank', 'Grace']
#             ['Bob', 'Eve', 'Hank']
def partition(collection, predicate):
    yes = []
    no = []
    for item in collection:
        if predicate(item):
            yes.append(item)
        else:
            no.append(item)
    return yes, no


active, inactive = partition(users, lambda x: x["isActive"])
print(list(u["name"] for u in active))
print(list(u["name"] for u in inactive))


# H20.
#   fn:       find_first(collection, predicate)
#   behavior: return the first item where predicate is True, or None if nothing matches
#   call:     print(find_first(users, func that checks role == "admin"))
#             print(find_first(products, func that checks price > 150))
#   output:   {'id': 1, 'name': 'Alice', ...}
#             {'id': 4, 'name': 'Dragon Bow', ...}
def find_first(collection, predicate):
    for item in collection:
        if predicate(item):
            return item


print(find_first(users, lambda x: x["role"] == "admin"))
print(find_first(products, lambda x: x["price"] > 150))


# H21.
#   fn:       count_by(collection, key_func)
#   vars:     result (dict), key (loop var)
#   new syn:  result.get(key, 0)  returns 0 if key not in dict yet
#   behavior: count how many items fall into each group
#   call:     print(count_by(users, func that gets role))
#             print(count_by(orders, func that gets status))
#   output:   {'admin': 2, 'user': 4, 'moderator': 2}
#             {'completed': 5, 'pending': 3, 'shipped': 2}
def count_by(collection, key_func):
    result = {}
    for item in collection:
        key = key_func(item)
        result[key] = result.get(key, 0) + 1
    return result


print(count_by(users, lambda x: x["role"]))
print(count_by(orders, lambda x: x["status"]))


# H22.
#   fn:       sort_by(collection, *key_funcs, reverse=False)
#   vars:     result
#   new syn:  key=lambda x: tuple(f(x) for f in key_funcs)
#   behavior: sort by multiple keys in priority order
#             first key sorts first, second key breaks ties
#   call:     result = sort_by(users, func that gets role, func that gets salary, reverse=True)
#             for u in result: print(f"{u['name']} | {u['role']} | ${u['salary']}")
#   output:   David | admin | $95000
#             Alice | admin | $72000
#             ...
def sort_by(collection, *key_funcs, reverse=False):
    return list(
        sorted(
            collection,
            key=lambda x: tuple(func(x) for func in key_funcs),
            reverse=reverse,
        )
    )


result = sort_by(users, lambda x: x["salary"], lambda x: x["role"], reverse=True)
for u in result:
    print(f"{u['name']:^5} | {u['role']:^10} | ${u['salary']}")


# H23.
#   fn:        memoize(func)
#   vars:      cache (dict), wrapper, call_count, get_user_orders, cached
#   inner fn:  wrapper(arg)
#   behavior:  make a function that caches results — same input never reruns func
#   call:      call_count = 0
#              def get_user_orders(user_id):
#                  increment call_count
#                  return orders where o["userId"] == user_id
#              cached = memoize(get_user_orders)
#              cached(1); print(call_count)
#              cached(1); print(call_count)
#              cached(2); print(call_count)
#   output:    1
#              1
#              2
def memoize(func):
    cache = {}

    def wrapper(x):
        if x in cache:
            return cache[x]
        else:
            answer = func(x)
            cache[x] = answer
            return answer

    return wrapper


call_count = 0


def get_user_orders(user_id):
    global call_count
    call_count += 1
    return [o for o in orders if o["userId"] == user_id]


cached = memoize(get_user_orders)

cached(1)
print(f"Call count after first request for User 1: {call_count}")

cached(2)
print(f"Call count after first request for User 2: {call_count}")

cached(1)
print(f"Call count after second request for User 1: {call_count}")


# H24.
#   fn:       retry(func, times=3, fallback=None)
#   vars:     attempt (int), flaky, safe
#   inner fn: wrapper()
#   behavior: make a function that retries func on exception up to times attempts
#             returns fallback if all attempts fail
#   call:     attempt = 0
#             def flaky():
#                 increment attempt
#                 raise on first 2 calls, return "success" on 3rd
#             safe = retry(flaky, times=5, fallback="gave up")
#             print(safe())
#   output:   success
def retry(func, times=3, fallback=None):
    def wrapper():
        for attempt in range(times):
            try:
                return func()
            except Exception:
                pass
        return fallback

    return wrapper


attempt = 0


def flaky():
    global attempt
    attempt += 1
    if attempt <= 2:
        raise Exception("Failed!")
    return "success"


safe = retry(flaky, times=5, fallback="gave up")
print(safe())


# =============================================================================
# BOSS DRILL — FULL DATA PIPELINE
# =============================================================================

# BOSS. WHY: This ties together every concept from this drill.
#       You will use: map() to enrich, filter() to select, a custom group_by()
#       to aggregate, sorted() to rank, and map() again to format output.
#       No imperative for loops in the final pipeline — every step is a function.
#
#       STEPS:
#         enrich   — map() on orders, add user_name + product_name
#         filtered — filter() completed only
#         grouped  — group_by() on user_name
#         summaries — collapse each group: order_count, total_spent, products list
#         sorted   — sorted() by total_spent descending
#         output   — map() to format, then print
#
#       Each step = one named var. Chain them. Print the result.
