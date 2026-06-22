# I AM NOT DONE

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    country: str = "US"


class Customer(BaseModel):
    name: str
    # Fix: change the type of `address` from `dict` to `Address`
    address: dict  # Fix: should be Address, not dict


# DON'T EDIT THE TESTS
c = Customer(
    name="Ada",
    address={"street": "123 Main St", "city": "Springfield"}
)
assert c.name == "Ada"

# Nested model gives attribute access and default values
assert isinstance(c.address, Address)
assert c.address.city == "Springfield"
assert c.address.country == "US"  # default only works with Address type
