import os
import sys
import asyncio

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "data"))
from training_data import numbers, orders, products, students, users

# =============================================================================
# DRILL 11 — PYDANTIC
# =============================================================================
# HOW TO RUN:  pip install pydantic
#              python drill-11-pydantic.py
# RULES:       Write your answer directly below each drill.
#              Every drill must print something.
#              No skipping — do them in order.
# =============================================================================

# NEW SYNTAX REFERENCE
# --------------------
# INSTALL:      pip install pydantic
#
# BASIC MODEL:
#   from pydantic import BaseModel
#
#   class User(BaseModel):
#       name: str
#       age: int
#       role: str = "user"        # default value
#       bio: str | None = None    # optional field
#
# CREATING AN INSTANCE:
#   user = User(name="Alice", age=32)        # keyword args
#   user = User(**{"name": "Alice", "age": 32})  # from dict
#
# ACCESSING FIELDS:
#   user.name        # dot access — like a normal class
#
# SERIALIZING:
#   user.model_dump()              # → plain dict
#   user.model_dump_json()         # → JSON string
#
# PARSING FROM DICT:
#   user = User.model_validate({"name": "Alice", "age": 32})
#
# VALIDATION:
#   Pydantic validates types automatically on creation.
#   User(name="Alice", age="not_a_number")  → raises ValidationError
#   But it also COERCES where it can:
#   User(name="Alice", age="32")  → age becomes int 32 (coerced from str)
#
# FIELD WITH CONSTRAINTS:
#   from pydantic import Field
#   class User(BaseModel):
#       name: str = Field(min_length=1, max_length=50)
#       age: int = Field(ge=0, lt=150)       # ge=greater-or-equal, lt=less-than
#       salary: float = Field(gt=0)          # gt=greater-than
#
# VALIDATORS:
#   from pydantic import field_validator
#   class User(BaseModel):
#       name: str
#       @field_validator("name")
#       @classmethod
#       def name_must_not_be_empty(cls, v):
#           if not v.strip():
#               raise ValueError("name cannot be blank")
#           return v.strip()      # validators can also transform the value
#
# NESTED MODELS:
#   class Address(BaseModel):
#       city: str
#       country: str
#
#   class User(BaseModel):
#       name: str
#       address: Address          # nested model
#
# MODEL CONFIG:
#   class User(BaseModel):
#       model_config = {"str_strip_whitespace": True}  # strips all str fields
#       name: str


# =============================================================================
# SECTION A — BASIC MODELS (1–15)
# =============================================================================

from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional

# 1. Define a Pydantic model `UserModel` with fields:
#    name: str, age: int, role: str, salary: int, isActive: bool
#    Create an instance from users[0] using UserModel(**users[0]).
#    Print the instance. Print instance.name and instance.salary.

# 2. Create UserModel instances from ALL users using a list comprehension.
#    Print each one.

# 3. Call .model_dump() on users[0] as a UserModel.
#    Print the result. Confirm it's a plain dict.
#    Print type(result).

# 4. Call .model_dump_json() on users[0] as a UserModel.
#    Print the result. Notice it's a JSON string, not a dict.

# 5. Use UserModel.model_validate(users[0]) to create an instance.
#    Print it. This is the same as UserModel(**users[0]) but the FastAPI way.

# 6. Pydantic coerces types. Try: UserModel(name="Test", age="29", role="user", salary="50000", isActive=1)
#    Note: age is a string "29", isActive is int 1 — Pydantic converts them.
#    Print the result and the types of age and isActive.

# 7. Pydantic raises ValidationError on bad data.
#    Try: UserModel(name="Test", age="not_a_number", role="user", salary=0, isActive=True)
#    Wrap in try/except ValidationError and print the error.
#    Hint: from pydantic import ValidationError

# 8. Define a model `ProductModel` with:
#    id: int, name: str, price: float, category: str, inStock: bool, quantity: int
#    Create instances from ALL products. Print only the available ones (inStock=True).

