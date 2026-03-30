# ============================================================================
# DRILL 07: OBJECT-ORIENTED PROGRAMMING (OOP) - RESTRUCTURED
# ============================================================================
# Python transitioning from JavaScript
# ============================================================================

# NEW SYNTAX REFERENCE: JS → Python OOP
# ============================================================================
# [same reference table as before]
# ============================================================================
import os

os.system("cls")


# ============================================================================
# PHASE 1: BASIC CLASSES & INSTANCE METHODS (Drills 1-5)
# ============================================================================
# Using class: Car
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.brand
    def set_brand

# 1. Basic class definition with __init__
#   Create Car with brand and model attributes
#   call:   car = Car("Toyota", "Camry")
car = Car("Toyota", "Camry")
# 2. Instance method (simple getter)
#   Add get_brand() method
#   call:   car.get_brand()
#   output: "Toyota"
print(car.get_brand())
# 3. Instance method (simple setter)
#   Add set_brand() method
#   call:   car.set_brand("BMW"); print(car.brand)
#   output: "BMW"

# 4. Instance method (behavior)
#   Add describe() method returning formatted string
#   call:   car.describe()
#   output: "Toyota Camry"

# 5. Multiple instance attributes
#   Extend Car with year, color attributes
#   Add get_specs() method
#   call:   car.get_specs()
#   output: formatted specs string


# ============================================================================
# PHASE 2: STRING REPRESENTATION & CLASS VARIABLES (Drills 6-9)
# ============================================================================
# Using class: Car (extended)

# 6. String representation with __str__
#   Add __str__() returning user-friendly format
#   call:   print(car)
#   output: "2020 Toyota Camry"

# 7. Class variable (shared across instances)
#   Add class variable: car_count = 0
#   Initialize count in __init__
#   call:   car1 = Car(...); car2 = Car(...); print(Car.car_count)
#   output: 2

# 8. Accessing instance vs class variables
#   Add method info() using both self.brand and Car.car_count
#   call:   car.info()
#   output: "Car #2: Toyota Camry"

# 9. Instance method modifying class variable (pitfall)
#   Create multiple instances, show car_count increments
#   call:   c1 = Car(...); c2 = Car(...); c3 = Car(...)
#           print(Car.car_count)
#   output: 3


# ============================================================================
# PHASE 3: MAGIC METHODS - REPRESENTATION (Drills 10-12)
# ============================================================================
# Using class: Person (new)

# 10. __str__ vs __repr__ (side-by-side comparison)
#   Add both methods to Person
#   __str__() returns "Alice (30)"
#   __repr__() returns "Person('Alice', 30)"
#   call:   p = Person("Alice", 30); print(str(p)); print(repr(p))
#   output: Alice (30)
#            Person('Alice', 30)

# 11. __len__ for len() support
#   Create NameList class holding list of names
#   Add __len__() returning count
#   call:   nl = NameList(["Alice", "Bob", "Charlie"]); len(nl)
#   output: 3

# 12. __repr__ for debugging
#   Add meaningful __repr__() to NameList
#   call:   nl = NameList([...]); repr(nl)
#   output: NameList(['Alice', 'Bob', 'Charlie'])


# ============================================================================
# PHASE 4: INDEXING & CONTAINER OPERATIONS (Drills 13-16)
# ============================================================================
# Using class: CustomList (new)

# 13. __getitem__ for indexing
#   Add __getitem__() to CustomList
#   call:   cl = CustomList([10, 20, 30]); cl[1]
#   output: 20

# 14. __setitem__ for assignment by index
#   Add __setitem__() to CustomList
#   call:   cl = CustomList([1, 2, 3]); cl[1] = 99; print(cl[1])
#   output: 99

# 15. __contains__ for "in" operator
#   Add __contains__() to CustomList
#   call:   cl = CustomList([1, 2, 3]); 2 in cl
#   output: True

