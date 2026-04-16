import asyncio

from pydantic import BaseModel, Field, ValidationError


# 1
class UserProfile(BaseModel):
    username: str = Field(min_length=3)
    age: int = Field(gt=18)


def attempt_login(payload: dict):
    try:
        valid_data = UserProfile(**payload)
        print(f"Valid user: {valid_data.username}")
    except ValidationError:
        print("Invalid user data")


# 2
event_listeners = {}


def on_event(event_name: str):
    def decorator(fn):
        event_listeners[event_name] = fn
        return fn

    return decorator


@on_event("click")
async def handle_click():
    pass


# 3 i dont know

# 4


def track_usage(fn):
    async def wrapper(*args):
        self = args[0]
        await fn(*args)
        self.api_calls += 1
        return fn

    return wrapper


class RateLimiter:
    def __init__(self):
        self.api_calls = 0

    @track_usage
    async def fetch_data(self):
        return "Data fetched"


async def main():
    test1 = await asyncio.run(attempt_login({"username": "Yo", "age": 20}))
    print(test1)
    print(event_listeners)


asyncio.run(main())
