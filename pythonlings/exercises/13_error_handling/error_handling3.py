"""
raise NewError() from original_error links two exceptions together.
The original becomes e.__cause__ and appears in the traceback chain.
Use "from e" when translating low-level exceptions to higher-level ones.

Fix fetch_user() to raise DatabaseError from the caught KeyError.
"""

# I AM NOT DONE


class DatabaseError(Exception):
    pass


def fetch_user(user_id):
    try:
        raise KeyError(f"user:{user_id}")
    except KeyError as e:
        raise DatabaseError("User not found")
