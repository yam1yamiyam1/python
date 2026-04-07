import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import numbers, orders, products, users

os.system("cls")

# =============================================================================
# DRILL 08 — TYPE HINTS
# =============================================================================
# HOW TO RUN:  python drill-08-type-hints.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              No skipping — do them in order.
# =============================================================================

# NEW SYNTAX REFERENCE
# --------------------
# Basic param hint      def fn(x: int) -> str:
# Optional (3.10+)      def fn(x: str | None = None):
# Optional (older)      from typing import Optional
#                       def fn(x: Optional[str] = None):
# Union                 from typing import Union
#                       def fn(x: str | int):        # 3.10+
#                       def fn(x: Union[str, int]):  # older
# List hint             def fn(items: list[int]) -> list[str]:
# Dict hint             def fn(data: dict[str, int]) -> dict:
# Tuple hint            def fn(pair: tuple[str, int]):
# Variable hint         name: str = "Alice"
#                       age: int
# Type alias            Vector = list[float]
# Callable              from typing import Callable
#                       def fn(callback: Callable[[int], str]):
# NOTE: Python does NOT enforce hints at runtime — they are for
#       tools, editors, and frameworks like FastAPI to read.


# =============================================================================
# SECTION A — BASIC FUNCTION ANNOTATIONS (1–15)
# =============================================================================


# 1. Write a function `double(n: int) -> int` that returns n * 2. Print double(5).
def double(n: int) -> int:
    return n * 2


print(double(5))


# 2. Write a function `greet(name: str) -> str` that returns "Hello, {name}!". Print it.
def greet(name: str):
    print(f"Hello, {name}")


greet("Yuan")


# 3. Write a function `is_adult(age: int) -> bool` that returns True if age >= 18. Print it with 17 and 20.
def is_adult(age: int) -> bool:
    return age >= 18


print(is_adult(17))
print(is_adult(20))


# 4. Write a function `to_price(amount: float) -> str` that returns f"${amount:.2f}". Print it.
def to_price(amount: float) -> str:
    return f"${amount:.2f}"


print(to_price(5))


# 5. Write a function `add(a: int, b: int) -> int`. Print add(10, 25).
def add(a: int, b: int) -> int:
    return a + b


print(add(10, 25))


# 6. Write a function `multiply(a: float, b: float) -> float`. Print multiply(2.5, 4.0).
def multiply(a: float, b: float) -> float:
    return a * b


print(multiply(2.5, 4))


# 7. Write a function `repeat(text: str, times: int) -> str` that returns text repeated times times.
#    Print repeat("ha", 3).  Expected: hahaha
def repeat(text: str, times: int) -> str:
    return text * times


print(repeat("ha", 3))


# 8. Write a function `first_char(s: str) -> str` that returns the first character of s.
#    Print first_char("Alice").
def first_char(s: str) -> str:
    return s[0]


print(first_char("Alice"))


# 9. Write a function `negate(flag: bool) -> bool` that returns the opposite. Print negate(True).
def negate(flag: bool) -> bool:
    return not flag


print(negate(True))


# 10. Write a function `clamp(value: int, min_val: int, max_val: int) -> int`
#     that returns value clamped between min_val and max_val.
#     Print clamp(150, 0, 100) → 100 and clamp(-5, 0, 100) → 0.
def clamp(value: int, min_val: int, max_val: int) -> int:
    return (
        value
        if min_val < value < max_val
        else (min_val if value < min_val else max_val)
    )


print(clamp(150, 0, 100))
print(clamp(-5, 0, 100))


# 11. Write a function `get_name(user: dict) -> str` that returns user["name"].
#     Print it for users[0].
def get_name(user: dict) -> str:
    return user["name"]


print(get_name(users[0]))


# 12. Write a function `get_salary(user: dict) -> int` that returns user["salary"].
#     Print it for every user using a loop.
def get_salary(user: dict) -> int:
    return user["salary"]


for u in users:
    print(get_salary(u))


# 13. Write a function `format_user(user: dict) -> str` that returns
#     "{name} ({role})" — e.g. "Alice (admin)". Print for all users.
def format_user(user: dict) -> str:
    return f"{user['name']} ({user['role']})"


for u in users:
    print(format_user(u))