# 16. Combining container methods
#   Test all three together on same CustomList instance
#   call:   cl = CustomList([1, 2, 3])
#           cl[0] = 100
#           print(100 in cl and len(cl) == 3)
#   output: True


# ============================================================================
# PHASE 5: OPERATOR OVERLOADING (Drills 17-22)
# ============================================================================
# Using class: Vector (new)

# 17. __add__ for + operator
#   Add __add__() returning new Vector
#   call:   v1 = Vector(1, 2); v2 = Vector(3, 4); v3 = v1 + v2
#   output: v3 = Vector(4, 6)

# 18. __sub__ for - operator
#   Add __sub__() to Vector
#   call:   v1 = Vector(5, 7); v2 = Vector(2, 3); v3 = v1 - v2
#   output: v3 = Vector(3, 4)

# 19. __mul__ for * operator
#   Add __mul__() to Vector (scalar multiplication)
#   call:   v = Vector(2, 3); v2 = v * 2
#   output: v2 = Vector(4, 6)

# 20. __str__ for Vector
#   Add __str__() returning "Vector(x, y)"
#   call:   v = Vector(2, 3); print(v)
#   output: Vector(2, 3)

# 21. __eq__ for == operator
#   Add __eq__() comparing x and y
#   call:   v1 = Vector(1, 2); v2 = Vector(1, 2); v1 == v2
#   output: True

# 22. Combining operations
#   v1 + v2 * 2 == v3, then check if in list
#   call:   v1 = Vector(1, 1); v2 = Vector(1, 1)
#           v3 = v1 + v2 * 2  # Vector(3, 3)
#           print(v3 == Vector(3, 3))
#   output: True


# ============================================================================
# PHASE 6: COMPARISON OPERATORS (Drills 23-26)
# ============================================================================
# Using class: Student (new)

# 23. __eq__ for == operator
#   Add __eq__() comparing by student_id
#   call:   s1 = Student("Alice", 101); s2 = Student("Alice", 101)
#           s1 == s2
#   output: True

# 24. __lt__ for < operator (for sorting)
#   Add __lt__() comparing by gpa
#   call:   students = [Student("Bob", 2.5), Student("Alice", 3.5)]
#           sorted(students)[0].name
#   output: "Bob"

# 25. __le__, __gt__, __ge__ (complete comparison set)
#   Add all comparison methods
#   call:   s1 = Student("Alice", 3.0); s2 = Student("Bob", 3.0)
#           print(s1 <= s2); print(s1 >= s2)
#   output: True
#            True

# 26. Sorting students by multiple attributes
#   Use __lt__() in real sorting scenario
#   call:   students = [...]
#           sorted(students) -> sorted by gpa
#   output: [students sorted by gpa]


# ============================================================================
# PHASE 7: PROPERTIES (Drills 27-32)
# ============================================================================
# Using class: Rectangle (new)

# 27. @property basic (read-only)
#   Add @property width, height
#   call:   r = Rectangle(4, 5); print(r.width)
#   output: 4

# 28. @property computed (area)
#   Add @property area (computed, not stored)
#   call:   r = Rectangle(4, 5); print(r.area)
#   output: 20

# 29. @property.setter with validation
#   Add width.setter validating > 0
#   call:   r = Rectangle(4, 5); r.width = 10; print(r.area)
#   output: 50

# 30. @property.setter rejecting invalid values
#   Try r.width = -5, catch error
#   call:   try: r.width = -5
#           except ValueError: print("Invalid")
#   output: Invalid

# 31. Multiple computed properties
#   Add @property perimeter
#   call:   r = Rectangle(4, 5); print(r.perimeter)
#   output: 18

# 32. Properties work like attributes (not methods)
#   Compare property access vs method call
#   call:   r.area vs r.get_area()  (if method existed)
#           Both called as r.area (no parentheses)


# ============================================================================
# PHASE 8: STATIC & CLASS METHODS (Drills 33-36)
# ============================================================================
# Using class: Date (new)

# 33. @staticmethod utility function
#   Add @staticmethod is_leap_year(year)
#   call:   Date.is_leap_year(2024)
#   output: True

