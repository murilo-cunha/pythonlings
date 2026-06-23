"""
A decorator factory is a function that accepts arguments and returns a decorator.
Pattern: def repeat(n): def decorator(func): def wrapper(*a, **kw): ...
Usage: @repeat(3) — the outer call (repeat(3)) returns the actual decorator.

Implement repeat(n) so the wrapped function is called exactly n times,
returning the last result.
"""

# I AM NOT DONE


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            return result
        return wrapper
    return decorator


@repeat(3)
def say(msg):
    return msg
