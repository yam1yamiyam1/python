1  # ============================================================================
# DRILL 07: OOP COMPACT CLASS-DIAGRAM CHECKLIST (EX1-EX100)
# ============================================================================
# Format:
# ClassName:
# - Attributes...
# - Functions (signature: brief desc -> sample outcome)
# ============================================================================


# ============================================================================
# 1) Car (EX1-EX20)
# ============================================================================
# Car:
# - Class Attributes:
#   - car_count: int
# - Instance Attributes:
#   - brand:str, model:str, year:int, color:str, index:int, features:list[str]
# - Functions:
#   - __init__(self, brand, model, year, color, features=None): initialize object -> Car("Toyota","Camry",2025,"Red")
#   - get_brand(self): return brand -> "Toyota"
#   - set_brand(self, new_brand): update brand -> brand becomes "BMW"
#   - describe(self): brand + model -> "BMW Camry"
#   - get_specs(self): full one-line specs -> "BMW Camry 2025 - Red"
#   - __str__(self): user-friendly print -> "BMW Camry 2025 - Red"
#   - info(self): indexed label -> "Car #1: BMW Camry"
#   - __repr__(self): debug text -> "Car(BMW,Camry)"
#   - total_created(cls) [classmethod]: return car_count -> 2
#   - reset_count(cls) [classmethod]: reset counter -> 0
#   - brand_is_premium(brand) [staticmethod]: premium check -> True (for "BMW")
#   - from_string(cls, s) [classmethod]: alt constructor -> Car from "Honda,Civic,2024,Blue"
#   - add_feature(self, feature_name): append feature -> features includes "GPS"
#   - has_feature(self, feature_name): membership check -> True
#   - remove_feature(self, feature_name): remove one feature -> "GPS" removed
#   - clear_features(self): remove all features -> []
#   - feature_count(self): count features -> 0 / 1 / n
class Car:
    car_count = 0

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.features = []
        Car.car_count += 1
        self.index = Car.car_count

    def get_brand(self):
        return self.brand

    def set_brand(self, new_brand):
        self.brand = new_brand

    def describe(self):
        return f"{self.brand} {self.model}"

    def get_specs(self):
        return f"{self.describe()} {self.year} - {self.color}"

    def __str__(self):
        return self.get_specs()

    def info(self):
        return f"Car #{self.index}: {self.brand} {self.model}"

    def __repr__(self):
        return f"Car{tuple(f'{k}={v}' for k, v in self.__dict__.items() if v and k != 'index')}"

    def add_feature(self, feature_name):
        self.features.append(feature_name)

    def has_feature(self, feature_name):
        return feature_name in self.features

    def remove_feature(self, feature_name):
        try:
            self.features.remove(feature_name)
        except ValueError as e:
            print(f"{feature_name} {e}")

    def clear_features(self):
        self.features = []

    def feature_count(self):
        return len(self.features)

    @classmethod
    def total_created(cls):
        return cls.car_count

    @classmethod
    def reset_count(cls):
        cls.car_count = 0

    @classmethod
    def from_string(cls, s):
        return cls(*s.split(","))

    @staticmethod
    def brand_is_premium(brand):
        return brand in ["BMW", "Mercedes", "Audi", "Lexus"]


# ==========================================
# TEST SCRIPT FOR CAR CLASS
# ==========================================

print("--- 1. Class Initialization ---")
print(f"Total created initially: {Car.total_created()}")  # Should be 0

print("\n--- 2. Creating an Instance & Basic Methods ---")
c1 = Car("Toyota", "Camry", 2025, "Red")
print(f"Brand initially: {c1.get_brand()}")
c1.set_brand("BMW")
print(f"Brand after set_brand: {c1.get_brand()}")
print(f"Describe: {c1.describe()}")
print(f"Specs: {c1.get_specs()}")
print(f"Info: {c1.info()}")

print("\n--- 3. Dunder Methods (__str__ and __repr__) ---")
# print(c1) automatically calls c1.__str__()
print(f"__str__ output: {c1}")
# Notice features are empty, so they are filtered out in your __repr__
print(f"__repr__ output: {repr(c1)}")