# 9. Define a model `OrderModel` with:
#    id: int, userId: int, productId: int, quantity: int, total: int, status: str
#    Create all orders. Print orders where status == "completed".

# 10. Add a default value to UserModel: role defaults to "user" if not provided.
#     Test: UserModel(name="Yuan", age=25, salary=40000, isActive=True)
#     Print the role — should be "user".

# 11. Add an optional field `bio: str | None = None` to UserModel.
#     Create one with bio and one without. Print both.

# 12. Access a nested key — add a computed approach:
#     Create a UserModel from users[0].
#     Print f"{user.name} is {'active' if user.isActive else 'inactive'}"

# 13. model_dump() with include/exclude:
#     user = UserModel(**users[0])
#     Print user.model_dump(include={"name", "role"})    # only name and role
#     Print user.model_dump(exclude={"salary", "id"})    # everything except salary and id

# 14. Convert ALL users to UserModel, then call model_dump() on each,
#     and collect into a list of dicts. Print it.
#     This is what FastAPI does when it serializes a response.

# 15. Create a UserModel list response wrapper:
#     class UserListResponse(BaseModel):
#         data: list[UserModel]
#         total: int
#     Instantiate it with all users. Print total. Print data[0].name.


# =============================================================================
# SECTION B — FIELD CONSTRAINTS AND VALIDATORS (16–30)
# =============================================================================

# 16. Add Field constraints to UserModel:
#     name: str = Field(min_length=1, max_length=100)
#     age: int = Field(ge=0, lt=150)
#     salary: int = Field(ge=0)
#     Test with valid data (users[0]). Then test with age=-1 — catch ValidationError.

# 17. Add a constraint to ProductModel:
#     price: float = Field(gt=0)
#     quantity: int = Field(ge=0)
#     Test with a product where price=0 — should raise ValidationError.

# 18. Write a field_validator for UserModel that ensures name is title-cased.
#     (i.e., "alice" becomes "Alice", "ALICE" becomes "Alice")
#     Syntax:
#       @field_validator("name")
#       @classmethod
#       def normalize_name(cls, v: str) -> str:
#           return v.strip().title()
#     Test with UserModel(name="  alice  ", age=25, role="user", salary=40000, isActive=True).
#     Print name — should be "Alice".

# 19. Write a field_validator for UserModel that ensures role is one of:
#     ["admin", "user", "moderator"]. Raise ValueError if not.
#     Test with role="hacker" — catch ValidationError and print the error.

# 20. Write a field_validator for OrderModel that ensures status is one of:
#     ["pending", "shipped", "completed", "cancelled"].
#     Test valid and invalid statuses.

# 21. Write a field_validator for ProductModel that ensures name is not blank
#     after stripping whitespace. Raise ValueError("name cannot be blank").
#     Test with name="   " — catch ValidationError.

# 22. Write a field_validator on UserModel for age that raises ValueError
#     if age < 18 with message "must be at least 18".
#     Test with age=15 — catch and print error.

# 23. Use a model_validator (whole-model validation) to check that
#     if isActive is True, salary must be > 0.
#     NEW SYNTAX:
#       @model_validator(mode="after")
#       def check_active_salary(self):
#           if self.isActive and self.salary <= 0:
#               raise ValueError("active users must have salary > 0")
#           return self
#     Test with isActive=True, salary=0 — catch ValidationError.

# 24. Use model_config to auto-strip whitespace from all string fields:
#     class UserModel(BaseModel):
#         model_config = {"str_strip_whitespace": True}
#     Test: UserModel(name="  Alice  ", ...) → name should be "Alice" with no spaces.

# 25. Use model_config to forbid extra fields:
#     model_config = {"extra": "forbid"}
#     Try passing an unknown field like UserModel(..., nickname="ace") — catch ValidationError.

