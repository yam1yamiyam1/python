import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from collections import deque
from functools import reduce

from training_data import numbers, orders, products, students, users

# =============================================================================
# DRILL 04 — DATA STRUCTURES
# Lists · Tuples · Sets · Stacks · Queues
# 100 Drills | Increasing Entropy
# =============================================================================
# HOW TO RUN:  python drill-04-data-structures.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              Do them in order — each section builds on the last.
# =============================================================================


# =============================================================================
# NEW SYNTAX REFERENCE — JS vs PYTHON
# =============================================================================
#
# LISTS (like JS arrays, but more methods)
# ─────────────────────────────────────────────────────────────
# JS                        Python
# arr.push(x)           →   lst.append(x)
# arr.pop()             →   lst.pop()
# arr.shift()           →   lst.pop(0)
# arr.unshift(x)        →   lst.insert(0, x)
# arr.splice(i,1)       →   lst.pop(i)  or  del lst[i]
# arr.splice(i,0,x)     →   lst.insert(i, x)
# arr.includes(x)       →   x in lst
# arr.indexOf(x)        →   lst.index(x)
# arr.length            →   len(lst)
# arr.reverse()         →   lst.reverse()   ← mutates in place, returns None
# [...arr].reverse()    →   lst[::-1]        ← returns new reversed list
# arr.sort()            →   lst.sort()       ← mutates in place
# [...arr].sort()       →   sorted(lst)      ← returns new sorted list
# arr.slice(a, b)       →   lst[a:b]
# arr.concat(arr2)      →   lst + lst2       ← returns new list
# arr.join(", ")        →   ", ".join(lst)   ← separator on the LEFT in Python
# arr.fill(x)           →   [x] * n
# arr.flat()            →   no direct — use list comprehension or itertools
# arr.some(fn)          →   any(fn(x) for x in lst)
# arr.every(fn)         →   all(fn(x) for x in lst)
# arr.find(fn)          →   next((x for x in lst if fn(x)), None)
# arr.filter(fn)        →   [x for x in lst if fn(x)]
# arr.map(fn)           →   [fn(x) for x in lst]
# arr.reduce(fn, init)  →   use a for loop or functools.reduce
#
# TUPLES (immutable list — no JS equivalent)
# ─────────────────────────────────────────────────────────────
# t = (1, 2, 3)         ← parentheses, or just: t = 1, 2, 3
# t[0]                  ← access same as list
# a, b, c = t           ← unpack same as list
# len(t)                ← same as list
# x in t                ← same as list
# t.count(x)            ← how many times x appears
# t.index(x)            ← first index of x
# list(t)               ← convert to list
# tuple(lst)            ← convert from list
# NOTE: cannot append, remove, or change values after creation
#
# SETS (unique unordered values — like JS Set)
# ─────────────────────────────────────────────────────────────
# JS                        Python
# new Set([1,2,3])      →   {1, 2, 3}  or  set([1, 2, 3])
# s.add(x)              →   s.add(x)
# s.delete(x)           →   s.remove(x)   ← raises if missing
#                           s.discard(x)  ← silent if missing
# s.has(x)              →   x in s
# s.size                →   len(s)
# [...new Set(arr)]     →   list(set(lst))   ← deduplicate
# set math:
#   a | b               ← union (all items from both)
#   a & b               ← intersection (only items in both)
#   a - b               ← difference (in a but not b)
#   a ^ b               ← symmetric difference (in one but not both)
#
# STACKS (LIFO — Last In First Out)
# ─────────────────────────────────────────────────────────────
# Python uses a plain list as a stack:
#   stack = []
#   stack.append(x)     ← push
#   stack.pop()         ← pop (from the end)
#   stack[-1]           ← peek (top of stack without removing)
#
# QUEUES (FIFO — First In First Out)
# ─────────────────────────────────────────────────────────────
# Use collections.deque for efficient queues:
#   from collections import deque
#   q = deque()
#   q.append(x)         ← enqueue (add to right)
#   q.popleft()         ← dequeue (remove from left)
#   q[0]                ← peek front
# NOTE: list.pop(0) works but is O(n) — deque.popleft() is O(1)
#
# =============================================================================


# =============================================================================
# SECTION A — LIST BASICS (1–15)
# Creating, accessing, slicing, basic mutation
# =============================================================================

# 1. Create a list of the first 5 user names. Print it.
#
#   lst = [users[0]["name"], ...]
#
#   output: ['Alice', 'Bob', 'Carol', 'David', 'Eve']

print(list(u["name"] for u in users)[:5])


