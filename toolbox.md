### 1. Pydantic `BaseModel` & `Field` (Validation)

```python
from pydantic import BaseModel, Field, ValidationError

class GenericModel(BaseModel):
    var_string: str
    var_integer: int
    var_list: list[int]

    # Field(**validators)
    constrained_num: float = Field(gt=0.0) # gt = greater than
    constrained_str: str = Field(min_length=5)

# Usage:
try:
    instance = GenericModel(**{"var_string": "hello", "var_integer": 1, "var_list": [1], "constrained_num": 1.5, "constrained_str": "hello world"})
    safe_dict = instance.model_dump() # Converts back to dict
except ValidationError as e:
    print(e)
```

### 2. Async Basics (Non-Blocking)

```python
import asyncio

async def simulate_database_save(data: dict) -> bool:
    await asyncio.sleep(1) # Simulate waiting without freezing the app
    return True

# To run: result = await simulate_database_save({"id": 1})
```

### 3. Async Decorators

```python
import time

def async_generic_decorator(func):
    async def wrapper(*args, **kwargs):
        # Code BEFORE the function runs
        start = time.time()

        # Await the original async function
        result = await func(*args, **kwargs)

        # Code AFTER the function runs
        print(f"Time taken: {time.time() - start}")
        return result
    return wrapper
```

### 4. OOP + Decorators Trap

```python
class GenericClass:
    def __init__(self):
        self.state = "active"
        self.processed_items = set()

    @async_generic_decorator
    async def generic_method(self, data: dict):
        # In the decorator wrapper, args[0] is 'self'!
        # This means the wrapper can access and modify `self.processed_items` directly.
        pass
```

### 5. Nested Pydantic Models

```python
from pydantic import BaseModel

# Define the "inner" data first
class Address(BaseModel):
    city: str
    zip_code: str

# Use the inner class as a type hint in the "outer" data
class User(BaseModel):
    username: str
    address: Address

# It automatically validates nested dictionaries!
data = {
    "username": "Yam",
    "address": {
        "city": "Tokyo",
        "zip_code": "100-0001"
    }
}
```

### 6. Decorators with Arguments

```python
# To pass arguments to a decorator (like @retry(times=3)),
# you need THREE levels of functions!
def repeat_decorator(times: int):
    # Level 1: Receives the decorator arguments

    def decorator(func):
        # Level 2: Receives the function being wrapped

        async def wrapper(*args, **kwargs):
            # Level 3: Receives the function's arguments (self, raw_request)
            for _ in range(times):
                print("Running...")
                result = await func(*args, **kwargs)
            return result

        return wrapper
    return decorator
```

### 7. The Registry Pattern (Decorators without Wrappers)

Decorators execute at _import/definition time_. We can use this to our advantage. If we don't need to run code _before_ or _after_ the function, we don't need the `wrapper` layer at all! We just do something with the function, and return it untouched.

```python
# A global dictionary acting as our "router"
route_registry = {}

def register_route(path: str):
    # Level 1: Takes the argument (e.g., "/checkout")

    def decorator(func):
        # Level 2: Takes the function being decorated

        # 1. Save the function's memory address into the dictionary
        route_registry[path] = func

        # 2. Return the ORIGINAL function (No async wrapper needed!)
        return func

    return decorator

# --- Usage ---
@register_route("/ping")
async def ping_handler(data: dict):
    return {"status": "pong"}

# Look! The function is now saved in the dictionary under the key "/ping"!
print(route_registry)
# Output: {'/ping': <function ping_handler at 0x...>}
```

### 8. Class-Bound Decorators (The `app.post` illusion)

In modern frameworks, the router isn't usually a global variable. It's a class instance (like `app = FastAPI()`). You can put a decorator factory _inside_ a class so it can access `self.routes`!

```python
class APIRouter:
    def __init__(self):
        # The internal state storing our paths -> functions
        self.routes = {}

    def post(self, path: str):
        """This method ACTS as a decorator factory."""
        def decorator(func):
            # Save the function into the instance's dictionary
            self.routes[path] = func
            return func
        return decorator

# --- Usage ---
router = APIRouter()

@router.post("/checkout")
async def handle_checkout(payload: dict):
    print("Checkout logic goes here.")
```

### 9. Dynamic Dispatch (Calling functions from a dictionary)

Once your functions are registered in a dictionary, you can call them dynamically based on user input (like an incoming HTTP request path).

```python
async def dispatch_request(router_instance, requested_path: str, payload: dict):
    # 1. Check if the path exists in our dictionary
    if requested_path in router_instance.routes:
        # 2. Get the function object
        handler_func = router_instance.routes[requested_path]

        # 3. Execute it!
        result = await handler_func(payload)
        return result
    else:
        raise ValueError(f"404 Not Found: {requested_path}")
```

---
