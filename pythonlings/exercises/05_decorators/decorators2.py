"""
Without @functools.wraps(func) inside a decorator, the wrapper loses the
original function's __name__, __doc__, and other metadata.
Always use @functools.wraps when writing decorators to preserve introspection.

Add @functools.wraps(func) to the wrapper inside log_call.
"""

# I AM NOT DONE

import functools


def log_call(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@log_call
def add(a, b):
    """Add two numbers."""
    return a + b
