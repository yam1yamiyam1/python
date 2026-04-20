# =============================================================================
# PYTHON BACKEND INTERNALS — 200 DRILLS
# CHUNK 1: Drills 01–20 | Concepts: Pydantic & Async/Await Foundations
# =============================================================================

import asyncio

from pydantic import BaseModel, Field, ValidationError


# =============================================================================
# DRILL 01 — Pydantic: BaseModel basics
# =============================================================================
async def run_drill_01():
    # TODO: Define a Product model with 3 fields:
    #       - name: plain string
    #       - price: float
    #       - in_stock: boolean
    # TODO: Create an instance with name="Keyboard", price=49.99, in_stock=True
    # TODO: Print the name field
    class ProductModel(BaseModel):
        name: str
        price: float
        in_stock: bool

    instance = ProductModel(name="Keyboard", price=49.99, in_stock=True)
    print(instance.name)
    # EXPECTED OUTPUT:
    # Keyboard
    pass


# =============================================================================
# DRILL 02 — Pydantic: Default values
# =============================================================================
async def run_drill_02():
    # TODO: Define a UserProfile model with 3 fields:
    #       - username: plain string
    #       - bio: string, defaults to "No bio yet"
    #       - followers: integer, defaults to 0
    # TODO: Create an instance using only username="alice"
    # TODO: Print bio and followers on separate lines
    class UserProfile(BaseModel):
        username: str
        bio: str = Field(default="No bio yet")
        followers: int = Field(default=0)

    instance = UserProfile(username="Alice")
    print(instance.bio)
    print(instance.followers)
    # EXPECTED OUTPUT:
    # No bio yet
    # 0
    pass


# =============================================================================
# DRILL 03 — Pydantic: Field() with constraints
# =============================================================================
async def run_drill_03():
    # TODO: Define an Order model with 3 fields:
    #       - item_name: plain string
    #       - quantity: integer, must be greater than 0, add a description "Must be positive"
    #       - discount: float, defaults to 0.0, must be between 0.0 and 1.0 inclusive
    # TODO: Create a valid instance: item_name="Widget", quantity=3, discount=0.1
    # TODO: Print quantity and discount on separate lines
    class Order(BaseModel):
        item_name: str
        quantity: int = Field(gt=0, description="Must be positive")
        discount: float = Field(default=0.0, ge=0.0, le=1.0)

    instance = Order(item_name="Widget", quantity=3, discount=0.1)
    print(instance.quantity)
    print(instance.discount)
    # EXPECTED OUTPUT:
    # 3
    # 0.1
    pass


# =============================================================================
# DRILL 04 — Pydantic: ValidationError on bad data
# =============================================================================
async def run_drill_04():
    # TODO: Reuse or redefine the Order model from Drill 03
    # TODO: Attempt to create an Order with quantity=-1 inside a try/except block
    # TODO: Catch ValidationError, loop through e.errors(), and print: "Caught: quantity"
    #       Hint: the field name is at error['loc'][0]
    class Order(BaseModel):
        item_name: str
        quantity: int = Field(gt=0, description="Must be positive")
        discount: float = Field(default=0.0, ge=0.0, le=1.0)

    try:
        Order(item_name="test", quantity=-1)
    except ValidationError as e:
        print(e)
    # EXPECTED OUTPUT:
    # Caught: quantity
    pass


# =============================================================================
# DRILL 05 — Pydantic: Dict-to-model with model_validate()
# =============================================================================
async def run_drill_05():
    # TODO: Define a BlogPost model with 3 fields:
    #       - title: plain string
    #       - tags: list of strings
    #       - published: boolean
    # TODO: Create this raw dict:
    #       data = {"title": "Async Python", "tags": ["python", "async"], "published": True}
    # TODO: Parse it using model_validate() (not the constructor)
    # TODO: Print the title and the first tag on separate lines

    # EXPECTED OUTPUT:
    # Async Python
    # python
    pass


