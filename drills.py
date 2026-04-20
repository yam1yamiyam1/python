# =============================================================================
# 200 PYTHON BACKEND DRILLS
# Concepts: Pydantic, Async/Await, Decorators (Wrapper/Registry/OOP), Dynamic Dispatch
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 01 — Pydantic: BaseModel basics
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a Product model with:
#   - name: str
#   - price: float
#   - in_stock: bool

# TODO: Create a Product instance with:
#   - name: "Keyboard"
#   - price: 49.99
#   - in_stock: True

# TODO: Print each field on its own line:
#   - print(product.name)
#   - print(product.price)
#   - print(product.in_stock)

# EXPECTED:
# Keyboard
# 49.99
# True


# -----------------------------------------------------------------------------
# DRILL 02 — Pydantic: Field with gt and min_length
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field

# TODO: Define an Item model with:
#   - name: str with min_length=3
#   - quantity: int with gt=0

# TODO: Create a valid Item with:
#   - name: "Pen"
#   - quantity: 5

# TODO: Print the item

# EXPECTED:
# name='Pen' quantity=5


# -----------------------------------------------------------------------------
# DRILL 03 — Pydantic: Catching ValidationError on Field constraint
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field, ValidationError

# TODO: Define an Item model with:
#   - name: str with min_length=3
#   - quantity: int with gt=0

# TODO: Try creating an Item with:
#   - name: "Pen"
#   - quantity: -1

# TODO: Wrap it in a try/except block that:
#   - catches ValidationError
#   - prints "Invalid: <the error>"

# EXPECTED:
# Invalid: 1 validation error for Item
# quantity
#   Input should be greater than 0 ...


# -----------------------------------------------------------------------------
# DRILL 04 — Pydantic: Converting a dict to a model using **unpacking
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a Car model with:
#   - brand: str
#   - year: int

# TODO: Create a dict called `data` with:
#   - brand: "Toyota"
#   - year: 2020

# TODO: Unpack `data` into a Car instance using **data

# TODO: Print the car

# EXPECTED:
# brand='Toyota' year=2020


# -----------------------------------------------------------------------------
# DRILL 05 — Pydantic: model_dump() to convert model back to dict
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a User model with:
#   - username: str
#   - email: str

# TODO: Create a User with:
#   - username: "john"
#   - email: "john@example.com"

# TODO: Call .model_dump() on the user and print the result

# EXPECTED:
# {'username': 'john', 'email': 'john@example.com'}


# -----------------------------------------------------------------------------
# DRILL 06 — Pydantic: Optional field with default value
# -----------------------------------------------------------------------------
from pydantic import BaseModel
from typing import Optional

# TODO: Define a Profile model with:
#   - name: str
#   - bio: Optional[str] with default=None

# TODO: Create a Profile with only name="Alice" (no bio)

# TODO: Print the profile

# EXPECTED:
# name='Alice' bio=None


# -----------------------------------------------------------------------------
# DRILL 07 — Pydantic: Nested model
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define an Address model with:
#   - city: str
#   - zip_code: str

# TODO: Define a Person model with:
#   - name: str
#   - address: Address

# TODO: Create a Person with:
#   - name: "Bob"
#   - address: Address(city="Manila", zip_code="1000")

# TODO: Print person.address.city

# EXPECTED:
# Manila


# -----------------------------------------------------------------------------
# DRILL 08 — Pydantic: Catching ValidationError on wrong type
# -----------------------------------------------------------------------------
from pydantic import BaseModel, ValidationError

# TODO: Define a Box model with:
#   - width: float
#   - height: float

# TODO: Try creating a Box with:
#   - width: "wide"
#   - height: 10.0

# TODO: Wrap it in a try/except block that:
#   - catches ValidationError
#   - prints "Caught: <the error>"

# EXPECTED:
# Caught: 1 validation error for Box
# width
#   Input should be a valid number ...


# -----------------------------------------------------------------------------
# DRILL 09 — Pydantic: Field with max_length
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field, ValidationError

# TODO: Define a Tag model with:
#   - label: str with min_length=1 and max_length=10

# TODO: Try creating a Tag with:
#   - label: "this-is-too-long-for-a-tag"

# TODO: Wrap it in a try/except block that:
#   - catches ValidationError
#   - prints "Error: <the error>"

# EXPECTED:
# Error: 1 validation error for Tag
# label
#   String should have at most 10 characters ...


# -----------------------------------------------------------------------------
# DRILL 10 — Pydantic: List field
# -----------------------------------------------------------------------------
from pydantic import BaseModel
from typing import List

# TODO: Define a Playlist model with:
#   - title: str
#   - songs: List[str]

# TODO: Create a Playlist with:
#   - title: "Chill"
#   - songs: ["Song A", "Song B", "Song C"]

# TODO: Print playlist.title and then each song in a for loop

# EXPECTED:
# Chill
# Song A
# Song B
# Song C


# -----------------------------------------------------------------------------
# DRILL 11 — Async: Basic async def and asyncio.run()
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `greet` that:
#   - prints "Hello from async"

# TODO: Run `greet` using asyncio.run()

# EXPECTED:
# Hello from async


# -----------------------------------------------------------------------------
# DRILL 12 — Async: await asyncio.sleep() inside async def
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `delayed_hello` that:
#   - awaits asyncio.sleep(1)
#   - prints "Done waiting"

# TODO: Run `delayed_hello` using asyncio.run()

# EXPECTED: (after ~1 second)
# Done waiting


# -----------------------------------------------------------------------------
# DRILL 13 — Async: Returning a value from an async function
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `get_number` that:
#   - returns 42

# TODO: Define an async function called `main` that:
#   - awaits get_number() and stores the result in `result`
#   - prints result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# 42


# -----------------------------------------------------------------------------
# DRILL 14 — Async: Awaiting two functions in sequence
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `fetch_user` that:
#   - awaits asyncio.sleep(0)
#   - returns "Alice"

# TODO: Define an async function called `fetch_score` that:
#   - awaits asyncio.sleep(0)
#   - returns 99

# TODO: Define an async function called `main` that:
#   - awaits both functions and stores results
#   - prints "<user> scored <score>"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Alice scored 99


# -----------------------------------------------------------------------------
# DRILL 15 — Async: asyncio.gather() for concurrent execution
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `task` that takes a `name` param and:
#   - awaits asyncio.sleep(0)
#   - prints f"Task {name} done"

# TODO: Define an async function called `main` that:
#   - uses asyncio.gather() to run task("A"), task("B"), task("C") concurrently

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Task A done
# Task B done
# Task C done


# -----------------------------------------------------------------------------
# DRILL 16 — Async: Passing arguments to async functions
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `multiply` that:
#   - takes `a` and `b` as params
#   - returns a * b

# TODO: Define an async function called `main` that:
#   - awaits multiply(6, 7) and prints the result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# 42


# -----------------------------------------------------------------------------
# DRILL 17 — Async: Async function calling another async function
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `get_prefix` that:
#   - returns "Mr."

# TODO: Define an async function called `get_full_greeting` that:
#   - awaits get_prefix() and stores it in `prefix`
#   - returns f"{prefix} Smith"

# TODO: Define an async function called `main` that:
#   - awaits get_full_greeting() and prints the result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Mr. Smith


# -----------------------------------------------------------------------------
# DRILL 18 — Async: List of results from asyncio.gather()
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `square` that:
#   - takes `n` as a param
#   - returns n * n

# TODO: Define an async function called `main` that:
#   - uses asyncio.gather() to run square(2), square(3), square(4)
#   - stores all results in `results`
#   - prints results

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# [4, 9, 16]


# -----------------------------------------------------------------------------
# DRILL 19 — Async: Try/except inside async function
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `risky` that:
#   - raises ValueError("something went wrong")

# TODO: Define an async function called `main` that:
#   - awaits risky() inside a try/except block
#   - catches ValueError and prints "Caught: <the error>"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Caught: something went wrong


# -----------------------------------------------------------------------------
# DRILL 20 — Async: Async function with a loop
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `count_up` that:
#   - loops from 1 to 3 (inclusive)
#   - awaits asyncio.sleep(0) each iteration
#   - prints the current number each iteration

# TODO: Run `count_up` using asyncio.run()

# EXPECTED:
# 1
# 2
# 3


# -----------------------------------------------------------------------------
# DRILL 21 — Wrapper Decorator: Basic interception
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `logger` that:
#   - wraps any function
#   - prints "Calling <function name>" before calling it
#   - prints "Done" after calling it

# TODO: Apply @logger to a function called `say_hello` that:
#   - prints "Hello!"

# TODO: Call say_hello()

# EXPECTED:
# Calling say_hello
# Hello!
# Done


# -----------------------------------------------------------------------------
# DRILL 22 — Wrapper Decorator: Intercepting and printing args
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `show_args` that:
#   - wraps any function
#   - prints "Args: <args>" before calling the function

# TODO: Apply @show_args to a function called `add` that:
#   - takes `a` and `b`
#   - returns a + b

# TODO: Call add(3, 4) and print the result

# EXPECTED:
# Args: (3, 4)
# 7


# -----------------------------------------------------------------------------
# DRILL 23 — Wrapper Decorator: Intercepting kwargs
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `show_kwargs` that:
#   - wraps any function using *args, **kwargs
#   - prints "Kwargs: <kwargs>" before calling the function

# TODO: Apply @show_kwargs to a function called `greet` that:
#   - takes `name` and `title`
#   - prints f"{title} {name}"

# TODO: Call greet(name="Alice", title="Dr.")

# EXPECTED:
# Kwargs: {'name': 'Alice', 'title': 'Dr.'}
# Dr. Alice


# -----------------------------------------------------------------------------
# DRILL 24 — Wrapper Decorator: Modifying the return value
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `shout` that:
#   - wraps any function
#   - calls the function and stores its return value
#   - returns the result uppercased

# TODO: Apply @shout to a function called `get_word` that:
#   - returns "hello"

# TODO: Print get_word()

# EXPECTED:
# HELLO


# -----------------------------------------------------------------------------
# DRILL 25 — Wrapper Decorator: Checking a kwarg before calling
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `require_name` that:
#   - wraps any function using *args, **kwargs
#   - checks if "name" is in kwargs
#   - if not, prints "Error: name is required" and returns None
#   - otherwise calls the function normally

# TODO: Apply @require_name to a function called `greet` that:
#   - takes **kwargs
#   - prints f"Hello {kwargs['name']}"

# TODO: Call greet() with no arguments
# TODO: Call greet(name="Bob")

# EXPECTED:
# Error: name is required
# Hello Bob


# -----------------------------------------------------------------------------
# DRILL 26 — Wrapper Decorator: Using functools.wraps
# -----------------------------------------------------------------------------
from functools import wraps

# TODO: Define a decorator called `my_decorator` that:
#   - uses @wraps(func) on the inner wrapper
#   - just calls the wrapped function normally

# TODO: Apply @my_decorator to a function called `do_work` that:
#   - has docstring "Does important work"
#   - prints "Working..."

# TODO: Print do_work.__name__ and do_work.__doc__

# EXPECTED:
# do_work
# Does important work


# -----------------------------------------------------------------------------
# DRILL 27 — Wrapper Decorator: Counting how many times a function is called
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `count_calls` that:
#   - keeps track of how many times the wrapped function is called
#   - stores the count on the wrapper as wrapper.calls
#   - calls the original function normally

# TODO: Apply @count_calls to a function called `ping` that:
#   - prints "ping"

# TODO: Call ping() three times
# TODO: Print ping.calls

# EXPECTED:
# ping
# ping
# ping
# 3


# -----------------------------------------------------------------------------
# DRILL 28 — Wrapper Decorator: Timer decorator
# -----------------------------------------------------------------------------
import time

# TODO: Define a decorator called `timer` that:
#   - records the time before calling the function using time.time()
#   - calls the function
#   - records the time after
#   - prints f"Elapsed: <elapsed> seconds"

# TODO: Apply @timer to a function called `slow_task` that:
#   - calls time.sleep(0.1)
#   - prints "Task done"

# TODO: Call slow_task()

# EXPECTED:
# Task done
# Elapsed: 0.1... seconds


# -----------------------------------------------------------------------------
# DRILL 29 — Wrapper Decorator: Decorator with its own argument (factory)
# -----------------------------------------------------------------------------

# TODO: Define a decorator factory called `repeat` that:
#   - takes `times` as a parameter
#   - returns a decorator that calls the wrapped function `times` times

# TODO: Apply @repeat(times=3) to a function called `wave` that:
#   - prints "Hello!"

# TODO: Call wave()

# EXPECTED:
# Hello!
# Hello!
# Hello!


# -----------------------------------------------------------------------------
# DRILL 30 — Wrapper Decorator: Blocking a call based on a kwarg value
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `admin_only` that:
#   - wraps any function using *args, **kwargs
#   - checks if kwargs.get("role") == "admin"
#   - if not, prints "Access denied" and returns None
#   - otherwise calls the function normally

# TODO: Apply @admin_only to a function called `delete_record` that:
#   - prints "Record deleted"

# TODO: Call delete_record(role="user")
# TODO: Call delete_record(role="admin")

# EXPECTED:
# Access denied
# Record deleted


# -----------------------------------------------------------------------------
# DRILL 31 — Registry Decorator: Saving a function to a dict
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `registry`

# TODO: Define a decorator called `register` that:
#   - saves the function to registry using the function's name as the key
#   - returns the function unchanged (no wrapper)

# TODO: Apply @register to a function called `send_email` that:
#   - prints "Sending email"

# TODO: Print registry

# EXPECTED:
# {'send_email': <function send_email at 0x...>}


# -----------------------------------------------------------------------------
# DRILL 32 — Registry Decorator: Registering multiple functions
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `handlers`

# TODO: Define a decorator called `handler` that:
#   - saves the function to handlers using the function's name as the key
#   - returns the function unchanged

# TODO: Apply @handler to:
#   - a function called `on_login` that prints "User logged in"
#   - a function called `on_logout` that prints "User logged out"

# TODO: Print list(handlers.keys())

# EXPECTED:
# ['on_login', 'on_logout']


# -----------------------------------------------------------------------------
# DRILL 33 — Registry Decorator: Calling a function from the registry by name
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `commands`

# TODO: Define a decorator called `command` that:
#   - saves the function to commands using the function's name as the key
#   - returns the function unchanged

# TODO: Apply @command to a function called `reboot` that:
#   - prints "Rebooting system"

# TODO: Look up "reboot" in commands and call it

# EXPECTED:
# Rebooting system


# -----------------------------------------------------------------------------
# DRILL 34 — Registry Decorator: Custom string key instead of function name
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `routes`

# TODO: Define a decorator factory called `route` that:
#   - takes a `path` string as a parameter
#   - saves the function to routes using `path` as the key
#   - returns the function unchanged

# TODO: Apply @route("/home") to a function called `home_view` that:
#   - prints "Home page"

# TODO: Apply @route("/about") to a function called `about_view` that:
#   - prints "About page"

# TODO: Print list(routes.keys())

# EXPECTED:
# ['/home', '/about']


# -----------------------------------------------------------------------------
# DRILL 35 — Registry Decorator: Calling a route from the registry by path
# -----------------------------------------------------------------------------

# TODO: Reuse the `routes` dict and `route` decorator from DRILL 34

# TODO: Look up "/home" in routes and call it
# TODO: Look up "/about" in routes and call it

# EXPECTED:
# Home page
# About page


# -----------------------------------------------------------------------------
# DRILL 36 — Registry Decorator: Registering with metadata
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `task_registry`

# TODO: Define a decorator factory called `task` that:
#   - takes a `priority` int as a parameter
#   - saves {"fn": func, "priority": priority} to task_registry using the function's name as key
#   - returns the function unchanged

# TODO: Apply @task(priority=1) to a function called `cleanup` that:
#   - prints "Cleaning up"

# TODO: Apply @task(priority=5) to a function called `send_report` that:
#   - prints "Sending report"

# TODO: Print task_registry["cleanup"]["priority"]
# TODO: Print task_registry["send_report"]["priority"]

# EXPECTED:
# 1
# 5


# -----------------------------------------------------------------------------
# DRILL 37 — Registry Decorator: Listing all registered keys
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `plugins`

# TODO: Define a decorator called `plugin` that:
#   - saves the function to plugins using the function's name as the key
#   - returns the function unchanged

