"""
Field() adds constraints to model fields beyond simple type checks.
Common constraints: min_length for strings; gt (greater than), ge (greater than
or equal) for numbers; default for optional fields.

Add fields to Product:
  name: str with min_length=1
  price: float greater than 0
  quantity: int >= 0 that defaults to 0
"""

# I AM NOT DONE

from pydantic import BaseModel, Field


class Product(BaseModel):
    pass
