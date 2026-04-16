import asyncio

from pydantic import BaseModel, Field, ValidationError


# 1. Nested Models
class ContactInfo(BaseModel):
    email: str
    phone: str = Field(pattern=r"^[0-9]{10}$")


class NotificationPayload(BaseModel):
    message: str
    user: ContactInfo


# 2. Decorator Factory (3 layers)
def retry(max_retries: int):
    def decorator(fn):
        async def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return await fn(*args, **kwargs)
                except ConnectionError:
                    print(f"⚠️ Network glitch (Attempt {attempt + 1}). Retrying...")

            # If the loop finishes without returning success
            return "🚨 ERROR: Unreachable"

        return wrapper

    return decorator


# 3. Vanilla Class
class NotificationService:
    def __init__(self):
        self.network_attempts = 0

    @retry(max_retries=3)
    async def send_alert(self, raw_request: dict) -> str:
        try:
            payload = NotificationPayload(**raw_request)

            # Deterministic failure: Force it to fail twice, succeed on the 3rd
            self.network_attempts += 1
            if self.network_attempts < 3:
                await asyncio.sleep(1)  # Pause so you can see the retry happen
                raise ConnectionError("Network Down!")

            # If it survives, reset the counter for the next message
            self.network_attempts = 0

            print(f"\n📱 [MESSAGE SENT TO {payload.user.phone}]")
            print(f"✉️  {payload.message}\n")
            await asyncio.sleep(1)

            return "✅ SUCCESS"

        except ValidationError:
            return "❌ ERROR: Invalid Contact Data"


service = NotificationService()


# 4. Interactive Test Runner
async def main():
    print("=== 📡 NOTIFICATION TERMINAL ONLINE ===")

    # Keep the drafted message outside the loop!
    draft_msg = ""
    draft_email = ""

    while True:
        print("\n--- Message Draft ---")

        # Only ask for a new message if we don't have a draft
        if not draft_msg:
            draft_msg = input("Enter message (or type 'quit'): ")
            if draft_msg.lower() == "quit":
                break

        if not draft_email:
            draft_email = input("Enter user email: ")

        # We always ask for the phone number so you can fix typos
        phone = input("Enter user phone (10 digits): ")

        raw_request = {
            "message": draft_msg,
            "user": {"email": draft_email, "phone": phone},
        }

        print("\n⏳ Dispatching...")
        result = await service.send_alert(raw_request)
        print(f"System Response: {result}")

        # If it was successful, clear the draft so we can write a new one!
        if "SUCCESS" in result:
            draft_msg = ""
            draft_email = ""
        # If it failed, the loop restarts but keeps our draft_msg!


if __name__ == "__main__":
    asyncio.run(main())