# 26. Use model_config to allow extra fields and store them:
#     model_config = {"extra": "allow"}
#     Try UserModel(**users[0], nickname="ace").
#     Print instance.nickname — should work.

# 27. Write a validator that transforms salary: if salary is given as a string
#     like "72000" or "72,000", strip commas and convert to int.
#     @field_validator("salary", mode="before")
#     @classmethod
#     def parse_salary(cls, v):
#         if isinstance(v, str):
#             return int(v.replace(",", ""))
#         return v
#     Test: UserModel(name="Alice", age=32, role="admin", salary="72,000", isActive=True)
#     Print salary — should be int 72000.

# 28. Write a field_validator that validates email format (basic check):
#     Add an optional field `email: str | None = None` to UserModel.
#     Validator: if email is provided, it must contain "@" and ".".
#     Raise ValueError("invalid email") if not.
#     Test with email="alice@example.com" (valid) and email="notanemail" (invalid).

# 29. Chain two validators on the same field — name must be:
#     1. non-empty after stripping
#     2. title-cased
#     Both as separate @field_validator("name") methods with different names.
#     Test with "  ALICE  " → should become "Alice".

# 30. Write a model `CreateUserRequest` (for POST /users) and
#     `UserResponse` (for GET /users response) — different shapes:
#     CreateUserRequest: name, age, role, salary, isActive (no id)
#     UserResponse: id, name, age, role  (no salary, no isActive — hidden from API)
#     Convert users[0] to both. Print both model_dump() results.
#     This is exactly how FastAPI separates input and output schemas.


# =============================================================================
# SECTION C — NESTED MODELS AND RELATIONSHIPS (31–45)
# =============================================================================

# 31. Define a nested model:
#     class RoleModel(BaseModel):
#         title: str
#         level: int
#
#     class UserWithRole(BaseModel):
#         name: str
#         age: int
#         role: RoleModel
#
#     Create: UserWithRole(name="Alice", age=32, role={"title": "admin", "level": 3})
#     Note: Pydantic automatically converts the dict to RoleModel.
#     Print user.role.title and user.role.level.

# 32. Define an OrderWithProduct model that embeds a ProductModel:
#     class OrderWithProduct(BaseModel):
#         id: int
#         quantity: int
#         total: int
#         status: str
#         product: ProductModel
#
#     Manually build one using orders[0] + products[0]. Print it.

# 33. Define a UserWithOrders model:
#     class UserWithOrders(BaseModel):
#         id: int
#         name: str
#         orders: list[OrderModel]
#
#     Build it for users[0] by filtering orders where userId == 1.
#     Print user.name and len(user.orders).

# 34. Add a computed property to a model using @property:
#     class ProductModel(BaseModel):
#         name: str
#         price: float
#         quantity: int
#
#         @property
#         def total_value(self) -> float:
#             return self.price * self.quantity
#
#     Print total_value for all products.
#     Note: @property works in Pydantic models just like regular classes.

# 35. Use model_validator to auto-compute a field:
#     class OrderModel(BaseModel):
#         quantity: int
#         unit_price: float
#         total: float = 0.0
#
#         @model_validator(mode="after")
#         def compute_total(self):
#             self.total = self.quantity * self.unit_price
#             return self
#
#     Create: OrderModel(quantity=3, unit_price=85.0)
#     Print total — should be 255.0 (auto-computed).

# 36. Write a model `PaginatedResponse` that is generic:
#     class PaginatedResponse(BaseModel):
#         data: list[dict]
#         page: int
#         size: int
#         total: int
#
#     @property
#     def pages(self) -> int:
#         return (self.total + self.size - 1) // self.size
#
#     Build one with users as data, page=1, size=3. Print pages.

# 37. Write a model `LoginRequest`:
#     class LoginRequest(BaseModel):
#         username: str = Field(min_length=3)
#         password: str = Field(min_length=8)
#
#     And a model `LoginResponse`:
#     class LoginResponse(BaseModel):
#         access_token: str
#         token_type: str = "bearer"
#         user: UserModel
#
#     Simulate a login: if username=="alice" and password=="secret123",
#     return LoginResponse(access_token="fake-jwt-token", user=UserModel(**users[0])).
#     Print the response.