# TODO: Apply @plugin to three functions:
#   - `auth_plugin` that prints "Auth"
#   - `cache_plugin` that prints "Cache"
#   - `log_plugin` that prints "Log"

# TODO: Print all registered plugin names using a for loop

# EXPECTED:
# auth_plugin
# cache_plugin
# log_plugin


# -----------------------------------------------------------------------------
# DRILL 38 — Registry Decorator: Running all registered functions
# -----------------------------------------------------------------------------

# TODO: Reuse the `plugins` dict from DRILL 37 (or recreate it)

# TODO: Loop through plugins.values() and call each one

# EXPECTED:
# Auth
# Cache
# Log


# -----------------------------------------------------------------------------
# DRILL 39 — Registry Decorator: Checking if a key exists before calling
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `services`

# TODO: Define a decorator called `service` that:
#   - saves the function to services using the function's name as the key
#   - returns the function unchanged

# TODO: Apply @service to a function called `mailer` that:
#   - prints "Sending mail"

# TODO: Write logic that:
#   - checks if "mailer" is in services and calls it if so
#   - checks if "fax_machine" is in services and prints "Not found" if not

# EXPECTED:
# Sending mail
# Not found


# -----------------------------------------------------------------------------
# DRILL 40 — Registry Decorator: Registry as a simple event system
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `event_listeners`

# TODO: Define a decorator factory called `on` that:
#   - takes an `event` string as a parameter
#   - saves the function to event_listeners using `event` as the key
#   - returns the function unchanged

# TODO: Apply @on("user.created") to a function called `send_welcome` that:
#   - prints "Welcome email sent"

# TODO: Apply @on("user.deleted") to a function called `cleanup_data` that:
#   - prints "User data cleaned up"

# TODO: Simulate firing "user.created" by:
#   - looking it up in event_listeners and calling it

# EXPECTED:
# Welcome email sent


# -----------------------------------------------------------------------------
# DRILL 41 — OOP Decorator: Decorating a method, accessing self
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `log_method` that:
#   - wraps any function using *args, **kwargs
#   - accesses the instance via args[0]
#   - prints f"Calling method on: <instance>"
#   - then calls the original function

# TODO: Define a class called `Engine` with:
#   - a method called `start` decorated with @log_method
#   - start() prints "Engine started"

# TODO: Create an Engine instance and call start()

# EXPECTED:
# Calling method on: <__main__.Engine object at 0x...>
# Engine started


# -----------------------------------------------------------------------------
# DRILL 42 — OOP Decorator: Reading self.state inside a decorator
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `check_state` that:
#   - wraps any function using *args, **kwargs
#   - accesses the instance via args[0]
#   - prints f"State is: <instance.state>"
#   - calls the original function

# TODO: Define a class called `Machine` with:
#   - __init__ that sets self.state = "idle"
#   - a method called `run` decorated with @check_state
#   - run() prints "Running"

# TODO: Create a Machine instance and call run()

# EXPECTED:
# State is: idle
# Running


# -----------------------------------------------------------------------------
# DRILL 43 — OOP Decorator: Modifying self.state inside a decorator
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `set_running` that:
#   - wraps any function using *args, **kwargs
#   - accesses the instance via args[0]
#   - sets instance.state = "running" before calling the function
#   - calls the original function

# TODO: Define a class called `Worker` with:
#   - __init__ that sets self.state = "idle"
#   - a method called `do_work` decorated with @set_running
#   - do_work() prints f"State during work: {self.state}"

# TODO: Create a Worker instance and call do_work()
# TODO: Print worker.state after the call

# EXPECTED:
# State during work: running
# running


# -----------------------------------------------------------------------------
# DRILL 44 — OOP Decorator: Blocking method call based on self.state
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `require_idle` that:
#   - wraps any function using *args, **kwargs
#   - accesses the instance via args[0]
#   - if instance.state != "idle", prints "Blocked: not idle" and returns None
#   - otherwise calls the function normally

# TODO: Define a class called `Server` with:
#   - __init__ that sets self.state = "busy"
#   - a method called `restart` decorated with @require_idle
#   - restart() prints "Restarting"

# TODO: Create a Server instance and call restart()

# EXPECTED:
# Blocked: not idle


# -----------------------------------------------------------------------------
# DRILL 45 — OOP Decorator: Resetting self.state after method call
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `reset_after` that:
#   - wraps any function using *args, **kwargs
#   - calls the original function
#   - after the call, sets instance.state = "idle" (access via args[0])

# TODO: Define a class called `Task` with:
#   - __init__ that sets self.state = "pending"
#   - a method called `execute` decorated with @reset_after
#   - execute() sets self.state = "done" and prints "Executing"

# TODO: Create a Task instance and call execute()
# TODO: Print task.state after the call

# EXPECTED:
# Executing
# idle


# -----------------------------------------------------------------------------
# DRILL 46 — OOP Decorator: Logging self.name from inside decorator
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `log_name` that:
#   - wraps any function using *args, **kwargs
#   - accesses the instance via args[0]
#   - prints f"Running on: <instance.name>"
#   - calls the original function

# TODO: Define a class called `Bot` with:
#   - __init__ that takes a `name` param and sets self.name = name
#   - a method called `speak` decorated with @log_name
#   - speak() prints "Beep boop"

# TODO: Create a Bot("R2D2") instance and call speak()

# EXPECTED:
# Running on: R2D2
# Beep boop


# -----------------------------------------------------------------------------
# DRILL 47 — OOP Decorator: Decorator that modifies return value of a method
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `uppercase_result` that:
#   - wraps any function using *args, **kwargs
#   - calls the function and stores the return value
#   - returns the value uppercased

# TODO: Define a class called `Greeter` with:
#   - a method called `greet` decorated with @uppercase_result
#   - greet() returns "hello world"

# TODO: Create a Greeter instance, call greet(), and print the result

# EXPECTED:
# HELLO WORLD


# -----------------------------------------------------------------------------
# DRILL 48 — OOP Decorator: Tracking call count on the instance
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `track_calls` that:
#   - wraps any function using *args, **kwargs
#   - accesses the instance via args[0]
#   - increments instance.call_count by 1
#   - calls the original function

# TODO: Define a class called `Counter` with:
#   - __init__ that sets self.call_count = 0
#   - a method called `tick` decorated with @track_calls
#   - tick() prints "Tick"

# TODO: Create a Counter instance and call tick() three times
# TODO: Print counter.call_count

# EXPECTED:
# Tick
# Tick
# Tick
# 3


# -----------------------------------------------------------------------------
# DRILL 49 — OOP Decorator: Passing args to the decorated method
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `log_args` that:
#   - wraps any function using *args, **kwargs
#   - prints f"Args: {args[1:]}" (skip self)
#   - calls the original function

# TODO: Define a class called `Calculator` with:
#   - a method called `add` decorated with @log_args
#   - add() takes `a` and `b` and prints a + b

# TODO: Create a Calculator instance and call add(10, 20)

# EXPECTED:
# Args: (10, 20)
# 30


# -----------------------------------------------------------------------------
# DRILL 50 — OOP Decorator: __repr__ used inside decorator message
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `describe` that:
#   - wraps any function using *args, **kwargs
#   - accesses the instance via args[0]
#   - prints f"Invoking on: {repr(args[0])}"
#   - calls the original function

# TODO: Define a class called `Rocket` with:
#   - __init__ that takes `model` and sets self.model = model
#   - __repr__ that returns f"Rocket({self.model})"
#   - a method called `launch` decorated with @describe
#   - launch() prints "Launching!"

# TODO: Create a Rocket("Falcon9") instance and call launch()

# EXPECTED:
# Invoking on: Rocket(Falcon9)
# Launching!


# -----------------------------------------------------------------------------
# DRILL 51 — Dynamic Dispatch: Looking up and calling a function by string key
# -----------------------------------------------------------------------------

# TODO: Create a dict called `actions` with:
#   - "greet": a function that prints "Hello!"
#   - "bye": a function that prints "Goodbye!"

# TODO: Write logic that:
#   - stores "greet" in a variable called `key`
#   - looks up `key` in actions and calls the result

# EXPECTED:
# Hello!


# -----------------------------------------------------------------------------
# DRILL 52 — Dynamic Dispatch: Calling with a payload dict
# -----------------------------------------------------------------------------

# TODO: Create a dict called `processors` with:
#   - "print_name": a function that takes **payload and prints payload["name"]

# TODO: Create a payload dict with:
#   - name: "Alice"

# TODO: Look up "print_name" in processors and call it with **payload

# EXPECTED:
# Alice


# -----------------------------------------------------------------------------
# DRILL 53 — Dynamic Dispatch: Handling a missing key gracefully
# -----------------------------------------------------------------------------

# TODO: Create a dict called `handlers` with:
#   - "start": a function that prints "Starting"

# TODO: Write logic that:
#   - tries to look up "stop" in handlers
#   - if not found, prints "Unknown command: stop"

# EXPECTED:
# Unknown command: stop


# -----------------------------------------------------------------------------
# DRILL 54 — Dynamic Dispatch: Async function looked up and awaited by key
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `handle_ping` that:
#   - prints "Pong!"

# TODO: Create a dict called `dispatch` with:
#   - "ping": handle_ping

# TODO: Define an async function called `main` that:
#   - stores "ping" in a variable called `event`
#   - looks up `event` in dispatch and awaits the result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Pong!


# -----------------------------------------------------------------------------
# DRILL 55 — Dynamic Dispatch: Awaiting with a payload
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `handle_login` that:
#   - takes **payload
#   - prints f"Logging in: {payload['user']}"

# TODO: Create a dict called `dispatch` with:
#   - "login": handle_login

# TODO: Define an async function called `main` that:
#   - creates a payload dict with user: "Bob"
#   - looks up "login" in dispatch and awaits it with **payload

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Logging in: Bob


# -----------------------------------------------------------------------------
# DRILL 56 — Dynamic Dispatch: Multiple events, one dispatcher function
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions:
#   - `on_start` that prints "Started"
#   - `on_stop` that prints "Stopped"

# TODO: Create a dict called `events` with:
#   - "start": on_start
#   - "stop": on_stop

# TODO: Define an async function called `dispatch` that:
#   - takes an `event` string
#   - looks up the event in events and awaits it
#   - if not found, prints "Unknown event"

# TODO: Define an async function called `main` that:
#   - awaits dispatch("start")
#   - awaits dispatch("stop")
#   - awaits dispatch("pause")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Started
# Stopped
# Unknown event


# -----------------------------------------------------------------------------
# DRILL 57 — Dynamic Dispatch: Dispatch with payload and registry decorator
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `router`

# TODO: Define a decorator called `route` that:
#   - takes an `event` string
#   - saves the function to router using `event` as the key
#   - returns the function unchanged

# TODO: Apply @route("buy") to an async function called `handle_buy` that:
#   - takes **payload
#   - prints f"Buying: {payload['item']}"

# TODO: Define an async function called `main` that:
#   - creates a payload dict with item: "Laptop"
#   - looks up "buy" in router and awaits it with **payload

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Buying: Laptop


# -----------------------------------------------------------------------------
# DRILL 58 — Dynamic Dispatch: Dispatch table built from registry decorator
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `cmd_registry`

# TODO: Define a decorator called `cmd` that:
#   - takes a `name` string
#   - saves the function to cmd_registry using `name` as the key
#   - returns the function unchanged

# TODO: Apply @cmd("ping") to async function `ping_handler` that prints "Pong"
# TODO: Apply @cmd("status") to async function `status_handler` that prints "All OK"

# TODO: Define an async function called `run_command` that:
#   - takes a `name` string
#   - looks up name in cmd_registry and awaits it
#   - if not found, prints f"No command: {name}"

# TODO: Define an async function called `main` that:
#   - awaits run_command("ping")
#   - awaits run_command("status")
#   - awaits run_command("reboot")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Pong
# All OK
# No command: reboot


# -----------------------------------------------------------------------------
# DRILL 59 — Dynamic Dispatch: Passing the event name into the handler
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `generic_handler` that:
#   - takes **payload
#   - prints f"Handling event: {payload['event']}"

# TODO: Create a dict called `dispatch` with:
#   - "click": generic_handler
#   - "hover": generic_handler

# TODO: Define an async function called `fire` that:
#   - takes an `event` string
#   - looks up the event in dispatch
#   - calls it with payload={"event": event}

# TODO: Define an async function called `main` that:
#   - awaits fire("click")
#   - awaits fire("hover")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Handling event: click
# Handling event: hover


# -----------------------------------------------------------------------------
# DRILL 60 — Dynamic Dispatch: Chained dispatch — one handler calls another
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `pipeline`

# TODO: Define a decorator called `step` that:
#   - takes a `name` string
#   - saves the function to pipeline using `name` as the key
#   - returns the function unchanged

# TODO: Apply @step("validate") to async function `validate` that:
#   - prints "Validating..."
#   - awaits the next step by looking up "process" in pipeline and calling it

# TODO: Apply @step("process") to async function `process` that:
#   - prints "Processing..."

# TODO: Define an async function called `main` that:
#   - looks up "validate" in pipeline and awaits it

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Validating...
# Processing...


# -----------------------------------------------------------------------------
# DRILL 61 — Mix: Pydantic model passed as payload to async handler
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define a model called `Order` with:
#   - item: str
#   - quantity: int

# TODO: Define an async function called `handle_order` that:
#   - takes an `order` of type Order
#   - prints f"Order received: {order.quantity}x {order.item}"

# TODO: Define an async function called `main` that:
#   - creates an Order with item="Book", quantity=3
#   - awaits handle_order(order)

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Order received: 3x Book


# -----------------------------------------------------------------------------
# DRILL 62 — Mix: Wrapper decorator on an async function
# -----------------------------------------------------------------------------
import asyncio
from functools import wraps

# TODO: Define a decorator called `async_logger` that:
#   - wraps an async function
#   - prints "Before" before awaiting it
#   - prints "After" after awaiting it

# TODO: Apply @async_logger to an async function called `fetch_data` that:
#   - prints "Fetching..."

# TODO: Run fetch_data() using asyncio.run()

# EXPECTED:
# Before
# Fetching...
# After


# -----------------------------------------------------------------------------
# DRILL 63 — Mix: Registry decorator storing async functions, then dispatching
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `event_bus`

# TODO: Define a decorator called `listen` that:
#   - takes an `event` string
#   - saves the async function to event_bus using `event` as the key
#   - returns the function unchanged

# TODO: Apply @listen("order.placed") to async function `on_order_placed` that:
#   - prints "Processing new order"

# TODO: Define an async function called `emit` that:
#   - takes an `event` string
#   - looks it up in event_bus and awaits it if found
#   - prints "No listener" if not found

# TODO: Define an async function called `main` that:
#   - awaits emit("order.placed")
#   - awaits emit("order.cancelled")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Processing new order
# No listener


# -----------------------------------------------------------------------------
# DRILL 64 — Mix: OOP + Pydantic: method takes a Pydantic model as argument
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a Pydantic model called `Config` with:
#   - host: str
#   - port: int

# TODO: Define a class called `Server` with:
#   - a method called `configure` that:
#     - takes a `config` of type Config
#     - sets self.host = config.host and self.port = config.port
#     - prints f"Configured: {self.host}:{self.port}"

# TODO: Create a Server and call configure() with Config(host="localhost", port=8080)

# EXPECTED:
# Configured: localhost:8080


# -----------------------------------------------------------------------------
# DRILL 65 — Mix: OOP + wrapper decorator + self.state check
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `only_when_active` that:
#   - accesses the instance via args[0]
#   - if instance.active is False, prints "Inactive" and returns None
#   - otherwise calls the function

# TODO: Define a class called `Light` with:
#   - __init__ that sets self.active = False
#   - a method called `shine` decorated with @only_when_active
#   - shine() prints "Shining!"

# TODO: Create a Light instance and call shine()
# TODO: Set light.active = True and call shine() again

# EXPECTED:
# Inactive
# Shining!


# -----------------------------------------------------------------------------
# DRILL 66 — Mix: Registry + OOP: registering a method reference
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `action_map`

# TODO: Define a class called `Notifier` with:
#   - a method called `send` that prints "Notification sent"

# TODO: Create a Notifier instance called `notifier`

# TODO: Manually add notifier.send to action_map under the key "notify"

