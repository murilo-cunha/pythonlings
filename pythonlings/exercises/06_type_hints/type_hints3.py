"""
TypeVar creates a placeholder type variable for generic functions.
T = TypeVar("T"); def first(items: list[T]) -> T: ...
Type-checkers infer: if you pass list[str], you get back str.

Annotate first() using list[T] for items and T for the return type.
"""

# I AM NOT DONE

from typing import TypeVar

T = TypeVar("T")


def first(items):
    return items[0]
