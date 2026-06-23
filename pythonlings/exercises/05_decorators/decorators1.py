# I AM NOT DONE


def shout(func):
    # Decorator: wraps func so its return value is uppercased
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)  # Fix: uppercase the result
    return wrapper


@shout
def greet(name):
    return f"hello, {name}"


# DON'T EDIT THE TESTS
assert greet("world") == "HELLO, WORLD"
assert greet("python") == "HELLO, PYTHON"
