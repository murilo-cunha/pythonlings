# I AM NOT DONE


def double(value):
    # Fix the annotation: value can be int OR float, return type is int | float
    # Use the Python 3.10+ pipe syntax: int | float
    return value * 2


def parse_id(raw):
    # raw is str, returns int | None (None if parsing fails)
    try:
        return int(raw)
    except ValueError:
        return None


# DON'T EDIT THE TESTS
hints = double.__annotations__
assert str(hints.get("value")) in ("int | float", "float | int")
assert str(hints.get("return")) in ("int | float", "float | int")

assert parse_id("42") == 42
assert parse_id("abc") is None
