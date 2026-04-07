import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import users


class User:
    def __init__(self, id, name, age, role, salary, is_active):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role
        self.is_active = is_active
        self.status = "Active" if is_active else "Inactive"

    def show_info(self):
        print(
            f"ID: {self.id}\nName: {self.name}\nAge: {self.age}\nRole: {self.role}\nSalary: {self.salary}\nStatus: {self.status}"
        )

    def __str__(self):

        return f"{self.name:^5} {f'({self.role})':^11} | ${self.salary:^5} | {self.age:^2} yrs old | {self.status}"

    def is_admin(self):
        return self.role == "admin"

    def is_active_user(self):
        return self.is_active

    def get_salary_category(self):
        return (
            "High"
            if self.salary >= 70000
            else ("Mid" if self.salary >= 40000 else "Low")
        )


def main():
    user_list = {
        u["id"]: User(
            u["id"], u["name"], u["age"], u["role"], u["salary"], u["isActive"]
        )
        for u in users
    }
    choice = None

    def get_filtered_users_by_role(key, value):
        return list(
            filter(lambda user: getattr(user, key) == value, user_list.values())
        )

    def get_filtered_by_salary(min, max):
        return list(filter(lambda user: min < getattr(user, "salary") < max))

    while choice != 0:
        os.system("cls")
        print(
            "=== USER MANAGEMENT SYSTEM ===\n1.  List all users\n2.  Search user by ID\n3.  Filter users by role\n4.  Filter by salary range\n5.  Show statistics\n6.  Add new user\n7.  Update user salary\n8.  Delete user\n9.  Find top earner\n10. Find users by salary bracket\n0.  Exit"
        )
        try:
            choice = int(input("Choose: "))
            match choice:
                case 1:
                    print("==================================================")
                    print(f"Total Users = {len(user_list)}")
                    print("==================================================")
                    for user in user_list.values():
                        print(user)
                case 2:
                    try:
                        id_query = int(input("User Id: "))
                        print("==================================================")
                        user_list[id_query].show_info()
                        print("==================================================")
                    except ValueError:
                        print("Error: Input invalid")
                case 3:
                    role_query = str(input("Filter Role: "))
                    filtered_users = get_filtered_users_by_role("role", role_query)
                    print(f"Found {len(filtered_users)} {role_query}(s):")
                    for user in filtered_users:
                        print(f"- {user.name}: ${user.salary:,}")
                case 4:
                    min_salary = float(input("Enter minimum salary: "))
                    max_salary = float(input("Enter maximum salary: "))
                    filtered_users = get_filtered_by_salary(min_salary, max_salary)
        except ValueError:
            print("Error: Input invalid")

        if choice != 0:
            input("Press any key to continue...")


print(*users[0])
main()
