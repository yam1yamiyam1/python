# ============================================================================
# DRILL 07: OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================================================
# Python transitioning from JavaScript
# ============================================================================

# NEW SYNTAX REFERENCE: JS → Python OOP
# ============================================================================
# JavaScript                          Python
# ──────────────────────────────────  ──────────────────────────────────────
# class MyClass {                     class MyClass:
#   constructor(x) {                      def __init__(self, x):
#     this.x = x;                             self.x = x
#   }
#   method() { ... }                    def method(self): ...
# }
#
# new MyClass(5)                      MyClass(5)
#
# this.x                              self.x
#
# static method() { ... }             @staticmethod
#                                     def method(): ...
#
# get x() { ... }                     @property
#                                     def x(self): ...
#
# class Child extends Parent { }      class Child(Parent):
#                                         pass
#
# super()                             super()
#
# instanceof                          isinstance()
#
# ============================================================================

from data.training_data import numbers, users, products, orders, students

# ============================================================================
# DRILLS 1-100
# ============================================================================

# 1. Basic class definition with __init__
#
#   class Car:
#       def __init__(self, brand, model):
#           ...store brand and model as instance attributes...
#
#   call:   car = Car("Toyota", "Camry")
#   output: Car object created




# 2. Instance method (simple getter)
#
#   class Car:
#       def __init__(self, brand):
#           self.brand = brand
#       def get_brand(self):
#           ...return self.brand...
#
#   call:   car = Car("Honda"); car.get_brand()
#   output: "Honda"




# 3. Instance method (simple setter)
#
#   class Car:
#       def __init__(self, brand):
#           self.brand = brand
#       def set_brand(self, new_brand):
#           ...update self.brand...
#
#   call:   car = Car("Ford"); car.set_brand("BMW"); print(car.brand)
#   output: "BMW"




# 4. Instance method (behavior)
#
#   class Calculator:
#       def add(self, a, b):
#           ...return sum of a and b...
#
#   call:   calc = Calculator(); calc.add(5, 3)
#   output: 8




# 5. Multiple instance attributes
#
#   class Person:
#       def __init__(self, name, age, email):
#           ...store all three attributes...
#
#   call:   person = Person("Alice", 30, "alice@example.com")
#   output: Person object with three attributes




# 6. String representation with __str__
#
#   class Person:
#       def __init__(self, name, age):
#           ...store name and age...
#       def __str__(self):
#           ...return formatted string representation...
#
#   call:   person = Person("Bob", 25); print(person)
#   output: "Person: Bob, 25" (or similar format)




# 7. Class variable (shared across instances)
#
#   class Dog:
#       species = "Canis familiaris"
#       def __init__(self, name):
#           self.name = name
#
#   call:   dog1 = Dog("Rex"); dog2 = Dog("Buddy"); print(Dog.species)
#   output: "Canis familiaris"




# 8. Accessing instance vs class variables
#
#   class Dog:
#       species = "Canis familiaris"
#       def __init__(self, name):
#           self.name = name
#       def info(self):
#           ...return formatted string with name and species...
#
#   call:   dog = Dog("Max"); dog.info()
#   output: "Max is a Canis familiaris"




# 9. Instance method modifying class variable (pitfall)
#
#   class Counter:
#       count = 0
#       def __init__(self):
#           Counter.count += 1
#
#   call:   c1 = Counter(); c2 = Counter(); print(Counter.count)
#   output: 2




# 10. Static method with @staticmethod
#
#   class MathUtils:
#       @staticmethod
#       def add(a, b):
#           ...return a + b...
#
#   call:   MathUtils.add(5, 3)
#   output: 8




# 11. Static method doesn't take self
#
#   class StringUtils:
#       @staticmethod
#       def reverse_string(s):
#           ...return reversed string...
#
#   call:   StringUtils.reverse_string("hello")
#   output: "olleh"




# 12. Class method with @classmethod and cls parameter
#
#   class Animal:
#       species = "Unknown"
#       @classmethod
#       def set_species(cls, name):
#           ...update cls.species...
#
#   call:   Animal.set_species("Mammal"); print(Animal.species)
#   output: "Mammal"




