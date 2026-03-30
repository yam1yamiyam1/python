import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from collections import Counter, defaultdict

from training_data import numbers, orders, products, students, users

# =============================================================================
# DRILL 05 — DICTIONARIES & COMPREHENSIONS
# dict basics · methods · nested dicts · dict comprehensions · defaultdict
# 100 Drills | Increasing Entropy
# =============================================================================
# HOW TO RUN:  python drill-05-dicts.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              Do them in order — each section builds on the last.
# =============================================================================


# =============================================================================
# NEW SYNTAX REFERENCE — JS vs PYTHON
# =============================================================================
#
# CREATING
#   JS:     const d = { name: "Alice", age: 32 }
#   Python: d = {"name": "Alice", "age": 32}
#   NOTE:   Python keys MUST be strings with quotes (or any hashable type)
#
# ACCESSING
#   JS:     d.name  or  d["name"]
#   Python: d["name"]               ← always brackets, no dot access
#   safe:   d.get("name")           ← returns None if missing (no crash)
#           d.get("name", "unknown") ← returns default if missing
#
# SETTING / DELETING
#   d["key"] = value                ← add or update
#   del d["key"]                    ← remove key (raises KeyError if missing)
#   d.pop("key")                    ← remove and return value
#   d.pop("key", None)              ← safe pop with default
#
# CHECKING
#   "key" in d                      ← True if key exists (JS: "key" in obj)
#   "key" not in d
#
# ITERATING
#   for key in d:                   ← iterates keys only
#   for key in d.keys():            ← same, explicit
#   for val in d.values():          ← values only
#   for key, val in d.items():      ← key-value pairs (JS: Object.entries)
#
# MERGING
#   JS:     { ...a, ...b }
#   Python: {**a, **b}              ← b wins on conflicts
#           a | b                   ← Python 3.9+, same result
#           a.update(b)             ← mutates a in place
#
# USEFUL METHODS
#   d.keys()                        ← dict_keys view (wrap in list() to print)
#   d.values()                      ← dict_values view
#   d.items()                       ← dict_items view of (key, val) pairs
#   d.copy()                        ← shallow copy
#   d.clear()                       ← empty the dict
#   d.setdefault(key, default)      ← sets key=default if missing, returns value
#   dict.fromkeys(keys, value)      ← create dict with same value for all keys
#
# DICT COMPREHENSIONS
#   {k: v for k, v in iterable}
#   {k: v for k, v in iterable if condition}
#   JS equivalent: Object.fromEntries(arr.map(...))
#
# DEFAULTDICT (auto-creates missing keys)
#   from collections import defaultdict
#   d = defaultdict(list)           ← missing key auto-creates []
#   d = defaultdict(int)            ← missing key auto-creates 0
#   d = defaultdict(set)            ← missing key auto-creates set()
#
# COUNTER (counts occurrences)
#   from collections import Counter
#   c = Counter(["a", "b", "a"])    → Counter({"a": 2, "b": 1})
#   c.most_common(n)                ← top n items
#
# =============================================================================


# =============================================================================
# SECTION A — DICT BASICS (1–15)
# Creating, accessing, adding, deleting
# =============================================================================

# 1. Print users[0] — the full dict. Then print just its keys as a list.
#
#   output: {'id': 1, 'name': 'Alice', ...}
#           ['id', 'name', 'age', 'role', 'salary', 'isActive']

print(list(users[0].keys()))


# 2. Print users[0]["name"] and users[0]["salary"] on one line.
#
#   output: Alice 72000
print(users[0]["name"], users[0]["salary"])

# 3. Use .get() to safely access a "nickname" key that doesn't exist.
#     Print the result, then print with a default of "no nickname".
#
#   output: None
#           no nickname
print(users[0].get("nickname", "no nickname"))

# 4. Create a new dict `profile` with keys: name, age, role.
#     Fill it with data from users[0]. Print it.
#
#   output: {'name': 'Alice', 'age': 32, 'role': 'admin'}

profile = {"name": None, "age": None, "role": None}
for k, v in users[0].items():
    if k in profile:
        profile[k] = v
print(profile)
# 5. Add a "level" key with value 99 to the profile dict. Print it.
#
#   output: {'name': 'Alice', 'age': 32, 'role': 'admin', 'level': 99}

profile["level"] = 99
print(profile)
# 6. Update the "role" key in profile to "superadmin". Print it.
#
#   output: {'name': 'Alice', 'age': 32, 'role': 'superadmin', 'level': 99}
profile["role"] = "superadmin"
print(profile)

