"""
Default argument values let callers omit parameters they don't need to override.
Syntax: def func(param, optional="default"). When the caller doesn't supply the
optional argument, Python uses the default value.

Fix greet() so it uses the greeting parameter instead of the hard-coded "Hello".
"""

# I AM NOT DONE


def greet(name, greeting="Hello"):
    return f"Hello, {name}!"