# 2. Print the first and last product name using index access.
#
#   output: Iron Sword
#           Elven Cloak

print(products[0]["name"])
print(products[-1]["name"])
# 3. Print the last 3 orders using negative slicing.
#
#   lst[start:stop]
#
#   output: last 3 order dicts
print(list(orders[-3:]))

# 4. Print every other product name (index 0, 2, 4, 6).
#
#   lst[::2]
#
#   output: ['Iron Sword', 'Health Potion', 'Leather Armor', 'War Axe']

print(list(products[::2]))
# 5. Print all product names in reverse order using slicing.
#
#   lst[::-1]
#
#   output: ['Elven Cloak', 'War Axe', 'Mana Potion', ...]

print(list(map(lambda x: x["name"], products[::-1])))
# 6. Create a list of all salaries. Print the min and max WITHOUT using min()/max().
#
#   salaries = [get each salary]
#   loop to find min, loop to find max
#
#   output: min: 34000  max: 95000
min_salary = users[0]["salary"]
max_salary = 0
for u in users:
    if u["salary"] > max_salary:
        max_salary = u["salary"]
    if u["salary"] < min_salary:
        min_salary = u["salary"]
print(f"min: {min_salary} max: {max_salary}")
# 7. Print the length of users, products, orders, students on one line.
#
#   output: 8 8 10 6
print(f"{len(users)} {len(products)} {len(orders)} {len(students)}")

# 8. Print a slice of numbers from index 2 to 6 (exclusive).
#
#   output: [15, 16, 23, 42]

print(numbers[2:6])
# 9. Print the middle element of numbers (index len//2).
#
#   output: 23