print("\n--- 4. Feature Management ---")
c1.add_feature("GPS")
c1.add_feature("Sunroof")
print(f"Features count: {c1.feature_count()}")
print(f"Has GPS? {c1.has_feature('GPS')}")
print(f"Has Leather Seats? {c1.has_feature('Leather Seats')}")

# Look at __repr__ again now that features are NOT empty!
print(f"__repr__ with features: {repr(c1)}")

c1.remove_feature("GPS")
print(f"Feature count after removing GPS: {c1.feature_count()}")
print("Attempting to remove a feature that doesn't exist:")
c1.remove_feature("Heated Seats")  # This will trigger your except block!

c1.clear_features()
print(f"Features after clear_features(): {c1.features}")

print("\n--- 5. Class Methods (@classmethod) ---")
# Create a second car using your custom string constructor
c2 = Car.from_string("Honda,Civic,2024,Blue")
print(f"Created from string: {c2}")
print(f"c2 Info: {c2.info()}")  # Notice index is 2!

print("\n--- 6. Static Methods (@staticmethod) ---")
print(f"Is BMW premium? {Car.brand_is_premium('BMW')}")
print(f"Is Honda premium? {Car.brand_is_premium('Honda')}")

print("\n--- 7. Class State & Reset ---")
print(f"Total cars created now: {Car.total_created()}")  # Should be 2
Car.reset_count()
print(f"Total cars after reset_count(): {Car.total_created()}")  # Should be 0


# ============================================================================
# 2) Person + NameList (EX21-EX26)
# ============================================================================
# Person:
# - Attributes: name:str, age:int
# - Functions:
#   - __init__(self, name, age): set fields -> Person("Alice",30)
#   - __str__(self): readable text -> "Alice (30)"
#   - __repr__(self): debug text -> "Person('Alice', 30)"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"

    def __repr__(self):
        return f"Person{tuple(f'{k}={v}' for k, v in self.__dict__.items())}"


p = Person("Alice", 30)

print("--- Testing __str__ ---")
print(p)  # This automatically calls __str__
print(str(p))  # This also calls __str__

print("\n--- Testing __repr__ ---")
print(repr(p))  # This calls __repr__


# NameList:
# - Attributes: names:list[str]
# - Functions:
#   - __init__(self, names): store list -> ["Alice","Bob","Charlie"]
#   - __len__(self): list size -> 3
#   - __repr__(self): debug text -> "NameList(['Alice','Bob','Charlie'])"
class NameList:
    def __init__(self, names):
        self.names = names or []

    def __len__(self):
        return len(self.names)

    def __repr__(self):
        return f"NameList({self.names})"


# --- TEST SCRIPT ---

# 1. Test with a normal list
names = NameList(["Alice", "Bob", "Charlie"])
print("--- Normal List ---")
print(f"Object: {repr(names)}")  # Tests __repr__
print(f"Length: {len(names)}")  # Tests __len__

# 2. Test with an empty list
empty_names = NameList([])
print("\n--- Empty List ---")
print(f"Object: {repr(empty_names)}")
print(f"Length: {len(empty_names)}")

# 3. Test with None (your 'names or []' logic handles this beautifully!)
none_names = NameList(None)
print("\n--- None Input ---")
print(f"Object: {repr(none_names)}")
print(f"Length: {len(none_names)}")
# ============================================================================
# 3) CustomList (EX27-EX32)
# ============================================================================
# CustomList:
# - Attributes: values:list
# - Functions:
#   - __init__(self, values): set storage -> [1,2,3]
#   - __getitem__(self, index_key): index access -> cl[1] == 2
#   - __setitem__(self, index_key, new_value): index assign -> cl[1] = 99
#   - __contains__(self, queried_value): in-check -> (99 in cl) == True
#   - __len__(self): length -> 3


class CustomList:
    def __init__(self, values):
        self.storage = values or []

    def __getitem__(self, key):
        return self.storage[key]

    def __setitem__(self, key, value):
        self.storage[key] = value

    def __contains__(self, item):
        return item in self.storage

    def __len__(self):
        return len(self.storage)


# ==========================================
# TEST SCRIPT FOR CustomList
# ==========================================

