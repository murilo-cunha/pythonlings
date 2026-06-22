# I AM NOT DONE

from pydantic import BaseModel


class User(BaseModel):
    # Fix: add three fields
    #   name: str
    #   age: int
    #   email: str
    pass


# DON'T EDIT THE TESTS
u = User(name="Alice", age=30, email="alice@example.com")
assert u.name == "Alice"
assert u.age == 30
assert u.email == "alice@example.com"

# Pydantic coerces compatible types
u2 = User(name="Bob", age="25", email="bob@example.com")
assert u2.age == 25  # "25" coerced to int

# Pydantic raises ValidationError for bad input
from pydantic import ValidationError
try:
    User(name="Eve", age="not_a_number", email="eve@example.com")
    assert False, "Expected ValidationError"
except ValidationError:
    pass