print(numbers[len(numbers) // 2])
# 10. Create a list of all product prices. Sort it in place. Print it.
#     new syn: lst.sort()  ← mutates the original list, returns None
#
#   output: [25, 30, 60, 85, 95, 120, 150, 200]

print([p["price"] for p in sorted(products, key=lambda x: x["price"])])
# 11. Create a list of all product prices. Get a new sorted list without mutating.
#     new syn: sorted(lst)  ← returns new list, original unchanged
#
#   output: [25, 30, 60, 85, 95, 120, 150, 200]
print([p["price"] for p in sorted(products, key=lambda x: x["price"])])


# 12. Append the string "done" to a copy of numbers. Print both lists.
#     new syn: lst.copy()  ← shallow copy, changes don't affect original
#
#   output: [4, 8, 15, 16, 23, 42, 7, 3, 19, 11]
#           [4, 8, 15, 16, 23, 42, 7, 3, 19, 11, 'done']
copy = [*numbers, "done"]
print(copy)

# 13. Insert "URGENT" at index 0 of a list of order statuses. Print it.
#     new syn: lst.insert(index, value)
#
#   output: ['URGENT', 'completed', 'pending', ...]
statuses = [o["status"] for o in orders]
statuses.insert(0, "URGENT")
print(statuses)
# 14. Remove the first occurrence of "pending" from the status list. Print it.
#     new syn: lst.remove(value)  ← removes first match, raises if not found
#
#   output: status list without first "pending"
statuses.remove("pending")
print(statuses)

# 15. Count how many times "completed" appears in the order status list.
#     new syn: lst.count(value)
#
#   output: 5
print(statuses.count("completed"))

# =============================================================================
# SECTION B — LIST MUTATION & METHODS (16–30)
# =============================================================================

# 16. Build a list of user names. Reverse it in place. Print it.
#     new syn: lst.reverse()  ← mutates in place, returns None
#
#   output: ['Hank', 'Grace', 'Frank', 'Eve', 'David', 'Carol', 'Bob', 'Alice']
user_names = [u["name"] for u in users]
user_names.reverse()
print(user_names)
# 17. Build a list of product prices. Pop the last one. Print the popped value and remaining list.
#     new syn: lst.pop()  ← removes and returns last item
#
#   output: popped: 95
#           remaining: [120, 85, 25, 200, 60, 30, 150]


# 18. Pop the first product price from the list. Print popped value and remaining list.
#     new syn: lst.pop(0)  ← removes and returns item at index
#
#   output: popped: 120
#           remaining: [85, 25, 200, 60, 30, 150, 95]
prices = [p["price"] for p in products]
print(f"popped: {prices.pop(0)}")
print(f"remaining: {prices}")
# 19. Build a list of order totals. Extend it with [999, 888]. Print result.
#     new syn: lst.extend(other)  ← adds each item from other, like JS arr.concat
#              lst += [999, 888]  ← same thing
#
#   output: [240, 125, 60, 255, 150, 100, 190, 120, 120, 85, 999, 888]
totals = [o["total"] for o in orders]
totals.extend([999, 888])
print(totals)
# 20. Build two lists: active user names and inactive user names.
#     Concatenate them with +. Print the combined list.
#
#   output: active names + inactive names in one list
active_user_names = []
inactive_user_names = []
for u in users:
    if u["isActive"]:
        active_user_names.append(u["name"])
    else:
        inactive_user_names.append(u["name"])
print(active_user_names + inactive_user_names)
# 21. Find the index of the first user with salary > 70000.
#     Hint: build a list of salaries, use lst.index(value) — but you need the value first.
#
#   output: 0  (Alice is index 0)
salaries = [u["salary"] for u in users]
first_high_salary = next(s for s in salaries if s > 70000)
print(salaries.index(first_high_salary))
# 22. Check if 42 is in numbers using `in`. Print True/False.
#     Then check if 99 is in numbers.
#
#   output: True
#           False
is_in = lambda x: x in numbers
print(is_in(42))
print(is_in(99))

# 23. Clear a copy of the numbers list. Print before and after.
#     new syn: lst.clear()  ← empties the list in place
#
#   output: [4, 8, 15, 16, 23, 42, 7, 3, 19, 11]
#           []
# new_nums = numbers
# print(new_nums)
# new_nums.clear()
# print(new_nums)
# 24. Build a flat list of ALL grades from ALL students using a loop.
#     (No flat_map — just a nested for loop and append.)
#
#   output: [88, 92, 79, 95, 84, 72, 68, 75, 80, 70, ...]

print([g for s in students for g in s["grades"]])

# 25. Build a list of [name, salary] pairs for every user using a loop.
#
#   output: [['Alice', 72000], ['Bob', 38000], ...]

print([[u["name"], u["salary"]] for u in users])
# 26. Given this nested list, flatten it manually:
#     nested = [[1, 2], [3, 4], [5, 6]]
#     Use a loop. No built-ins.
#
#   output: [1, 2, 3, 4, 5, 6]
nested = [[1, 2], [3, 4], [5, 6]]
print([y for x in nested for y in x])

# 27. Sort users by salary descending WITHOUT mutating the original list.
#     Print the sorted names only.
#
#   output: ['David', 'Alice', 'Grace', ...]

print([u["name"] for u in sorted(users, key=lambda x: -x["salary"])])
# 28. Sort products by price ascending, then print name + price.
#
#   output: Health Potion: $25
#           Mana Potion: $30
#           ...

for p in sorted(products, key=lambda x: x["price"]):
    print(f"{p['name']}: ${p['price']}")
# 29. Build a list of product names. Join them with " | ". Print the string.
#     new syn: "sep".join(lst)
#
#   output: Iron Sword | Steel Shield | Health Potion | ...

print(" | ".join([p["name"] for p in products]))
# 30. Multiply the string "ha" into a list: ["ha", "ha", "ha"] using * operator.
#     new syn: [value] * n  ← creates a list with n copies
#     Then do the same for a list of 5 zeros.
#
#   output: ['ha', 'ha', 'ha']
#           [0, 0, 0, 0, 0]

print(["ha"] * 3)
print([0] * 5)
# =============================================================================
# SECTION C — LIST COMPREHENSIONS (31–45)
# =============================================================================

# 31. Use a list comprehension to get all user names.
#     new syn: [expression for item in iterable]
#
#   output: ['Alice', 'Bob', 'Carol', ...]

print([u["name"] for u in users])
# 32. Use a list comprehension to get all product prices doubled.
#
#   output: [240, 170, 50, 400, 120, 60, 300, 190]
print([p["price"] * 2 for p in products])

# 33. Use a list comprehension to get names of active users only.
#     new syn: [expression for item in iterable if condition]
#
#   output: ['Alice', 'Carol', 'David', 'Frank', 'Grace']

print([u["name"] for u in users if u["isActive"]])
# 34. Use a list comprehension to get names of products with price < 100.
#
#   output: ['Steel Shield', 'Health Potion', 'Mana Potion', 'Leather Armor', 'Elven Cloak']
print([p["name"] for p in products if p["price"] < 100])

# 35. Use a list comprehension to build "Alice (admin)" strings for every user.
#
#   output: ['Alice (admin)', 'Bob (user)', ...]
print([f"{u['name']} ({u['role']})" for u in users])

# 36. Use a list comprehension to square every number in `numbers`.
#
#   output: [16, 64, 225, 256, 529, 1764, 49, 9, 361, 121]
print([n**2 for n in numbers])
# 37. Use a list comprehension to get all order totals above 150.
#
#   output: [240, 255, 190]

print([o["total"] for o in orders if o["total"] > 150])
# 38. Use a list comprehension to convert all user salaries to floats.
#
#   output: [72000.0, 38000.0, 51000.0, ...]

print([float(u["salary"]) for u in users])
# 39. Use a nested list comprehension to flatten all student grades.
#     new syn: [x for inner in outer for x in inner]
#
#   output: [88, 92, 79, 95, 84, 72, 68, 75, ...]
print([g for s in students for g in s["grades"]])

# 40. Use a list comprehension to get (name, price) tuples for all products.
#
#   output: [('Iron Sword', 120), ('Steel Shield', 85), ...]
print([(p["name"], p["price"]) for p in products])

# 41. Use a list comprehension with ternary to label each user:
#     salary > 60000 → "high" else "low"
#
#   new syn: [a if condition else b for x in lst]
#
#   output: ['high', 'low', 'low', 'high', 'low', 'low', 'low', 'low']
print(["high" if u["salary"] > 60000 else "low" for u in users])

# 42. Use a list comprehension to get names of users whose name starts with a vowel.
#
#   output: ['Alice', 'Eve']
print(
    [
        u["name"]
        for u in users
        if u["name"].lower().startswith(("a", "e", "i", "o", "u"))
    ]
)

# 43. Use a list comprehension to get all unique order statuses.
#     Hint: build the list first, then deduplicate with set().
#
#   output: ['completed', 'pending', 'shipped']  (order may vary)
print(list({o["status"] for o in orders}))

# 44. Use a list comprehension to build a multiplication table for 3 (1–10).
#
#   output: [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
print([i * 3 for i in range(1, 11)])

# 45. Use a list comprehension to get orders where the product is a weapon.
#     You'll need to look up the product by productId inside the comprehension.
#     Hint: next(p for p in products if p["id"] == o["productId"])
#
#   output: list of weapon orders
print(
    [
        o
        for o in orders
        if next(p for p in products if p["id"] == o["productId"])["category"]
        == "weapon"
    ]
)

# =============================================================================
# SECTION D — TUPLES (46–60)
# =============================================================================

# 46. Create a tuple of the first 3 product names. Print it and its type.
#     new syn: t = (a, b, c)  or  t = a, b, c
#
#   output: ('Iron Sword', 'Steel Shield', 'Health Potion')
#           <class 'tuple'>
t = tuple(p["name"] for p in products)[:3]
print(t)
print(type(t))
# 47. Access the second item of the tuple from #46. Print it.
#
#   output: Steel Shield
a, b, c = t
print(b)
# 48. Unpack the tuple from #46 into 3 variables. Print each.
#
#   output: Iron Sword
#           Steel Shield
#           Health Potion
print(a)
print(b)
print(c)

# 49. Try to change the first item of a tuple. Catch the TypeError and print it.
#     new syn: try: t[0] = "x"  except TypeError as e: print(e)
#
#   output: 'tuple' object does not support item assignment
try:
    t[0] = "x"
except TypeError as e:
    print(e)

# 50. Create a tuple of (name, salary) for every user using a loop.
#     Print the list of tuples.
#
#   output: [('Alice', 72000), ('Bob', 38000), ...]
print([(u["name"], u["salary"]) for u in users])

# 51. Convert the tuple from #46 to a list. Append "War Axe". Convert back to tuple.
#     new syn: list(t)  /  tuple(lst)
#
#   output: ('Iron Sword', 'Steel Shield', 'Health Potion', 'War Axe')
new_t = list(t)
new_t.append("War Axe")
print(tuple(new_t))

# 52. Count how many times "completed" appears in this tuple:
#     statuses = tuple(o["status"] for o in orders)
#     new syn: t.count(value)
#
#   output: 5
statuses = tuple(o["status"] for o in orders)
print(statuses.count("completed"))
# 53. Find the index of "shipped" in the statuses tuple.
#     new syn: t.index(value)
#
#   output: 3
print(statuses.index("shipped"))

# 54. Create a tuple of all numbers. Print its length, min, and max.
#     Hint: min() and max() work on tuples too.
#
#   output: length: 10  min: 3  max: 42

t_numbers = tuple(numbers)
print(f"length: {len(t_numbers)} min: {min(t_numbers)} max: {max(t_numbers)}")
# 55. Unpack the first 3 items from a tuple of all product prices, collect the rest.
#     new syn: a, b, c, *rest = t
#
#   output: first: 120  second: 85  third: 25  rest: (200, 60, 30, 150, 95)
a, b, c, *rest = tuple(p["price"] for p in products)
print(f"first: {a} second: {b} third: {c} rest: {rest}")

# 56. Create a tuple of tuples — each inner tuple is (id, name) for every user.
#     Print it.
#
#   output: ((1, 'Alice'), (2, 'Bob'), ...)

print(tuple((u["id"], u["name"]) for u in users))
# 57. Zip users and products together into a tuple of tuples.
#     new syn: tuple(zip(a, b))
#
#   output: tuple of (user_dict, product_dict) pairs

print(tuple(zip({u["name"] for u in users}, {p["name"] for p in products})))
# 58. Sort a list of (name, salary) tuples by salary descending.
#     new syn: sorted(lst, key=func that gets salary, reverse=True)
#
#   output: [('David', 95000), ('Alice', 72000), ...]
print([(u["name"], u["salary"]) for u in sorted(users, key=lambda x: -x["salary"])])

# 59. Use a tuple as a dict key. Store a count for each (role, isActive) combo.
#     new syn: d[(key1, key2)] = value
#
#   output: {('admin', True): 2, ('user', False): 2, ...}
d = {}
for u in users:
    key = (u["role"], u["isActive"])
    d[key] = d.get(key, 0) + 1
print(d)

# 60. Demonstrate that tuples are faster to create than lists.
#     Create both 1000 times using a loop, time each with time.time().
#     new syn: import time  /  time.time()
#
#   output: tuple time: ...  list time: ...  (tuples should be faster)
start_time_list = time.time()
for _ in range(1000):
    my_list = [1, 2, 3, 4, 5]
end_time_list = time.time()
list_time = end_time_list - start_time_list

start_time_tuple = time.time()
for _ in range(1000):
    my_tuple = (1, 2, 3, 4, 5)
end_time_tuple = time.time()
tuple_time = end_time_tuple - start_time_tuple
print(list_time)
print(tuple_time)
# =============================================================================
# SECTION E — SETS (61–75)
# =============================================================================

# 61. Create a set of all product categories. Print it.
#     new syn: set(lst)  or  {a, b, c}
#
#   output: {'weapon', 'armor', 'potion'}  (order may vary)
categories = set(p["category"] for p in products)

# 62. Create a set of all order statuses. Print it.
#
#   output: {'completed', 'pending', 'shipped'}
print(set(o["status"] for o in orders))

# 63. Check if "weapon" is in the categories set.
#     new syn: x in s
#
#   output: True
print("weapon" in categories)

# 64. Add "consumable" to the categories set. Print it.
#     new syn: s.add(value)
#
#   output: {'weapon', 'armor', 'potion', 'consumable'}
categories.add("consumable")
print(categories)

# 65. Remove "consumable" from the set using remove(). Print it.
#     Then try to remove "missing" using discard() — no error.
#     new syn: s.remove(x)  ← raises KeyError if missing
#              s.discard(x) ← silent if missing
#
#   output: {'weapon', 'armor', 'potion'}
categories.remove("consumable")
print(categories)
categories.discard("consumable")
print(categories)

# 66. Deduplicate this list using a set, then convert back to a sorted list:
#     dupes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
#
#   output: [1, 2, 3, 4, 5, 6, 9]
dupes = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(list(set(dupes)))
# 67. Get all unique user roles as a sorted list.
#
#   output: ['admin', 'moderator', 'user']
print(list(set(u["role"] for u in users)))

# 68. Get the UNION of these two sets:
#     a = {1, 2, 3, 4}
#     b = {3, 4, 5, 6}
#     new syn: a | b  or  a.union(b)
#
#   output: {1, 2, 3, 4, 5, 6}
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))
# 69. Get the INTERSECTION of sets a and b from #68.
#     new syn: a & b  or  a.intersection(b)
#
#   output: {3, 4}
print(a.intersection(b))