# 13. Class method as alternative constructor
#
#   class Date:
#       def __init__(self, day, month, year):
#           ...store day, month, year...
#       @classmethod
#       def from_string(cls, date_str):
#           ...parse "DD/MM/YYYY" and create instance...
#
#   call:   date = Date.from_string("25/12/2023")
#   output: Date object created




# 14. Property decorator @property
#
#   class Circle:
#       def __init__(self, radius):
#           self._radius = radius
#       @property
#       def radius(self):
#           ...return self._radius...
#
#   call:   circle = Circle(5); print(circle.radius)
#   output: 5




# 15. Property with getter and setter
#
#   class Circle:
#       def __init__(self, radius):
#           self._radius = radius
#       @property
#       def radius(self):
#           ...return self._radius...
#       @radius.setter
#       def radius(self, value):
#           ...validate value > 0 and set self._radius...
#
#   call:   circle = Circle(5); circle.radius = 10; print(circle.radius)
#   output: 10




# 16. Computed property
#
#   class Circle:
#       def __init__(self, radius):
#           self._radius = radius
#       @property
#       def area(self):
#           ...return pi * radius^2...
#
#   call:   circle = Circle(5); print(circle.area)
#   output: ~78.54




# 17. Private attribute convention (_attribute)
#
#   class BankAccount:
#       def __init__(self, balance):
#           self._balance = balance
#       def get_balance(self):
#           ...return self._balance...
#
#   call:   account = BankAccount(1000); account.get_balance()
#   output: 1000




# 18. Name mangling with double underscore (__attribute)
#
#   class BankAccount:
#       def __init__(self, balance):
#           self.__balance = balance
#       def get_balance(self):
#           ...return self.__balance...
#
#   call:   account = BankAccount(1000); account.get_balance()
#   output: 1000




# 19. __repr__ for developer-friendly representation
#
#   class Person:
#       def __init__(self, name, age):
#           self.name = name
#           self.age = age
#       def __repr__(self):
#           ...return repr string like Person('Bob', 25)...
#
#   call:   person = Person("Bob", 25); repr(person)
#   output: "Person('Bob', 25)" or similar




# 20. __len__ for len() support
#
#   class CustomList:
#       def __init__(self, items):
#           self.items = items
#       def __len__(self):
#           ...return length of self.items...
#
#   call:   cl = CustomList([1, 2, 3]); len(cl)
#   output: 3




# 21. __getitem__ for indexing
#
#   class CustomList:
#       def __init__(self, items):
#           self.items = items
#       def __getitem__(self, index):
#           ...return self.items[index]...
#
#   call:   cl = CustomList([10, 20, 30]); cl[1]
#   output: 20




# 22. __setitem__ for assignment by index
#
#   class CustomList:
#       def __init__(self, items):
#           self.items = items
#       def __setitem__(self, index, value):
#           ...set self.items[index] = value...
#
#   call:   cl = CustomList([1, 2, 3]); cl[1] = 99; print(cl.items)
#   output: [1, 99, 3]




# 23. __contains__ for "in" operator
#
#   class CustomList:
#       def __init__(self, items):
#           self.items = items
#       def __contains__(self, item):
#           ...return whether item is in self.items...
#
#   call:   cl = CustomList([1, 2, 3]); 2 in cl
#   output: True




# 24. __add__ for + operator
#
#   class Vector:
#       def __init__(self, x, y):
#           self.x = x
#           self.y = y
#       def __add__(self, other):
#           ...return new Vector with summed coordinates...
#
#   call:   v1 = Vector(1, 2); v2 = Vector(3, 4); v3 = v1 + v2
#   output: v3.x = 4, v3.y = 6




# 25. __sub__ for - operator
#
#   class Vector:
#       def __init__(self, x, y):
#           self.x = x
#           self.y = y
#       def __sub__(self, other):
#           ...return new Vector with subtracted coordinates...
#
#   call:   v1 = Vector(5, 7); v2 = Vector(2, 3); v3 = v1 - v2
#   output: v3.x = 3, v3.y = 4




# 26. __mul__ for * operator
#
#   class Vector:
#       def __init__(self, x, y):
#           self.x = x
#           self.y = y
#       def __mul__(self, scalar):
#           ...return new Vector with scaled coordinates...
#
#   call:   v = Vector(2, 3); v2 = v * 2
#   output: v2.x = 4, v2.y = 6