# 34. @staticmethod doesn't access instance
#   Add @staticmethod validate_date(day, month, year)
#   call:   Date.validate_date(29, 2, 2024)
#   output: True

# 35. @classmethod factory constructor
#   Add @classmethod from_string(cls, "25/12/2023")
#   call:   d = Date.from_string("25/12/2023")
#           print(d.day, d.month, d.year)
#   output: 25 12 2023

# 36. @classmethod vs @staticmethod (comparison)
#   Show difference: @classmethod can create instances
#   call:   d = Date.from_string("01/01/2024")  # @classmethod
#           vs
#           is_valid = Date.is_leap_year(2024)  # @staticmethod
#   output: Both work, different purposes


# ============================================================================
# PHASE 9: INHERITANCE - BASICS (Drills 37-41)
# ============================================================================
# Using class hierarchy: Animal → Dog, Cat

# 37. Basic single inheritance
#   class Animal:
#       def __init__(self, name):
#           self.name = name
#       def speak(self):
#           return "Some sound"
#
#   class Dog(Animal):
#       pass
#
#   call:   dog = Dog("Rex")
#   output: dog.name = "Rex"

# 38. Method overriding
#   Override speak() in Dog
#   call:   dog.speak()
#   output: "Woof"

# 39. super().__init__() in constructor
#   Dog.__init__ calls super().__init__(name) then adds breed
#   call:   dog = Dog("Rex", "Labrador")
#           print(dog.name, dog.breed)
#   output: Rex Labrador

# 40. super().method() calling parent method
#   Dog.speak() calls super().speak() then appends info
#   call:   dog.speak()
#   output: "Some sound (from dog)"

# 41. Polymorphism - same method, different behavior
#   Create Dog and Cat, both override speak()
#   Create list of animals, loop calling speak()
#   call:   animals = [Dog("Rex"), Cat("Whiskers")]
#           for animal in animals: print(animal.speak())
#   output: Woof
#            Meow


# ============================================================================
# PHASE 10: INHERITANCE - ADVANCED (Drills 42-46)
# ============================================================================
# Using class hierarchy: Animal → Dog → ServiceDog

# 42. Multi-level inheritance
#   ServiceDog(Dog) adds trained=True
#   call:   sd = ServiceDog("Max", "Labrador")
#           isinstance(sd, Animal)
#   output: True

# 43. isinstance() and issubclass()
#   Test isinstance on Dog and ServiceDog
#   Test issubclass relationships
#   call:   isinstance(sd, Dog), isinstance(sd, Animal)
#           issubclass(ServiceDog, Dog), issubclass(ServiceDog, Animal)
#   output: True, True, True, True

# 44. Method Resolution Order (MRO)
#   Show how super() decides which parent method to call
#   call:   print(ServiceDog.__mro__)
#   output: (ServiceDog, Dog, Animal, object)

# 45. Multiple inheritance (Diamond problem preview)
#   class Swimmer: def swim(): ...
#   class Flyer: def fly(): ...
#   class Duck(Swimmer, Flyer): pass
#   call:   duck = Duck(); duck.swim(); duck.fly()
#   output: Swimming...
#            Flying...

# 46. Property inheritance
#   Parent has @property age, child overrides it
#   call:   dog.age vs cat.age (different calculation)


# ============================================================================
# PHASE 11: CONTEXT MANAGERS & MAGIC METHODS (Drills 47-50)
# ============================================================================
# Using class: FileManager (new)

# 47. __enter__ and __exit__ for context manager
#   Add both methods
#   call:   with FileManager("test.txt") as f:
#               print("Inside context")
#   output: Opened test.txt
#            Inside context
#            Closed test.txt

# 48. Context manager error handling
#   __exit__ handles exceptions
#   call:   with FileManager("test.txt") as f:
#               raise ValueError("test error")
#           (error caught and file closed)

