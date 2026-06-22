# I AM NOT DONE

from pydantic import BaseModel, Field


class Product(BaseModel):
    # Fix: add fields with constraints using Field():
    #   name: str with min_length=1
    #   price: float with gt=0 (greater than 0)
    #   quantity: int with ge=0 (greater than or equal to 0), default=0
    pass


# DON'T EDIT THE TESTS
from pydantic import ValidationError

p = Product(name="Widget", price=9.99)
assert p.name == "Widget"
assert p.price == 9.99
assert p.quantity == 0  # default

# Validation: empty name
try:
    Product(name="", price=1.0)
    assert False, "Expected ValidationError"
except ValidationError:
    pass

# Validation: negative price
try:
    Product(name="X", price=-1.0)
    assert False, "Expected ValidationError"
except ValidationError:
    pass
