import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import orders, products, users

# =============================================================================
# DRILL 03 — FUNCTIONS & SCOPE
# Drills 101–200
# =============================================================================
# HOW TO RUN:  python drill-03-functions.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              No skipping — do them in order.
# =============================================================================

# =============================================================================
# CHEAT SHEET — JS vs PYTHON FUNCTIONS
# =============================================================================
#
# BASIC DEFINITION
# ──────────────────────────────────────────────────────────────
# JS:     const greet = (name) => `Hello ${name}`
# JS:     function greet(name) { return `Hello ${name}` }
# Python: def greet(name):
#             return f"Hello {name}"
#
# - No curly braces — indentation IS the block
# - `def` keyword, not `function` or `const`
# - `return` is optional — omitting it returns None
#
# DEFAULT ARGUMENTS
# ──────────────────────────────────────────────────────────────
# JS:     const greet = (name = "stranger") => ...
# Python: def greet(name="stranger"):
#
# ⚠️  MUTABLE DEFAULT WARNING — no JS equivalent, very common bug:
# NEVER:  def add_item(item, lst=[])    ← lst is shared across ALL calls!
# DO:     def add_item(item, lst=None)
#             if lst is None: lst = []
#
# KEYWORD ARGUMENTS
# ──────────────────────────────────────────────────────────────
# JS:     greet({ name: "Alice", age: 32 })   ← pass an object
# Python: greet(name="Alice", age=32)          ← named at the call site
#         greet(age=32, name="Alice")          ← order doesn't matter
#
# TYPE HINTS — Python's TypeScript-lite
# ──────────────────────────────────────────────────────────────
# TS:     function greet(name: string): string { ... }
# Python: def greet(name: str) -> str:
#
#   def add(a: int, b: int) -> int:
#   def get_user(id: int) -> dict:
#   def process(items: list) -> None:
#   def find(name: str, active: bool = True) -> dict | None:
#
# NOTE: Python does NOT enforce hints at runtime — hints only.
#       Use mypy for actual checking (like running tsc in TS).
#
# LAMBDA
# ──────────────────────────────────────────────────────────────
# JS:     const double = (x) => x * 2
# Python: double = lambda x: x * 2
#
# JS:     (x, y) => x + y
# Python: lambda x, y: x + y
#
# Ternary inside lambda:
# Python: lambda x: "yes" if x > 0 else "no"
#
# Limitations vs JS arrows:
# - ONE expression only — no multi-line body
# - No statements, no loops
# - Use def for anything complex
#
# *ARGS AND **KWARGS
# ──────────────────────────────────────────────────────────────
# JS:     const fn = (...args) => args        → array
# Python: def fn(*args):                      → tuple
#
# JS:     no equivalent
# Python: def fn(**kwargs):                   → dict of named args
#
# Combined:
# Python: def fn(*args, **kwargs):
#
# SCOPE — global and nonlocal
# ──────────────────────────────────────────────────────────────
# JS:     let x = 1; const fn = () => { x = 2 }   ← closure modifies outer
# Python: x = 1
#         def fn():
#             global x    ← must declare to modify module-level var
#             x = 2
#
# nonlocal — for nested functions (modifying enclosing scope, not global):
# Python: def outer():
#             count = 0
#             def inner():
#                 nonlocal count
#                 count += 1
#             inner()
#             return count
#
# =============================================================================


# =============================================================================
# SECTION A — BASIC def SYNTAX (101–110)
# Simple function definition, calling, returning values
# =============================================================================


# 101. Define a function `say_hello` that prints "Hello, World!". Call it.
#      Syntax: def name():
def say_hello():
    print("Hello, World!")


say_hello()


# 102. Define a function `greet(name)` that prints "Hello, Alice".
#      Call it with "Alice".
def greet(name):
    print(f"Hello, {name}")


greet("Alice")


# 103. Define a function `add(a, b)` that RETURNS a + b.
#      Call it and print the result.
#      Note: `return` sends a value back — without it, you get None.
def add(a, b):
    return a + b


print(add(1, 5))
# 104. Define a function `get_user_names()` that returns a list of all user names.
#      Call it and print the result.


def get_user_names():
    return [u["name"] for u in users]


print(get_user_names())