# TODO: Look up "notify" in action_map and call it

# EXPECTED:
# Notification sent


# -----------------------------------------------------------------------------
# DRILL 67 — Mix: Async + Pydantic + ValidationError handling
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel, Field, ValidationError

# TODO: Define a model called `Payment` with:
#   - amount: float with gt=0
#   - currency: str with min_length=3

# TODO: Define an async function called `process_payment` that:
#   - takes **data
#   - tries to create a Payment(**data)
#   - if ValidationError, prints "Invalid payment: <error>"
#   - if valid, prints f"Processing {payment.amount} {payment.currency}"

# TODO: Define an async function called `main` that:
#   - awaits process_payment(amount=100.0, currency="USD")
#   - awaits process_payment(amount=-5.0, currency="USD")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Processing 100.0 USD
# Invalid payment: 1 validation error for Payment ...


# -----------------------------------------------------------------------------
# DRILL 68 — Mix: Wrapper decorator + dynamic dispatch
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `log_dispatch` that:
#   - wraps any function using *args, **kwargs
#   - prints f"Dispatching with args={args} kwargs={kwargs}"
#   - calls the original function

# TODO: Create a dict called `dispatch` with:
#   - "run": a function decorated with @log_dispatch that prints "Running"

# TODO: Look up "run" in dispatch and call it

# EXPECTED:
# Dispatching with args=() kwargs={}
# Running


# -----------------------------------------------------------------------------
# DRILL 69 — Mix: Async OOP method + self.state modified by decorator
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a decorator called `mark_done` that:
#   - wraps an async function
#   - calls the function
#   - after it resolves, sets args[0].status = "done"

# TODO: Define a class called `Job` with:
#   - __init__ that sets self.status = "pending"
#   - an async method called `run` decorated with @mark_done
#   - run() prints "Job running"

# TODO: Define an async function called `main` that:
#   - creates a Job instance
#   - awaits job.run()
#   - prints job.status

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Job running
# done


# -----------------------------------------------------------------------------
# DRILL 70 — Mix: Full mini-pipeline: Pydantic → registry → async dispatch
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define a Pydantic model called `Event` with:
#   - type: str
#   - data: dict

# TODO: Create an empty dict called `listeners`

# TODO: Define a decorator called `on_event` that:
#   - takes an `event_type` string
#   - saves the async function to listeners using event_type as key
#   - returns the function unchanged

# TODO: Apply @on_event("signup") to async function `handle_signup` that:
#   - takes an `event` of type Event
#   - prints f"New signup: {event.data['email']}"

# TODO: Define an async function called `emit` that:
#   - takes an `event` of type Event
#   - looks up event.type in listeners and awaits it with the event
#   - if not found, prints "Unhandled event"

# TODO: Define an async function called `main` that:
#   - creates an Event(type="signup", data={"email": "user@test.com"})
#   - awaits emit(event)

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# New signup: user@test.com


# =============================================================================
# DRILLS 71–100: HARDER COMBINATIONS
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 71 — Pydantic: Validator using @field_validator
# -----------------------------------------------------------------------------
from pydantic import BaseModel, field_validator

# TODO: Define a model called `Username` with:
#   - value: str

# TODO: Add a @field_validator("value") classmethod that:
#   - raises ValueError("no spaces allowed") if " " is in the value
#   - returns the value otherwise

# TODO: Try creating Username(value="john doe") inside a try/except
#   - catch ValidationError and print "Error: <error>"

# TODO: Create Username(value="johndoe") and print it

# EXPECTED:
# Error: 1 validation error for Username ...
# value='johndoe'


# -----------------------------------------------------------------------------
# DRILL 72 — Pydantic: model_validate() from a raw dict
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a model called `Invoice` with:
#   - id: int
#   - total: float

# TODO: Create a raw dict called `raw` with:
#   - id: 101
#   - total: 250.0

# TODO: Use Invoice.model_validate(raw) to create an instance
# TODO: Print invoice.id and invoice.total

# EXPECTED:
# 101
# 250.0


# -----------------------------------------------------------------------------
# DRILL 73 — Pydantic: model with a computed default using default_factory
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field
from typing import List

# TODO: Define a model called `Basket` with:
#   - items: List[str] with default_factory=list

# TODO: Create two Basket instances with no arguments
# TODO: Append "apple" to basket1.items
# TODO: Print basket1.items and basket2.items to confirm they don't share state

# EXPECTED:
# ['apple']
# []


# -----------------------------------------------------------------------------
# DRILL 74 — Async: asyncio.create_task() and awaiting tasks
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `worker` that:
#   - takes a `name` string
#   - awaits asyncio.sleep(0)
#   - prints f"Worker {name} done"

# TODO: Define an async function called `main` that:
#   - creates two tasks using asyncio.create_task():
#     - task1 = asyncio.create_task(worker("A"))
#     - task2 = asyncio.create_task(worker("B"))
#   - awaits task1
#   - awaits task2

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Worker A done
# Worker B done


# -----------------------------------------------------------------------------
# DRILL 75 — Async: Returning values from asyncio.gather()
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `double` that:
#   - takes `n`
#   - returns n * 2

# TODO: Define an async function called `main` that:
#   - runs double(5), double(10), double(15) concurrently with asyncio.gather()
#   - unpacks results into a, b, c
#   - prints a, b, c

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# 10 20 30


# -----------------------------------------------------------------------------
# DRILL 76 — Wrapper Decorator: Retrying on exception
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `retry` that:
#   - wraps any function
#   - tries to call it up to 3 times
#   - if it raises an Exception, prints "Retrying..." and tries again
#   - if all 3 attempts fail, prints "All retries failed"

# TODO: Create a counter list `attempts = [0]` (use list so inner scope can mutate)

# TODO: Apply @retry to a function called `flaky` that:
#   - increments attempts[0]
#   - raises Exception if attempts[0] < 3
#   - prints "Success" on 3rd attempt

# TODO: Call flaky()

# EXPECTED:
# Retrying...
# Retrying...
# Success


# -----------------------------------------------------------------------------
# DRILL 77 — Wrapper Decorator: Caching return value (memoization)
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `memoize` that:
#   - stores a `cache` dict inside the wrapper closure
#   - checks if args are in cache before calling the function
#   - if yes, returns cached value
#   - if no, calls the function, stores result in cache, and returns it

# TODO: Apply @memoize to a function called `slow_square` that:
#   - prints f"Computing {n}^2"
#   - returns n * n

# TODO: Call slow_square(4) twice and slow_square(5) once
# TODO: Print the results

# EXPECTED:
# Computing 4^2
# Computing 5^2
# 16
# 16
# 25


# -----------------------------------------------------------------------------
# DRILL 78 — Registry + Wrapper mix: decorator that both registers and wraps
# -----------------------------------------------------------------------------
from functools import wraps

# TODO: Create an empty dict called `middleware_registry`

# TODO: Define a decorator called `middleware` that:
#   - saves the function to middleware_registry using its name as key
#   - wraps the function to print "Middleware: <function name>" before calling it
#   - returns the wrapper

# TODO: Apply @middleware to a function called `auth_check` that:
#   - prints "Auth check passed"

# TODO: Call auth_check()
# TODO: Print list(middleware_registry.keys())

# EXPECTED:
# Middleware: auth_check
# Auth check passed
# ['auth_check']


# -----------------------------------------------------------------------------
# DRILL 79 — OOP: Decorator that enforces method call order via self.state
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `require_initialized` that:
#   - accesses instance via args[0]
#   - if instance.initialized is False, prints "Not initialized" and returns None
#   - otherwise calls the function

# TODO: Define a class called `Database` with:
#   - __init__ that sets self.initialized = False
#   - a method called `initialize` that sets self.initialized = True and prints "DB ready"
#   - a method called `query` decorated with @require_initialized that prints "Running query"

# TODO: Create a Database instance
# TODO: Call query() before initialize() — should be blocked
# TODO: Call initialize()
# TODO: Call query() again — should work

# EXPECTED:
# Not initialized
# DB ready
# Running query


# -----------------------------------------------------------------------------
# DRILL 80 — OOP: Decorator that times an async method and stores result on self
# -----------------------------------------------------------------------------
import asyncio
import time

# TODO: Define a decorator called `time_it` that:
#   - wraps an async function
#   - records start time before calling it
#   - records end time after
#   - stores elapsed on args[0].last_duration

# TODO: Define a class called `Processor` with:
#   - __init__ that sets self.last_duration = None
#   - an async method called `process` decorated with @time_it
#   - process() awaits asyncio.sleep(0.05) and prints "Processed"

# TODO: Define an async function called `main` that:
#   - creates a Processor instance
#   - awaits processor.process()
#   - prints f"Duration: {processor.last_duration:.2f}s"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Processed
# Duration: 0.05s


# -----------------------------------------------------------------------------
# DRILL 81 — Dynamic Dispatch: Dispatch with fallback default handler
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions:
#   - `handle_get` that prints "Handling GET"
#   - `handle_post` that prints "Handling POST"
#   - `handle_default` that takes **kwargs and prints f"Unhandled method: {kwargs['method']}"

# TODO: Create a dict called `method_dispatch` with:
#   - "GET": handle_get
#   - "POST": handle_post

# TODO: Define an async function called `dispatch` that:
#   - takes a `method` string
#   - looks it up in method_dispatch, falls back to handle_default
#   - awaits the result, passing method=method as a kwarg

# TODO: Define an async function called `main` that:
#   - awaits dispatch("GET")
#   - awaits dispatch("POST")
#   - awaits dispatch("DELETE")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Handling GET
# Handling POST
# Unhandled method: DELETE


# -----------------------------------------------------------------------------
# DRILL 82 — Mix: Pydantic + Registry + OOP class-level dispatch
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a Pydantic model called `Command` with:
#   - action: str
#   - payload: dict

# TODO: Define a class called `CommandBus` with:
#   - a class-level dict called `_handlers = {}`
#   - a classmethod called `register` that:
#     - takes `action` and `fn`
#     - stores fn in _handlers under action
#   - a method called `handle` that:
#     - takes a Command instance
#     - looks up command.action in _handlers and calls it with command.payload
#     - prints "No handler" if not found

# TODO: Define a function called `do_greet` that:
#   - takes **payload and prints f"Hello {payload['name']}"

# TODO: Register do_greet under "greet" using CommandBus.register()
# TODO: Create a CommandBus and handle Command(action="greet", payload={"name": "Alice"})

# EXPECTED:
# Hello Alice


# -----------------------------------------------------------------------------
# DRILL 83 — Mix: Async + OOP + Pydantic method argument
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define a Pydantic model called `Task` with:
#   - name: str
#   - priority: int

# TODO: Define a class called `TaskRunner` with:
#   - an async method called `run` that:
#     - takes a `task` of type Task
#     - prints f"Running [{task.priority}] {task.name}"

# TODO: Define an async function called `main` that:
#   - creates a TaskRunner
#   - awaits runner.run(Task(name="Deploy", priority=5))

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Running [5] Deploy


# -----------------------------------------------------------------------------
# DRILL 84 — Mix: Wrapper decorator on async OOP method with self access
# -----------------------------------------------------------------------------
import asyncio
from functools import wraps

# TODO: Define a decorator called `async_log` that:
#   - wraps an async method using *args, **kwargs
#   - accesses instance via args[0]
#   - prints f"[LOG] {instance.name} calling {func.__name__}"
#   - awaits the original function

# TODO: Define a class called `Service` with:
#   - __init__ that sets self.name = "AuthService"
#   - an async method called `authenticate` decorated with @async_log
#   - authenticate() prints "Authentication complete"

# TODO: Define an async function called `main` that:
#   - creates a Service instance
#   - awaits service.authenticate()

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# [LOG] AuthService calling authenticate
# Authentication complete


# -----------------------------------------------------------------------------
# DRILL 85 — Mix: Registry decorator with Pydantic validation inside handler
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel, ValidationError

# TODO: Create an empty dict called `event_handlers`

# TODO: Define a decorator called `handles` that:
#   - takes an `event` string
#   - saves the async function to event_handlers using event as key
#   - returns the function unchanged

# TODO: Define a Pydantic model called `UserEvent` with:
#   - user_id: int
#   - action: str

# TODO: Apply @handles("user_action") to async function `process_user_action` that:
#   - takes **data
#   - tries to create UserEvent(**data)
#   - prints f"User {ue.user_id} did {ue.action}" if valid
#   - prints "Bad event data" if ValidationError

# TODO: Define an async function called `main` that:
#   - looks up "user_action" in event_handlers
#   - awaits it with user_id=42, action="login"
#   - awaits it with user_id="bad", action="login"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# User 42 did login
# Bad event data


# -----------------------------------------------------------------------------
# DRILL 86 — Mix: Multi-layer decorator (registry + wrapper on same function)
# -----------------------------------------------------------------------------
from functools import wraps

# TODO: Create an empty dict called `cmd_map`

# TODO: Define a decorator called `command` that:
#   - takes a `name` string
#   - saves the wrapped function to cmd_map under name
#   - wraps the function to print f"Running command: {name}" before calling it

# TODO: Apply @command("build") to a function called `build_fn` that:
#   - prints "Building project"

# TODO: Look up "build" in cmd_map and call it

# EXPECTED:
# Running command: build
# Building project


# -----------------------------------------------------------------------------
# DRILL 87 — Mix: OOP + async + registry: class registers its own methods
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `method_registry`

# TODO: Define a class called `App` with:
#   - an async method called `on_start` that:
#     - is manually added to method_registry under "start" inside __init__
#     - prints "App started"
#   - an async method called `on_stop` that:
#     - is manually added to method_registry under "stop" inside __init__
#     - prints "App stopped"
#   - __init__ that registers both methods into method_registry

# TODO: Define an async function called `main` that:
#   - creates an App instance
#   - looks up "start" in method_registry and awaits it
#   - looks up "stop" in method_registry and awaits it

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# App started
# App stopped


# -----------------------------------------------------------------------------
# DRILL 88 — Mix: Decorator chain — two decorators stacked on one function
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `bold` that:
#   - wraps a function
#   - calls it and wraps the returned string in "**<value>**"
#   - returns the result

# TODO: Define a decorator called `prefix` that:
#   - wraps a function
#   - calls it and prepends "INFO: " to the returned string
#   - returns the result

# TODO: Apply @bold then @prefix (so @bold is outer) to a function called `message` that:
#   - returns "hello"

# TODO: Print message()

# EXPECTED:
# **INFO: hello**


# -----------------------------------------------------------------------------
# DRILL 89 — Mix: Async generator consumed with async for
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async generator function called `ticker` that:
#   - loops from 1 to 3
#   - awaits asyncio.sleep(0) each iteration
#   - yields the current number

# TODO: Define an async function called `main` that:
#   - iterates over ticker() using async for
#   - prints each value

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# 1
# 2
# 3


# -----------------------------------------------------------------------------
# DRILL 90 — Mix: Full stack — Pydantic + OOP + async + registry + dispatch
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define a Pydantic model called `Request` with:
#   - route: str
#   - body: dict

# TODO: Create an empty dict called `route_table`

# TODO: Define a decorator called `endpoint` that:
#   - takes a `path` string
#   - saves the async function to route_table under path
#   - returns the function unchanged

# TODO: Apply @endpoint("/login") to an async function called `login` that:
#   - takes a `request` of type Request
#   - prints f"Login with {request.body['username']}"

# TODO: Define a class called `Router` with:
#   - an async method called `dispatch` that:
#     - takes a `request` of type Request
#     - looks up request.route in route_table and awaits it with request
#     - prints "404 Not Found" if not found

# TODO: Define an async function called `main` that:
#   - creates a Router
#   - awaits router.dispatch(Request(route="/login", body={"username": "alice"}))
#   - awaits router.dispatch(Request(route="/dashboard", body={}))

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Login with alice
# 404 Not Found


# =============================================================================
# DRILLS 91–130: EXPERT COMBINATIONS
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 91 — Pydantic: model_json_schema() inspection
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field
import json

# TODO: Define a model called `Article` with:
#   - title: str with min_length=5
#   - views: int with ge=0

# TODO: Get the JSON schema using Article.model_json_schema()
# TODO: Print the schema's "title" field
# TODO: Print list of top-level property keys

# EXPECTED:
# Article
# ['title', 'views']


