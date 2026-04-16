# 🧰 PROGRESSION SESSION: TOOLBOX & TICKET 1

## 🧱 THE LEGO BRICKS (Generic Syntax)

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
    instance = GenericModel(**{"var_string": "hello", ...})
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

    @async_generic_decorator
    async def generic_method(self, data: dict):
        # In the decorator wrapper, args[0] is 'self'!
        pass
```

---
