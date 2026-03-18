import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import numbers, orders, products, students, users

# =============================================================================
# DRILL 02 — CONTROL FLOW
# Comparison operators, logical operators, if/elif/else,
# for, for..else, while, iterables, break, continue
# =============================================================================
# HOW TO RUN:  python drill-02-control-flow.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              No skipping — do them in order.
# =============================================================================

# NEW SYNTAX REFERENCE
# --------------------
# Comparison        ==  !=  >  <  >=  <=
# Identity          is  /  is not          (use for None checks)
# Membership        in  /  not in          (replaces .includes() in JS)
# Chained compare   10 <= x <= 50          (NO JS equivalent)
# Logical           and   or   not         (replaces && || !)
# if block          if condition:           (colon, NO parentheses needed, NO braces)
#                       body
#                   elif other:
#                       body
#                   else:
#                       body
# Ternary           value = x if condition else y    (JS: condition ? x : y)
# for loop          for item in iterable:
# enumerate         for i, item in enumerate(collection):
# enumerate offset  for i, item in enumerate(collection, start=1):
# zip               for a, b in zip(list1, list2):
# range             range(5)       → 0 1 2 3 4
#                   range(1, 6)    → 1 2 3 4 5
#                   range(0,10,2)  → 0 2 4 6 8  (step)
# for..else         else block runs ONLY if loop was never broken
# while             while condition:
# break             exits the loop immediately
# continue          skips to next iteration
# pass              does nothing — placeholder for empty blocks


# =============================================================================
# SECTION A — COMPARISON OPERATORS (1–15)
# =============================================================================

# 1. Print True if users[0]["age"] is greater than 30.


# 2. Print True if products[0]["price"] is exactly 120.


# 3. Print True if orders[0]["status"] is NOT equal to "pending".


# 4. Print True if students[0]["attendance"] is greater than or equal to 90.


# 5. Print True if numbers[0] is less than or equal to 5.


# 6. Use a CHAINED comparison to check if users[0]["age"] is between 25 and 40.
#    Syntax: 25 <= age <= 40


# 7. Use `in` to check if "admin" is in the list ["admin", "moderator"].
#    Print the result.
#    Syntax: value in collection


# 8. Use `not in` to check if users[0]["role"] is NOT in ["banned", "suspended"].
#    Print result.


# 9. Use `is` to check if a variable `x = None` is None. Print result.
#    Syntax: x is None   (not x == None)


# 10. Use `is not` to check if users[0]["name"] is not None. Print result.


# 11. Print True if users[0]["salary"] equals users[1]["salary"].


# 12. Print True if the number of users equals the number of orders.


# 13. For each user, print whether their age is between 25 and 35 (inclusive).
#     Format: "Alice: True"


# 14. For each product, print whether its price is NOT between 50 and 100.


# 15. For each order, print whether its total is greater than the average total.
#     Compute the average first using a loop (no built-ins like sum() or statistics).


# =============================================================================
# SECTION B — LOGICAL OPERATORS (16–30)
# =============================================================================

# 16. Print True if users[0] is active AND has salary above 60000.
#     Syntax: condition and condition


# 17. Print True if products[0] is inStock OR its price is under 50.


# 18. Print True if users[0] is NOT active.
#     Syntax: not value


# 19. Print True if users[0]["role"] is "admin" AND users[0]["isActive"] is True.


# 20. Print True if products[0]["price"] < 50 OR products[0]["price"] > 150.


# 21. For each user, print their name if they are active AND their salary > 50000.


# 22. For each product, print its name if it's inStock AND price < 100.


# 23. For each order, print its id if status is "pending" OR total > 200.


# 24. For each user, print their name if role is NOT "user".


# 25. For each student, print their name if attendance > 80 AND average grade > 80.
#     Compute average with sum() and len().
#     Syntax: sum(list) / len(list)


# 26. Print users whose salary is between 40000 and 70000 AND are active.


# 27. Print products that are inStock AND quantity > 5 AND price < 150.


# 28. Print orders that are NOT completed AND total > 100.


# 29. Use `or` with a default: get users[0]["nickname"] if it exists, else "no nickname".
#     Syntax: value = dict.get("key") or "default"
#     Note: dict.get("key") returns None if missing → None is falsy → "default" is used


# 30. For each user, print "Rich and active" / "Rich but inactive" / "Not rich" based on
#     salary > 60000 and isActive. Use nested if or logical operators.


# =============================================================================
# SECTION C — IF / ELIF / ELSE (31–50)
# =============================================================================

# 31. Print "High" / "Medium" / "Low" for each user's salary:
#     > 70000 → High,  > 45000 → Medium,  else → Low


