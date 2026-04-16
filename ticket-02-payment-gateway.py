import asyncio

from pydantic import BaseModel, Field, ValidationError


class PaymentPayload(BaseModel):
    transaction_id: str
    card_number: str = Field(pattern=r"^[a-zA-Z0-9]{16}$")
    amount: float = Field(gt=0)


def idempotent(fn):
    async def wrapper(*args):
        self, raw_request = args[0], args[1]
        tx_id = raw_request["transaction_id"]
        if tx_id in self.processed_transactions:
            return "BLOCKED: Duplicate Transaction"
        else:
            result = await fn(*args)
            if result == "SUCCESS":
                self.processed_transactions.add(tx_id)
            return result

    return wrapper


class PaymentGateway:
    def __init__(self):
        self.processed_transactions = set()

    @idempotent
    async def charge(self, raw_request: dict) -> str:
        try:
            PaymentPayload(**raw_request)
            await asyncio.sleep(1)
            return "SUCCESS"
        except ValidationError:
            return "ERROR: Invalid Data"


# ... your existing code (PaymentPayload, @idempotent, PaymentGateway) ...

gateway = PaymentGateway()

test_requests = [
    # 1. Valid charge (Should print: SUCCESS)
    {"transaction_id": "tx_001", "card_number": "1234567812345678", "amount": 50.00},
    # 2. Duplicate charge (Should print: BLOCKED: Duplicate Transaction)
    {"transaction_id": "tx_001", "card_number": "1234567812345678", "amount": 50.00},
    # 3. Invalid card - 15 digits (Should print: ERROR: Invalid Data)
    {"transaction_id": "tx_002", "card_number": "123456781234567", "amount": 25.00},
    # 4. Valid charge (Should print: SUCCESS)
    {"transaction_id": "tx_003", "card_number": "8765432187654321", "amount": 100.00},
]


async def main():
    print("--- Starting Payment Processing ---")
    for req in test_requests:
        print(f"Processing {req['transaction_id']}...")
        result = await gateway.charge(req)
        print(f"Result: {result}\n")

    print("--- Final Database State ---")
    print(f"Processed Transactions: {gateway.processed_transactions}")


if __name__ == "__main__":
    asyncio.run(main())
