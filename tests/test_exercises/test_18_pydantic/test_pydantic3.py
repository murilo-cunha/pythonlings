import pytest
from pydantic import ValidationError
from pydantic3 import UserForm


def test_valid_form():
    uf = UserForm(username="alice", email="alice@example.com")
    assert uf.username == "alice"

def test_uppercase_username_rejected():
    with pytest.raises(ValidationError):
        UserForm(username="Alice", email="alice@example.com")

def test_invalid_email_rejected():
    with pytest.raises(ValidationError):
        UserForm(username="bob", email="notanemail")
