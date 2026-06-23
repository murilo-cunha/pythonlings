"""
Python 3.10+ allows X | Y union syntax instead of Union[X, Y].
Use int | float for a value that can be either, int | None instead of Optional[int].
This syntax also works in isinstance(): isinstance(x, int | float).

Annotate double() with int | float for both param and return, and parse_id()
with str param and int | None return.
"""

# I AM NOT DONE


def double(value):
    return value * 2


def parse_id(raw):
    try:
        return int(raw)
    except ValueError:
        return None
