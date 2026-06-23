import pytest
from error_handling2 import ValidationError, validate_age


def test_valid_age():
    assert validate_age(25) == 25

def test_negative_age():
    with pytest.raises(ValidationError) as exc:
        validate_age(-1)
    assert exc.value.field == "age"
    assert exc.value.message == "must be between 0 and 150"

def test_inherits_value_error():
    with pytest.raises(ValueError):
        validate_age(200)