# =============================================================================
# DRILL 06 — Pydantic: Nested models
# =============================================================================
async def run_drill_06():
    # TODO: Define an Address model with 2 fields: street (string), city (string)
    # TODO: Define a Customer model with 2 fields:
    #       - name: string
    #       - address: type is Address (nested model)
    # TODO: Create a Customer with a nested Address where city="Manila"
    # TODO: Print customer.address.city

    # EXPECTED OUTPUT:
    # Manila
    pass


# =============================================================================
# DRILL 07 — Pydantic: model_dump()
# =============================================================================
async def run_drill_07():
    # TODO: Define a Session model with 3 fields:
    #       - session_id: string
    #       - user_id: integer
    #       - active: boolean
    # TODO: Create an instance with session_id="abc123", user_id=42, active=True
    # TODO: Call model_dump() on it and store the result
    # TODO: Print the result, then print type(result)

    # EXPECTED OUTPUT:
    # {'session_id': 'abc123', 'user_id': 42, 'active': True}
    # <class 'dict'>
    pass


# =============================================================================
# DRILL 08 — Pydantic: Custom field_validator
# =============================================================================
async def run_drill_08():
    # TODO: Define a SignupForm model with 2 fields: username (string), email (string)
    # TODO: Add a field_validator on "email" that raises a ValueError if "@" is not in the value
    # TODO: Try creating SignupForm(username="bob", email="notanemail") inside a try/except
    # TODO: Catch ValidationError, find the failing field name, and print: "Caught: email"

    # EXPECTED OUTPUT:
    # Caught: email
    pass


# =============================================================================
# DRILL 09 — Pydantic: Optional fields
# =============================================================================
async def run_drill_09():
    # TODO: Define a Report model with 2 fields:
    #       - title: plain string
    #       - summary: optional string, defaults to None
    # TODO: Create one instance with summary="All good"
    # TODO: Create another instance without providing summary
    # TODO: Print both summaries on separate lines

    # EXPECTED OUTPUT:
    # All good
    # None
    pass


# =============================================================================
# DRILL 10 — Pydantic: model_dump() with exclude
# =============================================================================
async def run_drill_10():
    # TODO: Define a PaymentRecord model with 3 fields:
    #       - card_holder: string
    #       - amount: float
    #       - card_number: string
    # TODO: Create an instance: card_holder="Jane Doe", amount=120.0, card_number="4111111111111111"
    # TODO: Call model_dump() and exclude the card_number field
    # TODO: Print the result

    # EXPECTED OUTPUT:
    # {'card_holder': 'Jane Doe', 'amount': 120.0}
    pass


# =============================================================================
# DRILL 11 — Async/Await: Basic async def and await
# =============================================================================
async def run_drill_11():
    # TODO: Define an inner async function fetch_greeting() that returns the string "Hello, async world!"
    # TODO: Await it inside run_drill_11 and print the result

    # EXPECTED OUTPUT:
    # Hello, async world!
    pass


# =============================================================================
# DRILL 12 — Async/Await: asyncio.sleep() — simulating I/O
# =============================================================================
async def run_drill_12():
    # TODO: Define an inner async function slow_task(name, delay) that:
    #       - awaits asyncio.sleep(delay) to simulate a wait
    #       - returns the string f"{name} done"
    # TODO: Await slow_task("DB Query", 0) and print the result

    # EXPECTED OUTPUT:
    # DB Query done
    pass


# =============================================================================
# DRILL 13 — Async/Await: asyncio.gather() — concurrent tasks
# =============================================================================
async def run_drill_13():
    # TODO: Define an inner async function task(label) that awaits asyncio.sleep(0) and returns label
    # TODO: Use asyncio.gather() to run task("A"), task("B"), task("C") at the same time
    # TODO: Print the results as a list

    # EXPECTED OUTPUT:
    # ['A', 'B', 'C']
    pass