# 27. __eq__ for == operator
#
#   class Point:
#       def __init__(self, x, y):
#           self.x = x
#           self.y = y
#       def __eq__(self, other):
#           ...return whether x and y match...
#
#   call:   p1 = Point(1, 2); p2 = Point(1, 2); p1 == p2
#   output: True




# 28. __lt__ for < operator
#
#   class Person:
#       def __init__(self, age):
#           self.age = age
#       def __lt__(self, other):
#           ...return whether self.age < other.age...
#
#   call:   p1 = Person(25); p2 = Person(30); p1 < p2
#   output: True




# 29. __gt__ for > operator
#
#   class Person:
#       def __init__(self, age):
#           self.age = age
#       def __gt__(self, other):
#           ...return whether self.age > other.age...
#
#   call:   p1 = Person(30); p2 = Person(25); p1 > p2
#   output: True




# 30. __le__ for <= operator
#
#   class Score:
#       def __init__(self, value):
#           self.value = value
#       def __le__(self, other):
#           ...return whether self.value <= other.value...
#
#   call:   s1 = Score(80); s2 = Score(90); s1 <= s2
#   output: True




# 31. __call__ to make object callable
#
#   class Multiplier:
#       def __init__(self, factor):
#           self.factor = factor
#       def __call__(self, x):
#           ...return x * self.factor...
#
#   call:   mult = Multiplier(3); mult(5)
#   output: 15




# 32. __bool__ for bool conversion
#
#   class Container:
#       def __init__(self, items):
#           self.items = items
#       def __bool__(self):
#           ...return whether items is non-empty...
#
#   call:   c1 = Container([1, 2]); bool(c1)
#   output: True




# 33. __iter__ for iteration support
#
#   class CustomRange:
#       def __init__(self, max_val):
#           self.max_val = max_val
#           self.current = 0
#       def __iter__(self):
#           ...return self...
#       def __next__(self):
#           ...increment current and yield up to max_val...
#
#   call:   for i in CustomRange(3): print(i)
#   output: 0, 1, 2




# 34. __enter__ and __exit__ for context manager
#
#   class FileManager:
#       def __init__(self, filename):
#           self.filename = filename
#       def __enter__(self):
#           ...open file and return...
#       def __exit__(self, exc_type, exc_val, exc_tb):
#           ...close file...
#
#   call:   with FileManager("test.txt") as f: ...use f...
#   output: File opened and closed automatically




# 35. Basic single inheritance
#
#   class Animal:
#       def __init__(self, name):
#           self.name = name
#       def speak(self):
#           ...return "Some sound"...
#
#   class Dog(Animal):
#       def speak(self):
#           ...return "Woof!"...
#
#   call:   dog = Dog("Rex"); print(dog.speak())
#   output: "Woof!"




# 36. Parent class initialization with super().__init__()
#
#   class Animal:
#       def __init__(self, name):
#           self.name = name
#
#   class Dog(Animal):
#       def __init__(self, name, breed):
#           ...call super().__init__(name)...
#           self.breed = breed
#
#   call:   dog = Dog("Rex", "Labrador")
#   output: Dog object with name and breed




# 37. Accessing parent method
#
#   class Animal:
#       def describe(self):
#           ...return "This is an animal"...
#
#   class Dog(Animal):
#       def describe(self):
#           ...call super().describe() and append dog info...
#
#   call:   dog = Dog(); dog.describe()
#   output: "This is an animal. It's a dog."




# 38. Method overriding
#
#   class Shape:
#       def area(self):
#           ...raise NotImplementedError...
#
#   class Circle(Shape):
#       def __init__(self, radius):
#           self.radius = radius
#       def area(self):
#           ...return pi * radius^2...
#
#   call:   circle = Circle(5); circle.area()
#   output: ~78.54




# 39. isinstance() check
#
#   class Animal:
#       pass
#
#   class Dog(Animal):
#       pass
#
#   call:   dog = Dog(); isinstance(dog, Dog)
#   output: True




