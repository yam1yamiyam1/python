import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import users


class User:
    def __init__(self, name, age, role, **rest):
        self.name = name
        self.age = age
        self.role = role

    def greet(self):
        print(f"Hi, I'm {self.name} and I'm an {self.role}.")

    def __str__(self):
        return f"User({self.name}, {self.age}, {self.role})"

    def is_senior(self):
        return self.age >= 35

    def to_dict(self):
        return {"name": self.name, "age": self.age, "role": self.role}

    @property
    def display_name(self):
        return self.name.upper()


alice = User("Alice", 32, "admin")
bob = User("Bob", 24, "user")

print(alice.name, alice.age)
print(bob.name, bob.age)
alice.greet()
print(alice)
user_objects = [User(**u) for u in users]
for u in user_objects:
    print(u)

for u in user_objects:
    if u.is_senior():
        print(u.name)


class AdminUser(User):
    def __init__(self, name, age, permissions, **rest):
        super().__init__(name, age, role="admin", **rest)
        self.permissions = permissions

    def can(self, action):
        return action in self.permissions


admin = AdminUser(**users[5], permissions=["read", "write", "delete"])
admin.greet()  # inherited from User
print(admin.can("delete"))  # True
print(admin.can("ban"))
print(admin.to_dict())
print(bob.to_dict())
print(admin.display_name)
print(alice.display_name)
print(bob.display_name)