# =============================================================================
# DRILL 14 — Async/Await: Unpacking gather() results
# =============================================================================
async def run_drill_14():
    # TODO: Define async function get_user() that returns the string "alice"
    # TODO: Define async function get_score() that returns the integer 95
    # TODO: Gather both and unpack into variables: user, score
    # TODO: Print user and score on separate lines

    # EXPECTED OUTPUT:
    # alice
    # 95
    pass


# =============================================================================
# DRILL 15 — Async/Await: asyncio.Queue basics
# =============================================================================
async def run_drill_15():
    # TODO: Create an asyncio.Queue
    # TODO: Put "job_1" and "job_2" into the queue using await queue.put()
    # TODO: Get and print each item using await queue.get()

    # EXPECTED OUTPUT:
    # job_1
    # job_2
    pass


# =============================================================================
# DRILL 16 — Async/Await: Producer–Consumer pattern
# =============================================================================
async def run_drill_16():
    # TODO: Create an asyncio.Queue
    # TODO: Define async producer() that puts "task_A" then "task_B" into the queue
    # TODO: Define async consumer() that gets 2 items and prints each one prefixed with "Processing:"
    # TODO: Await producer() first, then await consumer()

    # EXPECTED OUTPUT:
    # Processing: task_A
    # Processing: task_B
    pass


# =============================================================================
# DRILL 17 — Async/Await: asyncio.Lock — preventing race conditions
# =============================================================================
async def run_drill_17():
    # TODO: Create an asyncio.Lock and a shared counter variable set to 0
    # TODO: Define async increment(lock) that acquires the lock and adds 1 to the counter
    # TODO: Use asyncio.gather() to call increment() 5 times concurrently
    # TODO: Print the final counter value
    #       Hint: counter must be accessible inside increment() — think about scope

    # EXPECTED OUTPUT:
    # 5
    pass


# =============================================================================
# DRILL 18 — Async/Await: asyncio.wait_for() — timeout handling
# =============================================================================
async def run_drill_18():
    # TODO: Define async long_task() that awaits asyncio.sleep(999)
    # TODO: Wrap asyncio.wait_for(long_task(), timeout=0.001) in a try/except
    # TODO: Catch the timeout error and print: "Task timed out"

    # EXPECTED OUTPUT:
    # Task timed out
    pass


# =============================================================================
# DRILL 19 — Async/Await: Sequential vs concurrent execution
# =============================================================================
async def run_drill_19():
    # TODO: Define async job(name) that awaits asyncio.sleep(0) and prints f"job {name} complete"
    # TODO: Run job("X") and job("Y") concurrently using asyncio.gather()
    # TODO: Then run job("P") and job("Q") sequentially using two separate awaits

    # EXPECTED OUTPUT:
    # job X complete
    # job Y complete
    # job P complete
    # job Q complete
    pass


# =============================================================================
# DRILL 20 — Async/Await: Async function returning a Pydantic model
# =============================================================================
async def run_drill_20():
    # TODO: Define a UserResponse Pydantic model with 2 fields: id (integer), username (string)
    # TODO: Define async fetch_user(user_id: int) that returns a hardcoded UserResponse instance
    #       Use: id=1, username="alice"
    # TODO: Await fetch_user(1) and print result.username then result.id on separate lines

    # EXPECTED OUTPUT:
    # alice
    # 1
    pass


# =============================================================================
# MAIN RUNNER — CHUNK 1
# =============================================================================
async def main():
    drills = [
        run_drill_01,
        run_drill_02,
        run_drill_03,
        run_drill_04,
        run_drill_05,
        run_drill_06,
        run_drill_07,
        run_drill_08,
        run_drill_09,
        run_drill_10,
        run_drill_11,
        run_drill_12,
        run_drill_13,
        run_drill_14,
        run_drill_15,
        run_drill_16,
        run_drill_17,
        run_drill_18,
        run_drill_19,
        run_drill_20,
    ]
    for drill in drills:
        print(f"\n--- {drill.__name__} ---")
        await drill()


if __name__ == "__main__":
    asyncio.run(main())
