import pytest
from error_handling3 import fetch_user, DatabaseError


def test_raises_database_error():
    with pytest.raises(DatabaseError) as exc:
        fetch_user(42)
    assert str(exc.value) == "User not found"

def test_cause_is_key_error():
    with pytest.raises(DatabaseError) as exc:
        fetch_user(42)
    assert exc.value.__cause__ is not None
    assert isinstance(exc.value.__cause__, KeyError)