# 105. Define a function `get_active_users()` that returns only active users.
#      Call it and print the result.
def get_active_users():
    return [u["name"] for u in users if u["isActive"]]


print(get_active_users())


# 106. Define a function `count_orders(status)` that returns the count of orders
#      matching the given status string.
#      Call it with "completed" and "pending". Print both results.
def count_orders(status):
    count = 0
    for o in orders:
        if o["status"] == status:
            count += 1
    return count


print(count_orders("completed"))
print(count_orders("pending"))


# 107. Define a function `get_total_revenue()` that returns the sum of all order totals.
#      Call it and print the result.
def get_total_revenue():
    sum_total = 0
    for o in orders:
        sum_total += o["total"]
    return sum_total


print(get_total_revenue())


# 108. Define a function `is_expensive(product)` that returns True if price > 100.
#      Call it on each product and print the product name + result.
def is_expensive(product):
    return product["price"] > 100


for p in products:
    print(f"{p['name']} - {is_expensive(p)}")


# 109. Define a function `get_product_by_id(product_id)` that returns the product
#      dict matching the id, or None if not found.
#      Call it with id=1 and id=99. Print both results.
def get_product_by_id(product_id):
    for p in products:
        if p["id"] == product_id:
            return p


print(get_product_by_id(1))
print(get_product_by_id(99))


# 110. Define a function `summarize_user(user)` that returns a formatted string:
#      "Alice | admin | $72000 | active"
#      Call it on every user and print each result.
def summarize_user(user):
    status = ""
    if user["isActive"]:
        status = "active"
    else:
        status = "inactive"

    return f"{user['name']:^5} | {user['role']:^10} | {user['salary']} | {status}"


for u in users:
    print(summarize_user(u))
# =============================================================================
# SECTION B — DEFAULT ARGUMENTS (111–118)
# =============================================================================


# 111. Define `greet(name, greeting="Hello")`.
#      Call it with just a name. Then call it with a custom greeting.
#      Print both results.
def greet(name, greeting="Hello"):
    return f"{greeting} {name}"


print(greet("Yuan"))
print(greet("Yuan", "Sup Nigga"))


# 112. Define `get_users_by_role(role="user")` that returns users matching the role.
#      Call it with no arguments (defaults to "user").
#      Call it with role="admin". Print both results.
def get_users_by_role(role="user"):
    return [u["name"] for u in users if u["role"] == role]


print(get_users_by_role())
print(get_users_by_role("admin"))


# 113. Define `calculate_tax(salary, rate=0.2)` that returns salary * rate.
#      Call it with just a salary. Then call it with a custom rate.
#      Print both.
def calculate_tax(salary, rate=0.2):
    return salary * rate


print(calculate_tax(10000))
print(calculate_tax(10000, 0.3))
# 114. Define `format_price(price, currency="$", decimals=2)`.
#      Returns a string like "$120.00".
#      Call it three ways:
#        - just price
#        - price + currency="€"
#        - price + currency="€" + decimals=0
#      Print all three.


def format_price(price, currency="$", decimals=2):
    return f"{currency}{price:.{decimals}f}"


print(format_price(120))
print(format_price(120, "€"))
print(format_price(120, "€", 0))


# 115. ⚠️  MUTABLE DEFAULT BUG DRILL
#      Define this function EXACTLY as written and call it 3 times:
#
def add_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    print(tags)
    return tags


#
print(add_tag("python"))
print(add_tag("django"))
print(add_tag("flask"))
#
#      Observe the output — the list grows across calls. This is the bug.
#      Then fix it using None as the default.
#      Print the fixed version 3 times to confirm each call is independent.


# 116. Define `get_top_earner(users, min_salary=50000)` that returns the name
#      of the highest earner above min_salary.
#      Call it with default, then with min_salary=80000.
def get_top_earner(users, min_salary=50000):
    top_user = None
    users_above_min = [u for u in users if u["salary"] > min_salary]
    for u in users_above_min:
        if top_user is None or u["salary"] > top_user["salary"]:
            top_user = u
    return top_user["name"] if top_user else "No one found"


print(get_top_earner(users))
print(get_top_earner(users, 80000))
# 117. Define `repeat(text, times=1, separator=" ")` that returns text repeated
#      `times` times, joined by separator.
#      Example: repeat("Alice", 3, "-") → "Alice-Alice-Alice"
#      Call it several ways and print.


