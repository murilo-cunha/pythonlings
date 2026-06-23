# I AM NOT DONE

from typing import TypeVar

T = TypeVar("T")


def first(items):
    # Add a type annotation using T: items is list[T], return type is T
    return items[0]


# DON'T EDIT THE TESTS
import inspect

hints = first.__annotations__
# The return annotation should be T
assert hints.get("return") is T

# Behaviour check
assert first([1, 2, 3]) == 1
assert first(["a", "b"]) == "a"