# 70. Get the DIFFERENCE a - b from #68 (in a but not b).
#     new syn: a - b  or  a.difference(b)
#
#   output: {1, 2}
print(a.difference(b))

# 71. Get the SYMMETRIC DIFFERENCE of a and b (in one but not both).
#     new syn: a ^ b  or  a.symmetric_difference(b)
#
#   output: {1, 2, 5, 6}
print(a ^ b)

# 72. Check if {1, 2} is a subset of {1, 2, 3, 4}.
#     new syn: a.issubset(b)  or  a <= b
#
#   output: True

print({1, 2} <= a)
# 73. Check if {1, 2, 3, 4} is a superset of {2, 3}.
#     new syn: a.issuperset(b)  or  a >= b
#
#   output: True
print(a >= {2, 3})

# 74. Find users who have placed orders AND are active.
#     Hint: build a set of userIds from orders, build a set of ids of active users.
#           Use intersection to find the overlap.
#
#   output: set of user ids who are both active and have orders
order_user_ids = set(o["userId"] for o in orders)
active_user_ids = set(u["id"] for u in users if u["isActive"])
print(order_user_ids.intersection(active_user_ids))
# 75. Find product ids that appear in orders but are out of stock.
#     Hint: set of productIds from orders, set of ids of out-of-stock products.
#           Use intersection.
#
#   output: set of product ids
order_product_ids = set(o["productId"] for o in orders)
no_stock_product_ids = set(p["id"] for p in products if not p["inStock"])
print(order_product_ids & no_stock_product_ids)