# 32. Print a grade letter for each student's average grade:
#     >= 90 → A,  >= 80 → B,  >= 70 → C,  >= 60 → D,  else → F


# 33. Print a stock status for each product:
#     quantity > 10 → "Plenty",  quantity > 0 → "Low Stock",  else → "Out of Stock"


# 34. For each order, print shipping cost:
#     total > 200 → free ($0),  total > 100 → $5,  else → $10


# 35. For each user, print their access level:
#     role "admin" → "Full Access"
#     role "moderator" → "Partial Access"
#     role "user" → "Basic Access"
#     anything else → "No Access"


# 36. Use a TERNARY (one-liner if/else) to print "Adult" or "Minor" for each user.
#     Syntax: result = "Adult" if age >= 18 else "Minor"
for u in users:
    age = u["age"]
    print("Adult" if age >= 18 else "Minor")


# 37. For each product, use ternary to print "Available" or "Unavailable".
for p in products:
    inStock = p["inStock"]
    print("Available" if inStock else "Unavailable")

# 38. For each order, use ternary to label total as "Expensive" (>150) or "Cheap".
for o in orders:
    total = o["total"]
    print("Expensive" if total > 150 else "Cheap")
# 39. Print whether the number of active users is more, less, or equal to inactive users.
#     Compute both counts first.


# 40. For each student:
#     If attendance > 90 AND avg grade > 85 → "Star Student"
#     If attendance > 90 OR avg grade > 85  → "Good Student"
#     Else → "Needs Improvement"


# 41. For each user, build and print a "badge":
#     admin + active    → "🌟 Active Admin"
#     admin + inactive  → "😴 Inactive Admin"
#     not admin         → "👤 Regular User"


# 42. For each product, classify by both category and price:
#     weapon + price > 100 → "Premium Weapon"
#     weapon              → "Basic Weapon"
#     armor  + price > 80 → "Heavy Armor"
#     armor               → "Light Armor"
#     else                → "Consumable"


# 43. Nested if: for each order, print "VIP completed" if the user who placed it
#     has salary > 60000 AND the order is completed.
#     You'll need to find the user by userId.
#     Syntax: next((u for u in users if u["id"] == order["userId"]), None)
#     Or just use a for loop inside — either way is fine.


# 44. For each number in `numbers`, print:
#     divisible by both 2 and 3 → "FizzBuzz"
#     divisible by 2            → "Fizz"
#     divisible by 3            → "Buzz"
#     else                      → the number itself
#     Syntax: n % 2 == 0


# 45. Using only if/elif/else (no dict), map each order status to an emoji:
#     completed → ✅,  pending → ⏳,  shipped → 📦,  else → ❓


# 46. For each user, print their seniority based on age:
#     < 25 → "Junior",  25–35 → "Mid",  36–45 → "Senior",  > 45 → "Principal"
#     Use chained comparisons inside elif.


# 47. Print "Balanced dataset" if the number of products in each category is equal.
#     Otherwise print which category has the most. Compute counts with a for loop.


# 48. For each student, determine if they pass: avg grade >= 75 AND attendance >= 75.
#     Print "PASS" or "FAIL" with their name.


# 49. For each product, print a reorder alert:
#     quantity == 0 → "🚨 OUT OF STOCK"
#     quantity < 5  → "⚠️  Low — reorder soon"
#     else          → "✅ OK"


# 50. CHALLENGE: For each user, print their "profile tier":
#     Tier 1: admin + salary > 80000 + active
#     Tier 2: (admin OR moderator) + salary > 50000
#     Tier 3: active + salary > 40000
#     Tier 4: everything else


# =============================================================================
# SECTION D — FOR LOOPS & ITERABLES (51–70)
# =============================================================================

# 51. Print every number in `numbers` using a for loop.


# 52. Print every user's name using a for loop.


# 53. Print the index and name of every user using enumerate().
#     Format: "0 → Alice"
for i, u in enumerate(users):
    print(f"{i} → {u['name']}")

# 54. Print a 1-indexed list of all products.
#     Format: "1. Iron Sword"
#     Syntax: enumerate(collection, start=1)
my_list = [f"{i}. {p['name']}" for i, p in enumerate(products, start=1)]
print(my_list)

# 55. Use range() to print numbers 1 through 10.
#     Syntax: for i in range(1, 11):
for i in range(1, 11):
    print(i)

# 56. Use range() to print even numbers from 2 to 20.
#     Syntax: range(start, stop, step)
for i in range(2, 21, 2):
    print(i)


# 57. Use range() to count DOWN from 10 to 1.
#     Syntax: range(10, 0, -1)
for i in range(10, 0, -1):
    print(i)

