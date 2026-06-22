# I AM NOT DONE


class DatabaseError(Exception):
    pass


def fetch_user(user_id):
    try:
        # Simulating a raw exception from a lower layer
        raise KeyError(f"user:{user_id}")
    except KeyError as e:
        # Fix: raise DatabaseError("User not found") from e
        # This chains the exceptions so the original cause is preserved
        raise DatabaseError("User not found")  # Fix: add "from e"


# DON'T EDIT THE TESTS
try:
    fetch_user(42)
except DatabaseError as e:
    assert str(e) == "User not found"
    assert e.__cause__ is not None          # Fails without "from e"
    assert isinstance(e.__cause__, KeyError)
