"""
@dataclass auto-generates __init__, __repr__, and __eq__ from class-level
annotations. Fields with defaults must come after fields without defaults.
from dataclasses import dataclass; @dataclass; class Foo: x: int; y: str = "hi"

Add name: str, price: float, and in_stock: bool = True fields to Product.
"""

# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class Product:
    pass