# 40. isinstance() with inheritance
#
#   class Animal:
#       pass
#
#   class Dog(Animal):
#       pass
#
#   call:   dog = Dog(); isinstance(dog, Animal)
#   output: True (Dog is subclass of Animal)




# 41. Multiple inheritance
#
#   class Walker:
#       def walk(self):
#           ...return "Walking"...
#
#   class Swimmer:
#       def swim(self):
#           ...return "Swimming"...
#
#   class Duck(Walker, Swimmer):
#       pass
#
#   call:   duck = Duck(); duck.walk(); duck.swim()
#   output: "Walking", "Swimming"




# 42. Method Resolution Order (MRO) with __mro__
#
#   class A: pass
#   class B(A): pass
#   class C(A): pass
#   class D(B, C): pass
#
#   call:   print(D.__mro__)
#   output: (D, B, C, A, object)




# 43. Using super() with multiple inheritance
#
#   class A:
#       def method(self):
#           ...return "A"...
#
#   class B(A):
#       def method(self):
#           ...call super().method() and append "B"...
#
#   call:   b = B(); b.method()
#   output: "AB"




# 44. Abstract base class concept (without ABC module)
#
#   class Shape:
#       def area(self):
#           ...raise NotImplementedError("Subclasses must implement area()")...
#
#   class Rectangle(Shape):
#       def __init__(self, w, h):
#           self.w = w
#           self.h = h
#       def area(self):
#           ...return w * h...
#
#   call:   rect = Rectangle(5, 10); rect.area()
#   output: 50




# 45. Polymorphism: Different classes, same interface
#
#   class Circle:
#       def __init__(self, r):
#           self.r = r
#       def area(self):
#           ...return pi * r^2...
#
#   class Square:
#       def __init__(self, side):
#           self.side = side
#       def area(self):
#           ...return side^2...
#
#   call:   shapes = [Circle(5), Square(4)]; [s.area() for s in shapes]
#   output: [~78.54, 16]




# 46. Encapsulation with private methods
#
#   class BankAccount:
#       def __init__(self, balance):
#           self.__balance = balance
#       def __validate(self):
#           ...check balance > 0...
#       def withdraw(self, amount):
#           ...validate and update balance...
#
#   call:   account = BankAccount(1000); account.withdraw(100)
#   output: Balance updated (private method called internally)




# 47. Getters and setters pattern
#
#   class Temperature:
#       def __init__(self, celsius):
#           self._celsius = celsius
#       def get_celsius(self):
#           ...return self._celsius...
#       def get_fahrenheit(self):
#           ...return (celsius * 9/5) + 32...
#       def set_celsius(self, value):
#           ...validate value and set...
#
#   call:   temp = Temperature(0); temp.get_fahrenheit()
#   output: 32




# 48. Class with default parameter values
#
#   class Car:
#       def __init__(self, brand, model="Unknown", year=2020):
#           self.brand = brand
#           self.model = model
#           self.year = year
#
#   call:   car = Car("Toyota"); print(car.model, car.year)
#   output: "Unknown", 2020




# 49. Class with *args in __init__
#
#   class Container:
#       def __init__(self, *items):
#           self.items = items
#
#   call:   container = Container(1, 2, 3, 4); print(container.items)
#   output: (1, 2, 3, 4)




# 50. Class with **kwargs in __init__
#
#   class Config:
#       def __init__(self, **settings):
#           self.settings = settings
#
#   call:   config = Config(debug=True, timeout=30); print(config.settings)
#   output: {"debug": True, "timeout": 30}




# 51. __init__ with *args and **kwargs
#
#   class FlexibleClass:
#       def __init__(self, *args, **kwargs):
#           self.args = args
#           self.kwargs = kwargs
#
#   call:   obj = FlexibleClass(1, 2, name="test"); print(obj.args, obj.kwargs)
#   output: (1, 2), {"name": "test"}




# 52. Instance vs class variable shadowing
#
#   class Counter:
#       count = 0
#       def __init__(self):
#           self.count = 1
#
#   call:   c1 = Counter(); c2 = Counter(); print(c1.count, c2.count, Counter.count)
#   output: 1, 1, 0




