"""
Pydantic BaseModel validates data using Python type annotations.
Fields are declared as class attributes with type hints.
Pydantic coerces compatible types (e.g. "25" → int) and raises
ValidationError for invalid data.

Define a User model with three fields: name (str), age (int), email (str).
"""

# I AM NOT DONE

from pydantic import BaseModel


class User(BaseModel):
    pass
