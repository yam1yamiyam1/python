import os
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
# =============================================================================

# E1. Create a lambda `square` that returns x squared.
#     Call it with 5. Print the result.
square = lambda x: x**2
print(square(5))

# E2. Create a lambda `cube` that returns x cubed.
#     Call it with 3. Print the result.
cube = lambda x: x**3
print(cube(3))

# E3. Create a lambda `negate` that returns the negative of x.
#     Call it with 7 and -4. Print both.
negate = lambda x: -x
print(negate(7))
print(negate(-4))

# E4. Create a lambda `add` that takes two args and returns their sum.
#     Call it with (10, 20). Print.
add = lambda x, y: x + y
print(add(10, 20))

# E5. Create a lambda `percent` that takes a value and total,
#     returns (value / total) * 100.
#     Call it with (25, 200). Print.
percent = lambda x, y: x / y * 100
print(percent(25, 200))
# E6. Create a, lambda `clamp` that takes x, lo, hi and returns:
#     lo if x < lo, hi if x > hi, else x.
#     Use nested ternary: val if cond else (other_val if cond2 else fallback)
#     Call it with (5, 0, 10), (-3, 0, 10), (15, 0, 10). Print all.
clamp = lambda x, lo, hi: lo if x < hi else (hi if x > hi else x)
print(clamp(5, 0, 10))
print(clamp(-3, 0, 10))
print(clamp(15, 0, 10))
# E7. Store a lambda in a list:
#     ops = [lambda x: x+1, lambda x: x*2, lambda x: x**2]
#     Apply each op to the number 4. Print the results.
ops = [lambda x: x + 1, lambda x: x * 2, lambda x: x**2]
for op in ops:
    print(op(4))
# E8. Create a lambda `get_name` that takes a dict and returns its "name" key.
#     Call it on users[0]. Print.
get_name = lambda x: x["name"]
print(get_name(users[0]))

# E9. Create a lambda `get_salary` that takes a user dict and returns salary.
#     Call it on every user. Print each salary.
get_salary = lambda x: x["salary"]
for u in users:
    print(get_salary(u))

# E10. Use sorted() + lambda to sort users by age ascending.
#      Print just the names in sorted order.
#      Syntax: sorted(users, key=lambda u: u["age"])
for u in sorted(users, key=lambda u: u["age"]):
    print(u["name"])

# E11. Use sorted() + lambda to sort users by salary DESCENDING.
#      Print names + salaries.
for u in sorted(users, key=lambda u: u["salary"], reverse=True):
    print(f"{u['name']} - {u['salary']}")

# E12. Use sorted() + lambda to sort products by price ascending.
#      Print names + prices.
for p in sorted(products, key=lambda p: p["price"]):
    print(f"{p['name']} - {p['price']}")

# E13. Use sorted() + lambda to sort orders by total descending.
#      Print order ids + totals.
for o in sorted(orders, key=lambda o: o["total"], reverse=True):
    print(f"Order #{o['id']} - ${o['total']}")

# E14. Use sorted() + lambda to sort students by attendance descending.
#      Print names + attendance.
for s in sorted(students, key=lambda s: s["attendance"], reverse=True):
    print(f"{s['name']} - {s['attendance']}")

# E15. Use sorted() + lambda to sort users by NAME alphabetically.
#      Print the sorted names.
for u in sorted(users, key=lambda u: u["name"]):
    print(u["name"])

# E16. Use sorted() + lambda to sort products by category, then by price within category.
#      Hint: key=lambda p: (p["category"], p["price"])  ← tuple key sorts by first, then second
#      Print name + category + price for each.
for p in sorted(products, key=lambda p: (p["category"], p["price"])):
    print(f"{p['name']} {p['category']} - ${p['price']}")

# E17. Use a lambda with the built-in filter() to get active users.
#      Syntax: list(filter(lambda u: u["isActive"], users))
#      Print the names of results.
print(list(filter(lambda u: u["isActive"], users)))

# E18. Use filter() + lambda to get products with price < 100.
#      Print names + prices.
for p in list(filter(lambda p: p["price"] < 100, products)):
    print(f"{p['name']} - ${p['price']}")

