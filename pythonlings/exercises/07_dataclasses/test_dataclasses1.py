from dataclasses1 import Product


def test_default_in_stock():
    p = Product(name="Widget", price=9.99)
    assert p.in_stock is True

def test_explicit_fields():
    p = Product("Gadget", 24.99, False)
    assert p.name == "Gadget"
    assert p.price == 24.99
    assert p.in_stock is False

def test_repr():
    p = Product(name="Widget", price=9.99, in_stock=True)
    assert repr(p) == "Product(name='Widget', price=9.99, in_stock=True)"

def test_equality():
    assert Product("Widget", 9.99, True) == Product("Widget", 9.99, True)