def repeat(text, times=1, separator=" "):
    return separator.join([text] * times)


print(repeat("Alice", 3, "-"))
print(repeat("Alice", 10))
print(repeat("Alice", 3, "$$"))


# 118. Define `build_report(include_users=True, include_products=True, include_orders=True)`.
#      Print section headers ("=== USERS ===" etc.) only for included sections.
#      Count and print totals for each included section.
#      Call it three ways: all True, only users, only orders.
def build_report(include_users=True, include_products=True, include_orders=True):
    if include_users:
        print(f"==== {len(users)} USERS ====")
    if include_products:
        print(f"==== {len(products)} PRODUCTS ====")
    if include_orders:
        print(f"==== {len(orders)} ORDERS ====")


build_report()
build_report(True, False, False)
build_report(False, False, True)


# =============================================================================
# SECTION C — KEYWORD ARGUMENTS (119–125)
# =============================================================================

# 119. Define `create_profile(name, age, role)`.
#      Call it using KEYWORD arguments in a different order than defined:
#        create_profile(role="admin", name="Alice", age=32)
#      Print the result.
#      Note: In JS you'd pass an object — in Python you name args at call site.


def create_profile(name, age, role):
    return {"name": name, "age": age, "role": role}


profile = create_profile(role="admin", name="Alice", age=32)
print(profile)


# 120. Define `filter_users(min_age=0, max_age=100, active_only=False)`.
#      Returns users matching all criteria.
#      Call it four ways using keyword args:
#        - filter_users(min_age=30)
#        - filter_users(active_only=True)
#        - filter_users(min_age=25, max_age=35)
#        - filter_users(min_age=25, active_only=True)
#      Print each result.
def filter_users(min_age=0, max_age=100, active_only=False):
    return [
        u["name"]
        for u in users
        if min_age <= u["age"] <= max_age and (not active_only or u["isActive"])
    ]


print(filter_users(min_age=30))
print(filter_users(active_only=True))
print(filter_users(min_age=25, max_age=35))
print(filter_users(min_age=25, active_only=True))

# 121. Define `format_order(order, show_status=True, show_total=True, currency="$")`.
#      Returns a string summarizing the order.
#      Call it with different combinations of keyword args.
def format_order(order, show_status=True, show_total=True, currency="$"):
    
    

# 122. Define `search_products(category=None, max_price=None, in_stock_only=False)`.
#      Returns products matching all provided filters (ignore None filters).
#      Call it several ways. Print results.


# 123. Define `rank_students(students, by="average", reverse=True)`.
#      `by` can be "average" or "attendance".
#      Returns students sorted by the given field.
#      Call it both ways. Print the names in ranked order.
#      Syntax: sorted(collection, key=lambda x: ..., reverse=True)


# 124. You have this call:
#        send_email(to="alice@example.com", subject="Hello", body="Hi there", cc=None)
#      Define the function `send_email` to match this call signature.
#      Print a formatted summary of what would be sent.


# 125. MIXING positional and keyword args:
#      Define `log(level, message, prefix="[LOG]")`.
#      Call it:
#        log("ERROR", "Something broke")
#        log("INFO", "All good", prefix="[SYS]")
#        log(level="WARN", message="Watch out")
#      Print all three.
#      Note: positional args must come before keyword args.


# =============================================================================
# SECTION D — TYPE HINTS (126–132)
# =============================================================================
# Type hints are Python's TypeScript-lite.
# They do NOT enforce at runtime — they are documentation + IDE support.
# Syntax: def fn(param: type) -> return_type:

# 126. Rewrite drill 103's `add` function WITH type hints.
#      def add(a: int, b: int) -> int:
#      Call it and print.


# 127. Write `get_user_by_id(user_id: int) -> dict | None` that returns
#      the matching user or None.
#      Call it with id=1 and id=999. Print both.
#      Note: dict | None means "either a dict or None" (Python 3.10+)


# 128. Write `get_names(collection: list) -> list` that returns a list
#      of "name" values from any collection of dicts.
#      Call it with users, then products. Print both.


# 129. Write `is_active_admin(user: dict) -> bool` that returns True
#      if user is both active and an admin.
#      Call it on every user. Print name + result.