print("--- 1. Initialization ---")
cl = CustomList([1, 2, 3])
print(f"Created CustomList with storage: {cl.storage}")

print("\n--- 2. Testing __getitem__ ---")
print(f"cl[1] == {cl[1]} (Expected: 2)")
print(f"cl[0] == {cl[0]} (Expected: 1)")

print("\n--- 3. Testing __setitem__ ---")
cl[1] = 99
print("Executed: cl[1] = 99")
print(f"cl[1] is now: {cl[1]} (Expected: 99)")
print(f"Full storage is now: {cl.storage}")

print("\n--- 4. Testing __contains__ ---")
print(f"Is 99 in cl? {99 in cl} (Expected: True)")
print(f"Is 5 in cl? {5 in cl} (Expected: False)")

print("\n--- 5. Testing __len__ ---")
print(f"len(cl) == {len(cl)} (Expected: 3)")

print("\n--- 6. Testing None fallback ---")
empty_cl = CustomList(None)
print(f"Empty list length: {len(empty_cl)} (Expected: 0)")


# ============================================================================
# 4) Vector (EX33-EX40)
# ============================================================================
# Vector:
# - Attributes: x:number, y:number
# - Functions:
#   - __init__(self, x, y): set coordinates -> Vector(1,2)
#   - __add__(self, other): vector add -> Vector(1,2)+Vector(3,4)=Vector(4,6)
#   - __sub__(self, other): vector subtract -> Vector(5,7)-Vector(2,3)=Vector(3,4)
#   - __mul__(self, scalar): scalar multiply -> Vector(2,3)*2=Vector(4,6)
#   - __str__(self): readable text -> "Vector(2, 3)"
#   - __eq__(self, other): equality by x,y -> True for same coords
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x, new_y)

    def __mul__(self, scalar):
        new_x = self.x * scalar
        new_y = self.y * scalar
        return Vector(new_x, new_y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):

        return (self.x, self.y) == (other.x, other.y)


# Create vectors based on the instructions
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(5, 7)

# Test addition
# Vector(1,2) + Vector(3,4) = Vector(4,6)
print(v1 + v2)

# Test subtraction
# Vector(5,7) - Vector(2,3) = Vector(3,4)
print(v3 - Vector(2, 3))

# Test multiplication
# Vector(2,3) * 2 = Vector(4,6)
print(Vector(2, 3) * 2)

# Test equality
# True for same coords
print(v1 == Vector(1, 2))
print(v1 == v2)


# ============================================================================
# 5) Student (EX41-EX48)
# ============================================================================
# Student:
# - Attributes: name:str, student_id:int|str, gpa:float
# - Functions:
#   - __init__(self, name, student_id, gpa): set fields -> Student("Alice",101,3.5)
#   - __eq__(self, other): equality by student_id -> True (101 == 101)
#   - __lt__(self, other): compare by gpa -> 2.5 < 3.5 is True
#   - __le__(self, other): <= by gpa -> True/False
#   - __gt__(self, other): > by gpa -> True/False
#   - __ge__(self, other): >= by gpa -> True/False
class Student:
    def __init__(self, name, student_id, gpa):
        self.name = name
        self.sid = student_id
        self.gpa = gpa

    def __eq__(self, other):
        return self.sid == other.sid

    def __lt__(self, other):
        return self.gpa < other.gpa

    def __le__(self, other):

        return self.gpa <= other.gpa

    def __gt__(self, other):
        return self.gpa > other.gpa

    def __ge__(self, other):
        return self.gpa >= other.gpa


s1 = Student("Alice", 101, 3.5)
s2 = Student("Bob", 102, 2.5)
s3 = Student("Charlie", 101, 3.8)  # Same ID as Alice
s4 = Student("Diana", 104, 3.5)  # Same GPA as Alice

print("--- Testing __eq__ (==) by ID ---")
print(f"s1 == s3 (ID 101 == 101): {s1 == s3}")  # Expected: True
print(f"s1 == s2 (ID 101 == 102): {s1 == s2}")  # Expected: False

print("\n--- Testing Math Comparisons by GPA ---")
print(f"s2 < s1  (2.5 < 3.5):  {s2 < s1}")  # __lt__ Expected: True
print(f"s1 > s2  (3.5 > 2.5):  {s1 > s2}")  # __gt__ Expected: True