# 14. Write a function `total_price(product: dict) -> float`
#     that returns price * quantity as a float. Print for all products.
def total_price(product: dict) -> float:
    return float(product["price"] * product["quantity"])


for p in products:
    print(total_price(p))


# 15. Write a function `order_summary(order: dict) -> str`
#     that returns "Order #{id}: {status} — ${total}". Print for all orders.
def order_summary(order: dict) -> str:
    print(f"Order #{order['id']}: {order['status']} — ${order['total']}")


for o in orders:
    order_summary(o)
# =============================================================================
# SECTION B — LIST AND DICT HINTS (16–30)
# =============================================================================


# 16. Write a function `sum_numbers(nums: list[int]) -> int` using sum().
#     Print sum_numbers(numbers).
def sum_numbers(nums: list[int]) -> int:
    return sum(nums)


print(sum_numbers(numbers))


# 17. Write a function `to_strings(nums: list[int]) -> list[str]`
#     that converts every int to str. Use a list comprehension. Print it.
def to_strings(nums: list[int]) -> list[str]:
    return [str(n) for n in nums]


print(to_strings(numbers))
# 18. Write a function `average(nums: list[int]) -> float`
#     that returns the average. Print average(numbers).

# 19. Write a function `get_names(users: list[dict]) -> list[str]`
#     that returns all user names. Print it.

# 20. Write a function `get_active(users: list[dict]) -> list[dict]`
#     that returns only active users (isActive == True). Print the names.

# 21. Write a function `prices(products: list[dict]) -> list[float]`
#     that returns all prices as floats. Print it.

# 22. Write a function `count_by_role(users: list[dict]) -> dict[str, int]`
#     that returns {"admin": 2, "user": 4, "moderator": 2} etc.
#     Hint: loop and use dict.get(key, 0) + 1.
#     Print the result.

# 23. Write a function `index_by_id(users: list[dict]) -> dict[int, dict]`
#     that returns {1: user_dict, 2: user_dict, ...}.
#     Print the name of the user with id 3 using the result.

# 24. Write a function `totals_by_status(orders: list[dict]) -> dict[str, int]`
#     that sums order totals grouped by status.
#     Expected keys: "completed", "pending", "shipped". Print it.

# 25. Write a function `product_map(products: list[dict]) -> dict[str, float]`
#     that returns {product_name: price}. Print it.

# 26. Write a function `max_salary(users: list[dict]) -> int`
#     that returns the highest salary. Use max() with a key. Print it.

# 27. Write a function `min_price(products: list[dict]) -> float`
#     that returns the lowest price as float. Print it.

# 28. Write a function `filter_by_role(users: list[dict], role: str) -> list[dict]`
#     that returns users matching that role. Print names for "admin" and "moderator".

# 29. Write a function `sort_by_salary(users: list[dict], reverse: bool = False) -> list[dict]`
#     that returns users sorted by salary. Print names sorted ascending then descending.

# 30. Write a function `pluck(items: list[dict], key: str) -> list`
#     that extracts any field from a list of dicts.
#     Print pluck(users, "name"), pluck(products, "price"), pluck(orders, "status").


# =============================================================================
# SECTION C — OPTIONAL AND UNION HINTS (31–45)
# =============================================================================

# NEW SYNTAX — read before starting this section:
# -----------------------------------------------
# Optional means a value can be its type OR None.
#
#   from typing import Optional
#   def find_user(id: int) -> Optional[dict]:
#       ...
#
# Python 3.10+ shorthand (same meaning):
#   def find_user(id: int) -> dict | None:
#       ...
#
# Union means a value can be one of several types:
#   from typing import Union
#   def parse(val: Union[str, int]) -> int:
#       ...
#   # 3.10+:
#   def parse(val: str | int) -> int:
#       ...


# 31. Write `find_user(users: list[dict], id: int) -> Optional[dict]`
#     that returns the user dict if found, else None.
#     Print find_user(users, 1) and find_user(users, 99).

# 32. Write `find_product(products: list[dict], name: str) -> dict | None`
#     that returns the product if found, else None. Use 3.10+ syntax.
#     Print find_product(products, "War Axe") and find_product(products, "Dagger").

# 33. Write `get_bio(user: dict) -> str | None`
#     Users don't have a "bio" field. Use dict.get("bio") which returns None if missing.
#     Print get_bio(users[0]).