# 53. Method that modifies and returns self (fluent API)
#
#   class StringBuilder:
#       def __init__(self):
#           self.content = ""
#       def add(self, text):
#           self.content += text
#           ...return self...
#
#   call:   sb = StringBuilder().add("Hello").add(" ").add("World")
#   output: sb.content = "Hello World"




# 54. __hash__ for hashability
#
#   class Point:
#       def __init__(self, x, y):
#           self.x = x
#           self.y = y
#       def __hash__(self):
#           ...return hash of (x, y)...
#
#   call:   p = Point(1, 2); my_set = {p}
#   output: Point can be added to set




# 55. __slots__ for memory efficiency
#
#   class Point:
#       __slots__ = ["x", "y"]
#       def __init__(self, x, y):
#           self.x = x
#           self.y = y
#
#   call:   p = Point(1, 2); print(p.x, p.y)
#   output: 1, 2




# 56. Descriptor protocol with __get__ and __set__
#
#   class ValidatedInt:
#       def __init__(self, name):
#           self.name = name
#       def __get__(self, obj, objtype=None):
#           ...return obj.__dict__[self.name]...
#       def __set__(self, obj, value):
#           ...validate int and set...
#
#   call:   (descriptor protocol demo)
#   output: Descriptor behavior




# 57. Class decorator
#
#   def add_method(cls):
#       def new_method(self):
#           ...return "Added by decorator"...
#       cls.new_method = new_method
#       return cls
#
#   @add_method
#   class MyClass:
#       pass
#
#   call:   obj = MyClass(); obj.new_method()
#   output: "Added by decorator"




# 58. Composition over inheritance (has-a relationship)
#
#   class Engine:
#       def start(self):
#           ...return "Engine started"...
#
#   class Car:
#       def __init__(self):
#           self.engine = Engine()
#       def start(self):
#           ...return self.engine.start()...
#
#   call:   car = Car(); car.start()
#   output: "Engine started"




# 59. Inheritance chain (grandparent → parent → child)
#
#   class Animal: pass
#   class Mammal(Animal): pass
#   class Dog(Mammal): pass
#
#   call:   dog = Dog(); isinstance(dog, Animal)
#   output: True




# 60. Checking subclass with issubclass()
#
#   class Animal: pass
#   class Dog(Animal): pass
#
#   call:   issubclass(Dog, Animal)
#   output: True




# 61. Class method as factory pattern
#
#   class Person:
#       def __init__(self, name, age):
#           self.name = name
#           self.age = age
#       @classmethod
#       def from_birth_year(cls, name, birth_year):
#           age = 2024 - birth_year
#           ...return cls(name, age)...
#
#   call:   person = Person.from_birth_year("Alice", 1990)
#   output: Person with age calculated




# 62. Static method utility function
#
#   class Validator:
#       @staticmethod
#       def is_email(email):
#           ...check if "@" in email...
#
#   call:   Validator.is_email("test@example.com")
#   output: True




# 63. Class with all magic methods combined
#
#   class DynamicDict:
#       def __init__(self, **data):
#           self.data = data
#       def __getitem__(self, key):
#           ...return data[key]...
#       def __setitem__(self, key, value):
#           ...set data[key]...
#       def __contains__(self, key):
#           ...check key in data...
#       def __len__(self):
#           ...return len(data)...
#
#   call:   dd = DynamicDict(a=1, b=2); dd["a"]
#   output: 1




# 64. __del__ destructor (when object is garbage collected)
#
#   class Resource:
#       def __init__(self, name):
#           self.name = name
#       def __del__(self):
#           ...print cleanup message...
#
#   call:   r = Resource("test"); del r
#   output: Cleanup message printed




# 65. Metaclass preview (class of a class)
#
#   class SingletonMeta(type):
#       _instances = {}
#       def __call__(cls, *args, **kwargs):
#           if cls not in cls._instances:
#               cls._instances[cls] = ...create instance...
#           return cls._instances[cls]
#
#   call:   (demo singleton pattern)
#   output: Only one instance created




# 66. Dataclass @dataclass (Python 3.7+)
#
#   from dataclasses import dataclass
#   @dataclass
#   class Person:
#       name: str
#       age: int
#
#   call:   person = Person("Alice", 30)
#   output: Person with auto-generated __init__ and __repr__




