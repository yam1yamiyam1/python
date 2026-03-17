import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import numbers, orders, products, students, users

# =============================================================================
# DRILL 01 — VARIABLES, DATA TYPES, TYPE CONVERSION
# =============================================================================
# HOW TO RUN:  python drill-01-variables.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              No skipping — do them in order.
# =============================================================================

# NEW SYNTAX REFERENCE
# --------------------
# Declaration       x = 10                  # no const/let — just assign
# Types             int  float  str  bool  None
# Check type        type(x)
# Convert to int    int("42")   int(3.9)    # truncates → 3
# Convert to float  float("3.14")  float(5) # → 5.0
# Convert to str    str(100)    str(True)
# Convert to bool   bool(0)     bool("")    bool(None)  # all False
#                   bool(1)     bool("hi")              # all True
# Multiple assign   a, b, c = 1, 2, 3
# Swap              a, b = b, a
# f-string          f"Hello {name}, you are {age}"
# Multiline str     """line1\nline2"""
# None check        x is None   /   x is not None
# JS →  Python      typeof x    →   type(x)
#                   null        →   None
#                   undefined   →   (doesn't exist in Python)
#                   ===         →   ==  (Python never coerces types)


# =============================================================================
# SECTION A — DECLARING & PRINTING VARIABLES (1–15)
# =============================================================================

# 1. Create a variable `score` with value 100. Print it.
score = 100
print(score)
# 2. Create `pi` with value 3.14159. Print it.
pi = 3.14159
print(pi)
# 3. Create `username` with value "player_one". Print it.
username = "player_one"
print(username)
# 4. Create `is_online` with value True. Print it.
is_online = True
print(is_online)
# 5. Create `nothing` with value None. Print it.
nothing = None
print(nothing)

# 6. Print the TYPE of each variable you made in drills 1–5.
#    Expected output shape:  <class 'int'>  <class 'float'>  etc.
print(type(score))
print(type(pi))
print(type(username))
print(type(is_online))
print(type(nothing))

# 7. Create three variables in ONE line: x = 5, y = 10, z = 15. Print all three.
#    Syntax: a, b, c = 1, 2, 3
x, y, z = 5, 10, 15
print(x)
print(y)
print(z)

# 8. Assign the same value 0 to three variables: hp, mp, xp. Print them.
#    Syntax: a = b = c = 0
a = b = c = 0
print(a)
print(b)
print(c)

# 9. Swap the values of x and y (from drill 7) WITHOUT a temp variable.
#    Print both after the swap.
#    Syntax: a, b = b, a
print(x)
print(y)
x, y = y, x
print(x)
print(y)

# 10. Create a variable `level` = 1. Reassign it to 99. Print both steps.
level = 1
level = 99
print(level)

# 11. Print every user's "name" field using a for loop.
#     (This is a variable access drill — notice dict key access syntax.)
#     Syntax: user["name"]   ←  NOT user.name (Python dicts use brackets)
for user in users:
    print(user["name"])

# 12. Print every product's "price" field.
for product in products:
    print(product["price"])

# 13. Print every order's "total" field.
for order in orders:
    print(order["total"])

# 14. Create a variable `first_user` pointing to users[0]. Print its "name".
first_user = users[0]
print(first_user["name"])

# 15. Create `last_product` pointing to the last product WITHOUT using index -1.
#     Use len(). Print its "name".
#     Syntax: collection[len(collection) - 1]
last_product = products[len(products) - 1]
print(last_product["name"])
# =============================================================================
# SECTION B — TYPE CHECKING (16–25)
# =============================================================================

# 16. Print the type of users[0]["salary"]. What is it?
print(type(users[0]["salary"]))

# 17. Print the type of users[0]["isActive"]. What is it?
print(type(users[0]["isActive"]))


# 18. Print the type of users[0]["name"]. What is it?
print(type(users[0]["name"]))


# 19. Print the type of None.
print(type(None))

# 20. Print the type of 3.14.
print(type(3.14))


# 21. Print the type of users[0] itself (the whole dict).
print(type(users[0]))

# 22. Print the type of users (the whole list).
print(type(users))


# 23. Print the type of numbers[0].
print(type(numbers[0]))

# 24. Check if users[0]["salary"] is an int using isinstance().
#     Print True or False.
#     Syntax: isinstance(value, int)
print(isinstance(users[0]["salary"], int))