# 58. Loop through users and products at the same time using zip().
#     Print: "Alice owns Iron Sword"
#     Syntax: for user, product in zip(users, products):
for u, p in zip(users, products):
    print(f"{u['name']} owns {p['name']}")

# 59. Build a list of all user names using a for loop + append.
#     Print the final list.
my_list = []
for u in users:
    my_list.append(u["name"])
print(my_list)
# 60. Build a list of all product prices doubled. Print it.


# 61. Build a list of ONLY active users' names. Print it.


# 62. Loop through orders. Build a list of totals above 100. Print it.


# 63. Use a for loop to print every character in the string "Python" one by one.
#     Note: strings are iterable in Python.


# 64. Use a for loop to print each key in users[0].
#     Syntax: for key in dictionary:


# 65. Use a for loop to print each value in users[0].
#     Syntax: for value in dictionary.values():


# 66. Use a for loop to print each key-value pair in users[0].
#     Format: "name → Alice"
#     Syntax: for key, value in dictionary.items():


# 67. Loop through students and print each student's highest grade.
#     Do NOT use max() — find it manually with a for loop inside the outer loop.


# 68. Loop through users. Print users whose name starts with a vowel.
#     Syntax: name[0] in "aeiouAEIOU"


# 69. Loop through numbers. Build a new list where each number is squared.
#     Print it.


# 70. Loop through all orders. For each order, print the order id and
#     the name of the user who placed it (look up by userId).
#     You'll need a nested loop or a lookup inside the loop.


# =============================================================================
# SECTION E — BREAK, CONTINUE, PASS (71–80)
# =============================================================================

# 71. Loop through products. BREAK when you find the first out-of-stock one.
#     Print its name before breaking.


# 72. Loop through users. CONTINUE past any inactive users.
#     Print only active users' names.


# 73. Loop through numbers. CONTINUE for any number < 10. Print the rest.


# 74. Loop through orders. Find the FIRST completed order. Break and print its id.


# 75. Loop through users. Count how many you loop through BEFORE finding the first admin.
#     Print the count. Use break after finding them.


# 76. Loop through products. Skip (continue) any product with price > 100.
#     Print names of remaining products.


# 77. Loop through students. Skip any student with attendance below 80.
#     For the rest, print name + average grade.


# 78. Use `pass` to create a for loop that does nothing but doesn't error.
#     Then print "Loop complete" after it.
#     Syntax: pass   (placeholder — like an empty block)


# 79. Loop through numbers. Accumulate a sum. BREAK once the sum exceeds 50.
#     Print the final sum and which number caused the break.


# 80. Loop through orders. Skip orders with total < 100 (continue).
#     For remaining, print the order id and total.


# =============================================================================
# SECTION F — FOR..ELSE (81–88)
# =============================================================================
# KEY CONCEPT: else on a for loop runs ONLY if the loop finished WITHOUT break.
# This has NO equivalent in JavaScript.

# 81. Search users for role "superadmin".
#     Found → print "Found: {name}" and break.
#     Not found → the else block prints "No superadmin."
for u in users:
    if u["role"] == "superadmin":
        print(f"Found: {u['name']}")
        break
else:
    print("No superadmin.")

# 82. Search products for a price above 500.
#     Found → print "Expensive product: {name}".
#     Not found → else prints "All products under $500."
for p in products:
    if p["price"] > 500:
        print(f"Expensive product: {p['name']}")
        break
else:
    print("All products under $500")

# 83. Search orders for total above 1000.
#     Use for..else.
for o in orders:
    if o["total"] > 1000:
        print(f"Order Id: {o['id']}")
        break
else:
    print("No order above $1000")

# 84. Search students for an average grade above 99.
#     Use for..else.
for s in students:
    total_grades = 0
    grades = s["grades"]
    for g in grades:
        total_grades += g
    average_grade = total_grades / len(grades)
    if average_grade > 99:
        print(f"Name: {s['name']}")
        break
else:
    print("No student has higher grade than 99")

# 85. Search users for an inactive admin.
#     (isActive == False AND role == "admin")
#     Use for..else.
for u in users:
    if not u["isActive"] and u["role"] == "admin":
        print(f"Inactive Admin: {u['name']}")
        break
else:
    print("There is no inactive admin.")

# 86. Search products for a product named exactly "Magic Staff".
#     Use for..else.
for p in products:
    if p["name"] == "Magic Staff":
        print(f"{p['name']} found")
        break
else:
    print("No Magic Staff found.")

# 87. Search numbers for any number divisible by 7.
#     Found → print it and break.
#     Else → "None divisible by 7."
for i in numbers:
    if i % 7 == 0:
        print(f"{i} is the first divisible by 7")
        break