# 7. Delete the "level" key from profile using `del`. Print it.
#
#   output: {'name': 'Alice', 'age': 32, 'role': 'superadmin'}
del profile["level"]
print(profile)
# 8. Pop the "role" key from profile using .pop(). Print the popped value and remaining dict.
#
#   output: superadmin
#           {'name': 'Alice', 'age': 32}
print(profile.pop("role"))
print(profile)

# 9. Check if "name" is in profile. Check if "salary" is in profile.
#
#   output: True
#           False
print("name" in profile)
print("salary" in profile)

# 10. Print all keys of users[0] using a for loop.
#
#   output: id
#           name
#           age
#           role
#           salary
#           isActive
for k in users[0].keys():
    print(k)

# 11. Print all values of users[0] using .values().
#
#   output: 1
#           Alice
#           32
#           ...
for v in users[0].values():
    print(v)

# 12. Print all key-value pairs of users[0] using .items().
#     Format: "name: Alice"
#
#   output: id: 1
#           name: Alice
#           ...
for k, v in users[0].items():
    print(f"{k}: {v}")
# 13. Create a dict from two lists using zip():
#     keys = ["name", "age", "role"]
#     vals = ["Alice", 32, "admin"]
#     new syn: dict(zip(keys, vals))
#
#   output: {'name': 'Alice', 'age': 32, 'role': 'admin'}
keys = ["name", "age", "role"]
vals = ["Alice", 32, "admin"]
print(dict(zip(keys, vals)))

# 14. Use dict.fromkeys() to create a dict where all users' names map to 0.
#     new syn: dict.fromkeys(iterable, value)
#
#   output: {'Alice': 0, 'Bob': 0, 'Carol': 0, ...}
print(dict.fromkeys([u["name"] for u in users], 0))

# 15. Merge two dicts using {**a, **b}:
#     a = {"name": "Alice", "age": 32}
#     b = {"role": "admin", "age": 99}   ← age conflict, b wins
#
#   output: {'name': 'Alice', 'age': 99, 'role': 'admin'}
a = {"name": "Alice", "age": 32}
b = {"role": "admin", "age": 99}
print(a | b)
# =============================================================================
# SECTION B — ITERATING & TRANSFORMING DICTS (16–30)
# =============================================================================

# 16. Loop through all users and print "Alice earns $72000" for each.
#
#   output: Alice earns $72000
#           Bob earns $38000
#           ...
for u in users:
    print(f"{u['name']} earns ${u['salary']}")

# 17. Build a dict mapping user id → user name for all users.
#     Use a for loop.
#
#   output: {1: 'Alice', 2: 'Bob', ...}
print({u["id"]: u["name"] for u in users})

# 18. Build a dict mapping product name → price for all products.
#
#   output: {'Iron Sword': 120, 'Steel Shield': 85, ...}
print({p["name"]: p["price"] for p in products})

# 19. Build a dict mapping order id → status for all orders.
#
#   output: {1: 'completed', 2: 'pending', ...}
print({o["id"]: o["status"] for o in orders})

# 20. Build a dict mapping user id → list of their order totals.
#     Use setdefault or check-and-append.
#
#   output: {1: [240, 60], 2: [125, 190], ...}
result = {}
for o in orders:
    result.setdefault(o["userId"], []).append(o["total"])
print(result)
# 21. Build a dict mapping role → count of users with that role.
#     Use .get(key, 0) + 1 pattern.
#
#   output: {'admin': 2, 'user': 4, 'moderator': 2}
result = {}
for u in users:
    result[u["role"]] = result.get(u["role"], 0) + 1
print(result)

# 22. Build a dict mapping category → list of product names in that category.
#
#   output: {'weapon': ['Iron Sword', 'Dragon Bow', 'War Axe'],
#            'armor': [...], 'potion': [...]}
result = {}
for p in products:
    result.setdefault(p["category"], []).append(p["name"])
print(result)

# 23. Build a dict mapping student name → their average grade (float, 2 decimal places).
#
#   output: {'Liam': 87.6, 'Mia': 73.0, ...}
result = {}
for s in students:
    result[s["name"]] = result.get(s["name"], sum(s["grades"]) / len(s["grades"]))
print(result)

# 24. Invert users[0] — swap keys and values. Print the inverted dict.
#     new syn: {v: k for k, v in d.items()}
#     Note: only works cleanly when values are unique and hashable.
#
#   output: {1: 'id', 'Alice': 'name', 32: 'age', ...}
print({v: k for k, v in users[0].items()})

# 25. Find all keys in users[0] whose value is truthy.
#     Print the list of those keys.
#
#   output: ['id', 'name', 'age', 'role', 'salary', 'isActive']
print([k for k, v in users[0].items() if v])

