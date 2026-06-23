"""
A decorator is a function that takes a function and returns a new function.
The wrapper calls the original and can transform its return value.
Pattern: def decorator(func): def wrapper(*args, **kwargs): ...; return wrapper

Fix shout so the wrapper uppercases the return value of func.
"""

# I AM NOT DONE


def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@shout
def greet(name):
    return f"hello, {name}"