print(f"s1 <= s4 (3.5 <= 3.5): {s1 <= s4}")  # __le__ Expected: True
print(f"s1 >= s4 (3.5 >= 3.5): {s1 >= s4}")  # __ge__ Expected: True

print("\n--- Bonus: Automatic Sorting! ---")
# Because you defined these methods, Python knows how to sort them automatically by GPA!
roster = [s1, s2, s3]
roster.sort()  # Sorts from lowest GPA to highest

print("Sorted by GPA:")
for student in roster:
    print(f"{student.name}: {student.gpa}")


# ============================================================================
# 6) Rectangle (EX49-EX56)
# ============================================================================
# Rectangle:
# - Attributes: _width:number, _height:number
# - Properties: width, height, area, perimeter
# - Functions/Properties:
#   - __init__(self, width, height): initialize -> Rectangle(4,5)
#   - width (getter): read width -> 4
#   - width (setter): validate >0 -> ValueError if -5
#   - height (getter/setter): validate >0 -> works like width
#   - area (property): compute width*height -> 20
#   - perimeter (property): compute 2*(w+h) -> 18
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width should be > 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height should be > 0")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def perimeter(self):
        return 2 * (self._width + self._height)


# ============================================================================
# BASIC USAGE - Creating and accessing properties
# ============================================================================

# Create a rectangle with width=4 and height=5
rect = Rectangle(4, 5)

print(f"Width: {rect.width}")  # Output: Width: 4
print(f"Height: {rect.height}")  # Output: Height: 5
print(f"Area: {rect.area}")  # Output: Area: 20
print(f"Perimeter: {rect.perimeter}")  # Output: Perimeter: 18


# ============================================================================
# MODIFYING PROPERTIES
# ============================================================================

# Change the width
rect.width = 6
print("\nAfter changing width to 6:")
print(f"Area: {rect.area}")  # Output: Area: 30
print(f"Perimeter: {rect.perimeter}")  # Output: Perimeter: 22

# Change the height
rect.height = 10
print("\nAfter changing height to 10:")
print(f"Area: {rect.area}")  # Output: Area: 60
print(f"Perimeter: {rect.perimeter}")  # Output: Perimeter: 32


# ============================================================================
# VALIDATION IN ACTION
# ============================================================================

# Try to set invalid width (negative value)
try:
    rect.width = -5
except ValueError as e:
    print(f"\nError: {e}")  # Output: Error: Width should be > 0

# Try to set invalid height (zero)
try:
    rect.height = 0
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Height should be > 0


# ============================================================================
# PRACTICAL EXAMPLES
# ============================================================================

# Example 1: Calculate area of a room (in meters)
room = Rectangle(5, 4)
print(f"\nRoom dimensions: {room.width}m x {room.height}m")
print(f"Room area: {room.area} square meters")

# Example 2: Calculate perimeter for painting a border
print(f"Border length needed: {room.perimeter} meters")

# Example 3: Working with floats (e.g., actual room dimensions)
office = Rectangle(3.5, 4.2)
print(f"\nOffice area: {office.area:.2f} square meters")
print(f"Office perimeter: {office.perimeter:.2f} meters")

# Example 4: Resizing a rectangle
drawing = Rectangle(10, 8)
print(f"\nOriginal drawing: {drawing.width}x{drawing.height}, Area: {drawing.area}")

drawing.width = 12
print(f"After resizing width: {drawing.width}x{drawing.height}, Area: {drawing.area}")


# ============================================================================
# 7) Date (EX57-EX62)
# ============================================================================
# Date:
# - Attributes: day:int, month:int, year:int
# - Functions:
#   - __init__(self, day, month, year): set date -> Date(25,12,2023)
#   - is_leap_year(year) [staticmethod]: leap check -> True for 2024
#   - validate_date(day, month, year) [staticmethod]: date validity -> True for 29/2/2024
#   - from_string(cls, s) [classmethod]: parse "dd/mm/yyyy" -> Date(25,12,2023)
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    @staticmethod
    def validate_date(day, month, year):
        if month < 1 or month > 12:
            return False
        # Days in each month
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Date.is_leap_year(year):
            days_in_month[2] = 29
        if day < 1 or day > days_in_month[month]:
            return False
        return True

    @classmethod
    def from_string(cls, s):
        day, month, year = map(int, s.split("/"))
        return cls(day, month, year)