# -----------------------------------------------------------------------------
# DRILL 92 — Pydantic: Strict mode rejects coercion
# -----------------------------------------------------------------------------
from pydantic import BaseModel, ConfigDict, ValidationError

# TODO: Define a model called `Strict` with:
#   - model_config = ConfigDict(strict=True)
#   - value: int

# TODO: Try creating Strict(value="42") inside try/except
#   - catch ValidationError and print "Rejected: <error>"

# TODO: Create Strict(value=42) and print it

# EXPECTED:
# Rejected: 1 validation error for Strict ...
# value=42


# -----------------------------------------------------------------------------
# DRILL 93 — Pydantic: model_copy() with override
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a model called `Settings` with:
#   - debug: bool
#   - log_level: str

# TODO: Create Settings(debug=False, log_level="INFO")
# TODO: Use .model_copy(update={"debug": True}) to create a new instance
# TODO: Print both instances

# EXPECTED:
# debug=False log_level='INFO'
# debug=True log_level='INFO'


# -----------------------------------------------------------------------------
# DRILL 94 — Async: asyncio.wait_for() with timeout
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `slow` that:
#   - awaits asyncio.sleep(5)
#   - prints "Done" (this should never print)

# TODO: Define an async function called `main` that:
#   - tries to await asyncio.wait_for(slow(), timeout=0.1)
#   - catches asyncio.TimeoutError
#   - prints "Timed out"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Timed out


# -----------------------------------------------------------------------------
# DRILL 95 — Async: asyncio.Queue producer/consumer
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `producer` that:
#   - takes a `queue`
#   - puts "item_1", "item_2", "item_3" into the queue using await queue.put()

# TODO: Define an async function called `consumer` that:
#   - takes a `queue`
#   - gets 3 items using await queue.get()
#   - prints each item

# TODO: Define an async function called `main` that:
#   - creates an asyncio.Queue()
#   - gathers producer and consumer together

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# item_1
# item_2
# item_3


# -----------------------------------------------------------------------------
# DRILL 96 — Wrapper Decorator: Context-manager-style decorator using yield
# -----------------------------------------------------------------------------
from contextlib import contextmanager

# TODO: Define a generator-based context manager decorator called `managed` that:
#   - prints "Entering"
#   - yields
#   - prints "Exiting"

# TODO: Use it as a decorator by wrapping a function called `do_task` with @contextmanager
#   Wait — instead:
#   Define a decorator called `managed_call` that:
#   - prints "Entering"
#   - calls the wrapped function
#   - prints "Exiting"

# TODO: Apply @managed_call to a function called `do_task` that:
#   - prints "Task running"

# TODO: Call do_task()

# EXPECTED:
# Entering
# Task running
# Exiting


# -----------------------------------------------------------------------------
# DRILL 97 — OOP Decorator: class-based decorator using __call__
# -----------------------------------------------------------------------------

# TODO: Define a class called `Repeat` with:
#   - __init__ that takes `times` and stores it
#   - __call__ that takes a `func`, and returns a wrapper that:
#     - calls func `times` times

# TODO: Apply @Repeat(times=3) to a function called `cheer` that:
#   - prints "Hooray!"

# TODO: Call cheer()

# EXPECTED:
# Hooray!
# Hooray!
# Hooray!


# -----------------------------------------------------------------------------
# DRILL 98 — OOP Decorator: class-based decorator with state tracking
# -----------------------------------------------------------------------------

# TODO: Define a class called `CallTracker` with:
#   - __init__ that takes a `func`, stores it, and sets self.count = 0
#   - __call__ that increments self.count and calls self.func

# TODO: Apply @CallTracker to a function called `ping` that:
#   - prints "Ping!"

# TODO: Call ping() twice
# TODO: Print ping.count

# EXPECTED:
# Ping!
# Ping!
# 2


# -----------------------------------------------------------------------------
# DRILL 99 — Mix: Async + OOP + wrapper decorator that suppresses exceptions
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a decorator called `suppress_errors` that:
#   - wraps an async function
#   - awaits it inside a try/except
#   - if any Exception is raised, prints "Suppressed: <error>" and returns None

# TODO: Define a class called `Fetcher` with:
#   - an async method called `fetch` decorated with @suppress_errors
#   - fetch() raises RuntimeError("connection refused")

# TODO: Define an async function called `main` that:
#   - creates a Fetcher
#   - awaits fetcher.fetch()
#   - prints "Continuing after error"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Suppressed: connection refused
# Continuing after error


# -----------------------------------------------------------------------------
# DRILL 100 — Mix: Full Expert Stack
# Pydantic + async + OOP + registry decorator + dynamic dispatch + wrapper decorator
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel, ValidationError
from functools import wraps

# TODO: Define a Pydantic model called `Packet` with:
#   - type: str
#   - data: dict

# TODO: Create an empty dict called `packet_handlers`

# TODO: Define a decorator called `handles_packet` that:
#   - takes a `packet_type` string
#   - saves the async function to packet_handlers under packet_type
#   - returns the function unchanged

# TODO: Define a decorator called `validate_packet` that:
#   - wraps an async function
#   - tries to create a Packet from args[0] if it's a dict
#   - if ValidationError, prints "Invalid packet" and returns
#   - otherwise proceeds with the call

# TODO: Define a class called `PacketRouter` with:
#   - an async method called `route` that:
#     - takes a raw dict
#     - creates a Packet from it
#     - looks up packet.type in packet_handlers
#     - awaits the handler with packet
#     - prints "No handler" if not found

# TODO: Apply @handles_packet("auth") to async function `auth_handler` that:
#   - takes a `packet` of type Packet
#   - prints f"Auth token: {packet.data['token']}"

# TODO: Define an async function called `main` that:
#   - creates a PacketRouter
#   - awaits router.route({"type": "auth", "data": {"token": "abc123"}})
#   - awaits router.route({"type": "ping", "data": {}})

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Auth token: abc123
# No handler


# =============================================================================
# DRILLS 101–130: ADVANCED ISOLATED DRILLS
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 101 — Pydantic: Discriminated union with Literal types
# -----------------------------------------------------------------------------
from pydantic import BaseModel
from typing import Union, Literal

# TODO: Define a model called `Cat` with:
#   - type: Literal["cat"]
#   - indoor: bool

# TODO: Define a model called `Dog` with:
#   - type: Literal["dog"]
#   - breed: str

# TODO: Define a model called `Pet` with:
#   - animal: Union[Cat, Dog]

# TODO: Create a Pet with animal=Cat(type="cat", indoor=True) and print pet.animal.indoor
# TODO: Create a Pet with animal=Dog(type="dog", breed="Husky") and print pet.animal.breed

# EXPECTED:
# True
# Husky


# -----------------------------------------------------------------------------
# DRILL 102 — Pydantic: model_serializer for custom output shape
# -----------------------------------------------------------------------------
from pydantic import BaseModel, model_serializer

# TODO: Define a model called `Point` with:
#   - x: float
#   - y: float

# TODO: Add a @model_serializer that returns:
#   - {"coords": [self.x, self.y]}

# TODO: Create Point(x=1.0, y=2.5)
# TODO: Print point.model_dump()

# EXPECTED:
# {'coords': [1.0, 2.5]}


# -----------------------------------------------------------------------------
# DRILL 103 — Async: asyncio.Event for signaling between coroutines
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `waiter` that:
#   - takes an `event` (asyncio.Event)
#   - prints "Waiting for signal..."
#   - awaits event.wait()
#   - prints "Signal received!"

# TODO: Define an async function called `signaler` that:
#   - takes an `event`
#   - awaits asyncio.sleep(0)
#   - sets the event using event.set()
#   - prints "Signal sent!"

# TODO: Define an async function called `main` that:
#   - creates an asyncio.Event()
#   - gathers waiter(event) and signaler(event)

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Waiting for signal...
# Signal sent!
# Signal received!


# -----------------------------------------------------------------------------
# DRILL 104 — Async: asyncio.Semaphore to limit concurrency
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `limited_task` that:
#   - takes `name` and a `sem` (asyncio.Semaphore)
#   - acquires the semaphore using `async with sem:`
#   - prints f"Running {name}"
#   - awaits asyncio.sleep(0)

# TODO: Define an async function called `main` that:
#   - creates a Semaphore with value=2
#   - gathers 4 tasks: limited_task("A"), ("B"), ("C"), ("D"), all sharing the semaphore

# TODO: Run `main` using asyncio.run()

# EXPECTED (order may vary, but all 4 must print):
# Running A
# Running B
# Running C
# Running D


# -----------------------------------------------------------------------------
# DRILL 105 — Wrapper Decorator: Decorator that adds before/after hooks via kwargs
# -----------------------------------------------------------------------------

# TODO: Define a decorator factory called `hooks` that:
#   - takes `before` (a callable) and `after` (a callable)
#   - wraps the function by calling before(), then the function, then after()

# TODO: Define functions:
#   - `open_conn` that prints "Connection opened"
#   - `close_conn` that prints "Connection closed"

# TODO: Apply @hooks(before=open_conn, after=close_conn) to a function called `query` that:
#   - prints "Querying DB"

# TODO: Call query()

# EXPECTED:
# Connection opened
# Querying DB
# Connection closed


# -----------------------------------------------------------------------------
# DRILL 106 — Registry Decorator: Priority-sorted registry
# -----------------------------------------------------------------------------

# TODO: Create an empty list called `sorted_tasks`

# TODO: Define a decorator factory called `priority_task` that:
#   - takes a `priority` int
#   - appends (priority, func) to sorted_tasks
#   - returns the function unchanged

# TODO: Apply @priority_task(3) to function `low_prio` that prints "Low"
# TODO: Apply @priority_task(1) to function `high_prio` that prints "High"
# TODO: Apply @priority_task(2) to function `mid_prio` that prints "Mid"

# TODO: Sort sorted_tasks by priority and call each function in order

# EXPECTED:
# High
# Mid
# Low


# -----------------------------------------------------------------------------
# DRILL 107 — OOP Decorator: Decorator that injects a dependency into self
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `inject_logger` that:
#   - wraps any method using *args, **kwargs
#   - accesses instance via args[0]
#   - sets instance.logger = "FileLogger" before calling the method

# TODO: Define a class called `ReportService` with:
#   - __init__ that sets self.logger = None
#   - a method called `generate` decorated with @inject_logger
#   - generate() prints f"Using logger: {self.logger}"

# TODO: Create a ReportService and call generate()

# EXPECTED:
# Using logger: FileLogger


# -----------------------------------------------------------------------------
# DRILL 108 — OOP Decorator: Decorator applied at class level with __init_subclass__
# -----------------------------------------------------------------------------

# TODO: Define a base class called `Plugin` with:
#   - a class-level list called `_registry = []`
#   - __init_subclass__ that appends the subclass name to _registry

# TODO: Define three subclasses:
#   - `AuthPlugin(Plugin)` (empty body, just pass)
#   - `CachePlugin(Plugin)` (empty body, just pass)
#   - `LogPlugin(Plugin)` (empty body, just pass)

# TODO: Print Plugin._registry

# EXPECTED:
# ['AuthPlugin', 'CachePlugin', 'LogPlugin']


# -----------------------------------------------------------------------------
# DRILL 109 — Dynamic Dispatch: Dispatch table built at class instantiation
# -----------------------------------------------------------------------------

# TODO: Define a class called `MessageBus` with:
#   - __init__ that builds a dict called self.handlers with:
#     - "email": self._send_email
#     - "sms": self._send_sms
#   - a method called `_send_email` that prints "Email sent"
#   - a method called `_send_sms` that prints "SMS sent"
#   - a method called `send` that:
#     - takes a `channel` string
#     - looks up the channel in self.handlers and calls it
#     - prints "Unknown channel" if not found

# TODO: Create a MessageBus and call send("email") and send("sms") and send("fax")

# EXPECTED:
# Email sent
# SMS sent
# Unknown channel


# -----------------------------------------------------------------------------
# DRILL 110 — Mix: Pydantic + discriminated union dispatched dynamically
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel
from typing import Union, Literal

# TODO: Define models:
#   - `LoginEvent` with type: Literal["login"] and username: str
#   - `LogoutEvent` with type: Literal["logout"] and username: str

# TODO: Define async functions:
#   - `handle_login` that takes a `LoginEvent` and prints f"Login: {event.username}"
#   - `handle_logout` that takes a `LogoutEvent` and prints f"Logout: {event.username}"

# TODO: Create a dict called `event_dispatch` with:
#   - "login": handle_login
#   - "logout": handle_logout

# TODO: Define an async function called `process` that:
#   - takes a raw dict
#   - reads raw["type"] to pick the right model and handler
#   - creates the model and awaits the handler

# TODO: Define an async function called `main` that:
#   - awaits process({"type": "login", "username": "alice"})
#   - awaits process({"type": "logout", "username": "alice"})

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Login: alice
# Logout: alice


# -----------------------------------------------------------------------------
# DRILL 111 — Wrapper Decorator: decorator that injects a default kwarg
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `inject_env` that:
#   - wraps any function using *args, **kwargs
#   - if "env" is not in kwargs, sets kwargs["env"] = "production"
#   - calls the function with updated kwargs

# TODO: Apply @inject_env to a function called `deploy` that:
#   - takes **kwargs
#   - prints f"Deploying to {kwargs['env']}"

# TODO: Call deploy()
# TODO: Call deploy(env="staging")

# EXPECTED:
# Deploying to production
# Deploying to staging


# -----------------------------------------------------------------------------
# DRILL 112 — OOP + Registry: class that self-registers on definition
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `service_registry`

# TODO: Define a base class called `BaseService` with:
#   - __init_subclass__ that registers the subclass in service_registry
#     using the subclass name as key and the subclass itself as value

# TODO: Define two subclasses:
#   - `EmailService(BaseService)` with a method `run` that prints "Email service"
#   - `SMSService(BaseService)` with a method `run` that prints "SMS service"

# TODO: Print list(service_registry.keys())
# TODO: Call service_registry["EmailService"]().run()

# EXPECTED:
# ['EmailService', 'SMSService']
# Email service


# -----------------------------------------------------------------------------
# DRILL 113 — Async: Context manager using __aenter__ and __aexit__
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a class called `AsyncResource` with:
#   - __aenter__ that prints "Resource acquired" and returns self
#   - __aexit__ that prints "Resource released" and returns None

# TODO: Define an async function called `main` that:
#   - uses `async with AsyncResource() as res:` 
#   - prints "Using resource"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Resource acquired
# Using resource
# Resource released


# -----------------------------------------------------------------------------
# DRILL 114 — Mix: Async generator with registry
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `stream_handlers`

# TODO: Define a decorator called `stream` that:
#   - takes an `event` string
#   - saves the async generator function to stream_handlers using event as key
#   - returns the function unchanged

# TODO: Apply @stream("numbers") to an async generator called `number_stream` that:
#   - yields 1, 2, 3 with asyncio.sleep(0) between each

# TODO: Define an async function called `main` that:
#   - looks up "numbers" in stream_handlers
#   - iterates over it with async for and prints each value

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# 1
# 2
# 3


# -----------------------------------------------------------------------------
# DRILL 115 — Mix: Pydantic + OOP + __post_init__ equivalent (model_validator)
# -----------------------------------------------------------------------------
from pydantic import BaseModel, model_validator

# TODO: Define a model called `DateRange` with:
#   - start: int
#   - end: int

# TODO: Add a @model_validator(mode="after") that:
#   - checks if self.start >= self.end
#   - raises ValueError("start must be before end") if so
#   - returns self otherwise

# TODO: Try creating DateRange(start=10, end=5) inside try/except
#   - print "Error: <error>"

# TODO: Create DateRange(start=1, end=10) and print it

# EXPECTED:
# Error: 1 validation error for DateRange ...
# start=1 end=10


# -----------------------------------------------------------------------------
# DRILL 116 — Wrapper Decorator: Decorator that rate-limits calls (max N per run)
# -----------------------------------------------------------------------------

# TODO: Define a decorator factory called `rate_limit` that:
#   - takes a `max_calls` int
#   - keeps a counter in the closure
#   - if calls exceed max_calls, prints "Rate limit exceeded" and returns None
#   - otherwise calls the function and increments the counter

# TODO: Apply @rate_limit(max_calls=2) to a function called `ping` that:
#   - prints "Ping!"

# TODO: Call ping() 4 times

