import pytest
from pydantic import ValidationError
from pydantic2 import Product


def test_create_product():
    p = Product(name="Widget", price=9.99)
    assert p.name == "Widget"
    assert p.price == 9.99

def test_quantity_default():
    p = Product(name="Widget", price=9.99)
    assert p.quantity == 0

def test_empty_name_invalid():
    with pytest.raises(ValidationError):
        Product(name="", price=1.0)

def test_negative_price_invalid():
    with pytest.raises(ValidationError):
        Product(name="X", price=-1.0)