# =============================================================================
# SECTION F — STACKS (76–85)
# =============================================================================
# Stack = LIFO (Last In First Out)
# Use a plain list: append() to push, pop() to pop, [-1] to peek

# 76. Build a stack. Push all product names onto it one by one. Print the stack.
#
#   stack = []
#   push each product name with append()
#
#   output: ['Iron Sword', 'Steel Shield', ..., 'Elven Cloak']

stack = []
for p in products:
    stack.append(p["name"])
print(stack)
# 77. Peek at the top of the stack (without removing). Print it.
#     new syn: stack[-1]
#
#   output: Elven Cloak
print(stack[-1])

# 78. Pop 3 items from the stack. Print each popped value.
#
#   output: Elven Cloak
#           War Axe
#           Mana Potion
for i in range(3):
    print(stack.pop(-i))
print(stack)
# 79. Check if the stack is empty.
#     new syn: len(stack) == 0  or  not stack
#
#   output: False
print(not stack)

# 80. Use a stack to reverse a list of numbers WITHOUT using [::-1] or .reverse().
#     Push all numbers on, then pop them all off into a new list.
#
#   output: [11, 19, 3, 7, 42, 23, 16, 15, 8, 4]
new_stack = []
for n in numbers:
    new_stack.append(n)
print(new_stack)
reverse_stack = []
for i in range(len(new_stack)):
    reverse_stack.append(new_stack.pop(-1))
