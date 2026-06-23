"""
Nested Pydantic models use another BaseModel as a field type.
Pydantic accepts a plain dict where a nested model is expected and coerces it
automatically, giving you attribute access and field defaults on the nested model.

Change the type of address from dict to Address.
"""

# I AM NOT DONE

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    country: str = "US"


class Customer(BaseModel):
    name: str
    address: dict
