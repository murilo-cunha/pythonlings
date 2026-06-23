import pytest
from error_handling4 import validate_all


def test_both_missing():
    with pytest.raises(ExceptionGroup) as exc:
        validate_all({})
    assert exc.value.message == "validation errors"
    assert len(exc.value.exceptions) == 2

def test_one_missing():
    with pytest.raises(ExceptionGroup) as exc:
        validate_all({"name": "Ada"})
    assert len(exc.value.exceptions) == 1

def test_all_present():
    validate_all({"name": "Ada", "age": 30})