print(reverse_stack)

# 81. Use a stack to check if a string has balanced parentheses.
#     "((()))"  → True
#     "(()"     → False
#     "(()()))" → False
#     Push "(" onto stack, pop when ")" found, unbalanced if stack non-empty at end.
#
#   output: True
#           False
#           False
a = "((()))"
b = "(()"
c = "(()()))"


def balance_checker(string):
    stack = []
    for c in string:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


print(balance_checker(a))
print(balance_checker(b))
print(balance_checker(c))
# 82. Simulate an undo stack.
#     actions = ["type A", "type B", "delete", "type C"]
#     Push each action. Then undo (pop) the last 2. Print remaining.
#
#   output: ['type A', 'type B']
actions = ["type A", "type B", "delete", "type C"]
actions.pop()
actions.pop()
print(actions)
# 83. Use a stack to evaluate this postfix expression: "3 4 + 2 *"
#     Postfix means operator comes after operands.
#     "3 4 +" means 3+4=7, then "7 2 *" means 7*2=14.
#     Push numbers, pop two when you hit an operator, push the result.
#
#   output: 14
a = "3 4 + 2 *"


def postfix(string):
    stack = []
    for c in string.split():
        if c not in ["+", "-", "*", "/"]:
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()
            match c:
                case "+":
                    result = left + right
                case "-":
                    result = left - right
                case "*":
                    result = left * right
                case "/":
                    result = left / right
            stack.append(result)
    return stack[0]


print(postfix(a))

# 84. Build a browser history stack. Visit 5 pages (push). Go back 2 (pop).
#     Print current page.
#
#   pages = ["home", "about", "products", "contact", "cart"]
#
#   output: products
stack = []
pages = ["home", "about", "products", "contact", "cart"]
for i in pages:
    stack.append(i)
stack.pop()
stack.pop()
print(stack[-1])