# E19. Use filter() + lambda to get orders with status "completed".
#      Print order ids.
print(
    [
        f"Order #{o['id']}"
        for o in list(filter(lambda o: o["status"] == "completed", orders))
    ]
)

# E20. Use filter() + lambda to get students with attendance above 85.
#      Print names.
print([s["name"] for s in list(filter(lambda s: s["attendance"] > 85, students))])

# E21. Use the built-in map() + lambda to extract all user names.
#      Syntax: list(map(lambda u: u["name"], users))
#      Print the result.
print(list(map(lambda u: u["name"], users)))

# E22. Use map() + lambda to create a list of strings: "Alice — $72000".
#      One entry per user. Print the list.
print(list(map(lambda u: f"{u['name']} - ${u['salary']}", users)))

# E23. Use map() + lambda to double every number in `numbers`.
#      Print the result.
print(list(map(lambda n: n * 2, numbers)))

# E24. Chain filter() and map() together in one expression:
#      Get names of users who are active AND salary > 50000.
#      Syntax: list(map(lambda u: u["name"], filter(lambda u: ..., users)))
#      Print result.
print(
    list(
        map(
            lambda u: u["name"],
            filter(lambda u: u["isActive"] and u["salary"] > 50000, users),
        )
    )
)

# E25. Create a lambda `salary_bracket` that returns "High"/"Mid"/"Low"
#      using nested ternary based on salary > 70000 / > 45000 / else.
#      Apply it to every user with map(). Print name + bracket for each.
salary_bracket = lambda u: (
    "High" if u["salary"] > 70000 else ("Mid" if u["salary"] > 45000 else "Low")
)
print(list(map(lambda u: f"{u['name']} - {salary_bracket(u)}", users)))
# =============================================================================
# SECTION F — *ARGS AND **KWARGS (F1–F25)
# =============================================================================


# F1. Define `add_all(*args)` that returns the sum of all arguments.
#     Call it with (1, 2, 3), then (10, 20, 30, 40). Print both.
def add_all(*args):
    return sum(args)


print(add_all(1, 2, 3))
print(add_all(10, 20, 30, 40))


# F2. Define `multiply_all(*args)` that returns the product of all arguments.
#     Call it with (2, 3, 4). Print.
def multiply_all(*args):
    return reduce(lambda x, y: x * y, args)


print(multiply_all(2, 3, 4))


# F3. Define `first_and_last(*args)` that prints the first and last argument.
#     Call it with 5 different values. Print.
def first_and_last(*args):
    return [args[0], args[-1]]


print(first_and_last(1, 9, 8, 744, 52))


# F4. Define `count_args(*args)` that returns how many arguments were passed.
#     Call it three times with different counts. Print each.
def count_args(*args):
    print(len(args))


count_args(1, 5, 4, 7, 8, 5)
count_args(1, 5, 4, 7, 8, 5, 5, 8, 7, 4)
count_args(1, 5, 4, 7, 8, 5, 5, 5, 2, 2, 4, 4, 7, 5, 5, 6)


# F5. Define `print_types(*args)` that prints the type of each argument.
#     Call it with a mix: (1, "hello", 3.14, True, None). Print.
def print_types(*args):
    print([type(a) for a in args])


print_types(1, "hello", 3.14, True, None)


# F6. Define `stats(*args)` that returns a dict:
#     {"count": n, "sum": s, "min": m, "max": m, "avg": a}
#     Use only built-ins (len, sum, min, max). Print the result.
#     Call it with numbers unpacked: stats(*numbers)
#     Syntax to unpack a list into args: fn(*my_list)
def stats(*args):
    result = {
        "count": len(args),
        "sum": sum(args),
        "min": min(args),
        "max": max(args),
        "avg": sum(args) / len(args),
    }
    print(result)


stats(*numbers)
print(*numbers)


# F7. Define `greet_all(*names)` that prints "Hello, {name}!" for each name.
#     Call it with 4 names. Print.
def greet_all(*names):
    for name in names:
        print(f"Hello, {name}!")