# 26. Build a dict of users[0] but with all string values uppercased.
#     Leave non-string values unchanged.
#
#   output: {'id': 1, 'name': 'ALICE', 'age': 32, 'role': 'ADMIN', ...}
print({k: v.upper() if isinstance(v, str) else v for k, v in users[0].items()})

# 27. Use .update() to merge products[0] with {"inStock": False, "discount": 0.1}.
#     Print the updated dict.
#     NOTE: use a copy so you don't mutate the original.
#
#   output: {'id': 1, 'name': 'Iron Sword', ..., 'inStock': False, 'discount': 0.1}
product1 = products[0].copy()
print(product1 | {"inStock": False, "discount": 0.1})
# 28. Sort a dict by its values (ascending).
#     d = {"banana": 3, "apple": 1, "cherry": 2}
#     new syn: dict(sorted(d.items(), key=func that gets value))
#
#   output: {'apple': 1, 'cherry': 2, 'banana': 3}
d = {"banana": 3, "apple": 1, "cherry": 2}
print(dict(sorted(d.items(), key=lambda x: x[1])))

# 29. Sort the user id → salary dict by salary descending.
#     Print sorted (name, salary) pairs.
#
#   output: ('David', 95000)
#           ('Alice', 72000)
#           ...
name_to_salary = {u["name"]: u["salary"] for u in users}
for name, salary in sorted(name_to_salary.items(), key=lambda x: -x[1]):
    print((name, salary))


# 30. Build a dict where each key is a number from 1–10 and the value is its square.
#     Use a loop.
#
#   output: {1: 1, 2: 4, 3: 9, ..., 10: 100}
print({i: i**2 for i in range(1, 11)})
# =============================================================================
# SECTION C — DICT COMPREHENSIONS (31–50)
# =============================================================================

# 31. Use a dict comprehension to map user id → user name.
#     new syn: {k: v for item in collection}
#
#   output: {1: 'Alice', 2: 'Bob', ...}

print({u["id"]: u["name"] for u in users})
# 32. Use a dict comprehension to map product name → price.
#
#   output: {'Iron Sword': 120, 'Steel Shield': 85, ...}

print({p["name"]: p["price"] for p in products})
# 33. Use a dict comprehension to map user name → salary, active users only.
#
#   output: {'Alice': 72000, 'Carol': 51000, 'David': 95000, 'Frank': 49000, 'Grace': 56000}
print({u["name"]: u["salary"] for u in users})

# 34. Use a dict comprehension to create {number: number squared} for numbers list.
#
#   output: {4: 16, 8: 64, 15: 225, ...}
print({i: i**2 for i in numbers})

# 35. Use a dict comprehension to map order id → total, completed orders only.
#
#   output: {1: 240, 3: 60, 5: 150, 9: 120, 10: 85}
print({o["id"]: o["total"] for o in orders if o["status"] == "completed"})

# 36. Use a dict comprehension to map product name → "in stock" or "out of stock".
#
#   output: {'Iron Sword': 'in stock', 'Dragon Bow': 'out of stock', ...}
print({p["name"]: "in stock" if p["inStock"] else "out of stock" for p in products})

# 37. Use a dict comprehension to map student name → letter grade.
#     avg >= 90 → "A", >= 80 → "B", >= 70 → "C", else → "F"
#
#   output: {'Liam': 'B', 'Mia': 'C', 'Noah': 'A', 'Olivia': 'F', 'Pablo': 'B', 'Quinn': 'C'}
letter_grade = lambda avg: (
    "A" if avg >= 90 else ("B" if avg >= 80 else ("C" if avg >= 70 else "F"))
)
average = lambda grades: sum(grades) / len(grades)
print({s["name"]: letter_grade(average(s["grades"])) for s in students})
# 38. Use a dict comprehension to double all product prices.
#
#   output: {'Iron Sword': 240, 'Steel Shield': 170, ...}
print({p["name"]: p["price"] * 2 for p in products})

# 39. Use a dict comprehension to invert the {id: name} dict from #31.
#     (name → id)
#
#   output: {'Alice': 1, 'Bob': 2, ...}
print({u["name"]: u["id"] for u in users})

# 40. Use a dict comprehension to build {role: [names]} from users.
#     Hint: get unique roles first with a set, then filter per role.
#
#   output: {'admin': ['Alice', 'David'], 'user': [...], 'moderator': [...]}
unique_roles = set(u["role"] for u in users)
print({role: [u["name"] for u in users if u["role"] == role] for role in unique_roles})

# 41. Use a dict comprehension to map each user name → their total spent on orders.
#     Users with no orders → 0.
#
#   output: {'Alice': 300, 'Bob': 315, 'Carol': 255, 'David': 270, 'Eve': 100,
#            'Frank': 120, 'Grace': 85, 'Hank': 0}
print(
    {
        u["name"]: sum([o["total"] for o in orders if o["userId"] == u["id"]])
        for u in users
    }
)

