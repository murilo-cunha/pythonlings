# I AM NOT DONE

import functools


def log_call(func):
    # Fix: use @functools.wraps(func) so the wrapper preserves func's metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@log_call
def add(a, b):
    """Add two numbers."""
    return a + b


# DON'T EDIT THE TESTS
assert add(2, 3) == 5
assert add.__name__ == "add"          # Fails without @functools.wraps
assert add.__doc__ == "Add two numbers."