# 67. Inheritance with multiple levels and super()
#
#   class A:
#       def method(self): ...return "A"...
#   class B(A):
#       def method(self): ...return super().method() + "B"...
#   class C(B):
#       def method(self): ...return super().method() + "C"...
#
#   call:   c = C(); c.method()
#   output: "ABC"




# 68. Diamond problem (multiple inheritance)
#
#   class A: pass
#   class B(A): pass
#   class C(A): pass
#   class D(B, C): pass
#
#   call:   print(D.__mro__)
#   output: (D, B, C, A, object)




# 69. Class with property and private attributes
#
#   class Rectangle:
#       def __init__(self, width, height):
#           self._width = width
#           self._height = height
#       @property
#       def area(self):
#           ...return width * height...
#       @property
#       def perimeter(self):
#           ...return 2 * (width + height)...
#
#   call:   rect = Rectangle(4, 5); rect.area
#   output: 20




# 70. Operator overloading with __str__, __repr__, and __format__
#
#   class Money:
#       def __init__(self, amount, currency):
#           self.amount = amount
#           self.currency = currency
#       def __str__(self):
#           ...return formatted string...
#       def __repr__(self):
#           ...return Money(amount, currency)...
#       def __format__(self, spec):
#           ...return formatted based on spec...
#
#   call:   m = Money(100, "USD"); print(m)
#   output: "100 USD"




# 71. Inherhitance with property override
#
#   class Animal:
#       @property
#       def sound(self):
#           ...return "Generic sound"...
#
#   class Dog(Animal):
#       @property
#       def sound(self):
#           ...return "Woof"...
#
#   call:   dog = Dog(); print(dog.sound)
#   output: "Woof"




# 72. Method as property (no @property decorator, just naming)
#
#   class Circle:
#       def __init__(self, radius):
#           self.radius = radius
#       def get_circumference(self):
#           ...return 2 * pi * radius...
#
#   call:   circle = Circle(5); circle.get_circumference()
#   output: ~31.4




# 73. Class inheritance with different __init__ signatures
#
#   class Parent:
#       def __init__(self, name):
#           self.name = name
#
#   class Child(Parent):
#       def __init__(self, name, age):
#           ...call super().__init__(name)...
#           self.age = age
#
#   call:   child = Child("Alice", 10)
#   output: Child with name and age




# 74. Type checking with type() function
#
#   class Dog: pass
#   class Cat: pass
#
#   call:   dog = Dog(); type(dog) == Dog
#   output: True




# 75. Type checking isinstance() vs type()
#
#   class Animal: pass
#   class Dog(Animal): pass
#
#   call:   dog = Dog(); isinstance(dog, Animal) vs type(dog) == Animal
#   output: isinstance is True, type check is False




# 76. Class with object initialization logic
#
#   class Config:
#       def __init__(self, **settings):
#           ...validate all settings...
#           ...store validated settings...
#
#   call:   config = Config(timeout=30, debug=True)
#   output: Config with validated settings




# 77. Inheritance with mixin class pattern
#
#   class TimestampMixin:
#       def timestamp(self):
#           ...return current timestamp...
#
#   class Document(TimestampMixin):
#       def __init__(self, title):
#           self.title = title
#
#   call:   doc = Document("Test"); doc.timestamp()
#   output: Current timestamp




# 78. Class variable vs instance variable in memory
#
#   class Test:
#       class_var = []
#       def __init__(self):
#           self.instance_var = []
#
#   call:   (demonstrate difference)
#   output: class_var shared, instance_var separate




# 79. Inheritance from built-in types
#
#   class MyList(list):
#       def first(self):
#           ...return self[0]...
#
#   call:   ml = MyList([1, 2, 3]); ml.first()
#   output: 1




# 80. Inheritance from built-in dict
#
#   class MyDict(dict):
#       def get_or_default(self, key, default=None):
#           ...return self.get(key, default)...
#
#   call:   md = MyDict({"a": 1}); md.get_or_default("b", 0)
#   output: 0




# 81. Class method modifying class state
#
#   class Registry:
#       items = []
#       @classmethod
#       def register(cls, item):
#           cls.items.append(item)
#       @classmethod
#       def get_all(cls):
#           ...return cls.items...
#
#   call:   Registry.register("item1"); Registry.get_all()
#   output: ["item1"]