# Test cases for Date class

# Test is_leap_year
assert Date.is_leap_year(2024) == True
assert Date.is_leap_year(2023) == False
assert Date.is_leap_year(2000) == True  # Century leap
assert Date.is_leap_year(1900) == False  # Century not leap

# Test validate_date
assert Date.validate_date(29, 2, 2024) == True  # Leap year Feb 29
assert Date.validate_date(29, 2, 2023) == False  # Non-leap
assert Date.validate_date(31, 12, 2023) == True
assert Date.validate_date(32, 12, 2023) == False  # Invalid day
assert Date.validate_date(31, 4, 2023) == False  # April has 30 days
assert Date.validate_date(0, 5, 2023) == False  # Invalid day
assert Date.validate_date(15, 13, 2023) == False  # Invalid month

# Test from_string
date_obj = Date.from_string("25/12/2023")
assert date_obj.day == 25
assert date_obj.month == 12
assert date_obj.year == 2023

date_obj2 = Date.from_string("29/02/2024")
assert date_obj2.day == 29
assert date_obj2.month == 2
assert date_obj2.year == 2024

print("All tests passed!")


# ============================================================================
# 8) Animal Hierarchy (EX63-EX74)
# ============================================================================
# Animal:
# - Attributes: name:str
# - Functions:
#   - __init__(self, name): set name -> Animal("Rex")
#   - speak(self): default sound -> "Some sound"
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"


# Dog(Animal):
# - Attributes: name, breed
# - Functions:
#   - __init__(self, name, breed): call super + set breed -> Dog("Rex","Labrador")
#   - speak(self): override -> "Woof!" (or extended with super)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{super().speak()} Woof!"


# Cat(Animal):
# - Functions:
#   - speak(self): override -> "Meow!"
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{super().speak()} Meow!"


# ServiceDog(Dog):
# - Attributes: trained:bool=True
# - Functions:
#   - inherits Dog/Animal methods -> isinstance(sd, Animal) == True
class ServiceDog(Dog):
    def __init__(self, name, breed, trained=True):
        super().__init__(name, breed)
        self.trained = trained


# Test cases for Animal Hierarchy

# Create instances
animal = Animal("Rex")
dog = Dog("Rex", "Labrador")
cat = Cat("Whiskers", "Siamese")
service_dog = ServiceDog("Buddy", "Golden Retriever", True)

# Test attributes
assert animal.name == "Rex"
assert dog.name == "Rex"
assert dog.breed == "Labrador"
assert cat.name == "Whiskers"
assert cat.breed == "Siamese"
assert service_dog.name == "Buddy"
assert service_dog.breed == "Golden Retriever"
assert service_dog.trained == True

# Test speak methods
assert animal.speak() == "Some sound"
assert dog.speak() == "Some sound Woof!"
assert cat.speak() == "Some sound Meow!"
assert service_dog.speak() == "Some sound Woof!"  # Inherits from Dog

# Test inheritance (isinstance checks)
assert isinstance(service_dog, ServiceDog) == True
assert isinstance(service_dog, Dog) == True
assert isinstance(service_dog, Animal) == True
assert isinstance(dog, Animal) == True
assert isinstance(cat, Animal) == True
assert not isinstance(animal, Dog)  # Animal is not a Dog

print("All Animal Hierarchy tests passed!")

# ============================================================================
# 9) Multiple Inheritance (EX75-EX78)
# ============================================================================
# Swimmer:
# - swim(self): swimming action -> "Swimming..."

# Flyer:
# - fly(self): flying action -> "Flying..."


# Duck(Swimmer, Flyer):
# - inherits both behaviors -> duck.swim()=="Swimming...", duck.fly()=="Flying..."
class Swimmer:
    def __init__(self):
        pass

    def swim(self):
        print("Swimming...")


class Flyer:
    def __init__(self):
        pass

    def fly(self):
        print("Flying...")


