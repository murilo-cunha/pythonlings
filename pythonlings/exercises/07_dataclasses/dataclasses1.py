# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class Product:
    # Fix: add three fields
    #   name: str
    #   price: float
    #   in_stock: bool = True
    pass


# DON'T EDIT THE TESTS
p = Product(name="Widget", price=9.99)
assert p.name == "Widget"
assert p.price == 9.99
assert p.in_stock is True  # default

p2 = Product("Gadget", 24.99, False)
assert p2.in_stock is False

# @dataclass generates __repr__ and __eq__ automatically
assert repr(p) == "Product(name='Widget', price=9.99, in_stock=True)"
assert p == Product("Widget", 9.99, True)