greet_all("Yuan", "Ann", "Gojo", "Sukuna")


# F8. Define `build_sentence(*words)` that joins all words with a space.
#     Call it with 5 words. Print.
def build_sentence(*words):
    print(" ".join(words))


build_sentence("Fuck", "you", "bitch", "ass", "nigga")


# F9. Define `tag(element, **attributes)` that returns an HTML-like string.
#     tag("a", href="https://example.com", class_="link")
#     → '<a href="https://example.com" class_="link">'
#     Hint: loop through kwargs.items() to build the attribute string.
#     Print the result.
def tag(element, **attr):
    string = [element]
    for k, v in attr.items():
        string.append(f'{k}="{v}"')
    print(f"<{' '.join(string)}>")


tag("a", href="https://example.com", class_="link")


# F10. Define `create_user(**kwargs)` that returns a dict from kwargs.
#      Call it: create_user(name="Alice", age=32, role="admin")
#      Print the result.
def create_user(**kwargs):
    user = {}
    for k, v in kwargs.items():
        user[k] = v
    print(user)


create_user(name="Alice", age=32, role="admin")


# F11. Define `log(**fields)` that prints each key=value on its own line.
#      Call it: log(event="login", user="Alice", ip="192.168.1.1")
#      Print.
def log(**fields):
    for k, v in fields.items():
        print(f"{k}={v}")


log(event="login", user="Alice", ip="192.168.1.1")


# F12. Define `update_user(user, **updates)` that returns a NEW dict with
#      the original user fields plus any overrides from updates.
#      Syntax: {**user, **updates}
#      Call it on users[0] with salary=99999, role="superadmin". Print.
def update_user(user, **updates):
    user_to_update = user
    for k, v in updates.items():
        user_to_update[k] = v
    print(user_to_update)


update_user(users[0], salary=99999, role="superadmin")