# 42. Use a dict comprehension to build a price lookup: {product_id: price}.
#     Then use it to calculate the total value of all orders without looping over products.
#
#   output: price_lookup then total order value
product_lookup = {p["id"]: p["price"] for p in products}
print(sum([product_lookup.get(o["productId"], 0) * o["quantity"] for o in orders]))
# 43. Use a dict comprehension to flag products that need restocking:
#     {name: True if quantity < 5 else False}
#
#   output: {'Iron Sword': False, 'Dragon Bow': True, ...}
print({p["name"]: p["quantity"] < 5 for p in products})

# 44. Use a dict comprehension to map (role, isActive) tuple → list of names.
#     Hint: get unique combos first, then filter.
#
#   output: {('admin', True): ['Alice', 'David'], ('user', False): ['Bob', 'Eve', 'Hank'], ...}
unique_active_roles = set((u["role"], u["isActive"]) for u in users)
print(
    {
        tuple_key: [u["name"] for u in users if (u["role"], u["isActive"]) == tuple_key]
        for tuple_key in unique_active_roles
    }
)

# 45. Use a nested dict comprehension to build:
#     {user_name: {order_id: total}} for each user's orders.
#
#   output: {'Alice': {1: 240, 3: 60}, 'Bob': {2: 125, 7: 190}, ...}
username_lookup = {u["id"]: u["name"] for u in users}
unique_user_orders = set(o["userId"] for o in orders)
print(unique_user_orders)
print(
    {
        username_lookup.get(user_id): {
            o["id"]: o["total"] for o in orders if o["userId"] == user_id
        }
        for user_id in unique_user_orders
    }
)

# =============================================================================
# SECTION D — NESTED DICTS (46–60)
# =============================================================================

# 46. Build a nested dict: {user_id: {"name": ..., "order_count": ...}}
#     Count orders per user.
#
#   output: {1: {'name': 'Alice', 'order_count': 2}, 2: {'name': 'Bob', 'order_count': 2}, ...}

print(
    {
        u["id"]: {
            "name": u["name"],
            "order_count": sum(1 for o in orders if u["id"] == o["userId"]),
        }
        for u in users
    }
)

# 47. Build a nested dict: {category: {"count": n, "total_value": sum(price*quantity)}}
#     for products grouped by category.
#
#   output: {'weapon': {'count': 3, 'total_value': ...}, ...}
unique_categories = set(p["category"] for p in products)
print(
    {
        category: {
            "count": sum(1 for p in products if p["category"] == category),
            "total_value": sum(
                p["price"] * p["quantity"]
                for p in products
                if p["category"] == category
            ),
        }
        for category in unique_categories
    }
)
# 48. Access a deeply nested value safely using .get() chaining.
#     data = {"user": {"profile": {"name": "Alice"}}}
#     Get data["user"]["profile"]["name"] safely.
#     Then try to get data["user"]["settings"]["theme"] safely (missing key).
#
#   output: Alice
#           None
data = {"user": {"profile": {"name": "Alice"}}}
print(data.get("user", {}).get("profile", {}).get("name", "no name"))
print(data.get("user", {}).get("settings", {}).get("theme", "no theme"))

# 49. Update a nested dict value without mutating the original.
#     Take users[0], create a deep-ish copy: {**users[0], "stats": {"logins": 0}}
#     Then update stats.logins to 5.
#
#   output: updated dict with stats.logins = 5


# 50. Build a config dict:
#     {"db": {"host": "localhost", "port": 5432},
#      "cache": {"host": "redis", "port": 6379}}
#     Print db host and cache port.
#
#   output: localhost
#           6379
user1_copy = {**users[0], "stats": {"logins": 0}}
user1_copy.update({"stats": {"logins": 5}})
print(user1_copy)
# 51. Flatten a nested dict one level deep.
#     nested = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "z": 4}}
#     Result: {"a_x": 1, "a_y": 2, "b_x": 3, "b_z": 4}
#
#   output: {'a_x': 1, 'a_y': 2, 'b_x': 3, 'b_z': 4}
nested = {"a": {"x": 1, "y": 2}, "b": {"x": 3, "z": 4}}
print(
    {
        f"{outer}_{inner}": value
        for outer, inner_dict in nested.items()
        for inner, value in inner_dict.items()
    }
)
# 52. Build a summary dict for each user:
#     {name: {"total_spent": x, "order_count": y, "avg_order": z}}
#
#   output: {'Alice': {'total_spent': 300, 'order_count': 2, 'avg_order': 150.0}, ...}
print(
    {
        u["name"]: {
            "total_spend": sum(o["total"] for o in orders if o["userId"] == u["id"]),
            "order_count": sum(1 for o in orders if o["userId"] == u["id"]),
            "avg_order": (
                sum(o["total"] for o in orders if o["userId"] == u["id"])
                / len([o for o in orders if o["userId"] == u["id"]])
            )
            if len([o for o in orders if o["userId"] == u["id"]]) > 0
            else 0,
        }
        for u in users
    }
)