# 85. Use a stack to convert a decimal number to binary.
#     Divide by 2, push remainder each time, pop all to build binary string.
#
#   def decimal_to_binary(n):
#       stack = []
#       while n > 0:
#           push n % 2 onto stack
#           n = n // 2
#       pop all items and join as string
#
#   call:   decimal_to_binary(13)
#   output: 1101
def dec_to_binary(n):
    stack = []
    while n > 0:
        stack.append(n % 2)
        n = n // 2
    binary_str = ""
    while stack:
        binary_str += str(stack.pop())
    return binary_str


print(dec_to_binary(13))

# =============================================================================
# SECTION G — QUEUES (86–95)
# =============================================================================
# Queue = FIFO (First In First Out)
# Use collections.deque: append() to enqueue, popleft() to dequeue

# 86. Import deque and create an empty queue. Enqueue all user names. Print it.
#     new syn: from collections import deque
#              q = deque()
#              q.append(x)   ← enqueue (add to right)
#
#   output: deque(['Alice', 'Bob', 'Carol', ...])
q = deque()
for u in users:
    q.append(u["name"])
print(q)
# 87. Peek at the front of the queue without removing.
#     new syn: q[0]
#
#   output: Alice
print(q[0])

# 88. Dequeue 3 items. Print each one as it comes out.
#     new syn: q.popleft()  ← removes and returns leftmost item
#
#   output: Alice
#           Bob
#           Carol
print(q.popleft())
print(q.popleft())
print(q.popleft())

# 89. Check if the queue is empty.
#     new syn: len(q) == 0  or  not q
#
#   output: False
print(not q)

# 90. Simulate a print queue. Add 5 jobs. Process (dequeue) them one by one.
#     Print "Processing: {job}" for each.
#
#   jobs = ["doc1.pdf", "photo.jpg", "report.xlsx", "slide.pptx", "note.txt"]
#
#   output: Processing: doc1.pdf
#           Processing: photo.jpg
#           ...
jobs = ["doc1.pdf", "photo.jpg", "report.xlsx", "slide.pptx", "note.txt"]
print_queue = deque(jobs)
while print_queue:
    print(f"Processing: {print_queue.popleft()}")
# 91. Use a queue to simulate order processing.
#     Enqueue all pending orders. Process (dequeue) them one by one.
#     Print "Processing order #{id}" for each.
#
#   output: Processing order #2
#           Processing order #6
#           Processing order #8
pending_orders = list(
    map(lambda x: x["id"], filter(lambda x: x["status"] == "pending", orders))
)
process_order = deque(pending_orders)
while process_order:
    print(f"Processing order #{process_order.popleft()}")
# 92. Use deque as a bounded queue (max size 3).
#     new syn: deque(maxlen=3)  ← automatically drops oldest when full
#     Add 5 items. Print after each addition.
#
#   output: deque([1], maxlen=3)
#           deque([1, 2], maxlen=3)
#           deque([1, 2, 3], maxlen=3)
#           deque([2, 3, 4], maxlen=3)
#           deque([3, 4, 5], maxlen=3)
my_queue = deque(maxlen=3)
to_add = [1, 2, 3, 4, 5]
for i in to_add:
    my_queue.append(i)
    print(my_queue)
# 93. Use deque to rotate items. Rotate right by 2.
#     new syn: q.rotate(n)  ← positive = rotate right, negative = rotate left
#
#   q = deque([1, 2, 3, 4, 5])
#   output: deque([4, 5, 1, 2, 3])
q = deque([1, 2, 3, 4, 5])
q.rotate(2)
print(q)

# 94. Use a queue to do a breadth-first level-order print of this tree:
#     tree = {"val": 1, "children": [
#                 {"val": 2, "children": [{"val": 4, "children": []}, {"val": 5, "children": []}]},
#                 {"val": 3, "children": [{"val": 6, "children": []}]}
#             ]}
#     Enqueue root, then dequeue and enqueue children, until queue is empty.
#
#   output: 1 2 3 4 5 6
tree = {
    "val": 1,
    "children": [
        {
            "val": 2,
            "children": [{"val": 4, "children": []}, {"val": 5, "children": []}],
        },
        {"val": 3, "children": [{"val": 6, "children": []}]},
    ],
}
queue = deque([tree])
while queue:
    print(queue)
    current_node = queue.popleft()
    print(current_node["val"])
    for child in current_node["children"]:
        queue.append(child)
print(queue)
# 95. Use deque to implement a "sliding window" of size 3 over numbers.
#     Print each window as you slide.
#
#   output: deque([4, 8, 15], maxlen=3)
#           deque([8, 15, 16], maxlen=3)
#           deque([15, 16, 23], maxlen=3)
#           ...
queue = deque(maxlen=3)
for n in numbers:
    queue.append(n)
    if len(queue) == 3:
        print(queue)