# 25. Check if users[0]["name"] is a str using isinstance(). Print result.

print(isinstance(users[0]["name"], str))
# =============================================================================
# SECTION C — TYPE CONVERSION (26–50)
# =============================================================================

# 26. Convert the string "500" to an integer. Print it and its type.
x = "500"
print(x)
print(type(int(x)))
# 27. Convert the integer 42 to a string. Print it and its type.
x = 42
print(x)
print(type(str(x)))

# 28. Convert the string "9.99" to a float. Print it and its type.
x = "9.99"
x = float(x)
print(x)
print(type(float(x)))

# 29. Convert the float 7.8 to an int. Print it. What happens to the decimal?
#     Note: int() truncates, does NOT round.
x = 7.8
print(int(x))

# 30. Convert the integer 1 to bool. Print it. Then convert 0 to bool. Print it.
x = 1
print(bool(x))

# 31. Convert the string "" (empty) to bool. Print it.
#     Then convert "hello" to bool. Print it.
x = ""
print(bool(x))
x = "hello"
print(bool(x))
# 32. Convert None to bool. Print it.
print(bool(None))

# 33. Convert the list [] (empty) to bool. Print it.
#     Then convert [1, 2, 3] to bool. Print it.
x = []
print(bool(x))
x = [1, 2, 3]
print(bool(x))

# 34. Every user salary is currently an int.
#     Convert users[0]["salary"] to a float. Print it.
print(float(users[0]["salary"]))

# 35. Every user's "isActive" is a bool.
#     Convert users[0]["isActive"] to an int. Print it. (True → 1, False → 0)
print(int(users[0]["isActive"]))

# 36. Convert users[0]["salary"] to a string, then concatenate it into:
#     "Salary: 72000". Print it.
#     Note: you CANNOT do "Salary: " + 72000 in Python — types don't coerce.
x = users[0]["salary"]
print(f"Salary: {x}")

# 37. The string "123abc" cannot be converted to int — it will raise a ValueError.
#     Wrap int("123abc") in a try/except and print "Cannot convert" if it fails.
#     Syntax:
#       try:
#           result = int("123abc")
#       except ValueError:
#           print("Cannot convert")

try:
    result = int("123abc")
    print(result)
except ValueError:
    print("Cannot convert")
# 38. Convert every number in the `numbers` list to a float. Print the new list.
#     Use a for loop + append, not list comprehension yet.
y = []
for i in numbers:
    y = [*y, float(i)]
print(y)

# 39. Convert every user's salary to a string and collect into a list. Print it.
x = []
for i in users:
    x = [*x, str(i["salary"])]
print(x)

# 40. Convert every product's price to a string formatted as "$120". Print list.
#     Syntax: f"${price}"
x = []
for i in products:
    x = [*x, f"${i['price']}"]
print(x)
# 41. Convert "True" (a string) to a real bool.
#     Note: bool("True") does NOT give you True — it gives True because non-empty string.
#     bool("False") also gives True — be careful.
#     The correct way: "True" == "True"   or   use a manual check.
#     Print the result of: "True" == "True"  and  "False" == "True"

x = "True"
y = "False"
print(x == "True")
print(y == "True")
# 42. Convert every order total to a float. Print results.
for i in orders:
    print(float(i["total"]))

# 43. Add up all numbers in `numbers` by converting each to float first.
#     Print the total.
x = 0
for n in numbers:
    x += float(n)
print(x)

# 44. Convert users[0]["age"] to float, add 0.5, convert back to int. Print it.
x = float(users[0]["age"]) + 0.5
print(int(x))
# 45. Build a string sentence for each user:
#     "Alice is 32 years old and earns 72000."
#     Use str() conversion (NOT f-strings — do it the manual concat way).
#     Syntax: "text" + str(value) + "text"
for user in users:
    name = user["name"]
    age = user["age"]
    salary = user["salary"]
    print(f"{name} is {age} years old and earns {salary}")

# =============================================================================
# SECTION D — F-STRINGS & STRING FORMATTING (46–65)
# =============================================================================

# 46. For each user, print:  "Name: Alice  |  Age: 32"
#     Use f-strings.
for user in users:
    name = user["name"]
    age = user["age"]
    print(f"Name: {name} | Age: {age}")