else:
    print("None divisible by 7.")

# 88. Search orders for a "shipped" order with total > 300.
#     Use for..else.
for o in orders:
    if o["status"] == "shipped" and o["total"] > 300:
        print(f"OrderId: {o['id']} has been shipped with a total greater than 300")
        break
else:
    print("No order with a total greater than 100 is shipped")

# =============================================================================
# SECTION G — WHILE LOOPS (89–96)
# =============================================================================

# 89. Print numbers 1 to 5 using a while loop.
count = 0
while count < 5:
    count += 1
    print(count)


# 90. Start at 100. Keep subtracting 13 until the value goes below 0.
#     Print each value. Count how many subtractions it took.
value = 100
sub_count = 0
while value > 0:
    value -= 13
    sub_count += 1
    if value > 0:
        print(value)
print(sub_count)
# 91. Use a while loop to walk through all users and print their names.
#     Use an index variable `i = 0`.
i = 0
while i < len(users):
    print(users[i]["name"])
    i += 1

# 92. Use a while loop to find the first product with price below 30.
#     Print its name and break.
i = 0
while i < len(products):
    if products[i]["price"] < 30:
        print(f"{products[i]['name']} - {products[i]['price']}")
        break
    i += 1
else:
    print("No product priced below 30")


# 93. Simulate a game loop: start with hp = 100.
#     Each iteration subtract a random damage between 10 and 20.
#     Print hp after each hit. Stop when hp <= 0. Print "Dead!"
#     Syntax: import random   then   random.randint(10, 20)
hp = 100
while hp > 0:
    hp -= random.randint(10, 20)
    if hp <= 0:
        print("Dead!")
    else:
        print(hp)


# 94. Use a while loop to count how many orders have totals above 150.
#     Stop as soon as you've counted 3 such orders. Print the count.
threshold = 150
above_count = 0
i = 0
while i < len(orders):
    if orders[i]["total"] > threshold:
        above_count += 1
        if above_count == 3:
            break
    i += 1
print(above_count)


# 95. Walk through `numbers` with a while loop. Accumulate a product (multiply).
#     Print the running product after each step.
i = 0
num_products = 1
while i < len(numbers):
    num_products *= numbers[i]
    print(num_products)
    i += 1

# 96. Use a while loop + index to print every other user (0, 2, 4...).
#     Syntax: i += 2
i = 0
while i < len(users):
    print(users[i])
    i += 2

# =============================================================================
# SECTION H — MIXED CHALLENGE (97–100)
# =============================================================================

# 97. Loop through all users.
#     For each user, loop through all orders to find their orders.
#     Print: "Alice has 2 orders totalling $300"
#     Compute total per user by accumulating inside the inner loop.
for u in users:
    total = 0
    order_count = 0
    for o in orders:
        if u["id"] == o["userId"]:
            total += o["total"]
            order_count += 1
    print(f"{u['name']:^5} has {order_count} orders totalling ${total}")


# 98. FizzBuzz 1–30 using a while loop (not for).
#     Divisible by 3 AND 5 → "FizzBuzz"
#     Divisible by 3       → "Fizz"
#     Divisible by 5       → "Buzz"
#     Else                 → the number

i = 1
while i <= 30:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1

# 99. Loop through products. Build TWO lists in one pass:
#     `cheap` → price < 100
#     `expensive` → price >= 100
#     Print both lists at the end.

cheap = [p["name"] for p in products if p["price"] < 100]
expensive = [p["name"] for p in products if p["price"] >= 100]
print(cheap)
print(expensive)

# 100. BOSS DRILL
#      Loop through all users (outer loop).
#      For each user, loop through all orders (inner loop).
#      For each order belonging to the user, look up the product by productId.
#      Build and print a summary:
#      "Alice:
#         - Iron Sword x2 ($240) — completed
#         - Leather Armor x1 ($60) — completed"
#      Use for..else on the inner loop to print "  No orders." if the user
#      had no orders at all.
for user in users:
    user_order = []

    print(f"{user['name']}:")

    for order in orders:
        if user["id"] == order["userId"]:
            for product in products:
                if order["productId"] == product["id"]:
                    orderAdd = {
                        "id": order["id"],
                        "product_name": product["name"],
                        "quantity": order["quantity"],
                        "total": order["total"],
                        "status": order["status"],
                    }
                    user_order.append(orderAdd)

    if not user_order:
        print("  No order")
    else:
        for i in user_order:
            print(
                f"  - {i['product_name']} x{i['quantity']} (${i['total']}) - {i['status']}"
            )