# EXPECTED:
# Ping!
# Ping!
# Rate limit exceeded
# Rate limit exceeded


# -----------------------------------------------------------------------------
# DRILL 117 — Registry: method-level route registry inside a class
# -----------------------------------------------------------------------------

# TODO: Define a class called `MiniRouter` with:
#   - a class-level dict called `_routes = {}`
#   - a classmethod called `route` that:
#     - takes a `path` string
#     - returns a decorator that saves the method to _routes under path
#     - returns the method unchanged
#   - a method called `dispatch` that:
#     - takes a `path` string
#     - looks it up in _routes and calls it (passing self)
#     - prints "Not found" if missing

# TODO: Apply @MiniRouter.route("/ping") to a method called `ping` that:
#   - prints "Pong!"

# TODO: Create a MiniRouter and call dispatch("/ping") and dispatch("/missing")

# EXPECTED:
# Pong!
# Not found


# -----------------------------------------------------------------------------
# DRILL 118 — Async: Running sync code in executor to avoid blocking
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a regular (sync) function called `blocking_task` that:
#   - simulates blocking work by returning "Sync result"

# TODO: Define an async function called `main` that:
#   - gets the running loop using asyncio.get_event_loop()
#   - runs blocking_task in a thread pool using loop.run_in_executor(None, blocking_task)
#   - prints the result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Sync result


# -----------------------------------------------------------------------------
# DRILL 119 — Mix: OOP + Pydantic + async + full request/response cycle
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define models:
#   - `Request` with method: str and path: str and body: dict
#   - `Response` with status: int and message: str

# TODO: Define a class called `Handler` with:
#   - an async method called `handle` that:
#     - takes a `request` of type Request
#     - if request.method == "POST" and request.path == "/echo":
#       - returns Response(status=200, message=request.body.get("text", ""))
#     - otherwise returns Response(status=404, message="Not found")

# TODO: Define an async function called `main` that:
#   - creates a Handler
#   - sends Request(method="POST", path="/echo", body={"text": "Hello!"})
#   - sends Request(method="GET", path="/missing", body={})
#   - prints each response

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# status=200 message='Hello!'
# status=404 message='Not found'


# -----------------------------------------------------------------------------
# DRILL 120 — Mix: Three decorators stacked — registry + wrapper + OOP access
# -----------------------------------------------------------------------------
import asyncio
from functools import wraps

# TODO: Create an empty dict called `ops`

# TODO: Define a decorator called `register_op` that:
#   - takes a `name` string
#   - saves the function to ops under name
#   - returns the function unchanged

# TODO: Define a decorator called `log_op` that:
#   - wraps any async function
#   - prints f"OP: {func.__name__}" before awaiting it

# TODO: Define a class called `Executor` with:
#   - __init__ that sets self.label = "EX"
#   - an async method called `run_build`:
#     - decorated with @register_op("build") (outer)
#     - decorated with @log_op (inner)
#     - prints f"[{self.label}] Building"

# TODO: Define an async function called `main` that:
#   - creates an Executor
#   - awaits executor.run_build()
#   - prints list(ops.keys())

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# OP: run_build
# [EX] Building
# ['build']


# =============================================================================
# DRILLS 121–160: MASTER-LEVEL DRILLS
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 121 — Pydantic: Generic model with TypeVar
# -----------------------------------------------------------------------------
from pydantic import BaseModel
from typing import Generic, TypeVar

T = TypeVar("T")

# TODO: Define a generic model called `Envelope` that:
#   - inherits from BaseModel and Generic[T]
#   - has fields:
#     - payload: T
#     - meta: str

# TODO: Create an Envelope[int](payload=42, meta="count") and print it
# TODO: Create an Envelope[str](payload="hello", meta="greeting") and print it

# EXPECTED:
# payload=42 meta='count'
# payload='hello' meta='greeting'


# -----------------------------------------------------------------------------
# DRILL 122 — Pydantic: __eq__ between two model instances
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a model called `Point` with:
#   - x: int
#   - y: int

# TODO: Create two Points with the same values and one different
# TODO: Print whether point1 == point2 and point1 == point3

# EXPECTED:
# True
# False


# -----------------------------------------------------------------------------
# DRILL 123 — Async: asyncio.Lock preventing race condition
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create a shared list called `log = []`
# TODO: Create an asyncio.Lock called `lock`

# TODO: Define an async function called `safe_append` that:
#   - takes a `value`
#   - acquires the lock using `async with lock:`
#   - appends value to log

# TODO: Define an async function called `main` that:
#   - gathers safe_append(1), safe_append(2), safe_append(3)
#   - prints the sorted log

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# [1, 2, 3]


# -----------------------------------------------------------------------------
# DRILL 124 — Wrapper Decorator: Decorator that validates all arg types at runtime
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `typecheck` that:
#   - wraps any function
#   - reads func.__annotations__ to get expected types
#   - for each param name and type, checks isinstance(actual_value, expected_type)
#   - if any mismatch, raises TypeError(f"{name} must be {expected_type}")
#   - otherwise calls the function

# TODO: Apply @typecheck to a function called `add` that:
#   - takes a: int and b: int
#   - returns a + b and prints the result

# TODO: Call add(1, 2) — should work
# TODO: Try add(1, "two") inside try/except and print the TypeError

# EXPECTED:
# 3
# b must be <class 'int'>


# -----------------------------------------------------------------------------
# DRILL 125 — OOP: Descriptor protocol for validated attribute
# -----------------------------------------------------------------------------

# TODO: Define a descriptor class called `PositiveInt` with:
#   - __set_name__ that stores the attribute name
#   - __get__ that returns the stored value from instance.__dict__
#   - __set__ that:
#     - raises ValueError if value <= 0
#     - stores value in instance.__dict__ otherwise

# TODO: Define a class called `Product` that uses PositiveInt for:
#   - price = PositiveInt()

# TODO: Create a Product and set product.price = 10 and print it
# TODO: Try setting product.price = -5 inside try/except and print the ValueError

# EXPECTED:
# 10
# Value must be positive


# -----------------------------------------------------------------------------
# DRILL 126 — Async: Chained coroutines passing data forward
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions that form a pipeline:
#   - `load_data` returns [1, 2, 3, 4, 5]
#   - `filter_data` takes a list and returns items > 2
#   - `transform_data` takes a list and returns each item squared

# TODO: Define an async function called `main` that:
#   - awaits load_data() → raw
#   - awaits filter_data(raw) → filtered
#   - awaits transform_data(filtered) → result
#   - prints result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# [9, 16, 25]


# -----------------------------------------------------------------------------
# DRILL 127 — Mix: Decorator that conditionally makes a function async
# -----------------------------------------------------------------------------
import asyncio
import inspect

# TODO: Define a decorator called `ensure_async` that:
#   - if the wrapped function is already a coroutine function, returns it as-is
#   - if it's sync, wraps it in an async function that calls it and returns the result

# TODO: Apply @ensure_async to a sync function called `compute` that:
#   - returns 99

# TODO: Define an async function called `main` that:
#   - awaits compute() and prints the result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# 99


# -----------------------------------------------------------------------------
# DRILL 128 — Mix: Registry with priority queue — call in priority order
# -----------------------------------------------------------------------------
import heapq

# TODO: Create an empty list called `task_heap`

# TODO: Define a decorator factory called `scheduled` that:
#   - takes a `priority` int
#   - pushes (priority, func) onto task_heap using heapq.heappush
#   - returns the function unchanged

# TODO: Apply @scheduled(priority=3) to function `cleanup` that prints "Cleanup"
# TODO: Apply @scheduled(priority=1) to function `validate` that prints "Validate"
# TODO: Apply @scheduled(priority=2) to function `process` that prints "Process"

# TODO: Pop and call each function from the heap in priority order

# EXPECTED:
# Validate
# Process
# Cleanup


# -----------------------------------------------------------------------------
# DRILL 129 — Mix: Async + OOP + context manager + Pydantic
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define a Pydantic model called `DBConfig` with:
#   - host: str
#   - port: int

# TODO: Define a class called `AsyncDB` with:
#   - __init__ that takes a `config` of type DBConfig and sets self.connected = False
#   - __aenter__ that:
#     - sets self.connected = True
#     - prints f"Connected to {self.config.host}:{self.config.port}"
#     - returns self
#   - __aexit__ that:
#     - sets self.connected = False
#     - prints "Disconnected"
#   - an async method called `query` that prints "Running query"

# TODO: Define an async function called `main` that:
#   - creates DBConfig(host="localhost", port=5432)
#   - uses `async with AsyncDB(config) as db:` to connect
#   - calls db.query() inside

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Connected to localhost:5432
# Running query
# Disconnected


# -----------------------------------------------------------------------------
# DRILL 130 — Mix: Full plugin system — registry + OOP + async dispatch + Pydantic
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel
from typing import Dict, Any

# TODO: Define a Pydantic model called `PluginInput` with:
#   - name: str
#   - params: Dict[str, Any]

# TODO: Create an empty dict called `plugin_store`

# TODO: Define a class called `PluginBase` with:
#   - __init_subclass__ that registers the subclass in plugin_store
#     using the subclass name (lowercase) as key

# TODO: Define a subclass called `EchoPlugin(PluginBase)` with:
#   - an async method called `execute` that:
#     - takes a `plugin_input` of type PluginInput
#     - prints f"Echo: {plugin_input.params.get('message', '')}"

# TODO: Define a subclass called `ReversePlugin(PluginBase)` with:
#   - an async method called `execute` that:
#     - takes a `plugin_input` of type PluginInput
#     - prints f"Reversed: {plugin_input.params.get('text', '')[::-1]}"

# TODO: Define an async function called `run_plugin` that:
#   - takes `plugin_name` and `params` dict
#   - looks up plugin_name in plugin_store
#   - creates the plugin instance
#   - creates PluginInput(name=plugin_name, params=params)
#   - awaits plugin.execute(plugin_input)

# TODO: Define an async function called `main` that:
#   - awaits run_plugin("echoplugin", {"message": "hello world"})
#   - awaits run_plugin("reverseplugin", {"text": "python"})

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Echo: hello world
# Reversed: nohtyp


# =============================================================================
# DRILLS 131–170: SYNTHESIS DRILLS
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 131 — Pydantic: field alias for JSON key remapping
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field

# TODO: Define a model called `APIResponse` with:
#   - status_code: int with alias="statusCode"
#   - message: str with alias="msg"

# TODO: Use model_validate() with by_alias=False (default) from this dict:
#   - {"statusCode": 200, "msg": "OK"}
# Hint: use APIResponse.model_validate(data)

# TODO: Print response.status_code and response.message

# EXPECTED:
# 200
# OK


# -----------------------------------------------------------------------------
# DRILL 132 — Pydantic: Exporting with include/exclude
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a model called `UserProfile` with:
#   - username: str
#   - password: str
#   - email: str

# TODO: Create UserProfile(username="alice", password="secret", email="a@b.com")
# TODO: Use model_dump(exclude={"password"}) and print the result

# EXPECTED:
# {'username': 'alice', 'email': 'a@b.com'}


# -----------------------------------------------------------------------------
# DRILL 133 — Async: asyncio.shield to protect a coroutine from cancellation
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `important_task` that:
#   - awaits asyncio.sleep(0)
#   - prints "Important task done"

# TODO: Define an async function called `main` that:
#   - creates a task using asyncio.ensure_future(asyncio.shield(important_task()))
#   - awaits asyncio.sleep(0)
#   - awaits the shielded task
#   - prints "All done"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Important task done
# All done


# -----------------------------------------------------------------------------
# DRILL 134 — Wrapper Decorator: Decorator that enforces return type
# -----------------------------------------------------------------------------

# TODO: Define a decorator factory called `returns` that:
#   - takes an `expected_type`
#   - wraps the function
#   - calls it and checks if the result is an instance of expected_type
#   - if not, raises TypeError(f"Expected {expected_type}, got {type(result)}")
#   - returns the result if valid

# TODO: Apply @returns(int) to a function called `get_count` that:
#   - returns "five" (wrong type on purpose)

# TODO: Call get_count() inside try/except and print the TypeError

# EXPECTED:
# Expected <class 'int'>, got <class 'str'>


# -----------------------------------------------------------------------------
# DRILL 135 — Registry: auto-discovery by iterating a package namespace
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `discovered`

# TODO: Define a decorator called `auto_register` that:
#   - saves the function to discovered using its name as key
#   - returns the function unchanged

# TODO: Apply @auto_register to functions:
#   - `task_one` that prints "One"
#   - `task_two` that prints "Two"
#   - `task_three` that prints "Three"

# TODO: Iterate over discovered.items() and call each function, printing its name first

# EXPECTED:
# task_one → One
# task_two → Two
# task_three → Three


# -----------------------------------------------------------------------------
# DRILL 136 — OOP Decorator: Decorator that enforces a method can only be called once
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `once` that:
#   - wraps a method using *args, **kwargs
#   - uses a set on the decorator itself to track called instances
#   - if the instance has already called the method, prints "Already called" and returns None
#   - otherwise calls the method and marks the instance as called

# TODO: Define a class called `Initializer` with:
#   - a method called `setup` decorated with @once
#   - setup() prints "Setup complete"

# TODO: Create an Initializer and call setup() twice

# EXPECTED:
# Setup complete
# Already called


# -----------------------------------------------------------------------------
# DRILL 137 — Mix: Async middleware chain using a list of handlers
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create a list called `middleware_chain`

# TODO: Define 3 async functions and append them to middleware_chain:
#   - `auth_middleware` that prints "Auth OK"
#   - `log_middleware` that prints "Request logged"
#   - `handler` that prints "Response sent"

# TODO: Define an async function called `run_chain` that:
#   - iterates over middleware_chain
#   - awaits each one in sequence

# TODO: Define an async function called `main` that:
#   - awaits run_chain()

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Auth OK
# Request logged
# Response sent


# -----------------------------------------------------------------------------
# DRILL 138 — Mix: OOP + Pydantic + registry — typed command pattern
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Create an empty dict called `command_handlers`

# TODO: Define a decorator called `handles` that:
#   - takes a model class (not a string)
#   - saves the function to command_handlers using the model class as key
#   - returns the function unchanged

# TODO: Define a Pydantic model called `CreateUser` with:
#   - username: str

# TODO: Apply @handles(CreateUser) to a function called `create_user_handler` that:
#   - takes a `cmd` of type CreateUser
#   - prints f"Creating user: {cmd.username}"

# TODO: Define a class called `CommandBus` with:
#   - a method called `dispatch` that:
#     - takes any Pydantic model instance
#     - looks up type(cmd) in command_handlers and calls it with cmd
#     - prints "No handler" if not found

# TODO: Create a CommandBus and dispatch CreateUser(username="carol")

# EXPECTED:
# Creating user: carol


# -----------------------------------------------------------------------------
# DRILL 139 — Mix: Async + dynamic dispatch + per-request logging
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `api_handlers`

# TODO: Define a decorator called `api_route` that:
#   - takes a `path` string
#   - saves the async function to api_handlers under path
#   - returns the function unchanged

# TODO: Apply @api_route("/users") to async function `get_users` that:
#   - prints "Returning users list"

# TODO: Apply @api_route("/orders") to async function `get_orders` that:
#   - prints "Returning orders list"

# TODO: Define an async function called `handle_request` that:
#   - takes a `path` string
#   - prints f"[REQUEST] {path}"
#   - looks up path in api_handlers and awaits it
#   - prints f"[DONE] {path}"
#   - prints "404" if not found

# TODO: Define an async function called `main` that:
#   - awaits handle_request("/users")
#   - awaits handle_request("/orders")
#   - awaits handle_request("/admin")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# [REQUEST] /users
# Returning users list
# [DONE] /users
# [REQUEST] /orders
# Returning orders list
# [DONE] /orders
# [REQUEST] /admin
# 404


# -----------------------------------------------------------------------------
# DRILL 140 — Mix: Full lifecycle — init → validate → process → teardown
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define a model called `Job` with:
#   - name: str
#   - retries: int = 0

# TODO: Define a class called `JobRunner` with:
#   - __init__ that sets self.state = "idle"
#   - an async method called `init` that:
#     - sets self.state = "initialized"
#     - prints "Runner initialized"
#   - an async method called `run` that:
#     - takes a `job` of type Job
#     - sets self.state = "running"
#     - prints f"Running {job.name} (retries={job.retries})"
#   - an async method called `teardown` that:
#     - sets self.state = "idle"
#     - prints "Runner idle"

