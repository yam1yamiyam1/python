import asyncio
import time

from pydantic import BaseModel, Field, ValidationError


def time_it(fn):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await fn(*args, **kwargs)
        print(f"Executed in: {time.time() - start}s")
        return result

    return wrapper


class OrderPayload(BaseModel):
    customer_email: str = Field(min_length=5)
    item_ids: list[int]
    total_price: float = Field(gt=0)


class OrderService:
    def __init__(self):
        self.db = []

    @time_it
    async def process_order(self, raw_request: dict) -> str:
        try:
            process = OrderPayload(**raw_request)
            self.db.append(process.model_dump())
            await asyncio.sleep(1)
            return "SUCCESS"
        except ValidationError:
            print("ERROR: Invalid Data")


service = OrderService()

test_requests = [
    # 1. Should pass validation, take ~1 second, and return SUCCESS
    {"customer_email": "test@mail.com", "item_ids": [101, 102], "total_price": 45.99},
    # 2. Should fail validation (price is 0), run instantly, return ERROR
    {"customer_email": "cheap@mail.com", "item_ids": [103], "total_price": 0.0},
    # 3. Should fail validation (email too short), run instantly, return ERROR
    {"customer_email": "a@b", "item_ids": [104], "total_price": 10.00},
]


async def main():
    print("--- Starting Processing ---")
    for req in test_requests:
        result = await service.process_order(req)
        print(f"Result: {result}\n")

    print(f"Final DB state: {service.db}")


if __name__ == "__main__":
    asyncio.run(main())