# 130. Write `calculate_average(grades: list) -> float` that returns
#      the average of a list of numbers.
#      Call it on each student's grades. Print name + average.


# 131. Write `format_currency(amount: float, symbol: str = "$") -> str`.
#      Returns "$1,234.56" style string.
#      Call it on the total revenue. Print result.
#      Syntax: f"{amount:,.2f}"


# 132. Write `get_order_summary(order: dict, users: list, products: list) -> str`.
#      Returns: "Alice bought Iron Sword x2 for $240 (completed)"
#      Call it on every order. Print each.


# =============================================================================
# SECTION E — LAMBDA (133–141)
# =============================================================================
# lambda = throwaway single-expression function
# Use for short transforms, sorting keys, filtering — not complex logic

# 133. Create a lambda `double` that multiplies a number by 2.
#      Call it with numbers[0]. Print result.


# 134. Create a lambda `get_name` that takes a dict and returns its "name" key.
#      Call it on users[0]. Print result.


# 135. Create a lambda `is_over_100` that returns True if a price > 100.
#      Call it on each product's price. Print results.


# 136. Use a lambda as the `key` in sorted() to sort users by age.
#      Print the sorted names.
#      Syntax: sorted(collection, key=lambda x: x["field"])


# 137. Use a lambda to sort products by price DESCENDING.
#      Print sorted product names + prices.
#      Syntax: sorted(..., key=lambda x: x["price"], reverse=True)


# 138. Use a lambda with sorted() to sort students by their average grade.
#      You'll need sum()/len() inside the lambda.
#      Print sorted names + averages.


# 139. Use a lambda with sorted() to sort orders by total descending,
#      then print each order id and total.


# 140. Create a lambda `label` that takes a salary and returns
#      "High" / "Mid" / "Low" using a NESTED ternary.
#      Syntax: lambda x: "A" if x > 90 else ("B" if x > 80 else "C")
#      Call it on each user's salary. Print name + label.


# 141. Use sorted() with a lambda to sort users by salary descending,
#      then filter with a regular for loop to keep only active users.
#      Print name + salary for each.


# =============================================================================
# SECTION F — *ARGS AND **KWARGS (142–149)
# =============================================================================

# 142. Define `add_all(*args)` that returns the sum of all arguments.
#      Call it with 3 numbers, then with 6 numbers. Print both.
#      Note: *args is a TUPLE inside the function — iterate with for.


# 143. Define `print_all(*args)` that prints each argument on its own line
#      with its index.
#      Call it with 5 different values of mixed types.


# 144. Define `merge_dicts(**kwargs)` that returns a single dict from all
#      keyword arguments.
#      Call it: merge_dicts(name="Alice", age=32, role="admin")
#      Print the result.
#      Note: **kwargs is a DICT inside the function.


# 145. Define `log_event(event, **details)` that prints:
#      "EVENT: login | user=Alice | role=admin"
#      Call it: log_event("login", user="Alice", role="admin")


# 146. Define `build_user(*args, **kwargs)`.
#      args → positional values in order: (id, name)
#      kwargs → remaining fields: role="admin", salary=72000
#      Return a dict combining both.
#      Print the result.


# 147. Define `calculate(*args, operation="sum")`.
#      operation can be "sum", "product", "max", "min".
#      Perform the matching calculation on args. Return result.
#      Call it four ways. Print each.


# 148. Define `filter_collection(collection, **filters)`.
#      For each key-value in filters, keep only items where item[key] == value.
#      Example: filter_collection(users, role="admin", isActive=True)
#      Print the result.


# 149. Define `describe(*items, label="Item", separator=", ")`.
#      Returns a string: "Item: Iron Sword, Health Potion, War Axe"
#      Call it with product names + custom label + separator.


# =============================================================================
# SECTION G — SCOPE: global AND nonlocal (150–157)
# =============================================================================

# 150. Create a module-level variable `call_count = 0`.
#      Define a function `track_call()` that increments call_count using `global`.
#      Call track_call() 5 times. Print call_count.
#      Note: without `global`, Python treats it as a local variable → error.


# 151. Same as 150 but WRONG version first:
#      Define `track_call_broken()` WITHOUT the global keyword.
#      Wrap the call in try/except UnboundLocalError and print "Scope error caught".
#      Then show the fixed version.