# 53. Build a product catalog nested dict:
#     {category: {name: price}} for all products.
#
#   output: {'weapon': {'Iron Sword': 120, 'Dragon Bow': 200, 'War Axe': 150},
#            'armor': {...}, 'potion': {...}}
print(
    {
        category: {p["name"]: p["price"] for p in products if p["category"] == category}
        for category in unique_categories
    }
)

# 54. Find the most expensive product per category from the catalog in #53.
#     {category: (name, price)} for max price in each category.
#
#   output: {'weapon': ('Dragon Bow', 200), 'armor': ('Elven Cloak', 95), 'potion': ('Mana Potion', 30)}
print(
    {
        category: max(
            [(p["name"], p["price"]) for p in products if p["category"] == category],
            key=lambda x=category: x[1],
        )
        for category in unique_categories
    }
)

# 55. Merge two nested dicts, combining inner dicts (not overwriting).
#     a = {"x": {"p": 1, "q": 2}, "y": {"p": 3}}
#     b = {"x": {"r": 4}, "z": {"p": 5}}
#     result: {"x": {"p": 1, "q": 2, "r": 4}, "y": {"p": 3}, "z": {"p": 5}}
#
#   output: {'x': {'p': 1, 'q': 2, 'r': 4}, 'y': {'p': 3}, 'z': {'p': 5}}
a = {"x": {"p": 1, "q": 2}, "y": {"p": 3}}
b = {"x": {"r": 4}, "z": {"p": 5}}
print({k: a.get(k, {}) | b.get(k, {}) for k in a.keys() | b.keys()})
# 56. Build a dict of {order_id: {"user_name": ..., "product_name": ..., "total": ...}}
#     for all orders. Look up names from users and products.
#
#   output: {1: {'user_name': 'Alice', 'product_name': 'Iron Sword', 'total': 240}, ...}
product_name_lookup = {p["id"]: p["name"] for p in products}
order_summary = {
    o["id"]: {
        "user_name": username_lookup.get(o["userId"]),
        "product_name": product_name_lookup.get(o["productId"]),
        "total": o["total"],
    }
    for o in orders
}
print(order_summary)

# 57. Given the order summary from #56, find all orders where total > 150.
#     Print order id + user name + total.
#
#   output: 1: Alice — $240
#           4: Carol — $255
#           ...
for o, v in order_summary.items():
    print(f"{o}: {v['user_name']} - ${v['total']}")

# 58. Build {user_name: [product_names]} — all products each user has ever ordered.
#
#   output: {'Alice': ['Iron Sword', 'Leather Armor'], 'Bob': ['Health Potion', 'Elven Cloak'], ...}
print(
    {
        u["name"]: [
            product_name_lookup.get(o["productId"])
            for o in orders
            if o["userId"] == u["id"]
        ]
        for u in users
    }
)

# 59. Find users who ordered more than one product (multiple distinct products).
#     Build {user_name: [product_names_they_ordered]}.
#     Only include users with 2+ orders.
#
#   output: {'Alice': ['Iron Sword', 'Leather Armor'],
#            'Bob': ['Health Potion', 'Elven Cloak'],
#            'David': ['War Axe', 'Leather Armor']}
print(
    {
        u["name"]: [
            product_name_lookup.get(o["productId"])
            for o in orders
            if o["userId"] == u["id"]
        ]
        for u in users
        if len([o for o in orders if o["userId"] == u["id"]]) >= 2
    }
)

# 60. Build a leaderboard dict sorted by total_spent descending.
#     {rank: {"name": ..., "total_spent": ...}}
#     Rank starts at 1.
#
#   output: {1: {'name': 'Bob', 'total_spent': 315},
#            2: {'name': 'Carol', 'total_spent': 255}, ...}
user_totals = [
    (u["name"], sum(o["total"] for o in orders if o["userId"] == u["id"]))
    for u in users
]
sorted_users = sorted(user_totals, key=lambda x: -x[1])
print(
    {
        rank: {"name": name, "total_spent": total}
        for rank, (name, total) in enumerate(sorted_users, start=1)
    }
)
# =============================================================================
# SECTION E — DEFAULTDICT & COUNTER (61–75)
# =============================================================================