class Duck(Swimmer, Flyer):
    def __init__(self):
        super().__init__()

    def swim(self):
        super().swim()

    def fly(self):
        super().fly()


# Test the Duck class
duck = Duck()

# Test swim
print("Testing swim:")
duck.swim()  # Should print: Swimming...

# Test fly
print("Testing fly:")
duck.fly()  # Should print: Flying...

# Test MRO
print("MRO:", Duck.__mro__)  # Shows resolution order: (Duck, Swimmer, Flyer, object)

# Test isinstance
print("Is Duck a Swimmer?", isinstance(duck, Swimmer))  # True
print("Is Duck a Flyer?", isinstance(duck, Flyer))  # True
# ============================================================================
# 10) FileManager / Multiplier / Container (EX79-EX86)
# ============================================================================
# FileManager:
# - Attributes: filename:str, file/resource handle
# - Functions:
#   - __init__(self, filename): store target file -> "test.txt"
#   - __enter__(self): open/acquire resource -> returns file-like object
#   - __exit__(self, exc_type, exc_val, exc_tb): close/release -> resource closed

# Multiplier:
# - Attributes: factor:number
# - Functions:
#   - __init__(self, factor): set multiplier -> 3
#   - __call__(self, input_value): callable object -> mult(5)=15

# Container:
# - Attributes: items:list
# - Functions:
#   - __init__(self, items): set items -> [1,2]
#   - __bool__(self): truthiness by content -> bool(Container([])) == False


# ============================================================================
# 11) BankAccount (EX87-EX92)
# ============================================================================
# BankAccount:
# - Attributes: _balance / __balance:number
# - Functions:
#   - __init__(self, initial_balance): initialize money -> 1000
#   - get_balance(self): return current balance -> 1000
#   - balance (property getter): read balance -> 500
#   - balance (property setter): validated set -> ValueError for invalid
#   - deposit(self, amount): add money -> 500 + 200 = 700
#   - withdraw(self, amount): subtract with checks -> 700 - 100 = 600
class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    @property
    def balance(self):
        return self.get_balance()

    @balance.setter
    def balance(self, value):
        if value <= 0:
            raise ValueError("Value should be greater than 0")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount to deposit should be greater than 0")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount to withdraw should be greater than 0")
        if amount > self._balance:
            raise ValueError("Insufficient balance")
        else:
            self._balance -= amount


# ============================================================================
# BASIC USAGE - Creating account and checking balance
# ============================================================================

# Create account with initial balance of 1000
account = BankAccount(1000)
print(f"Initial balance: {account.balance}")  # Output: 1000

# Get balance using method
print(f"Using get_balance(): {account.get_balance()}")  # Output: 1000


# ============================================================================
# DEPOSIT MONEY
# ============================================================================

# Deposit 200
account.deposit(200)
print(f"\nAfter depositing 200: {account.balance}")  # Output: 1200

# Deposit another 300
account.deposit(300)
print(f"After depositing 300: {account.balance}")  # Output: 1500


# ============================================================================
# WITHDRAW MONEY
# ============================================================================

# Withdraw 500
account.withdraw(500)
print(f"\nAfter withdrawing 500: {account.balance}")  # Output: 1000

# Withdraw 200
account.withdraw(200)
print(f"After withdrawing 200: {account.balance}")  # Output: 800


# ============================================================================
# SET BALANCE USING PROPERTY SETTER
# ============================================================================

# Set balance directly
account.balance = 1500
print(f"\nAfter setting balance to 1500: {account.balance}")  # Output: 1500


# ============================================================================
# VALIDATION IN ACTION
# ============================================================================

# Try to deposit negative amount
try:
    account.deposit(-50)
except ValueError as e:
    print(f"\nError: {e}")  # Output: Error: Amount to deposit should be greater than 0

# Try to withdraw more than balance
try:
    account.withdraw(2000)
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Insufficient balance

# Try to set invalid balance
try:
    account.balance = -500
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Value should be greater than 0


# ============================================================================
# PRACTICAL EXAMPLE - Simple transactions
# ============================================================================

bank = BankAccount(5000)
print("\n\n--- Bank Account Transactions ---")
print(f"Starting balance: ${bank.balance}")