# 38. Write a model `ErrorResponse`:
#     class ErrorResponse(BaseModel):
#         detail: str
#         code: int
#         field: str | None = None
#
#     Create errors for: 404 not found, 422 validation error, 403 forbidden.
#     Print all three.

# 39. Write a model `UpdateUserRequest` where ALL fields are optional
#     (for PATCH /users/{id} — only send what you want to change):
#     class UpdateUserRequest(BaseModel):
#         name: str | None = None
#         age: int | None = None
#         role: str | None = None
#         salary: int | None = None
#         isActive: bool | None = None
#
#     Write a function `apply_update(user: dict, update: UpdateUserRequest) -> dict`
#     that merges only the non-None fields from update into user.
#     Hint: update.model_dump(exclude_none=True)
#     Test: apply_update(users[0], UpdateUserRequest(salary=99000, isActive=False))
#     Print the result.

# 40. Write a model `BatchCreateRequest`:
#     class BatchCreateRequest(BaseModel):
#         items: list[CreateUserRequest]
#         created_by: str
#
#     Create it with 3 new users and created_by="admin".
#     Print len(request.items) and request.created_by.

# 41. Use model_dump(mode="json") to get JSON-safe types (e.g. datetimes become strings).
#     Add a field `created_at: str = "2024-01-01"` to UserModel.
#     Print user.model_dump() and user.model_dump(mode="json").
#     In this case they'll be the same — the point is knowing the option exists.

# 42. Write a model `Config` as a singleton-style settings model:
#     class AppConfig(BaseModel):
#         model_config = {"frozen": True}   # immutable after creation
#         host: str = "localhost"
#         port: int = 8000
#         debug: bool = False
#         db_url: str = "sqlite:///./app.db"
#
#     config = AppConfig()
#     Print config.host and config.port.
#     Try config.host = "remotehost" in a try/except — should raise.
#     Note: frozen=True makes the model immutable — useful for settings.

# 43. Write a function `validate_and_create(data: dict, model: type) -> BaseModel | None`
#     that tries to create a model instance from data, returns None on ValidationError.
#     Test with valid and invalid data for UserModel and ProductModel.

# 44. Write a model `SearchQuery`:
#     class SearchQuery(BaseModel):
#         q: str = Field(min_length=1)
#         page: int = Field(default=1, ge=1)
#         size: int = Field(default=10, ge=1, le=100)
#         role: str | None = None
#         min_salary: int | None = Field(default=None, ge=0)
#         max_salary: int | None = Field(default=None, ge=0)
#
#         @model_validator(mode="after")
#         def check_salary_range(self):
#             if self.min_salary and self.max_salary:
#                 if self.min_salary > self.max_salary:
#                     raise ValueError("min_salary cannot exceed max_salary")
#             return self
#
#     Test with valid query and with min_salary=100000, max_salary=50000 — catch error.

# 45. Build the complete schema set for a mini user API — all in one place:
#
#     CreateUserRequest  — input for POST /users (no id)
#     UpdateUserRequest  — input for PATCH /users/{id} (all optional)
#     UserResponse       — output for GET /users (no salary)
#     UserListResponse   — output for GET /users (paginated)
#     ErrorResponse      — output for errors
#
#     Write an async function `simulate_api()` that runs:
#       POST /users   → create Yuan → print UserResponse
#       GET /users    → return all users → print UserListResponse
#       PATCH /users/1 → update Alice's salary → print updated UserResponse
#       GET /users/99  → not found → print ErrorResponse
#
#     Use asyncio.run(simulate_api()).
#     This is the full Pydantic layer of a real FastAPI app. After this, you
#     just add @app.get() and a real DB — the structure is identical.