# 34. Write `safe_divide(a: int, b: int) -> float | None`
#     that returns a / b, or None if b == 0. Print safe_divide(10, 2) and safe_divide(5, 0).

# 35. Write `parse_int(value: str | int) -> int`
#     that accepts either a string or an int and always returns an int.
#     If string → convert. If already int → return as-is.
#     Print parse_int("42") and parse_int(99).

# 36. Write `display(value: str | int | float | None) -> str`
#     that returns str(value) if value is not None, else "N/A".
#     Print display("hello"), display(42), display(3.14), display(None).

# 37. Write `first(items: list) -> Optional[int]`  (note: untyped list is fine here)
#     that returns the first item or None if the list is empty.
#     Print first([10, 20, 30]) and first([]).

# 38. Write `last(items: list) -> Optional[int]`
#     that returns the last item or None if empty.
#     Print last(numbers) and last([]).

# 39. Write `safe_get(data: dict, key: str) -> str | int | None`
#     that returns data[key] if it exists, else None.
#     Print safe_get(users[0], "name"), safe_get(users[0], "salary"), safe_get(users[0], "bio").

# 40. Write `find_order(orders: list[dict], user_id: int) -> list[dict]`
#     that returns all orders for a given user_id (may be empty list — not None).
#     Print find_order(orders, 1) and find_order(orders, 999).

# 41. Write `lookup_salary(users: list[dict], name: str) -> int | None`
#     that returns the salary for a user by name, or None if not found.
#     Print lookup_salary(users, "Carol") and lookup_salary(users, "Zara").

# 42. Write `coerce_to_int(val: str | float | int) -> int`
#     that converts any of those three types to int.
#     Print coerce_to_int("7"), coerce_to_int(3.9), coerce_to_int(5).

# 43. Write `nullable_upper(s: str | None) -> str | None`
#     that returns s.upper() if s is not None, else None.
#     Print nullable_upper("hello") and nullable_upper(None).

# 44. Write `merge(a: dict, b: dict) -> dict` that merges two dicts (b overrides a).
#     Use the | operator. Print merge({"x": 1}, {"x": 99, "y": 2}).

# 45. Write `wrap_in_list(item: str | int | dict) -> list`
#     that wraps any single item in a list and returns it.
#     Print wrap_in_list("hello"), wrap_in_list(42), wrap_in_list(users[0]).


# =============================================================================
# SECTION D — TYPE ALIASES AND CALLABLE HINTS (46–60)
# =============================================================================

# NEW SYNTAX — read before starting this section:
# -----------------------------------------------
# Type aliases let you name complex types for reuse:
#
#   UserDict = dict[str, str | int | bool]
#   UserList = list[UserDict]
#
#   def process(users: UserList) -> UserList:
#       ...
#
# Callable hints describe functions passed as arguments:
#
#   from typing import Callable
#
#   def apply(fn: Callable[[int], int], value: int) -> int:
#       return fn(value)
#                ↑
#   Callable[[arg_types], return_type]
#   Callable[[int, str], bool] = takes int + str, returns bool
#   Callable[[], None]         = takes nothing, returns nothing


# 46. Define a type alias `UserDict = dict` and `UserList = list`.
#     Write `get_admins(users: UserList) -> UserList`
#     that returns only admin users. Print their names.

# 47. Define `ProductDict = dict` and write `in_stock(products: list[ProductDict]) -> list[ProductDict]`
#     that returns only products where inStock is True. Print their names.

# 48. Write `apply(fn: Callable[[int], int], value: int) -> int`
#     that calls fn(value) and returns the result.
#     Test it with: apply(lambda x: x * 2, 5) and apply(lambda x: x ** 2, 4).
#     Print both results.

# 49. Write `apply_to_all(fn: Callable[[int], int], nums: list[int]) -> list[int]`
#     that applies fn to every item. Print apply_to_all(lambda x: x * 3, numbers).

# 50. Write `transform_users(users: list[dict], fn: Callable[[dict], str]) -> list[str]`
#     that applies fn to each user and collects results.
#     Print transform_users(users, lambda u: u["name"].upper()).
#     Print transform_users(users, lambda u: f"{u['name']} earns {u['salary']}").

