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
    # Fix: use pytest.raises to assert that divide(1, 0) raises ZeroDivisionError
    divide(1, 0)  # Fix: wrap with pytest.raises(ZeroDivisionError)


def test_parse_positive_valid():
    assert parse_positive("42") == 42


def test_parse_positive_invalid():
    # Fix: use pytest.raises to check the ValueError message contains "not positive"
    with pytest.raises(ValueError):  # Fix: also check match="not positive"
        parse_positive("-5")


# DON'T EDIT BELOW
import sys
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