# TODO: Define an async function called `main` that:
#   - creates a JobRunner
#   - awaits runner.init()
#   - awaits runner.run(Job(name="DataSync", retries=2))
#   - awaits runner.teardown()
#   - prints runner.state

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Runner initialized
# Running DataSync (retries=2)
# Runner idle
# idle


# =============================================================================
# DRILLS 141–170
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 141 — Pydantic: Nested model with validation on child
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field, ValidationError

# TODO: Define a model called `Address` with:
#   - street: str with min_length=5
#   - city: str

# TODO: Define a model called `Customer` with:
#   - name: str
#   - address: Address

# TODO: Try creating Customer(name="Dave", address=Address(street="X", city="Manila"))
#   - catch ValidationError and print "Invalid: <error>"

# EXPECTED:
# Invalid: 1 validation error for Address ...


# -----------------------------------------------------------------------------
# DRILL 142 — Async: Parallel fetch simulation with asyncio.gather + return values
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions:
#   - `fetch_users` that returns ["alice", "bob"]
#   - `fetch_products` that returns ["book", "pen"]
#   - `fetch_orders` that returns [101, 102, 103]

# TODO: Define an async function called `main` that:
#   - runs all three with asyncio.gather and unpacks into users, products, orders
#   - prints each

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# ['alice', 'bob']
# ['book', 'pen']
# [101, 102, 103]


# -----------------------------------------------------------------------------
# DRILL 143 — Wrapper Decorator: Decorator that logs exceptions without swallowing
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `log_errors` that:
#   - wraps any function
#   - calls it inside try/except
#   - if an exception is raised, prints f"ERROR: {e}" and re-raises it
#   - otherwise returns the result

# TODO: Apply @log_errors to a function called `divide` that:
#   - takes `a` and `b`
#   - returns a / b

# TODO: Call divide(10, 2) and print the result
# TODO: Call divide(1, 0) inside try/except and print "Caught ZeroDivision"

# EXPECTED:
# 5.0
# ERROR: division by zero
# Caught ZeroDivision


# -----------------------------------------------------------------------------
# DRILL 144 — Registry: hot-swap — replacing a registered function at runtime
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `live_handlers`

# TODO: Define a decorator called `live` that:
#   - saves the function to live_handlers using its name as key
#   - returns the function unchanged

# TODO: Apply @live to a function called `respond` that:
#   - prints "v1 response"

# TODO: Call live_handlers["respond"]()

# TODO: Redefine `respond` (no decorator) to print "v2 response"
# TODO: Manually update live_handlers["respond"] = respond
# TODO: Call live_handlers["respond"]() again

# EXPECTED:
# v1 response
# v2 response


# -----------------------------------------------------------------------------
# DRILL 145 — OOP Decorator: Decorator that prevents calling method on deleted state
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `require_alive` that:
#   - accesses instance via args[0]
#   - if instance.alive is False, prints "Object is dead" and returns None
#   - otherwise calls the method

# TODO: Define a class called `Entity` with:
#   - __init__ that sets self.alive = True
#   - a method called `act` decorated with @require_alive
#   - act() prints "Entity acting"
#   - a method called `destroy` that sets self.alive = False

# TODO: Create an Entity
# TODO: Call act() — should work
# TODO: Call destroy()
# TODO: Call act() again — should be blocked

# EXPECTED:
# Entity acting
# Object is dead


# -----------------------------------------------------------------------------
# DRILL 146 — Mix: Async + Pydantic + retry logic in a wrapper decorator
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel, ValidationError

# TODO: Define a model called `Input` with:
#   - value: int

# TODO: Define a decorator called `async_retry` that:
#   - wraps an async function
#   - retries up to 3 times on any Exception
#   - prints f"Retry {n}" before each retry
#   - raises the last exception if all retries fail

# TODO: Create a counter `calls = [0]`

# TODO: Apply @async_retry to an async function called `unstable` that:
#   - increments calls[0]
#   - raises ValueError("not ready") if calls[0] < 3
#   - prints "Stable!" on success

# TODO: Define an async function called `main` that:
#   - awaits unstable()

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Retry 1
# Retry 2
# Stable!


# -----------------------------------------------------------------------------
# DRILL 147 — Mix: Registry + OOP + call count per registered function
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `fn_stats`  (stores {"fn": func, "calls": 0})

# TODO: Define a decorator called `track` that:
#   - saves {"fn": func, "calls": 0} to fn_stats under the function's name
#   - wraps the function to increment fn_stats[func.__name__]["calls"] on each call
#   - calls the original function

# TODO: Apply @track to:
#   - a function called `build` that prints "Building"
#   - a function called `deploy` that prints "Deploying"

# TODO: Call build() 3 times and deploy() once
# TODO: Print fn_stats["build"]["calls"] and fn_stats["deploy"]["calls"]

# EXPECTED:
# Building
# Building
# Building
# Deploying
# 3
# 1


# -----------------------------------------------------------------------------
# DRILL 148 — Mix: OOP + async + abstract method pattern (no ABC)
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a base class called `BaseHandler` with:
#   - an async method called `handle` that:
#     - raises NotImplementedError("Subclasses must implement handle()")

# TODO: Define a subclass called `EmailHandler(BaseHandler)` with:
#   - an async method called `handle` that:
#     - prints "Handling email"

# TODO: Define an async function called `main` that:
#   - creates an EmailHandler
#   - awaits handler.handle()

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Handling email


# -----------------------------------------------------------------------------
# DRILL 149 — Mix: Pydantic + OOP + async — service class with model I/O
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define Pydantic models:
#   - `CreateProductRequest` with name: str and price: float
#   - `ProductResponse` with id: int and name: str and price: float

# TODO: Define a class called `ProductService` with:
#   - an async method called `create` that:
#     - takes a `req` of type CreateProductRequest
#     - simulates an ID by using id=1 (hardcoded)
#     - returns ProductResponse(id=1, name=req.name, price=req.price)

# TODO: Define an async function called `main` that:
#   - creates a ProductService
#   - awaits service.create(CreateProductRequest(name="Laptop", price=999.99))
#   - prints the response

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# id=1 name='Laptop' price=999.99


# -----------------------------------------------------------------------------
# DRILL 150 — Mix: Full system — plugin + middleware + async + Pydantic pipeline
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define a model called `Message` with:
#   - topic: str
#   - body: str

# TODO: Create an empty list called `middleware_stack`
# TODO: Create an empty dict called `topic_handlers`

# TODO: Define a decorator called `middleware` that:
#   - appends the async function to middleware_stack
#   - returns it unchanged

# TODO: Define a decorator called `topic` that:
#   - takes a `name` string
#   - saves the async function to topic_handlers under name
#   - returns it unchanged

# TODO: Apply @middleware to async function `log_middleware` that:
#   - takes a `message` of type Message
#   - prints f"[LOG] topic={message.topic}"

# TODO: Apply @middleware to async function `auth_middleware` that:
#   - takes a `message` of type Message
#   - prints "[AUTH] OK"

# TODO: Apply @topic("alerts") to async function `handle_alert` that:
#   - takes a `message` of type Message
#   - prints f"ALERT: {message.body}"

# TODO: Define an async function called `publish` that:
#   - takes a `message` of type Message
#   - runs all middleware with the message
#   - looks up message.topic in topic_handlers and awaits it with the message
#   - prints "No handler for topic" if not found

# TODO: Define an async function called `main` that:
#   - awaits publish(Message(topic="alerts", body="Server is down"))

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# [LOG] topic=alerts
# [AUTH] OK
# ALERT: Server is down


# =============================================================================
# DRILLS 151–200: FINAL BOSS DRILLS
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 151 — Pydantic: Recursive model (tree structure)
# -----------------------------------------------------------------------------
from pydantic import BaseModel
from typing import Optional, List

# TODO: Define a model called `TreeNode` with:
#   - value: int
#   - children: List["TreeNode"] = []

# TODO: Build this tree:
#       1
#      / \
#     2   3

# TODO: Create the tree using nested TreeNode instances
# TODO: Print root.value, root.children[0].value, root.children[1].value

# EXPECTED:
# 1
# 2
# 3


# -----------------------------------------------------------------------------
# DRILL 152 — Pydantic: Field with custom validator using Annotated
# -----------------------------------------------------------------------------
from pydantic import BaseModel
from typing import Annotated
from pydantic import AfterValidator

# TODO: Define a validator function called `must_be_even` that:
#   - raises ValueError("must be even") if v % 2 != 0
#   - returns v otherwise

# TODO: Define a type alias called `EvenInt` using Annotated[int, AfterValidator(must_be_even)]

# TODO: Define a model called `Grid` with:
#   - columns: EvenInt

# TODO: Try Grid(columns=3) inside try/except — print "Error: <error>"
# TODO: Create Grid(columns=4) and print it

# EXPECTED:
# Error: 1 validation error for Grid ...
# columns=4


# -----------------------------------------------------------------------------
# DRILL 153 — Async: Fan-out pattern — one input dispatched to multiple handlers
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions:
#   - `notify_email` that takes `event` and prints f"Email: {event}"
#   - `notify_sms` that takes `event` and prints f"SMS: {event}"
#   - `notify_push` that takes `event` and prints f"Push: {event}"

# TODO: Create a list called `notification_handlers` containing all three

# TODO: Define an async function called `fan_out` that:
#   - takes an `event` string
#   - gathers all handlers called with event

# TODO: Define an async function called `main` that:
#   - awaits fan_out("user.signup")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Email: user.signup
# SMS: user.signup
# Push: user.signup


# -----------------------------------------------------------------------------
# DRILL 154 — Wrapper Decorator: Decorator that enforces argument count
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `max_args` that:
#   - takes a `limit` int
#   - wraps the function
#   - if len(args) > limit, raises TypeError(f"Too many args: max {limit}")
#   - otherwise calls the function

# TODO: Apply @max_args(2) to a function called `process` that:
#   - prints f"Processing {args}"

# TODO: Call process("a", "b")
# TODO: Call process("a", "b", "c") inside try/except and print the TypeError

# EXPECTED:
# Processing ('a', 'b')
# Too many args: max 2


# -----------------------------------------------------------------------------
# DRILL 155 — Registry: Registry with teardown — calling cleanup on each entry
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `resource_registry`

# TODO: Define a decorator factory called `resource` that:
#   - takes a `cleanup` callable
#   - saves {"fn": func, "cleanup": cleanup} to resource_registry under func's name
#   - returns the function unchanged

# TODO: Define a cleanup function called `close_db` that prints "DB closed"
# TODO: Apply @resource(cleanup=close_db) to a function called `open_db` that prints "DB opened"

# TODO: Call open_db()
# TODO: Call resource_registry["open_db"]["cleanup"]()

# EXPECTED:
# DB opened
# DB closed


# -----------------------------------------------------------------------------
# DRILL 156 — OOP Decorator: Decorator applied inside __init__ dynamically
# -----------------------------------------------------------------------------
from functools import wraps

# TODO: Define a logging wrapper function called `add_logging` that:
#   - takes a method and an instance
#   - returns a new function that prints f"[{instance.name}] calling {method.__name__}"
#   - then calls the original method

# TODO: Define a class called `DynamicService` with:
#   - __init__ that:
#     - sets self.name = "DynSvc"
#     - replaces self.process with add_logging(self.process, self)
#   - a method called `process` that prints "Processing"

# TODO: Create a DynamicService and call process()

# EXPECTED:
# [DynSvc] calling process
# Processing


# -----------------------------------------------------------------------------
# DRILL 157 — Mix: Async + Fan-in — collecting results from multiple sources
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions that each return a list:
#   - `source_a` returns ["a1", "a2"]
#   - `source_b` returns ["b1"]
#   - `source_c` returns ["c1", "c2", "c3"]

# TODO: Define an async function called `fan_in` that:
#   - gathers all three sources
#   - flattens the results into a single list
#   - returns it

# TODO: Define an async function called `main` that:
#   - awaits fan_in() and prints the result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# ['a1', 'a2', 'b1', 'c1', 'c2', 'c3']


# -----------------------------------------------------------------------------
# DRILL 158 — Mix: OOP + async + state machine
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a class called `StateMachine` with:
#   - __init__ that sets self.state = "idle"
#   - an async method called `start` that:
#     - if self.state != "idle", prints "Cannot start" and returns
#     - sets self.state = "running" and prints "Started"
#   - an async method called `pause` that:
#     - if self.state != "running", prints "Cannot pause" and returns
#     - sets self.state = "paused" and prints "Paused"
#   - an async method called `stop` that:
#     - sets self.state = "idle" and prints "Stopped"

# TODO: Define an async function called `main` that:
#   - creates a StateMachine
#   - awaits sm.start()
#   - awaits sm.start()   ← should be blocked
#   - awaits sm.pause()
#   - awaits sm.stop()

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Started
# Cannot start
# Paused
# Stopped


# -----------------------------------------------------------------------------
# DRILL 159 — Mix: All 6 concepts in one coherent system
# Pydantic + async + wrapper decorator + registry decorator + OOP + dynamic dispatch
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel
from functools import wraps

# --- Pydantic ---
# TODO: Define a model called `APIRequest` with:
#   - endpoint: str
#   - payload: dict

# --- Registry ---
# TODO: Create an empty dict called `endpoint_registry`

# TODO: Define a decorator called `endpoint` that:
#   - takes a `path` string
#   - saves the async function to endpoint_registry under path
#   - returns the function unchanged

# --- Wrapper ---
# TODO: Define a decorator called `validate_request` that:
#   - wraps an async function
#   - prints f"Validating request to {args[0].endpoint}" (args[0] is the APIRequest)
#   - awaits the original function

# --- OOP ---
# TODO: Define a class called `APIGateway` with:
#   - an async method called `handle` that:
#     - takes a `request` of type APIRequest
#     - looks up request.endpoint in endpoint_registry
#     - awaits the handler with request
#     - prints "Endpoint not found" if missing

# --- Handlers ---
# TODO: Apply @endpoint("/create") to an async function called `create_handler` that:
#   - is decorated with @validate_request
#   - takes a `request` of type APIRequest
#   - prints f"Creating with {request.payload}"

# --- Dynamic Dispatch ---
# TODO: Define an async function called `main` that:
#   - creates an APIGateway
#   - awaits gateway.handle(APIRequest(endpoint="/create", payload={"name": "Widget"}))
#   - awaits gateway.handle(APIRequest(endpoint="/delete", payload={}))

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Validating request to /create
# Creating with {'name': 'Widget'}
# Endpoint not found


# -----------------------------------------------------------------------------
# DRILL 160 — Mix: Recursive async dispatcher
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `pipeline_steps`

# TODO: Define a decorator called `step` that:
#   - takes a `name` string and optional `next_step` string (default None)
#   - saves {"fn": func, "next": next_step} to pipeline_steps under name
#   - returns the function unchanged

# TODO: Apply @step("validate", next_step="transform") to async function `validate` that:
#   - takes `data` and prints f"Validating {data}"

# TODO: Apply @step("transform", next_step="save") to async function `transform` that:
#   - takes `data` and prints f"Transforming {data}"

# TODO: Apply @step("save") to async function `save` that:
#   - takes `data` and prints f"Saving {data}"

# TODO: Define an async function called `run_pipeline` that:
#   - takes a `step_name` and `data`
#   - looks up step_name in pipeline_steps
#   - awaits the function with data
#   - if there's a next step, recursively awaits run_pipeline with the next step

# TODO: Define an async function called `main` that:
#   - awaits run_pipeline("validate", "record_42")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Validating record_42
# Transforming record_42
# Saving record_42


# -----------------------------------------------------------------------------
# DRILL 161 — Pydantic: model with a computed property using @property
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a model called `Rectangle` with:
#   - width: float
#   - height: float

# TODO: Add a @property called `area` that:
#   - returns self.width * self.height

# TODO: Create Rectangle(width=4.0, height=5.0)
# TODO: Print rect.area

# EXPECTED:
# 20.0


# -----------------------------------------------------------------------------
# DRILL 162 — Async: Collecting results from an async generator into a list
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async generator called `produce` that:
#   - yields 10, 20, 30 with await asyncio.sleep(0) between each

