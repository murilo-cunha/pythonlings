"""
pytest.raises(ExceptionType) asserts that a block of code raises a specific exception.
Use it as a context manager: with pytest.raises(ValueError): ...
Add match="pattern" to also check that the exception message matches a regex.

Fix test_zero_division and test_parse_invalid to use pytest.raises correctly.
"""

# I AM NOT DONE

import pytest


def divide(a, b):
    return a / b


def parse_positive(s):
    n = int(s)
    if n <= 0:
        raise ValueError(f"{s!r} is not positive")
    return n


def test_zero_division():
    divide(1, 0)


def test_parse_positive_valid():
    assert parse_positive("42") == 42


def test_parse_invalid():
    with pytest.raises(ValueError):
        parse_positive("-5")
