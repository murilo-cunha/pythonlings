from pydantic4 import Customer, Address


def test_nested_model_type():
    c = Customer(name="Ada", address={"street": "123 Main St", "city": "Springfield"})
    assert isinstance(c.address, Address)

def test_nested_attribute_access():
    c = Customer(name="Ada", address={"street": "123 Main St", "city": "Springfield"})
    assert c.address.city == "Springfield"

def test_nested_default():
    c = Customer(name="Ada", address={"street": "123 Main St", "city": "Springfield"})
    assert c.address.country == "US"