# 51. Write `pipe(value: int, *fns: Callable[[int], int]) -> int`
#     that passes value through each function in order.
#     Print pipe(2, lambda x: x*2, lambda x: x+10, lambda x: x**2)
#     Expected: ((2*2)+10)**2 = 196

# 52. Write a type alias `Predicate = Callable[[dict], bool]`.
#     Write `filter_users(users: list[dict], pred: Predicate) -> list[dict]`
#     that filters users by pred.
#     Print names from filter_users(users, lambda u: u["salary"] > 50000).
#     Print names from filter_users(users, lambda u: u["age"] < 30).

# 53. Write `reduce_salaries(users: list[dict], fn: Callable[[int, int], int]) -> int`
#     that folds all salaries with fn.
#     Print reduce_salaries(users, lambda acc, s: acc + s)  → total salary.
#     Print reduce_salaries(users, lambda acc, s: max(acc, s))  → max salary.
#     Hint: start with fn(users[0]["salary"], users[1]["salary"]) then continue the fold.

# 54. Write `sort_users(users: list[dict], key: Callable[[dict], int], reverse: bool = False) -> list[dict]`
#     Print names sorted by age ascending, then by salary descending.

# 55. Write `make_formatter(prefix: str) -> Callable[[str], str]`
#     that returns a function which prepends prefix to any string.
#     Syntax: return lambda s: f"{prefix}{s}"
#     Use it: fmt = make_formatter(">>> ")
#     Print fmt("Hello") and apply it to all user names.

# 56. Write `make_validator(min_val: int, max_val: int) -> Callable[[int], bool]`
#     that returns a function checking if a number is in range.
#     validator = make_validator(0, 100)
#     Print validator(50), validator(150), validator(-1).

# 57. Write `make_adder(n: int) -> Callable[[int], int]`
#     that returns a function adding n to any value.
#     add10 = make_adder(10)
#     Print add10(5), add10(100), apply_to_all(add10, numbers).

# 58. Annotate this existing pattern with full type hints and make it work:
#     def build_pipeline(fns):
#         def run(value):
#             for fn in fns:
#                 value = fn(value)
#             return value
#         return run
#     pipeline = build_pipeline([lambda x: x*2, lambda x: x+1, lambda x: x**2])
#     Print pipeline(3)  → ((3*2)+1)**2 = 49

# 59. Write `safe_apply(fn: Callable[[int], int], value: int) -> int | None`
#     that calls fn(value) inside a try/except and returns None on any Exception.
#     Test with: safe_apply(lambda x: x * 2, 5)
#     and: safe_apply(lambda x: int("bad"), 5)
#     Print both.

# 60. Write `batch(users: list[dict], fn: Callable[[dict], dict]) -> list[dict]`
#     that applies fn to each user and returns the new list.
#     Use it to add a "display" key to each user: display = "{name} [{role}]"
#     Print the "display" field of each result.


# =============================================================================
# SECTION E — ANNOTATING CLASSES (61–75)
# =============================================================================

# NEW SYNTAX — read before starting this section:
# -----------------------------------------------
# You can annotate class attributes at the top of the class body.
# This is exactly how Pydantic BaseModel works — just with extra powers.
#
#   class User:
#       name: str
#       age: int
#       role: str = "user"      # default value
#       bio: str | None = None  # optional field
#
#       def __init__(self, name: str, age: int, role: str = "user") -> None:
#           self.name = name
#           self.age = age
#           self.role = role
#
# Return type of __init__ is always None.
# Methods that return nothing annotate -> None.
# @property return type goes on the def line: def display(self) -> str:

# 61. Rewrite your User class from drill-08 with FULL type hints:
#     - class-level attribute annotations
#     - __init__ with typed params and -> None
#     - greet() -> str  (make it return, not print)
#     - __str__ -> str
#     - is_senior() -> bool
#     - to_dict() -> dict[str, str | int]
#     - display_name @property -> str
#     Instantiate alice and bob. Print alice.greet() and alice.display_name.

# 62. Add a method `promote(self, new_role: str) -> None`
#     that updates self.role. Call alice.promote("superadmin"). Print alice.role.

# 63. Add a class method (not instance method) `from_dict(cls, data: dict) -> "User"`
#     that creates a User from a dict.
#     Syntax:
#       @classmethod
#       def from_dict(cls, data: dict) -> "User":
#           return cls(name=data["name"], age=data["age"], role=data["role"])
#     Create all users using User.from_dict(u) for u in users. Print each.