# 47. For each product, print:  "Iron Sword costs $120.00"
#     Format the price to 2 decimal places.
#     Syntax: f"{price:.2f}"

for p in products:
    name = p["name"]
    price = float(p["price"])
    print(f"{name} costs ${price:.2f}")
# 48. For each order, print:  "Order #1 — Total: $240"
for o in orders:
    id = o["id"]
    total = o["total"]
    print(f"Order #{id} - ${total}")

# 49. For each student, print their name in UPPERCASE.
#     Syntax: str.upper()
for s in students:
    name = str.upper(s["name"])
    print(name)

# 50. For each user, print their name padded to 10 characters (left-aligned).
#     Syntax: f"{name:<10}"   (< = left, > = right, ^ = center)
for user in users:
    name = user["name"]
    print(f"{name:<10}")

# 51. For each product, print price right-aligned in a field of 8 chars.
#     Syntax: f"{price:>8}"
for p in products:
    price = p["price"]
    print(f"{price:>8}")

# 52. Print "Hello, World!" using three different methods:
#     a) print with +
#     b) print with f-string
#     c) print with .format()
#     Syntax: "Hello, {}!".format("World")
x = "Hello,"
y = "World!"
print(x + " " + y)
print(f"{x} {y}")
print("Hello, {}!".format("World"))
# 53. Create a `template` string: "User {name} has salary {salary}."
#     Fill it using .format() for users[0].
#     Syntax: template.format(name="Alice", salary=72000)
template = "User {name} has salary {salary}."
user = users[0]
name = user["name"]
salary = user["salary"]
print(template.format(name=name, salary=salary))
# 54. For each user print their name centered in 20 characters using f-string.
for user in users:
    name = user["name"]
    print(f"{name:^20}")

# 55. Print the total of all order totals formatted as currency: "$1,085.00"
#     Syntax: f"{total:,.2f}"
for o in orders:
    total = o["total"]
    print(f"${total:,.2f}")

# 56. For each product, print:
#     "Iron Sword    | weapon   | $120.00 | In Stock: True"
#     Align name to 14 chars, category to 8 chars.
for p in products:
    name = p["name"]
    category = p["category"]
    price = p["price"]
    inStock = p["inStock"]
    print(f"{name:^14} | {category:^8} | ${price:^5} | In Stock: {inStock}")

# 57. Print a separator line of 40 dashes. Then print all user names.
#     Syntax: "-" * 40
print("-" * 40)
for u in users:
    name = u["name"]
    print(name)


# 58. For each student, print their grades joined with " | ".
#     Syntax: " | ".join(str(g) for g in grades)   ← just follow the pattern for now


# 59. Print the repr() of the string "hello\nworld".
#     Syntax: repr(x)  — shows escape characters literally instead of interpreting them


# 60. Print users[0]["name"] in title case, lower case, and upper case.
#     Syntax: str.title()  str.lower()  str.upper()


# =============================================================================
# SECTION E — NONE & TRUTHINESS (61–75)
# =============================================================================

# 61. Create a variable `result` = None. Check if it is None using `is None`. Print result.
#     Syntax: x is None   (use `is` not == for None checks)


# 62. Create `result` = 0. Check if it is None. Print result.


# 63. Print which of these are "truthy" and which are "falsy":
#     0, 1, "", "hello", None, [], [1], False, True
#     Use bool() on each.


# 64. For each user, print their name only if isActive is truthy.
#     Syntax: if user["isActive"]:   (no == True needed)


# 65. For each product, print its name only if inStock is falsy.
#     Syntax: if not product["inStock"]:


# 66. Create a variable `data` = None.
#     Print "No data" if it is None, else print the data.


# 67. Print how many users have a "truthy" isActive value.
#     Count using a for loop.


# 68. Print how many products have a "falsy" inStock value.


# 69. Create a variable `discount` = 0.
#     Print "No discount" if discount is falsy, else print the discount.


# 70. For each order, print "High value" if total > 200, else print "Normal".


# =============================================================================
# SECTION F — MULTIPLE ASSIGNMENT & SWAP (71–85)
# =============================================================================

# 71. Unpack users[0] values into separate variables:
#     id, name, age, role, salary, is_active = users[0].values()
#     Print each.
#     Syntax: a, b, c = iterable   (must match count exactly)