# 82. __getattr__ for dynamic attribute access
#
#   class DynamicAttrs:
#       def __getattr__(self, name):
#           ...return f"Attribute {name} not found"...
#
#   call:   da = DynamicAttrs(); da.anything
#   output: "Attribute anything not found"




# 83. __getattribute__ override (all attribute access)
#
#   class Logged:
#       def __getattribute__(self, name):
#           print(f"Accessing {name}")
#           ...return super().__getattribute__(name)...
#
#   call:   l = Logged(); l.x
#   output: "Accessing x" printed




# 84. Abstract methods with NotImplementedError
#
#   class Shape:
#       def area(self):
#           ...raise NotImplementedError...
#       def perimeter(self):
#           ...raise NotImplementedError...
#
#   class Circle(Shape):
#       def area(self):
#           ...compute area...
#
#   call:   circle = Circle(); circle.area()
#   output: Area computed




# 85. Class with validation in __init__
#
#   class User:
#       def __init__(self, email, age):
#           ...validate email format...
#           ...validate age >= 0...
#           self.email = email
#           self.age = age
#
#   call:   user = User("test@example.com", 25)
#   output: User object created




# 86. Multiple inheritance with method conflict resolution
#
#   class A:
#       def method(self): ...return "A"...
#   class B:
#       def method(self): ...return "B"...
#   class C(A, B):
#       pass
#
#   call:   c = C(); c.method()
#   output: "A" (MRO resolves to A first)




# 87. Object comparison with __ne__
#
#   class Person:
#       def __init__(self, name):
#           self.name = name
#       def __eq__(self, other):
#           ...return self.name == other.name...
#       def __ne__(self, other):
#           ...return not self.__eq__(other)...
#
#   call:   p1 = Person("Alice"); p2 = Person("Bob"); p1 != p2
#   output: True




# 88. Class with inheritance and property override
#
#   class Base:
#       def __init__(self, value):
#           self._value = value
#       @property
#       def value(self):
#           ...return self._value...
#
#   class Derived(Base):
#       @property
#       def value(self):
#           ...return self._value * 2...
#
#   call:   d = Derived(5); d.value
#   output: 10




# 89. __index__ for integer conversion
#
#   class CustomInt:
#       def __init__(self, value):
#           self.value = value
#       def __index__(self):
#           ...return self.value...
#
#   call:   ci = CustomInt(5); lst = [1, 2, 3]; lst[ci]
#   output: lst[5] raises IndexError or lst[5]




# 90. Class with lazy evaluation
#
#   class LazyValue:
#       def __init__(self, fn):
#           self._fn = fn
#           self._value = None
#       @property
#       def value(self):
#           if self._value is None:
#               ...self._value = self._fn()...
#           return self._value
#
#   call:   lv = LazyValue(lambda: 10 + 20); lv.value
#   output: 30 (computed on first access)




# 91. Inheritance with __init__ chain
#
#   class A:
#       def __init__(self):
#           print("A")
#   class B(A):
#       def __init__(self):
#           ...super().__init__()...
#           print("B")
#   class C(B):
#       def __init__(self):
#           ...super().__init__()...
#           print("C")
#
#   call:   c = C()
#   output: "A", "B", "C"




# 92. Class adapting from dict to object
#
#   class DictToObj:
#       def __init__(self, data_dict):
#           ...set all keys as attributes...
#
#   call:   obj = DictToObj({"name": "Alice", "age": 30}); obj.name
#   output: "Alice"




# 93. Class with read-only properties
#
#   class Immutable:
#       def __init__(self, value):
#           self._value = value
#       @property
#       def value(self):
#           ...return self._value...
#       @value.setter
#       def value(self, val):
#           ...raise AttributeError("read-only")...
#
#   call:   im = Immutable(10); im.value = 20
#   output: AttributeError: read-only




# 94. Operator overloading with __truediv__ for /
#
#   class Vector:
#       def __init__(self, x, y):
#           self.x = x
#           self.y = y
#       def __truediv__(self, scalar):
#           ...return new Vector with divided coordinates...
#
#   call:   v = Vector(10, 20); v2 = v / 2
#   output: v2.x = 5, v2.y = 10