# 61. Use defaultdict(list) to group users by role.
#     new syn: from collections import defaultdict
#              d = defaultdict(list)
#              d[key].append(value)   ← no need to check if key exists
#
#   output: defaultdict(<class 'list'>, {'admin': ['Alice', 'David'], ...})
d = defaultdict(list)
for u in users:
    role = u["role"]
    name = u["name"]
    d[role].append(name)
print(d)
# 62. Use defaultdict(int) to count order statuses.
#     new syn: d = defaultdict(int)
#              d[key] += 1
#
#   output: defaultdict(<class 'int'>, {'completed': 5, 'pending': 3, 'shipped': 2})
d = defaultdict(int)
for o in orders:
    d[o["status"]] += 1
print(d)

# 63. Use defaultdict(set) to map category → set of product names.
#
#   output: defaultdict(<class 'set'>, {'weapon': {'Iron Sword', ...}, ...})
d = defaultdict(set)
for p in products:
    d[p["category"]].add(p["name"])
print(d)
# 64. Use defaultdict(list) to build user_id → list of order ids.
#
#   output: defaultdict(<class 'list'>, {1: [1, 3], 2: [2, 7], ...})
d = defaultdict(list)
for o in orders:
    d[o["userId"]].append(o["id"])
print(d)
# 65. Use defaultdict(int) to count how many orders each user has made.
#
#   output: defaultdict(<class 'int'>, {1: 2, 2: 2, 3: 1, ...})
d = defaultdict(int)
for o in orders:
    d[o["userId"]] += 1
print(d)

# 66. Use Counter to count product categories across all products.
#     new syn: from collections import Counter
#              Counter(iterable)
#
#   output: Counter({'armor': 3, 'weapon': 3, 'potion': 2})
category_counts = Counter(p["category"] for p in products)

print(category_counts)
# 67. Use Counter to count order statuses.
#
#   output: Counter({'completed': 5, 'pending': 3, 'shipped': 2})
status_counts = Counter(o["status"] for o in orders)
print(status_counts)

# 68. Use Counter.most_common(n) to get the top 2 most ordered products by order count.
#     new syn: counter.most_common(n)
#
#   output: [(product_id, count), (product_id, count)]
counts = Counter(o["productId"] for o in orders)

top_products = counts.most_common(2)

print(top_products)

# 69. Use Counter to find which user has placed the most orders.
#     new syn: counter.most_common(1)[0]
#
#   output: ('Alice', 2)  or whichever user has most orders (by name)
counts = Counter(username_lookup.get(o["userId"]) for o in orders)
top_user = counts.most_common(1)[0]
print(top_user)

# 70. Combine two Counters using +:
#     c1 = Counter({"a": 3, "b": 2})
#     c2 = Counter({"b": 1, "c": 4})
#     new syn: c1 + c2
#
#   output: Counter({'c': 4, 'a': 3, 'b': 3})
c1 = Counter({"a": 3, "b": 2})
c2 = Counter({"b": 1, "c": 4})
print(c1 + c2)
# 71. Use Counter to count character frequency in "mississippi".
#
#   output: Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
counts = Counter(c for c in "mississippi")
print(counts)

# 72. Use defaultdict(lambda: "unknown") as a fallback dict.
#     Build a lookup of id → name for users.
#     Access a missing id (e.g. 99). It should return "unknown".
#     new syn: defaultdict(lambda: "unknown")
#
#   output: Alice
#           unknown
user_lookup = defaultdict(lambda: "unknown")
for u in users:
    user_lookup[u["id"]] = u["name"]
print(user_lookup[1])  # Accessing a known ID
print(user_lookup[99])
# 73. Use defaultdict(list) to build a multi-level grouping:
#     {role: {True/False (isActive): [names]}}
#     Hint: outer defaultdict, inner dict with setdefault.
#
#   output: {'admin': {True: ['Alice', 'David']},
#            'user': {True: ['Frank'], False: ['Bob', 'Eve', 'Hank']}, ...}
usernames = defaultdict(dict)
for u in users:
    usernames[u["role"]].setdefault(u["isActive"], []).append(u["name"])
print(dict(usernames))
# 74. Use Counter to find words that appear more than once in this sentence:
#     text = "the cat sat on the mat and the cat sat"
#
#   output: {'the': 3, 'cat': 2, 'sat': 2}
text = "the cat sat on the mat and the cat sat"
words = Counter(text.split())
print({word: count for word, count in words.items() if count > 1})


