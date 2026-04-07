# started 10:02am
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import products, users


def add_all(*nums):
    print(sum(nums))


add_all(1, 2, 3)


def greet(*names):
    for name in names:
        print(f"Hello {name}")


greet("Yuan")
greet("A", "B", "Yuan")


def describe(**info):
    for k, v in info.items():
        print(f"{k}:{v}")


describe(name="Alice", age=32, role="admin")


def mixed(required, *args, **kwargs):
    print(required)
    print(args)
    print(kwargs)


mixed("hello", 1, 2, 3, x=10, y=20)

nums = [1, 2, 3]
add_all(*nums)


def create_user(name, **fields):
    print({"name": name} | fields)


create_user(name="Alice", age=32, role="admin")

try:
    int("abc")
except ValueError as e:
    print(e)
else:
    print("Success")
finally:
    print("Done")

try:
    int("42")
except ValueError as e:
    print(e)
else:
    print("Success")
finally:
    print("Done")

user_lookup = {user["id"]: user for user in users}


def get_user(id):
    user = user_lookup.get(id)
    if user is None:
        raise ValueError(f"User {id} not found")
    return user


try:
    print(get_user(1))  # works
    print(get_user(99))  # raises
except ValueError as e:
    print(e)

##i dont have items data

print(list(sorted(users, key=lambda x: -x["age"])))

print(list(filter(lambda x: x["isActive"], users)))

print(list(map(lambda x: x["name"], users)))

key = lambda x: x["price"]
print(list(sorted(products, key=key)))
print(list(sorted(products, key=key, reverse=True)))
print(
    list(
        map(
            lambda x: x["name"],
            sorted(filter(lambda x: x["isActive"], users), key=lambda x: -x["salary"]),
        )
    )
)