# 64. Add a static method `validate_role(role: str) -> bool`
#     that returns True if role is in ["admin", "user", "moderator"].
#     Syntax:
#       @staticmethod
#       def validate_role(role: str) -> bool:
#           ...
#     Print User.validate_role("admin") and User.validate_role("hacker").

# 65. Write a class `Product` with full type hints:
#     Fields: id: int, name: str, price: float, category: str, inStock: bool, quantity: int
#     Methods:
#       - __init__ -> None
#       - __str__ -> str  (e.g. "Iron Sword — $120.00")
#       - is_available() -> bool  (inStock and quantity > 0)
#       - to_dict() -> dict[str, str | int | float | bool]
#     Instantiate all products from the products list. Print available ones.

# 66. Write a class `Order` with full type hints:
#     Fields: id: int, userId: int, productId: int, quantity: int, total: int, status: str
#     Methods:
#       - __init__ -> None
#       - __str__ -> str  (e.g. "Order #1 [completed] — $240")
#       - is_complete() -> bool
#       - to_dict() -> dict
#     Instantiate all orders. Print completed ones.

# 67. Write a class `Inventory` that holds a list of Products:
#     Fields: items: list  (a list of Product instances)
#     Methods:
#       - __init__(self, items: list) -> None
#       - add(self, product) -> None         appends to self.items
#       - remove(self, name: str) -> None    removes product by name
#       - find(self, name: str) -> Optional[object]   returns product or None
#       - available(self) -> list            returns available products
#       - total_value(self) -> float         sum of price * quantity
#     Build one from all products. Print total_value().

# 68. Add __len__ and __contains__ to Inventory:
#     __len__(self) -> int          returns len(self.items)
#     __contains__(self, name: str) -> bool   returns True if name found
#     Syntax: def __contains__(self, item: str) -> bool
#     Print len(inventory) and print("Iron Sword" in inventory).

# 69. Write a subclass `DiscountedProduct(Product)`:
#     Extra field: discount: float  (0.0 to 1.0 — e.g. 0.2 = 20% off)
#     Override __str__ to show original and discounted price.
#     Add property `final_price(self) -> float`.
#     Instantiate one with discount=0.25. Print it.

# 70. Write a class `UserStore` that wraps a list of User instances:
#     Methods (all fully typed):
#       - add(user: User) -> None
#       - get(id: int) -> User | None
#       - all_admins() -> list[User]
#       - sorted_by_age(reverse: bool = False) -> list[User]
#       - to_dicts() -> list[dict]
#     Populate it from all users. Print to_dicts().

# 71. Add a method `search(self, query: str) -> list[User]` to UserStore
#     that returns users whose name contains query (case-insensitive).
#     Print search("a") — should return Alice, Grace, Hank (contains "a").

# 72. Write a class `Report` that takes a UserStore and an Inventory:
#     Methods:
#       - summary(self) -> dict   returns:
#             {"total_users": int,
#              "active_users": int,
#              "total_products": int,
#              "inventory_value": float,
#              "avg_salary": float}
#     Print Report(store, inventory).summary().

# 73. Add a method `top_earners(self, n: int = 3) -> list[User]` to Report
#     that returns the top n users by salary. Print their names and salaries.

# 74. Add `__repr__` to your User class:
#     Syntax: def __repr__(self) -> str
#     It should return something like: User(name='Alice', age=32, role='admin')
#     Note: __repr__ is for developers (shown in the REPL), __str__ is for end users.
#     Print repr(alice) and str(alice) — they should differ.

# 75. Write a class `Pipeline` that chains Callable[[dict], dict] transformers:
#     class Pipeline:
#         steps: list[Callable[[dict], dict]]
#
#         def __init__(self) -> None: ...
#         def add(self, fn: Callable[[dict], dict]) -> "Pipeline":   # returns self for chaining
#             ...
#         def run(self, data: dict) -> dict:
#             ...
#
#     Build a pipeline that:
#       1. Adds a "display" key: f"{name} ({role})"
#       2. Adds a "senior" key: age >= 35
#       3. Uppercases the name
#     Run it on users[0] and print the result.
#     Hint: add() returns self so you can chain: Pipeline().add(fn1).add(fn2).run(data)