# 75. Use Counter subtraction to find what's left after removing:
#     inventory = Counter({"sword": 5, "shield": 3, "potion": 8})
#     sold      = Counter({"sword": 2, "potion": 5, "arrow": 1})
#     new syn:  inventory - sold   ← drops keys that go to 0 or negative
#
#   output: Counter({'potion': 3, 'sword': 3, 'shield': 3})
inventory = Counter({"sword": 5, "shield": 3, "potion": 8})
sold = Counter({"sword": 2, "potion": 5, "arrow": 1})
print(inventory - sold)
# =============================================================================
# SECTION F — MIXED CHALLENGES (76–90)
# =============================================================================

# 76. Build a dict where each key is an order status and the value is
#     the total revenue for that status.
#
#   output: {'completed': 695, 'pending': 325, 'shipped': 275}  (approx)
d = defaultdict(int)
for o in orders:
    d[o["status"]] += o["total"]
print(dict(d))

# 77. Build a dict of {user_name: "VIP"} for users who have spent over $200 total.
#     Users under $200 → "regular".
#
#   output: {'Alice': 'VIP', 'Bob': 'VIP', 'Carol': 'VIP', 'David': 'VIP',
#            'Eve': 'regular', 'Frank': 'regular', 'Grace': 'regular', 'Hank': 'regular'}
d = defaultdict(int)
for o in orders:
    d[o["userId"]] += o["total"]
print(
    {
        username_lookup.get(user_id): "VIP" if total > 200 else "regular"
        for user_id, total in d.items()
    }
)

# 78. Given a list of dicts, deduplicate by a key.
#     Keep the last occurrence of each id.
#     records = [{"id": 1, "val": "a"}, {"id": 2, "val": "b"}, {"id": 1, "val": "c"}]
#     new syn: {r["id"]: r for r in records}
#
#   output: {1: {'id': 1, 'val': 'c'}, 2: {'id': 2, 'val': 'b'}}
records = [{"id": 1, "val": "a"}, {"id": 2, "val": "b"}, {"id": 1, "val": "c"}]
print({r["id"]: r for r in records})

# 79. Build a frequency dict of first letters of all user names.
#
#   output: {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'E': 1, 'F': 1, 'G': 1, 'H': 1}
print(dict(Counter(u["name"][0] for u in users)))

# 80. Build a dict of {product_name: total_quantity_ordered} across all orders.
#
#   output: {'Iron Sword': 3, 'Health Potion': 9, ...}
d = defaultdict(int)
for o in orders:
    d[product_name_lookup.get(o["productId"])] += o["quantity"]
print(dict(d))

# 81. Find the product that generated the most revenue.
#     Build {product_name: revenue} then find the max.
#
#   output: Health Potion: $225  (or whatever is highest)
d = Counter()
for o in orders:
    d[product_name_lookup.get(o["productId"])] += o["total"]
top = d.most_common(1)[0]
print(f"{top[0]}: ${top[1]}")
# 82. Build a "report card" dict for each student:
#     {name: {"grades": [...], "average": x, "highest": x, "lowest": x, "pass": bool}}
#     pass = average >= 75
#
#   output: {'Liam': {'grades': [...], 'average': 87.6, 'highest': 95, 'lowest': 79, 'pass': True}, ...}


# 83. Pivot the product catalog:
#     From: list of product dicts
#     To:   {"weapon": [...product dicts...], "armor": [...], "potion": [...]}
#     Sort each category list by price ascending.
#
#   output: pivoted catalog with sorted products per category


# 84. Build a dict of {user_name: {"bought": [product names], "spent": total}}.
#     Only include users who have at least one order.
#
#   output: {'Alice': {'bought': ['Iron Sword', 'Leather Armor'], 'spent': 300}, ...}


# 85. Use dict comprehension + zip to build a mapping of
#     {student_name: rank} where rank 1 = highest average.
#     Sort by average descending, assign rank by position.
#
#   output: {'Noah': 1, 'Pablo': 2, 'Liam': 3, 'Quinn': 4, 'Mia': 5, 'Olivia': 6}


# 86. Deep copy a nested dict without using copy.deepcopy.
#     d = {"user": {"name": "Alice", "scores": [10, 20, 30]}}
#     Modify the copy's scores list. Show original is unchanged.
#     new syn: {k: {**v} for k, v in d.items()}   ← one level deep
#     Hint: for the list inside you'll need to copy that too.
#
#   output: original scores unchanged / copy scores modified


# 87. Use dict comprehension to transpose a matrix represented as
#     {row: {col: value}}:
#     matrix = {"r1": {"c1": 1, "c2": 2}, "r2": {"c1": 3, "c2": 4}}
#     Transposed: {"c1": {"r1": 1, "r2": 3}, "c2": {"r1": 2, "r2": 4}}
#
#   output: {'c1': {'r1': 1, 'r2': 3}, 'c2': {'r1': 2, 'r2': 4}}