# 72. Unpack the first 3 numbers from `numbers` into a, b, c. Print them.


# 73. Unpack with a "rest" collector — get first number, last number, rest in middle.
#     Syntax: first, *middle, last = numbers
#     Print first, last, and middle.


# 74. Get just the first two users unpacked, collect the rest.
#     Syntax: u1, u2, *rest = users


# 75. Swap the price of products[0] and products[1] using tuple swap.
#     Print both prices before and after.


# 76. Unpack a student's grades into exactly 5 variables. Print each.
#     Pick students[0] which has 5 grades.


# 77. Create three variables from a string: first, second, third = "abc"
#     Python can unpack strings too. Print them.


# 78. Unpack the first order's values — id, userId, productId, quantity, total, status.
#     Print each with a label.


# 79. Create x = 10. Then do: y = x. Change x to 99.
#     Print both x and y. What happened to y?
#     Note: integers are immutable — y keeps its original value.


# 80. Create a = [1, 2, 3]. Then do: b = a. Append 4 to a.
#     Print both a and b. What happened?
#     Note: lists are mutable — b and a point to the SAME list. This is a key Python gotcha.


# =============================================================================
# SECTION G — MIXED CHALLENGE (81–100)
# =============================================================================

# 81. Print the full name + salary of every admin user.
#     Format: "Alice — $72000"


# 82. Count how many distinct types appear in this list:
#     mixed = [1, "hello", 3.14, True, None, 42, "world", False]
#     Hint: collect types in a list, then count unique ones.


# 83. Print "Alice is active" or "Alice is inactive" for every user.
#     Use f-string with the bool value of isActive.


# 84. Convert every student's grade list to a list of floats. Print results.


# 85. For each product, print:
#     - name as uppercase
#     - price as float
#     - inStock converted to int (1 or 0)


# 86. Build a list of strings: each item is "id:name" for every user.
#     Example: ["1:Alice", "2:Bob", ...]
#     Use str() conversion in a loop.


# 87. Print the type of every value inside users[0].
#     Loop through users[0].values() and print type(v) for each.
#     Syntax: dict.values()


# 88. Find the user whose salary is closest to 50000.
#     Hint: track a min_diff and best_user as you loop.
#     Syntax: abs(x)  for absolute value


# 89. Print every order where total, when converted to str, starts with "1".
#     Syntax: str(x).startswith("1")


# 90. Create a variable `summary` that is a multiline f-string summarizing:
#     - total number of users
#     - total number of products
#     - total number of orders
#     Print it.
#     Syntax:
#       summary = f"""
#       Users: {len(users)}
#       ...
#       """


# 91. For each user, determine their tax bracket based on salary:
#     > 80000 → "High"
#     > 50000 → "Mid"
#     else    → "Low"
#     Store each result as a string, print "Alice: High" etc.


# 92. Convert all user salaries to floats and print the average.
#     Do the sum manually with a for loop.


# 93. For each product, print whether its price is an integer or has decimals.
#     Hint: price % 1 == 0 means no decimals.
#     Syntax: x % 1   (modulo)


# 94. Build a string that lists all product names separated by ", ".
#     Do NOT use join() — manually build it in a loop.
#     Hint: handle the trailing comma carefully.


# 95. Print the name and type of every field in products[0].
#     Loop through products[0].items().
#     Syntax: for key, value in dict.items():


# 96. Check if all users have salaries above 30000.
#     Use a for loop and a flag variable `all_above = True`.
#     If any salary fails, set flag to False and break.
#     Print the flag.


# 97. Find and print the name of the youngest user without using min() or sort().


# 98. Build a dict where keys are user IDs and values are their names.
#     { 1: "Alice", 2: "Bob", ... }
#     Use a for loop.
#     Syntax: d = {}   then   d[key] = value


# 99. Print every user's name repeated salary//10000 times.
#     Example: Alice (72000 salary) → "Alice Alice Alice Alice Alice Alice Alice"
#     Syntax: "word " * n


# 100. BOSS DRILL
#      Build and print a "report" string for the entire dataset:
#      - Total users, active count, inactive count
#      - Total products, in-stock count, out-of-stock count
#      - Total orders, completed count, pending count
#      - Total revenue (sum of all order totals)
#      Format it neatly using a multiline f-string.
#      All values must be computed from the data — no hardcoding.