# 95. Class with dependency injection
#
#   class Logger:
#       def log(self, msg): ...print msg...
#
#   class Service:
#       def __init__(self, logger):
#           self.logger = logger
#       def do_work(self):
#           ...self.logger.log("Working")...
#
#   call:   logger = Logger(); service = Service(logger); service.do_work()
#   output: "Working" printed




# 96. Abstract base class (Python ABC module preview)
#
#   from abc import ABC, abstractmethod
#   class Animal(ABC):
#       @abstractmethod
#       def speak(self):
#           pass
#
#   class Dog(Animal):
#       def speak(self):
#           ...return "Woof"...
#
#   call:   dog = Dog(); dog.speak()
#   output: "Woof"




# 97. Inheritance with cached property
#
#   from functools import cached_property
#   class Circle:
#       def __init__(self, radius):
#           self.radius = radius
#       @cached_property
#       def area(self):
#           ...return pi * radius^2...
#
#   call:   circle = Circle(5); circle.area
#   output: ~78.54 (cached on first access)




# 98. Class composition with multiple objects
#
#   class Engine: pass
#   class Transmission: pass
#   class Car:
#       def __init__(self):
#           self.engine = Engine()
#           self.transmission = Transmission()
#
#   call:   car = Car(); car.engine, car.transmission
#   output: Engine and Transmission objects




# 99. Complex class hierarchy with shared behavior
#
#   class Vehicle:
#       def __init__(self, brand):
#           self.brand = brand
#       def start(self):
#           ...return "Starting"...
#   class Car(Vehicle):
#       def start(self):
#           ...return super().start() + " car"...
#   class Motorcycle(Vehicle):
#       def start(self):
#           ...return super().start() + " motorcycle"...
#
#   call:   car = Car("Toyota"); moto = Motorcycle("Harley"); car.start(); moto.start()
#   output: "Starting car", "Starting motorcycle"




# 100. BOSS DRILL: Complete User Management System
#
#   Create a user management system combining:
#   - Multiple classes with inheritance
#   - Magic methods for comparison and representation
#   - Properties with validation
#   - Class methods for factory pattern
#   - Static methods for utilities
#   - Polymorphism
#
#   class User:
#       """Base user class"""
#       def __init__(self, username, email):
#           ...validate username and email...
#           self.username = username
#           self.email = email
#           self.created_at = ...current time...
#
#       def __str__(self):
#           ...return formatted user info...
#       def __repr__(self):
#           ...return User('...', '...')...
#       def __eq__(self, other):
#           ...compare by username...
#       def __lt__(self, other):
#           ...compare by creation time...
#
#       @property
#       def email(self):
#           ...return self._email...
#       @email.setter
#       def email(self, value):
#           ...validate email format...
#           self._email = value
#
#       @staticmethod
#       def is_valid_email(email):
#           ...check "@" and domain...
#
#       @classmethod
#       def from_user_dict(cls, user_data):
#           ...create User from {"username": ..., "email": ...}...
#
#   class Admin(User):
#       """Admin user with permissions"""
#       def __init__(self, username, email, permissions=None):
#           ...super().__init__(username, email)...
#           self.permissions = permissions or []
#
#       def grant_permission(self, permission):
#           ...add permission...
#       def has_permission(self, permission):
#           ...check permission...
#
#   class UserRegistry:
#       """Manage multiple users"""
#       def __init__(self):
#           self.users = {}
#
#       def add_user(self, user):
#           ...validate user instance...
#           ...store by username...
#       def find_user(self, username):
#           ...return user or None...
#       def get_all_users(self):
#           ...return list of all users...
#       def get_admins(self):
#           ...return only Admin instances...
#       def remove_user(self, username):
#           ...remove user from registry...
#
#   call:
#       - Create users and admins from user_data list
#       - Add them to registry
#       - Find specific users
#       - List all users sorted
#       - Filter admins
#       - Demonstrate polymorphism (both User and Admin have email property)
#
#   output: Complete user management with:
#       - 3+ users of mixed types
#       - Admin with permissions
#       - Search results
#       - Sorted user list
#       - Polymorphic method calls