# 88. Build a rolling average dict:
#     {order_id: running_avg_total_up_to_that_order}
#     Process orders in id order.
#
#   output: {1: 240.0, 2: 182.5, 3: 141.67, ...}


# 89. Build a dict that maps each user to their most expensive single order.
#     {user_name: max_order_total}
#     Users with no orders → 0.
#
#   output: {'Alice': 240, 'Bob': 190, 'Carol': 255, 'David': 150,
#            'Eve': 100, 'Frank': 120, 'Grace': 85, 'Hank': 0}


# 90. Use dict comprehension to create a sparse matrix (only store non-zero values):
#     grid = [[0,1,0],[2,0,3],[0,0,4]]
#     Result: {(row, col): value} for all non-zero values.
#
#   output: {(0, 1): 1, (1, 0): 2, (1, 2): 3, (2, 2): 4}


# =============================================================================
# SECTION G — BOSS DRILLS (91–100)
# =============================================================================

# 91. Build a complete order enrichment pipeline using only dict operations.
#     Result: list of dicts, each containing:
#     {order_id, user_name, product_name, category, quantity, total, status}
#     No for loops in the final expression — use dict lookups and comprehensions.
#
#   output: list of enriched order dicts


# 92. Build a "category performance" report dict:
#     {category: {
#         "products": [names],
#         "total_revenue": sum of all order totals for products in category,
#         "units_sold": sum of quantities,
#         "avg_price": avg product price in category
#     }}
#
#   output: {'weapon': {'products': [...], 'total_revenue': ..., ...}, ...}


# 93. Find the "power users" — users whose total spending is above the average
#     spending across all users. Return {name: total_spent}.
#
#   output: {'Bob': 315, 'Carol': 255, 'Alice': 300, 'David': 270}  (approx — above avg)


# 94. Build an inverted index:
#     {word: [user_names_whose_name_contains_that_word_as_substring_or_letter]}
#     For each letter a-z, which user names contain that letter?
#     Only include letters that appear in at least one name.
#
#   output: {'a': ['Alice', 'Carol', 'David', 'Frank', 'Grace', 'Hank'],
#            'b': ['Bob'], ...}


# 95. Build a transition matrix for order statuses:
#     If you look at consecutive orders (sorted by id), what status follows what?
#     {from_status: {to_status: count}}
#
#   output: {'completed': {'pending': ..., 'shipped': ...}, ...}


# 96. Implement a simple in-memory cache using a dict.
#     def memoize_with_dict(func, cache=None):
#     Cache stores {arg: result}. On cache hit, print "cache hit" and return stored.
#     On cache miss, compute, store, return.
#     Test with a function that sums a user's order totals (by user_id).
#
#   output: cache miss then result / cache hit then same result


# 97. Build a "co-purchase" dict:
#     Which products are ordered by the same user?
#     {product_name: set_of_other_product_names_ordered_by_same_users}
#
#   output: {'Iron Sword': {'Leather Armor'}, 'Health Potion': {'Elven Cloak'}, ...}


# 98. Build a dict-based graph (adjacency list) from this edge list:
#     edges = [(1,2), (1,3), (2,4), (3,4), (4,5)]
#     {node: [connected_nodes]}
#     Make it undirected (both directions).
#
#   output: {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3, 5], 5: [4]}


# 99. Implement a word frequency normalizer.
#     text = "the quick brown fox jumps over the lazy dog the fox"
#     1. Count word frequencies with Counter.
#     2. Normalize: divide each count by total words → frequency as float.
#     3. Sort by frequency descending.
#     Result: {word: normalized_frequency}
#
#   output: {'the': 0.3, 'fox': 0.2, 'quick': 0.1, ...}


# 100. BOSS — Build a complete analytics dashboard dict.
#
#      Build one dict `dashboard` with these exact keys:
#
#      "summary": {
#          "total_users": n,
#          "active_users": n,
#          "total_products": n,
#          "total_orders": n,
#          "total_revenue": n
#      }
#      "top_spender":    {"name": ..., "spent": ...}
#      "top_product":    {"name": ..., "revenue": ...}  ← most revenue generated
#      "by_status":      {"completed": n, "pending": n, "shipped": n}  ← order counts
#      "by_category":    {"weapon": revenue, "armor": revenue, "potion": revenue}
#      "user_segments":  {"VIP": [names], "regular": [names]}  ← VIP = spent > avg
#
#      Print each section with a header line.
#      All values must be computed — no hardcoding.
#
#   output:
#      === SUMMARY ===
#      total_users: 8  active_users: 5  ...
#      === TOP SPENDER ===
#      Bob: $315
#      ...
