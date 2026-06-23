"""
@field_validator("field_name") defines a custom validator for a specific field.
The method must be decorated with @classmethod; it receives the coerced value
and should return it unchanged or raise ValueError with a message.

Complete the two validators:
- username_must_be_lowercase: raise ValueError if the username has any uppercase letters
- email_must_contain_at: raise ValueError("invalid email") if "@" is not in the value
"""

# I AM NOT DONE

from pydantic import BaseModel, field_validator


class UserForm(BaseModel):
    username: str
    email: str

    @field_validator("username")
    @classmethod
    def username_must_be_lowercase(cls, v):
        return v

    @field_validator("email")
    @classmethod
    def email_must_contain_at(cls, v):
        return v