# TODO: Define an async function called `main` that:
#   - collects all values from produce() into a list using async for
#   - prints the list

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# [10, 20, 30]


# -----------------------------------------------------------------------------
# DRILL 163 — Wrapper Decorator: Decorator that measures memory delta (simple version)
# -----------------------------------------------------------------------------
import sys

# TODO: Define a decorator called `mem_check` that:
#   - wraps any function
#   - records sys.getsizeof of the return value
#   - prints f"Return size: {size} bytes"
#   - returns the value

# TODO: Apply @mem_check to a function called `make_list` that:
#   - returns list(range(100))

# TODO: Call make_list()

# EXPECTED:
# Return size: <N> bytes   (exact number varies, just make sure it prints)


# -----------------------------------------------------------------------------
# DRILL 164 — Registry: Registry that auto-expires entries after N calls
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `expiring_registry`
#   Structure: { name: {"fn": func, "remaining": int} }

# TODO: Define a decorator factory called `expires_after` that:
#   - takes `n` calls
#   - saves {"fn": func, "remaining": n} to expiring_registry under func's name
#   - returns the function unchanged

# TODO: Define a function called `invoke` that:
#   - takes a `name` string
#   - looks up the entry in expiring_registry
#   - if remaining > 0: calls the function and decrements remaining
#   - if remaining == 0: prints f"{name} expired"

# TODO: Apply @expires_after(2) to a function called `greet` that:
#   - prints "Hello!"

# TODO: Call invoke("greet") 3 times

# EXPECTED:
# Hello!
# Hello!
# greet expired


# -----------------------------------------------------------------------------
# DRILL 165 — OOP: Decorator that compares self state before and after method
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `diff_state` that:
#   - wraps any method using *args, **kwargs
#   - reads instance.value before the call (args[0].value)
#   - calls the method
#   - reads instance.value after
#   - prints f"State changed: {before} → {after}"

# TODO: Define a class called `Counter` with:
#   - __init__ that sets self.value = 0
#   - a method called `increment` decorated with @diff_state
#   - increment() increments self.value by 1

# TODO: Create a Counter and call increment() twice

# EXPECTED:
# State changed: 0 → 1
# State changed: 1 → 2


# -----------------------------------------------------------------------------
# DRILL 166 — Mix: Async + OOP + fan-out notification system
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a class called `EventSystem` with:
#   - __init__ that sets self.listeners = {} (dict of event → list of async funcs)
#   - a method called `on` that:
#     - takes `event` and `fn`
#     - appends fn to self.listeners[event] (create list if missing)
#   - an async method called `emit` that:
#     - takes an `event` and **kwargs
#     - gathers all listeners for that event, calling each with **kwargs
#     - does nothing if no listeners

# TODO: Create an EventSystem called `bus`
# TODO: Define two async listeners:
#   - `on_signup_email` that takes **kwargs and prints f"Email to {kwargs['email']}"
#   - `on_signup_log` that takes **kwargs and prints f"Log: signup by {kwargs['email']}"
# TODO: Register both under "signup" using bus.on()

# TODO: Define an async function called `main` that:
#   - awaits bus.emit("signup", email="user@example.com")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Email to user@example.com
# Log: signup by user@example.com


# -----------------------------------------------------------------------------
# DRILL 167 — Mix: Registry + OOP + versioned handlers
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `versioned_handlers`
#   Structure: { action: { version: func } }

# TODO: Define a decorator factory called `versioned` that:
#   - takes `action` string and `version` int
#   - stores the function in versioned_handlers[action][version]
#   - returns the function unchanged

# TODO: Apply @versioned("process", 1) to function `process_v1` that prints "Process v1"
# TODO: Apply @versioned("process", 2) to function `process_v2` that prints "Process v2"

# TODO: Define a function called `dispatch_versioned` that:
#   - takes `action` and `version`
#   - looks up versioned_handlers[action][version] and calls it
#   - prints "Not found" if missing

# TODO: Call dispatch_versioned("process", 1)
# TODO: Call dispatch_versioned("process", 2)
# TODO: Call dispatch_versioned("process", 3)

# EXPECTED:
# Process v1
# Process v2
# Not found


# -----------------------------------------------------------------------------
# DRILL 168 — Mix: Async + Pydantic + stateful OOP + registry — full CRUD simulation
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel
from typing import Dict, List

# TODO: Define models:
#   - `CreateItem` with name: str
#   - `Item` with id: int and name: str

# TODO: Create an empty dict called `crud_handlers`

# TODO: Define a decorator called `crud_op` that:
#   - takes an `op` string
#   - saves the async function to crud_handlers under op
#   - returns the function unchanged

# TODO: Define a class called `ItemStore` with:
#   - __init__ that sets self.items: Dict[int, Item] = {} and self._next_id = 1
#   - async method `create` decorated with @crud_op("create") that:
#     - takes a `req` of type CreateItem
#     - creates an Item with the next id and req.name
#     - stores it in self.items and increments self._next_id
#     - prints f"Created: {item}"
#   - async method `list_all` decorated with @crud_op("list") that:
#     - prints each item in self.items.values()

# TODO: Define an async function called `main` that:
#   - creates an ItemStore
#   - awaits store.create(CreateItem(name="Apple"))
#   - awaits store.create(CreateItem(name="Banana"))
#   - awaits store.list_all()

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Created: id=1 name='Apple'
# Created: id=2 name='Banana'
# id=1 name='Apple'
# id=2 name='Banana'


# -----------------------------------------------------------------------------
# DRILL 169 — Mix: The Interceptor — wrapper that transforms both input and output
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a Pydantic model called `RawInput` with:
#   - text: str

# TODO: Define a Pydantic model called `ProcessedOutput` with:
#   - result: str
#   - length: int

# TODO: Define a decorator called `transform_io` that:
#   - wraps any function
#   - before calling: strips and lowercases args[0].text, creates a new RawInput with it
#   - calls the function with the cleaned input
#   - after calling: wraps the returned string in ProcessedOutput(result=ret, length=len(ret))
#   - returns the ProcessedOutput

# TODO: Apply @transform_io to a function called `process` that:
#   - takes a `raw` of type RawInput
#   - returns f"processed: {raw.text}"

# TODO: Call process(RawInput(text="  HELLO WORLD  ")) and print the result

# EXPECTED:
# result='processed: hello world' length=22


# -----------------------------------------------------------------------------
# DRILL 170 — Mix: The Full Architecture
# Pydantic + async + OOP + wrapper + registry + dynamic dispatch + fan-out + state machine
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel
from functools import wraps
from typing import List, Dict, Any

# --- Models ---
# TODO: Define a model called `Event` with:
#   - name: str
#   - data: Dict[str, Any]

# --- Registry ---
# TODO: Create an empty dict called `event_handlers`
# TODO: Create an empty list called `global_middleware`

# TODO: Define a decorator called `on` that:
#   - takes an `event_name` string
#   - appends the async function to event_handlers[event_name] (create list if needed)
#   - returns the function unchanged

# TODO: Define a decorator called `middleware` that:
#   - appends the async function to global_middleware
#   - returns it unchanged

# --- Middleware ---
# TODO: Apply @middleware to async function `logger` that:
#   - takes an `event` of type Event
#   - prints f"[LOG] {event.name}"

# --- State Machine OOP ---
# TODO: Define a class called `AppState` with:
#   - __init__ that sets self.state = "booting"
#   - an async method called `ready` that:
#     - sets self.state = "ready"
#     - prints "App is ready"

# --- Handlers ---
# TODO: Apply @on("user.created") to async function `send_welcome` that:
#   - takes an `event` of type Event
#   - prints f"Welcome {event.data['username']}"

# TODO: Apply @on("user.created") to async function `create_profile` that:
#   - takes an `event` of type Event
#   - prints f"Profile created for {event.data['username']}"

# --- Dispatcher ---
# TODO: Define a class called `EventBus` with:
#   - __init__ that takes an `app_state` of type AppState
#   - an async method called `publish` that:
#     - takes an `event` of type Event
#     - if app_state.state != "ready", prints "Bus not ready" and returns
#     - runs all global_middleware with the event via gather
#     - fans out to all handlers registered under event.name via gather
#     - prints "No handlers" if none registered

# --- Main ---
# TODO: Define an async function called `main` that:
#   - creates an AppState
#   - awaits app_state.ready()
#   - creates an EventBus(app_state)
#   - awaits bus.publish(Event(name="user.created", data={"username": "alice"}))

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# App is ready
# [LOG] user.created
# Welcome alice
# Profile created for alice


# =============================================================================
# DRILLS 171–200: FINAL 30 — PURE MUSCLE MEMORY SPEED DRILLS
# =============================================================================


# -----------------------------------------------------------------------------
# DRILL 171 — Pydantic: model with ge and le constraints
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field, ValidationError

# TODO: Define a model called `Score` with:
#   - value: int with ge=0 and le=100

# TODO: Try Score(value=150) → catch ValidationError → print "Invalid: <error>"
# TODO: Create Score(value=85) and print it

# EXPECTED:
# Invalid: 1 validation error for Score ...
# value=85


# -----------------------------------------------------------------------------
# DRILL 172 — Pydantic: model_fields to inspect field metadata
# -----------------------------------------------------------------------------
from pydantic import BaseModel, Field

# TODO: Define a model called `Config` with:
#   - timeout: int = Field(default=30, description="Timeout in seconds")
#   - retries: int = Field(default=3)

# TODO: Print list(Config.model_fields.keys())

# EXPECTED:
# ['timeout', 'retries']


# -----------------------------------------------------------------------------
# DRILL 173 — Async: Run two tasks and cancel the slower one
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define an async function called `fast` that:
#   - awaits asyncio.sleep(0.01)
#   - prints "Fast done"

# TODO: Define an async function called `slow` that:
#   - awaits asyncio.sleep(10)
#   - prints "Slow done"

# TODO: Define an async function called `main` that:
#   - creates tasks for both using asyncio.create_task()
#   - awaits the fast task
#   - cancels the slow task
#   - prints "Slow cancelled"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Fast done
# Slow cancelled


# -----------------------------------------------------------------------------
# DRILL 174 — Wrapper Decorator: Decorator that prints function signature info
# -----------------------------------------------------------------------------
import inspect

# TODO: Define a decorator called `show_signature` that:
#   - wraps any function
#   - before calling it, prints the function's parameter names using inspect.signature

# TODO: Apply @show_signature to a function called `connect` that:
#   - takes `host` and `port`
#   - prints f"Connecting to {host}:{port}"

# TODO: Call connect("localhost", 8080)

# EXPECTED:
# (host, port)
# Connecting to localhost:8080


# -----------------------------------------------------------------------------
# DRILL 175 — Registry: Registry with aliases — multiple keys, one function
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `alias_registry`

# TODO: Define a decorator factory called `aliases` that:
#   - takes *names (multiple strings)
#   - saves the function under each name in alias_registry
#   - returns the function unchanged

# TODO: Apply @aliases("quit", "exit", "q") to a function called `shutdown` that:
#   - prints "Shutting down"

# TODO: Call alias_registry["q"]()
# TODO: Call alias_registry["quit"]()

# EXPECTED:
# Shutting down
# Shutting down


# -----------------------------------------------------------------------------
# DRILL 176 — OOP Decorator: Decorator that wraps __init__ to log construction
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `log_init` that:
#   - wraps the __init__ method of a class
#   - prints f"Creating {args[0].__class__.__name__}" before calling __init__

# TODO: Define a class called `Widget` with:
#   - @log_init applied to __init__
#   - __init__ sets self.name = name and prints f"Widget ready: {self.name}"

# TODO: Create Widget("Spinner")

# EXPECTED:
# Creating Widget
# Widget ready: Spinner


# -----------------------------------------------------------------------------
# DRILL 177 — Mix: Async + OOP + property that checks self.state
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a class called `Connection` with:
#   - __init__ that sets self._connected = False
#   - a @property called `connected` that returns self._connected
#   - an async method called `connect` that:
#     - sets self._connected = True
#     - prints "Connected"
#   - an async method called `send` that:
#     - if not self.connected: prints "Not connected" and returns
#     - prints "Data sent"

# TODO: Define an async function called `main` that:
#   - creates a Connection
#   - awaits conn.send()      ← blocked
#   - awaits conn.connect()
#   - awaits conn.send()      ← works

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Not connected
# Connected
# Data sent


# -----------------------------------------------------------------------------
# DRILL 178 — Mix: Registry + priority + async dispatch
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty list called `priority_handlers`

# TODO: Define a decorator factory called `priority` that:
#   - takes a `level` int
#   - appends (level, func) to priority_handlers
#   - returns the function unchanged

# TODO: Apply @priority(3) to async function `low_handler` that prints "Low"
# TODO: Apply @priority(1) to async function `high_handler` that prints "High"
# TODO: Apply @priority(2) to async function `mid_handler` that prints "Mid"

# TODO: Define an async function called `run_by_priority` that:
#   - sorts priority_handlers by level
#   - awaits each function in order

# TODO: Define an async function called `main` that:
#   - awaits run_by_priority()

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# High
# Mid
# Low


# -----------------------------------------------------------------------------
# DRILL 179 — Mix: Pydantic + OOP + classmethod factory
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a model called `ServerConfig` with:
#   - host: str
#   - port: int
#   - debug: bool = False

# TODO: Define a class called `Server` with:
#   - __init__ that takes a `config` of type ServerConfig and stores it
#   - a @classmethod called `from_defaults` that:
#     - creates ServerConfig(host="localhost", port=8000, debug=True)
#     - returns Server(config)
#   - a method called `info` that prints f"{self.config.host}:{self.config.port} debug={self.config.debug}"

# TODO: Create a Server using Server.from_defaults() and call info()

# EXPECTED:
# localhost:8000 debug=True


# -----------------------------------------------------------------------------
# DRILL 180 — Mix: Dynamic dispatch + middleware list + Pydantic
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define a model called `Command` with:
#   - name: str
#   - args: list

# TODO: Create an empty list called `pre_hooks`
# TODO: Create an empty dict called `command_dispatch`

# TODO: Define a decorator called `pre_hook` that:
#   - appends the async function to pre_hooks
#   - returns it unchanged

# TODO: Define a decorator called `dispatch_cmd` that:
#   - takes a `name` string
#   - saves the async function to command_dispatch under name
#   - returns it unchanged

# TODO: Apply @pre_hook to async function `validate_cmd` that:
#   - takes a `cmd` of type Command
#   - prints f"Validating: {cmd.name}"

# TODO: Apply @dispatch_cmd("run") to async function `run_cmd` that:
#   - takes a `cmd` of type Command
#   - prints f"Running {cmd.name} with {cmd.args}"

# TODO: Define an async function called `execute` that:
#   - takes a `cmd` of type Command
#   - runs all pre_hooks with cmd
#   - dispatches to command_dispatch[cmd.name] with cmd
#   - prints "Unknown command" if not found

# TODO: Define an async function called `main` that:
#   - awaits execute(Command(name="run", args=["--verbose"]))

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Validating: run
# Running run with ['--verbose']


# -----------------------------------------------------------------------------
# DRILL 181 — Pydantic: model_rebuild() for forward references
# -----------------------------------------------------------------------------
from pydantic import BaseModel
from typing import Optional, List

# TODO: Define a model called `Node` with:
#   - id: int
#   - next: Optional["Node"] = None

# TODO: Call Node.model_rebuild()

# TODO: Create a chain: node3 → node2 → node1
#   node1 = Node(id=1)
#   node2 = Node(id=2, next=node1)
#   node3 = Node(id=3, next=node2)

# TODO: Print node3.id, node3.next.id, node3.next.next.id

# EXPECTED:
# 3
# 2
# 1


# -----------------------------------------------------------------------------
# DRILL 182 — Async: Timeout per task using asyncio.wait_for in a loop
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions:
#   - `task_fast` that awaits asyncio.sleep(0.01) and returns "fast"
#   - `task_slow` that awaits asyncio.sleep(10) and returns "slow"

# TODO: Define an async function called `main` that:
#   - runs both tasks through asyncio.wait_for with timeout=0.1
#   - for each: if it completes, prints the result; if TimeoutError, prints "Timed out"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# fast
# Timed out


