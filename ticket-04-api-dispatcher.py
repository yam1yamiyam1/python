import asyncio

from pydantic import BaseModel, Field, ValidationError


class CheckoutPayload(BaseModel):
    item_id: int
    amount: float = Field(gt=0)


class NotifyPayload(BaseModel):
    username: str
    message: str = Field(min_length=5)


class APIRouter:
    def __init__(self):
        self.routes = {}

    def post(self, path: str):
        def decorator(fn):
            self.routes[path] = fn
            return fn

        return decorator

    async def dispatch(self, path: str, payload: dict):
        if path not in self.routes:
            return f"404 Error: Path {path} not found"
        else:
            return await self.routes[path](payload)


app = APIRouter()


@app.post("/checkout")
async def process_checkout(payload: dict):
    try:
        valid_data = CheckoutPayload(**payload)
        return f"Checkout Successful for item {valid_data.item_id}"
    except ValidationError:
        return "Checkout Failed: Bad Data"


@app.post("/notify")
async def send_notifications(payload: dict):
    try:
        valid_data = NotifyPayload(**payload)
        return f"Notification sent to {valid_data.username}"
    except ValidationError:
        return "Notify Failed: Bad Data"


async def main():
    # Simulated incoming web requests
    requests = [
        # 1. Valid Checkout
        {"path": "/checkout", "payload": {"item_id": 101, "amount": 25.50}},
        # 2. Invalid Checkout (amount is negative)
        {"path": "/checkout", "payload": {"item_id": 102, "amount": -5.00}},
        # 3. Valid Notification
        {"path": "/notify", "payload": {"username": "Yam", "message": "Hello World!"}},
        # 4. Invalid Notification (message too short)
        {"path": "/notify", "payload": {"username": "Yam", "message": "Hi"}},
        # 5. 404 Not Found (Path doesn't exist)
        {"path": "/delete_user", "payload": {"user_id": 1}},
    ]

    for req in requests:
        print(f"Incoming Request to {req['path']}...")
        # The router dynamically figures out which function to run!
        result = await app.dispatch(req["path"], req["payload"])
        print(f"Response: {result}\n")

    print("Registered Routes Engine:", app.routes)


asyncio.run(main())