bank.deposit(1000)
print(f"Deposited $1000 → Balance: ${bank.balance}")

bank.withdraw(500)
print(f"Withdrew $500 → Balance: ${bank.balance}")

bank.deposit(250)
print(f"Deposited $250 → Balance: ${bank.balance}")

bank.withdraw(2000)
print(f"Withdrew $2000 → Balance: ${bank.balance}")

print(f"Final balance: ${bank.balance}")

# ============================================================================
# 12) Advanced Features (EX93-EX100)
# ============================================================================
# Point:
# - Attributes: x:int, y:int (with __slots__ optionally)
# - Functions:
#   - __eq__(self, other): compare coordinates -> Point(1,2)==Point(1,2) True
#   - __hash__(self): hash by coordinates -> set dedup keeps one
#   - __slots__ = ("x","y"): restrict dynamic attrs -> assigning p.z raises AttributeError

# Range (iterator):
# - Functions:
#   - __iter__(self): return iterator object -> iter(r)
#   - __next__(self): next value or StopIteration -> 1,2,3 then stop

# ValidatedInt (descriptor):
# - Functions:
#   - __get__(self, instance, owner): read managed value -> current int value
#   - __set__(self, instance, value): validate on assign -> reject invalid type/range

# add_repr (class decorator):
# - Functions:
#   - add_repr(cls): inject __repr__ dynamically -> repr(obj) shows generated format

# Composition demo:
# - Engine.start(self): engine action -> "Engine started"
# - CarWithEngine.__init__(self): has Engine instance -> self.engine exists
# - CarWithEngine.start(self): delegate call -> "Engine started"


# BOSS SYSTEM:
# - Product(id, name, price, stock): item model -> Product(1,"Sword",150,10)
# - Order(order_id, customer_id): holds items -> order.add_item(...)
# - Order.add_item(product, qty): add line item -> items count increases
# - Order.total (property): sum line totals -> 400
# - Order.__len__(self): number of lines -> 2
# - OrderProcessor.process(order): apply stock updates -> p1.stock becomes 8
class Product:
    def __init__(self, pid, name, price, stock):
        self.id = pid
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name!r}, price={self.price}, stock={self.stock})"


class Order:
    def __init__(self, order_id, customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self._lines = []  # list of (Product, qty)

    def add_item(self, product, qty):
        if qty <= 0:
            raise ValueError("Quantity must be positive")
        self._lines.append((product, qty))

    @property
    def total(self):
        return sum(p.price * qty for p, qty in self._lines)

    def __len__(self):
        return len(self._lines)

    def __repr__(self):
        return f"Order(order_id={self.order_id}, customer_id={self.customer_id}, lines={len(self)})"


class OrderProcessor:
    @staticmethod
    def process(order):
        for product, qty in order._lines:
            if qty > product.stock:
                raise ValueError(f"Insufficient stock for {product.name}")
            product.stock -= qty
        return order


# ==========================================
# TEST SCRIPT FOR BOSS SYSTEM
# ==========================================

print("--- 1. Creating Products ---")
p1 = Product(1, "Sword", 150, 10)
p2 = Product(2, "Shield", 50, 5)
print(f"Product 1: {p1}")
print(f"Product 2: {p2}")

print("\n--- 2. Creating Order & Adding Items ---")
order = Order(101, 555)
order.add_item(p1, 2)  # 2 swords @ 150 = 300
order.add_item(p2, 2)  # 2 shields @ 50 = 100
print(f"Order: {order}")
print(f"Number of lines: {len(order)}")  # Expected: 2
print(f"Total: {order.total}")  # Expected: 400

print("\n--- 3. Processing Order (Stock Deduction) ---")
print(f"Before process - Sword stock: {p1.stock}, Shield stock: {p2.stock}")
OrderProcessor.process(order)
print(
    f"After process - Sword stock: {p1.stock}, Shield stock: {p2.stock}"
)  # Sword: 8, Shield: 3

print("\n--- 4. Error Handling ---")
try:
    order2 = Order(102, 556)
    order2.add_item(p1, 20)  # Try to order 20 but only 8 left
    OrderProcessor.process(order2)
except ValueError as e:
    print(f"Error: {e}")
