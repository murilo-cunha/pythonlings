import pytest
from pydantic import ValidationError
from pydantic1 import User


def test_create_user():
    u = User(name="Alice", age=30, email="alice@example.com")
    assert u.name == "Alice"
    assert u.age == 30
    assert u.email == "alice@example.com"

def test_type_coercion():
    u = User(name="Bob", age="25", email="bob@example.com")
    assert u.age == 25

def test_validation_error():
    with pytest.raises(ValidationError):
        User(name="Eve", age="not_a_number", email="eve@example.com")