# 152. Create `total_processed = 0`.
#      Define `process_order(order)` that adds the order total to total_processed.
#      Loop through all orders calling process_order on each.
#      Print total_processed at the end.


# 153. Define a function `make_counter()` that:
#      - Has a local variable `count = 0`
#      - Defines an inner function `increment()` using `nonlocal count`
#      - increment() adds 1 to count and returns it
#      - make_counter() returns the increment function
#      Call it:
#        counter = make_counter()
#        print(counter())   → 1
#        print(counter())   → 2
#        print(counter())   → 3
#      Note: this is a closure — like useState in React but manual.


# 154. Build TWO independent counters using make_counter() from drill 153.
#      Show that counter_a and counter_b don't share state.
#        counter_a = make_counter()
#        counter_b = make_counter()
#        counter_a() → 1
#        counter_a() → 2
#        counter_b() → 1   ← independent


# 155. Define `make_accumulator(start=0)` that returns an inner function.
#      The inner function takes a value, adds it to the running total, returns total.
#      Use nonlocal.
#      Test it by accumulating all order totals one by one.


# 156. Scope reading drill — predict the output BEFORE running:
#
#      x = "global"
#
#      def outer():
#          x = "outer"
#          def inner():
#              x = "inner"
#              print(x)
#          inner()
#          print(x)
#
#      outer()
#      print(x)
#
#      Write your prediction as a comment, then run it and compare.


# 157. Same as 156 but with nonlocal in inner():
#
#      x = "global"
#
#      def outer():
#          x = "outer"
#          def inner():
#              nonlocal x
#              x = "inner"
#              print(x)
#          inner()
#          print(x)
#
#      outer()
#      print(x)
#
#      Write your prediction as a comment, then run it and compare.


# =============================================================================
# SECTION H — FUNCTIONS AS VALUES (158–165)
# Higher-order functions — passing and returning functions
# Like callbacks and HOCs in React
# =============================================================================

# 158. Define `apply(func, value)` that calls func(value) and returns the result.
#      Pass a lambda that doubles a number.
#      Pass a lambda that uppercases a string.
#      Print both results.
#      Note: functions are first-class in Python — just like JS.


# 159. Define `apply_to_all(collection, func)` that returns a new list
#      with func applied to each item.
#      Use it to extract all user names.
#      Use it to double all numbers.
#      Print both.


# 160. Define `my_filter(collection, predicate)` that returns items
#      where predicate(item) is True.
#      Use it to get active users.
#      Use it to get products with price > 100.
#      Print both.
#      Note: this is reimplementing Python's built-in filter() from scratch.


# 161. Define `my_reduce(collection, func, initial)` that folds a collection
#      down to a single value.
#      Use it to sum all order totals.
#      Use it to find the max salary.
#      Print both.
#      Note: this is reimplementing Python's functools.reduce() from scratch.


# 162. Define `compose(f, g)` that returns a new function h where h(x) = f(g(x)).
#      JS: const compose = (f, g) => (x) => f(g(x))
#      Python: def compose(f, g): return lambda x: f(g(x))
#      Use it to compose:
#        - a function that adds 10
#        - a function that doubles
#      Test: compose(add10, double)(5) → (5*2)+10 = 20
#      Print result.


# 163. Define `get_stat(stat)` that RETURNS a function.
#      stat can be "min", "max", "sum", "avg".
#      The returned function takes a list and computes that stat.
#      get_salary = get_stat("avg")
#      print(get_salary([u["salary"] for u in users]))
#      Test all 4 stat types.


# 164. Define `make_validator(*rules)` where each rule is a function that
#      takes a user dict and returns True/False.
#      make_validator returns a function that returns True only if ALL rules pass.
#      Example:
#        is_valid = make_validator(
#            lambda u: u["age"] > 25,
#            lambda u: u["isActive"],
#            lambda u: u["salary"] > 40000,
#        )
#        for user in users: print(user["name"], is_valid(user))


# 165. BOSS DRILL — Pipeline
#      Build a `pipeline(data, *steps)` function where each step is a function
#      that takes the data and returns transformed data.
#      Run this pipeline on users:
#        step 1: filter to active only
#        step 2: sort by salary descending
#        step 3: extract name + salary as formatted strings
#        step 4: keep only top 3
#      Print the final result.
#      Hint: loop through steps applying each one in sequence.
