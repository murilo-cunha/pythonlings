# I AM NOT DONE

from pydantic import BaseModel, field_validator


class UserForm(BaseModel):
    username: str
    email: str

    @field_validator("username")
    @classmethod
    def username_must_be_lowercase(cls, v):
        # Fix: raise ValueError if v contains uppercase letters
        # Otherwise return v
        return v

    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, v):
        # Fix: raise ValueError("invalid email") if "@" not in v
        return v


# DON'T EDIT THE TESTS
from pydantic import ValidationError

uf = UserForm(username="alice", email="alice@example.com")
assert uf.username == "alice"

try:
    UserForm(username="Alice", email="alice@example.com")
    assert False, "Expected ValidationError"
except ValidationError as e:
    assert "uppercase" in str(e).lower() or "value error" in str(e).lower()

try:
    UserForm(username="bob", email="notanemail")
    assert False, "Expected ValidationError"
except ValidationError:
    pass
