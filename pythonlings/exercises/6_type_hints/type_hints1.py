# I AM NOT DONE


def add(a, b):
    # Add type annotations: both params are int, return type is int
    return a + b


def greet(name):
    # Add type annotations: name is str, return type is str
    return f"Hello, {name}"


# DON'T EDIT THE TESTS
import inspect

hints_add = add.__annotations__
assert hints_add.get("a") is int
assert hints_add.get("b") is int
assert hints_add.get("return") is int

hints_greet = greet.__annotations__
assert hints_greet.get("name") is str
assert hints_greet.get("return") is str