# =============================================================================
# SECTION H — MIXED CHALLENGE (96–99)
# =============================================================================

# 96. Given a list of orders, build a dict mapping each userId to a list
#     of their order totals using only list/dict operations (no defaultdict).
#     Hint: check if key exists first, then append.
#
#   output: {1: [240, 60], 2: [125, 190], 3: [255], ...}

result = {}
for o in orders:
    result.setdefault(o["userId"], []).append(o["total"])
print(result)
# 97. Find the top 3 most expensive products per category.
#     Build a dict: {category: [sorted product names by price desc, top 3]}
#     Use list comprehensions and sorted().
#
#   output: {'weapon': ['Dragon Bow', 'War Axe', 'Iron Sword'],
#            'armor': ['Elven Cloak', 'Steel Shield', 'Leather Armor'],
#            'potion': ['Mana Potion', 'Health Potion']}
result = {}
for p in products:
    result.setdefault(p["category"], []).append(p["name"])
print(result)

# 98. Use a stack to validate this list of bracket pairs:
#     tests = ["()[]{}", "([)]", "{[]}"]
#     Rules: (, [, { push — ), ], } pop and check match.
#     Print True/False for each.
#
#   output: True
#           False
#           True
tests = ["()[]{}", "([)]", "{[]}"]

for item in tests:
    stack = []
    is_valid = True
    for c in item:
        if c in ["(", "[", "{"]:
            stack.append(c)
        else:
            if not stack:
                is_valid = False
                break
            top = stack.pop()
            match c:
                case ")":
                    if top != "(":
                        is_valid = False
                        break
                case "]":
                    if top != "[":
                        is_valid = False
                        break
                case "}":
                    if top != "{":
                        is_valid = False
                        break
    print(item, is_valid)

# 99. Use a set to find users who have ordered from at least 2 different categories.
#     Hint: for each user, collect the set of categories they've ordered.
#           Keep users where len(their category set) >= 2.
#
#   output: ['Alice', 'Bob', 'David']
orders_uid_pids = {}
user_lookup = {u["id"]: u["name"] for u in users}
product_lookup = {p["id"]: p["category"] for p in products}
for o in orders:
    orders_uid_pids.setdefault(user_lookup.get(o["userId"]), []).append(
        product_lookup.get(o["productId"])
    )
print([u_name for u_name, cats in orders_uid_pids.items() if len(set(cats)) >= 2])

# =============================================================================
# BOSS DRILL (100)
# =============================================================================

# 100. BOSS — Order Fulfilment System
#
#      Build a complete order fulfilment simulation using a queue and stack.
#
#      SETUP:
#        pending_queue  — deque of all pending orders (enqueue them)
#        processing     — plain list acting as a stack (max 3 at a time)
#        completed      — plain list of finished orders
#
#      RULES:
#        1. While pending_queue is not empty:
#             - If processing stack has < 3 items: dequeue from pending, push to processing
#             - If processing stack has 3 items: pop all 3, mark as completed, repeat
#        2. After queue is empty, process remaining items in the stack.
#        3. For each completed order, print:
#           "Completed: Order #{id} for {user_name} — ${total}"
#           (look up user_name from users by userId)
#        4. Print total revenue of completed orders at the end.
#
#      output: Completed: Order #2 for Bob — $125
#              Completed: Order #6 for Eve — $100
#              Completed: Order #8 for Frank — $120
#              ...
#              Total revenue: $...
pending_queue = deque([o for o in orders if o["status"] == "pending"])
processing = deque()
completed = []
get_order_id = lambda x: x["id"]
complete_format = lambda x: (
    f"Completed: Order #{x['id']} for {user_lookup.get(x['userId'])} - ${x['total']}"
)
revenue = lambda arr: reduce(lambda acc, x: acc + x["total"], arr, 0)
while pending_queue:
    if len(processing) < 3:
        current_queue = pending_queue.popleft()
        print(f"Submitted to Process Order #{get_order_id(current_queue)}")
        processing.append(current_queue)
        print(f"Order to Process {len(processing)}/3")
    if len(processing) == 3:
        print("Completed 3/3 Orders to Process")
        print(f"Orders #: {list(get_order_id(o) for o in processing)}\nProcessing...")
        while processing:
            done_order = processing.pop()
            print(complete_format(done_order))
            completed.append(done_order)
while processing:
    done_order = processing.pop()
    print(complete_format(done_order))
    completed.append(done_order)
print(f"Total revenue: ${revenue(completed)}")