# -----------------------------------------------------------------------------
# DRILL 183 — Wrapper Decorator: Decorator that adds structured tracing
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `trace` that:
#   - wraps any function using *args, **kwargs
#   - prints f"→ {func.__name__}({args}, {kwargs})"
#   - calls the function and stores the result
#   - prints f"← {func.__name__} returned {result}"
#   - returns the result

# TODO: Apply @trace to a function called `multiply` that:
#   - takes `a` and `b`
#   - returns a * b

# TODO: Call multiply(3, 4)

# EXPECTED:
# → multiply((3, 4), {})
# ← multiply returned 12


# -----------------------------------------------------------------------------
# DRILL 184 — Registry: Registry cleared and rebuilt at runtime
# -----------------------------------------------------------------------------

# TODO: Create an empty dict called `live_registry`

# TODO: Define a function called `register` that:
#   - takes `name` and `fn`
#   - adds fn to live_registry under name

# TODO: Define functions:
#   - `handler_a` that prints "Handler A"
#   - `handler_b` that prints "Handler B"

# TODO: Register handler_a under "action"
# TODO: Call live_registry["action"]()

# TODO: Clear live_registry using .clear()
# TODO: Register handler_b under "action"
# TODO: Call live_registry["action"]()

# EXPECTED:
# Handler A
# Handler B


# -----------------------------------------------------------------------------
# DRILL 185 — OOP Decorator: Decorator applied to classmethod
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `log_classmethod` that:
#   - wraps any function using *args, **kwargs
#   - prints f"classmethod called on {args[0].__name__}"
#   - calls the original function

# TODO: Define a class called `Factory` with:
#   - a @classmethod called `create` decorated with @log_classmethod (apply log_classmethod first, then classmethod)
#   - create() prints "Factory created"

# Hint: stack decorators as:
#   @classmethod
#   @log_classmethod
#   def create(cls): ...

# TODO: Call Factory.create()

# EXPECTED:
# classmethod called on Factory
# Factory created


# -----------------------------------------------------------------------------
# DRILL 186 — Mix: Async + OOP + cancellation handling
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define a class called `Worker` with:
#   - an async method called `run` that:
#     - tries to await asyncio.sleep(10) (simulates long work)
#     - catches asyncio.CancelledError
#     - prints "Worker cancelled gracefully"
#     - re-raises the CancelledError

# TODO: Define an async function called `main` that:
#   - creates a Worker
#   - creates a task with asyncio.create_task(worker.run())
#   - awaits asyncio.sleep(0)
#   - cancels the task
#   - tries to await the task, catches CancelledError and prints "Task done"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Worker cancelled gracefully
# Task done


# -----------------------------------------------------------------------------
# DRILL 187 — Mix: Registry + wrapper + output validation
# -----------------------------------------------------------------------------
from functools import wraps

# TODO: Create an empty dict called `validated_registry`

# TODO: Define a decorator factory called `register_validated` that:
#   - takes `name` and `expected_type`
#   - wraps the function to:
#     - call it and store result
#     - if not isinstance(result, expected_type): raise TypeError(f"Bad return type")
#     - otherwise store it in validated_registry under name and return it

# TODO: Apply @register_validated("get_count", int) to a function called `get_count` that:
#   - returns 42

# TODO: Apply @register_validated("get_label", int) to a function called `get_label` that:
#   - returns "hello"   (wrong type)

# TODO: Call get_count() and print the result
# TODO: Call get_label() inside try/except and print the TypeError

# EXPECTED:
# 42
# Bad return type


# -----------------------------------------------------------------------------
# DRILL 188 — Mix: OOP + Pydantic + async + computed response model
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define models:
#   - `SearchQuery` with keyword: str and limit: int = 10
#   - `SearchResult` with results: list and total: int

# TODO: Define a class called `SearchEngine` with:
#   - an async method called `search` that:
#     - takes a `query` of type SearchQuery
#     - creates a fake list: ["result_1", "result_2", "result_3"]
#     - slices to query.limit
#     - returns SearchResult(results=sliced, total=len(sliced))

# TODO: Define an async function called `main` that:
#   - creates a SearchEngine
#   - awaits engine.search(SearchQuery(keyword="python", limit=2))
#   - prints result.total and result.results

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# 2
# ['result_1', 'result_2']


# -----------------------------------------------------------------------------
# DRILL 189 — Mix: Three-layer async pipeline with data transformation
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions:
#   - `ingest` that takes `raw` string and returns raw.split(",")
#   - `clean` that takes a list and returns [s.strip() for s in the list]
#   - `summarize` that takes a list and returns f"{len(items)} items: {items}"

# TODO: Define an async function called `pipeline` that:
#   - calls ingest → clean → summarize in sequence
#   - prints the final result

# TODO: Define an async function called `main` that:
#   - awaits pipeline(" apple , banana , cherry ")

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# 3 items: ['apple', 'banana', 'cherry']


# -----------------------------------------------------------------------------
# DRILL 190 — Mix: Full async CQRS skeleton
# Command → validate → handler → response
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel

# TODO: Define models:
#   - `RegisterCommand` with username: str and email: str
#   - `RegisterResponse` with success: bool and message: str

# TODO: Create an empty dict called `command_bus`

# TODO: Define a decorator called `handles_command` that:
#   - takes a model class
#   - saves the async function under the class in command_bus
#   - returns the function unchanged

# TODO: Apply @handles_command(RegisterCommand) to async function `register_handler` that:
#   - takes a `cmd` of type RegisterCommand
#   - returns RegisterResponse(success=True, message=f"Registered {cmd.username}")

# TODO: Define an async function called `send` that:
#   - takes any command (Pydantic model)
#   - looks up type(cmd) in command_bus
#   - awaits the handler with cmd and returns the result
#   - returns None and prints "No handler" if not found

# TODO: Define an async function called `main` that:
#   - creates RegisterCommand(username="alice", email="alice@example.com")
#   - awaits send(cmd) and prints the response

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# success=True message='Registered alice'


# -----------------------------------------------------------------------------
# DRILL 191 — Pydantic: model with model_post_init for side effects
# -----------------------------------------------------------------------------
from pydantic import BaseModel

# TODO: Define a model called `AuditLog` with:
#   - action: str
#   - user: str

# TODO: Override model_post_init(self, __context) that:
#   - prints f"[AUDIT] {self.user} performed {self.action}"

# TODO: Create AuditLog(action="delete", user="admin")
# TODO: Create AuditLog(action="login", user="alice")

# EXPECTED:
# [AUDIT] admin performed delete
# [AUDIT] alice performed login


# -----------------------------------------------------------------------------
# DRILL 192 — Async: Gathering results and filtering in one pass
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define async functions:
#   - `get_a` returns 5
#   - `get_b` returns 12
#   - `get_c` returns 3
#   - `get_d` returns 8

# TODO: Define an async function called `main` that:
#   - gathers all four using asyncio.gather()
#   - filters the results to only values > 5
#   - prints the filtered list

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# [12, 8]


# -----------------------------------------------------------------------------
# DRILL 193 — Wrapper Decorator: Decorator that validates a specific kwarg is positive
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `positive_amount` that:
#   - wraps any function using *args, **kwargs
#   - checks if kwargs.get("amount", 1) > 0
#   - if not, prints "Amount must be positive" and returns None
#   - otherwise calls the function

# TODO: Apply @positive_amount to a function called `charge` that:
#   - takes **kwargs
#   - prints f"Charging ${kwargs['amount']}"

# TODO: Call charge(amount=50)
# TODO: Call charge(amount=-10)

# EXPECTED:
# Charging $50
# Amount must be positive


# -----------------------------------------------------------------------------
# DRILL 194 — Registry: Two separate registries, merged at call time
# -----------------------------------------------------------------------------

# TODO: Create two empty dicts: `read_ops` and `write_ops`

# TODO: Define decorators `read` and `write` that each save functions to their respective dicts

# TODO: Apply @read to function `get_user` that prints "Getting user"
# TODO: Apply @write to function `save_user` that prints "Saving user"

# TODO: Merge them: all_ops = {**read_ops, **write_ops}
# TODO: Call each function in all_ops

# EXPECTED:
# Getting user
# Saving user


# -----------------------------------------------------------------------------
# DRILL 195 — OOP Decorator: Decorator that provides self fallback default
# -----------------------------------------------------------------------------

# TODO: Define a decorator called `default_name` that:
#   - wraps any method using *args, **kwargs
#   - if instance.name is None, sets instance.name = "Anonymous" before calling
#   - calls the method

# TODO: Define a class called `Greeter` with:
#   - __init__ that sets self.name = None
#   - a method called `greet` decorated with @default_name
#   - greet() prints f"Hello, {self.name}"

# TODO: Create a Greeter and call greet()
# TODO: Create another Greeter, set name = "Alice", call greet()

# EXPECTED:
# Hello, Anonymous
# Hello, Alice


# -----------------------------------------------------------------------------
# DRILL 196 — Mix: Async + OOP + exception hierarchy handling
# -----------------------------------------------------------------------------
import asyncio

# TODO: Define exception classes:
#   - `AppError(Exception)` (base)
#   - `NotFoundError(AppError)`
#   - `AuthError(AppError)`

# TODO: Define a class called `ResourceService` with:
#   - an async method called `get` that takes `resource_id`:
#     - raises NotFoundError("Resource not found") if resource_id == 0
#     - raises AuthError("Unauthorized") if resource_id == -1
#     - returns f"Resource {resource_id}"

# TODO: Define an async function called `main` that:
#   - tries to get resource 42 → prints the result
#   - tries to get resource 0 → catches NotFoundError → prints "Not found"
#   - tries to get resource -1 → catches AuthError → prints "Auth failed"

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Resource 42
# Not found
# Auth failed


# -----------------------------------------------------------------------------
# DRILL 197 — Mix: Registry + OOP + async + hot reload simulation
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `handler_store`

# TODO: Define a class called `HandlerManager` with:
#   - a @staticmethod called `register` that takes `name` and `fn` and stores in handler_store
#   - a @staticmethod called `reload` that takes `name` and `fn` and replaces in handler_store
#   - an async method called `dispatch` that takes `name` and awaits handler_store[name]

# TODO: Define async functions:
#   - `v1` that prints "Handler v1"
#   - `v2` that prints "Handler v2"

# TODO: Define an async function called `main` that:
#   - registers v1 under "action"
#   - creates a HandlerManager
#   - awaits mgr.dispatch("action")       ← should print v1
#   - reloads "action" with v2
#   - awaits mgr.dispatch("action")       ← should print v2

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# Handler v1
# Handler v2


# -----------------------------------------------------------------------------
# DRILL 198 — Mix: Full async DI container — register → resolve → call
# -----------------------------------------------------------------------------
import asyncio

# TODO: Create an empty dict called `container`

# TODO: Define a function called `provide` that:
#   - takes `name` and `factory` (a callable)
#   - stores factory in container under name

# TODO: Define an async function called `resolve` that:
#   - takes a `name`
#   - looks up the factory in container and calls it
#   - if the result is a coroutine, awaits it
#   - returns the resolved value

# TODO: Define an async function called `create_db` that:
#   - returns "DatabaseConnection"

# TODO: Register create_db under "db" using provide()
# TODO: Register a lambda that returns "CacheService" under "cache"

# TODO: Define an async function called `main` that:
#   - resolves "db" and prints it
#   - resolves "cache" and prints it

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# DatabaseConnection
# CacheService


# -----------------------------------------------------------------------------
# DRILL 199 — Mix: Pydantic + async + OOP + full request validation pipeline
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel, ValidationError, Field
from functools import wraps

# TODO: Define models:
#   - `LoginRequest` with username: str with min_length=3 and password: str with min_length=6
#   - `LoginResponse` with token: str and username: str

# TODO: Define a decorator called `validate_body` that:
#   - takes a `model` class
#   - wraps an async function
#   - the first non-self arg should be a dict; parse it as model(**data)
#   - if ValidationError, prints "Validation failed: <error>" and returns None
#   - otherwise calls the function with the parsed model instance

# TODO: Define a class called `AuthService` with:
#   - an async method called `login` decorated with @validate_body(LoginRequest) that:
#     - takes a `req` of type LoginRequest
#     - returns LoginResponse(token="tok_abc", username=req.username)

# TODO: Define an async function called `main` that:
#   - creates an AuthService
#   - valid request: {"username": "alice", "password": "secret123"}
#   - invalid request: {"username": "ab", "password": "123"}
#   - prints each result

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# token='tok_abc' username='alice'
# Validation failed: 2 validation errors for LoginRequest ...


# -----------------------------------------------------------------------------
# DRILL 200 — THE FINAL BOSS
# Pydantic + async + OOP + wrapper + registry + dynamic dispatch
# + middleware + fan-out + state machine + error handling + DI
# -----------------------------------------------------------------------------
import asyncio
from pydantic import BaseModel, ValidationError
from functools import wraps
from typing import Dict, Any, List

# --- Models ---
# TODO: Define a model called `ServiceRequest` with:
#   - service: str
#   - operation: str
#   - payload: Dict[str, Any]

# TODO: Define a model called `ServiceResponse` with:
#   - success: bool
#   - data: Any = None
#   - error: str = None

# --- State Machine ---
# TODO: Define a class called `SystemState` with:
#   - __init__ that sets self.status = "offline"
#   - async method `boot` that sets status = "online" and prints "System online"
#   - async method `shutdown` that sets status = "offline" and prints "System offline"

# --- Registry ---
# TODO: Create empty dicts: `service_registry`, `operation_registry`
# TODO: Create empty list: `request_middleware`

# TODO: Define decorator `register_service` that takes `name`, saves to service_registry, returns fn unchanged
# TODO: Define decorator `register_operation` that takes `service` and `op`, saves to operation_registry[(service, op)], returns fn unchanged
# TODO: Define decorator `request_mw` that appends async fn to request_middleware, returns unchanged

# --- Middleware ---
# TODO: Apply @request_mw to async function `log_request` that:
#   - takes a `req` of type ServiceRequest
#   - prints f"[LOG] {req.service}.{req.operation}"

# TODO: Apply @request_mw to async function `validate_service` that:
#   - takes a `req` of type ServiceRequest
#   - if req.service not in service_registry: raises ValueError(f"Unknown service: {req.service}")

# --- Services ---
# TODO: Apply @register_service("user") to async function `user_service` that just passes (it's a marker)

# TODO: Apply @register_operation("user", "create") to async function `create_user` that:
#   - takes a `req` of type ServiceRequest
#   - returns ServiceResponse(success=True, data=f"User {req.payload.get('name')} created")

# TODO: Apply @register_operation("user", "delete") to async function `delete_user` that:
#   - takes a `req` of type ServiceRequest
#   - returns ServiceResponse(success=True, data=f"User {req.payload.get('id')} deleted")

# --- Gateway ---
# TODO: Define a class called `ServiceGateway` with:
#   - __init__ that takes a `system_state` of type SystemState
#   - async method `dispatch` that:
#     - takes a `req` of type ServiceRequest
#     - if system_state.status != "online": returns ServiceResponse(success=False, error="System offline")
#     - runs all request_middleware with req; if any raises, returns ServiceResponse(success=False, error=str(e))
#     - looks up (req.service, req.operation) in operation_registry
#     - if not found: returns ServiceResponse(success=False, error="Operation not found")
#     - awaits the handler with req and returns the result

# --- Main ---
# TODO: Define an async function called `main` that:
#   - creates a SystemState and boots it
#   - creates a ServiceGateway(system_state)
#
#   - dispatches ServiceRequest(service="user", operation="create", payload={"name": "Alice"})
#   - prints the response
#
#   - dispatches ServiceRequest(service="user", operation="delete", payload={"id": 42})
#   - prints the response
#
#   - dispatches ServiceRequest(service="user", operation="ban", payload={})
#   - prints the response
#
#   - dispatches ServiceRequest(service="ghost", operation="create", payload={})
#   - prints the response
#
#   - shuts down the system
#
#   - dispatches ServiceRequest(service="user", operation="create", payload={"name": "Bob"})
#   - prints the response

# TODO: Run `main` using asyncio.run()

# EXPECTED:
# System online
# [LOG] user.create
# success=True data='User Alice created' error=None
# [LOG] user.delete
# success=True data='User 42 deleted' error=None
# [LOG] user.ban
# success=False data=None error='Operation not found'
# [LOG] ghost.create
# success=False data=None error='Unknown service: ghost'
# System offline
# success=False data=None error='System offline'