# F13. Define `merge(*dicts)` that merges all dict arguments into one.
#      Later dicts override earlier ones on key conflicts.
#      Hint: result = {}; for d in dicts: result.update(d)
#      Call it with 3 dicts. Print result.
def merge(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    print(result)


print(users[1])
print(products[1])
print(students[1])


# F14. Define `flexible(a, b, *args, **kwargs)`.
#      Print: a, b, the extra positional args tuple, and the kwargs dict.
#      Call it: flexible(1, 2, 3, 4, 5, x="hello", y=True)
#      Note: required positional args come BEFORE *args.
def flexible(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


flexible(1, 2, 3, 4, 5, x="hello", y=True)


# F15. Define `only_kwargs(**kwargs)` that filters kwargs to only keep
#      values that are strings. Return the filtered dict.
#      Call it: only_kwargs(name="Alice", age=32, role="admin", score=99)
#      Print.
def only_kwargs(**kwargs):
    print([f"{k}={v}" for k, v in kwargs.items() if isinstance(v, str)])


only_kwargs(name="Alice", age=32, role="admin", score=99)


# F16. Define `apply_discount(price, *discount_rates)`.
#      Apply each discount rate in sequence (multiply by 1 - rate).
#      Example: apply_discount(100, 0.1, 0.2) → 100 * 0.9 * 0.8 = 72.0
#      Call it on products[0]["price"] with two rates. Print.
def apply_discount(price, *discount_rates):
    print({reduce(lambda final, d: final * (1 - d), discount_rates, price)})


apply_discount(100, 0.1, 0.2)


# F17. Define `zip_to_dict(*args)`.
#      Takes an even number of args: alternating keys and values.
#      zip_to_dict("name", "Alice", "age", 32) → {"name": "Alice", "age": 32}
#      Hint: zip(args[::2], args[1::2])
#      Print result.
def zip_to_dict(*args):
    result = dict(zip(args[::2], args[1::2]))
    print(result)


zip_to_dict("name", "Alice", "age", 32)


# F18. Define `require_fields(data: dict, *required)`.
#      Checks that all keys in `required` exist in `data`.
#      Returns True if all present, False if any missing.
#      Call it on users[0] with ("name", "salary", "nickname"). Print.
def require_fields(data: dict, *required):
    for r in required:
        if r not in data:
            return False
    return True


print(require_fields(users[0], "name", "salary", "nickname"))


# F19. Call a function using **dict unpacking.
#      Define `show(name, age, role)` that prints the three values.
#      Then call it by unpacking users[0]:
#        show(**{"name": users[0]["name"], "age": users[0]["age"], "role": users[0]["role"]})
#      Print.
def show(name, age, role):
    print(f"{name} {age} {role}")


show(**{"name": users[0]["name"], "age": users[0]["age"], "role": users[0]["role"]})


# F20. Define `batch_update(collection, **updates)`.
#      Returns a NEW list where every item dict is merged with updates.
#      Call it: batch_update(users, isActive=False)  ← deactivate all users
#      Print names + isActive from the result.
#      Note: do NOT mutate the original — use {**item, **updates} per item.
def batch_update(collection, **updates):
    new_collection = []
    for item in collection:
        new_item = {**item, **updates}
        new_collection.append(new_item)
    return new_collection


print(batch_update(users, isActive=False))


# F21. Define `group_by(collection, *keys)`.
#      Groups items by a composite key built from the given keys.
#      group_by(users, "role") → {"admin": [...], "user": [...], ...}
#      group_by(orders, "status") → {"completed": [...], "pending": [...], ...}
#      Call both. Print the group keys and counts.
def group_by(collection, *keys):
    group = {}
    filter_keys = list(set(k for k in keys))
    for k in filter_keys:
        collection_keys = []
        for item in collection:
            collection_keys = list(set([*collection_keys, item[k]]))
        for l in collection_keys:
            group[l] = list(item["name"] for item in collection if item[k] == l)
    print(group)


group_by(users, "role")
group_by(users, "role", "role", "role", "role")


# F22. Define `pipeline_args(*funcs)` that returns a function.
#      The returned function takes a value and passes it through each func.
#      result = pipeline_args(lambda x: x*2, lambda x: x+10, lambda x: x**2)
#      print(result(3))  → ((3*2)+10)**2 = 256
#      Print.


# F23. Define `partial_apply(func, *partial_args)` that returns a new function.
#      The new function takes more args and calls func with partial_args + new args.
#      This is a manual partial application (like functools.partial).
#      Example:
#        add = lambda x, y: x + y
#        add5 = partial_apply(add, 5)
#        print(add5(3))  → 8
#      Call it with a few examples. Print.


# F24. Define `validate(*validators)` that returns a function.
#      The returned function takes a value and returns True only if ALL validators pass.
#      validators are single-arg lambdas returning bool.
#      Example:
#        check = validate(lambda x: x > 0, lambda x: x < 100, lambda x: x % 2 == 0)
#        print(check(4))   → True
#        print(check(101)) → False
#      Test it. Print.


# F25. Define `dispatch(**handlers)` that returns a function.
#      The returned function takes a key and a value, calls handlers[key](value).
#      Example:
#        process = dispatch(
#            double=lambda x: x * 2,
#            upper=lambda x: x.upper(),
#            negate=lambda x: -x,
#        )
#        print(process("double", 5))   → 10
#        print(process("upper", "hi")) → "HI"
#        print(process("negate", 3))   → -3
#      Print all three.


# =============================================================================
# SECTION G — SCOPE & CLOSURES (G1–G25)
# =============================================================================

# G1. Create a module-level variable `counter = 0`.
#     Define `increment()` that adds 1 to counter using `global`.
#     Call it 5 times. Print counter.


# G2. Create `total = 0`.
#     Define `add_to_total(n)` that adds n to total using `global`.
#     Call it with each number in `numbers`. Print total.


# G3. Show the bug — WITHOUT global:
#     Create `score = 100`.
#     Define `lose_points()` that tries to do score -= 10 WITHOUT global.
#     Wrap the call in try/except UnboundLocalError.
#     Print "UnboundLocalError caught — forgot global keyword".
#     Then define the fixed version and show it works.


# G4. Create `login_count = 0` and `logout_count = 0`.
#     Define `login()` and `logout()` that each modify their respective globals.
#     Call login 3 times and logout 1 time. Print both counts.


# G5. Create `cache = {}`.
#     Define `remember(key, value)` that stores key→value in cache using global.
#     Call it 3 times with different keys. Print cache.


# G6. Define `make_counter()` that:
#     - creates local `count = 0`
#     - defines inner `increment()` using nonlocal
#     - increment adds 1 and returns count
#     - make_counter returns increment
#     Call it. Print increment() three times.
#     This is a closure — inner function "closes over" the outer variable.


# G7. Make TWO independent counters from G6.
#     Show they do NOT share state:
#       a = make_counter()
#       b = make_counter()
#       a() a() a()  → 1 2 3
#       b() b()      → 1 2   (not 4 5)
#     Print all calls.


# G8. Define `make_counter_from(start)` — same as G6 but count starts at `start`.
#     Create counters starting at 0, 10, and 100. Print a few calls each.


# G9. Define `make_adder(n)` that returns a lambda adding n to its argument.
#     add5 = make_adder(5)
#     add10 = make_adder(10)
#     print(add5(3))   → 8
#     print(add10(3))  → 13
#     Print.


# G10. Define `make_multiplier(n)` that returns a lambda multiplying by n.
#      Create double, triple, quadruple. Apply each to numbers[0]. Print.


# G11. Define `make_power(exp)` that returns a function raising its arg to exp.
#      square = make_power(2), cube = make_power(3)
#      Apply to 4. Print.


# G12. Define `make_between(lo, hi)` that returns a lambda checking lo <= x <= hi.
#      is_teen = make_between(13, 19)
#      is_adult = make_between(18, 65)
#      Test on several ages. Print.


# G13. Define `make_accumulator(initial=0)`.
#      Returns a function that takes a number, adds to running total, returns total.
#      Use nonlocal. Feed it all order totals one by one. Print running total each step.


# G14. Define `make_history()`.
#      Returns a function that:
#        - takes a value
#        - appends it to an internal list
#        - returns the full list so far
#      Use nonlocal. Record all user names one by one. Print after each.


# G15. Define `make_once(func)`.
#      Returns a version of func that runs ONLY on the first call.
#      Subsequent calls return the first result without re-running.
#      Use nonlocal with a `called` flag and `result` variable.
#      Example:
#        expensive = make_once(lambda: print("running...") or 42)
#        print(expensive())  → "running..." then 42
#        print(expensive())  → 42 (no "running..." this time)


# G16. Define `make_logger(prefix)`.
#      Returns a function that prints f"{prefix}: {message}".
#      error = make_logger("ERROR")
#      info  = make_logger("INFO")
#      error("File not found")
#      info("Server started")
#      Print.


# G17. Define `make_validator(min_val, max_val)`.
#      Returns a function that checks if a number is in range.
#      Use it to validate product prices and user ages.
#      Print name + valid/invalid for each.


# G18. Define `make_formatter(template)`.
#      Returns a function that formats a dict using the template string.
#      Syntax: template.format(**data)
#      Example:
#        fmt = make_formatter("{name} earns ${salary}")
#        print(fmt(users[0]))   → "Alice earns $72000"
#      Apply to all users. Print.


# G19. Define `make_tax_calculator(rate)`.
#      Returns a function that takes a salary and returns the tax amount.
#      Create calculators for 20%, 30%, 40%.
#      Apply 20% to all user salaries. Print name + tax.


# G20. Closure scope quiz — predict output BEFORE running:
#
#      fns = []
#      for i in range(3):
#          fns.append(lambda: i)
#
#      print(fns[0]())   # what prints here?
#      print(fns[1]())   # and here?
#      print(fns[2]())   # and here?
#
#      Write your prediction as a comment.
#      Then run it. Were you right?
#      Hint: all three lambdas share the SAME `i` from the loop scope.


# G21. Fix the bug from G20 using a default argument to capture the value:
#      fns = []
#      for i in range(3):
#          fns.append(lambda x=i: x)   ← default arg captures current i
#      Print all three. They should now be 0, 1, 2.


# G22. Define `make_multiplier_list(factors)`.
#      Takes a list of numbers. Returns a list of multiplier functions.
#      Use the G21 fix to avoid the closure loop bug.
#      factors = [2, 3, 5]
#      multipliers = make_multiplier_list(factors)
#      Apply each multiplier to 10. Print results: 20, 30, 50.


# G23. Define `make_pipeline(*funcs)`.
#      Returns a function that passes a value through all funcs in sequence.
#      Use nonlocal if needed, or just loop.
#      pipe = make_pipeline(lambda x: x*2, lambda x: x+10, lambda x: x**2)
#      print(pipe(3))  → ((3*2)+10)**2 = 256


# G24. Define `make_retry(func, max_attempts=3)`.
#      Returns a version of func that retries up to max_attempts times if it raises.
#      Use nonlocal to track attempt count.
#      Test with a function that randomly fails:
#        import random
#        def flaky():
#            if random.random() < 0.7: raise ValueError("failed")
#            return "success"
#      Print result or "All attempts failed".


# G25. SCOPE BOSS — Define `make_bank_account(initial_balance=0)`.
#      Returns a dict of functions: {"deposit": fn, "withdraw": fn, "balance": fn}
#      All three share the same `balance` variable via nonlocal.
#      deposit(n)  → adds n, returns new balance
#      withdraw(n) → subtracts n (prevent going below 0), returns new balance
#      balance()   → returns current balance
#      Test:
#        account = make_bank_account(100)
#        account["deposit"](50)    → 150
#        account["withdraw"](30)   → 120
#        account["withdraw"](200)  → 120 (blocked)
#        account["balance"]()      → 120
#      Print each operation.


# =============================================================================
# SECTION H — HIGHER-ORDER FUNCTIONS & PIPELINES (H1–H24)
# =============================================================================

# H1. Use the built-in map() to extract all user names.
#     list(map(lambda u: u["name"], users))
#     Print.


# H2. Use map() to convert all product prices to "$X.XX" strings.
#     Print.


# H3. Use map() to add a "display" field to each user:
#     "Alice (admin) — $72000"
#     Print the list of display strings.


# H4. Use the built-in filter() to get active users.
#     Print names.


# H5. Use filter() to get orders with total > 150.
#     Print order ids + totals.


# H6. Chain map() and filter():
#     Get display strings (from H3) for ONLY active users.
#     One expression. Print.


# H7. Use the built-in sorted() with a lambda key to sort users
#     by salary descending. Print top 3 names.


# H8. Define `my_map(func, collection)` — reimplements map() using a for loop.
#     Use it to extract product names. Print.
#     (Rebuilding built-ins by hand = understanding them.)


# H9. Define `my_filter(predicate, collection)` — reimplements filter().
#     Use it to get in-stock products. Print names.


# H10. Define `my_reduce(func, collection, initial)` — reimplements reduce().
#      Use it to sum all order totals. Print.
#      Syntax: result = initial; for item in collection: result = func(result, item)


# H11. Use my_reduce from H10 to find the user with the highest salary.
#      func = lambda best, u: u if u["salary"] > best["salary"] else best
#      Print the winner's name.


# H12. Define `apply_to_all(collection, *funcs)`.
#      Applies each func to each item and returns a list of lists.
#      Example: apply_to_all(users, lambda u: u["name"], lambda u: u["salary"])
#      → [["Alice", 72000], ["Bob", 38000], ...]
#      Print.


# H13. Define `compose(f, g)` → returns lambda x: f(g(x)).
#      Build these composed functions and test each:
#        get_salary_str = compose(lambda x: f"${x}", lambda u: u["salary"])
#        get_upper_name = compose(str.upper, lambda u: u["name"])
#      Apply to users[0]. Print.


# H14. Define `compose_all(*funcs)` that chains N functions left-to-right.
#      compose_all(f, g, h)(x) = h(g(f(x)))
#      Build a pipeline: get salary → apply tax → format as currency.
#      Apply to each user. Print.


# H15. Define `pipe(value, *funcs)` — applies funcs to value in sequence.
#      This is the non-closure version: pass data through functions directly.
#      pipe(users[0]["salary"], lambda x: x*0.8, lambda x: round(x), lambda x: f"${x}")
#      Print.


# H16. Define `group_by(collection, key_func)`.
#      Returns a dict grouping items by the result of key_func.
#      group_by(users, lambda u: u["role"])
#      → {"admin": [...], "user": [...], "moderator": [...]}
#      Print keys + counts.


# H17. Define `flat_map(collection, func)`.
#      func returns a list per item. flat_map flattens all into one list.
#      flat_map(students, lambda s: s["grades"])
#      → all grades from all students in one flat list
#      Print the flat list.


# H18. Define `zip_with(func, list_a, list_b)`.
#      Applies func(a, b) to paired elements. Returns result list.
#      zip_with(lambda u, o: f"{u['name']} — ${o['total']}", users, orders)
#      Print.


# H19. Define `partition(collection, predicate)`.
#      Returns (matching, not_matching) as a tuple of two lists.
#      Use it to split users into active/inactive.
#      Use it to split products into in-stock/out-of-stock.
#      Print both pairs.


# H20. Define `find_first(collection, predicate)`.
#      Returns the first item where predicate is True, or None.
#      find_first(users, lambda u: u["role"] == "admin")
#      find_first(products, lambda p: p["price"] > 150)
#      Print both.


# H21. Define `count_by(collection, key_func)`.
#      Returns a dict of counts grouped by key_func result.
#      count_by(users, lambda u: u["role"])  → {"admin": 2, "user": 4, ...}
#      count_by(orders, lambda o: o["status"]) → {"completed": 5, ...}
#      Print both.


# H22. Define `sort_by(collection, *key_funcs, reverse=False)`.
#      Sorts by multiple keys in order (primary, secondary, ...).
#      sort_by(users, lambda u: u["role"], lambda u: u["salary"], reverse=True)
#      Hint: key=lambda x: tuple(f(x) for f in key_funcs)
#      Print names + roles + salaries.


# H23. Define `memoize(func)`.
#      Returns a cached version of func — same input returns stored result.
#      Use a closure with a dict cache.
#      Test with a slow-ish function (simulate with a counter showing it ran):
#        call_count = 0
#        def get_user_orders(user_id):
#            nonlocal call_count
#            call_count += 1
#            return [o for o in orders if o["userId"] == user_id]
#        cached = memoize(get_user_orders)
#        cached(1)  → runs
#        cached(1)  → from cache (call_count stays same)
#        cached(2)  → runs
#      Print call_count after each call to show caching works.


# H24. Define `retry(func, times=3, fallback=None)`.
#      Calls func. If it raises, retries up to `times` times.
#      If all fail, returns fallback.
#      Test with a function that raises ValueError on the first 2 calls.
#      Use a closure counter to track attempts.
#      Print the final result.


# =============================================================================
# BOSS DRILL — FULL DATA PIPELINE
# =============================================================================

# BOSS. Build a complete data pipeline using ONLY the functional tools
#       from this drill. No imperative loops allowed in the final output —
#       use map(), filter(), sorted(), your custom compose/pipe/group_by etc.
#
#       The pipeline must:
#
#       STEP 1 — Enrich orders:
#         Each order gets two new fields added:
#           - "user_name": the name of the user who placed it
#           - "product_name": the name of the product ordered
#
#       STEP 2 — Filter:
#         Keep only orders where status == "completed"
#
#       STEP 3 — Group:
#         Group the filtered orders by user_name
#
#       STEP 4 — Summarize:
#         For each user group, produce:
#           {
#             "user": "Alice",
#             "order_count": 2,
#             "total_spent": 300,
#             "products": ["Iron Sword", "Leather Armor"]
#           }
#
#       STEP 5 — Sort:
#         Sort summaries by total_spent descending
#
#       STEP 6 — Format & Print:
#         Print each summary as:
#         "Alice | 2 orders | $300.00 | Iron Sword, Leather Armor"
#
#       Each step should be a named function or lambda.
#       Compose them cleanly. Print the final output.