# 49. __call__ making object callable
#   Add __call__() to Multiplier class
#   call:   mult = Multiplier(3); result = mult(5)
#   output: 15

# 50. __bool__ for truthy/falsy values
#   Add __bool__() to Container
#   call:   c = Container([1, 2])
#           if c: print("Has items")
#   output: Has items


# ============================================================================
# PHASE 12: PRIVATE ATTRIBUTES & ENCAPSULATION (Drills 51-54)
# ============================================================================
# Using class: BankAccount (new)

# 51. Private attribute convention (_attribute)
#   Use _balance private variable
#   Add public method get_balance()
#   call:   acc = BankAccount(1000)
#           print(acc.get_balance())  # public method
#           acc._balance = 0  # technically possible but not recommended
#   output: 1000

# 52. Name mangling with double underscore (__attribute)
#   Use __balance (becomes _BankAccount__balance internally)
#   call:   acc = BankAccount(1000)
#           acc.get_balance()  # works
#           acc.__balance  # raises AttributeError
#   output: 1000
#            AttributeError

# 53. Property with private attribute
#   @property balance returns __balance
#   @property.setter validates before updating
#   call:   acc = BankAccount(1000)
#           acc.balance = 500  # uses setter
#           print(acc.balance)  # uses getter
#   output: 500

# 54. Encapsulation in action
#   deposit() and withdraw() modify __balance
#   Balance can only change through methods
#   call:   acc.deposit(500); acc.withdraw(200)
#           print(acc.balance)
#   output: 1300


# ============================================================================
# PHASE 13: COMPLEX FEATURES (Drills 55-60)
# ============================================================================

# 55. __hash__ and __eq__ for set membership
#   Point class with both methods
#   call:   p1 = Point(1, 2); p2 = Point(1, 2)
#           points_set = {p1, p2}
#           len(points_set)
#   output: 1 (duplicate point recognized)

# 56. __iter__ and __next__ making class iterable
#   Range class with iteration
#   call:   for i in Range(1, 4): print(i)
#   output: 1
#            2
#            3

# 57. __slots__ for memory efficiency
#   Point with __slots__ = ['x', 'y']
#   call:   p = Point(1, 2); print(p.x)
#           p.z = 3  # raises AttributeError
#   output: 1
#            AttributeError

# 58. Descriptor protocol (__get__, __set__)
#   ValidatedInt descriptor
#   call:   (advanced topic - showcase only)

# 59. Class decorator
#   @add_repr decorator adds __repr__
#   call:   (showcase usage)

# 60. Composition over inheritance
#   Car has-a Engine (composition)
#   Car is-a Vehicle (inheritance)
#   call:   car = Car(); car.start()
#   output: "Engine started"


# ============================================================================
# PHASE 14: BOSS DRILL (Drill 100)
# ============================================================================
# Complete E-Commerce System

# 100. BOSS DRILL: E-Commerce System
#   Create 3 integrated classes: Product, Order, OrderProcessor
#
#   Product:
#     - __init__(id, name, price, stock)
#     - @property in_stock
#     - @classmethod from_dict(cls, dict)
#     - reduce_stock(qty)
#     - __str__(), __repr__()
#
#   Order:
#     - __init__(order_id, user_id)
#     - items list
#     - add_item(product, qty)
#     - @property total
#     - __len__(), __contains__()
#     - get_summary()
#
#   OrderProcessor:
#     - @staticmethod validate_order(order)
#     - process(order) - reduces stock
#     - cancel_order(order) - restores stock
#
#   call:
#     p1 = Product(1, "Sword", 150, 10)
#     p2 = Product(2, "Shield", 100, 5)
#     order = Order(101, 1)
#     order.add_item(p1, 2)
#     order.add_item(p2, 1)
#     print(f"Total: {order.total}")
#     print(f"Items: {len(order)}")
#     processor = OrderProcessor()
#     processor.process(order)
#     print(f"P1 stock: {p1.stock}")
#   output:
#     Total: 400
#     Items: 2
#     P1 stock: 8
