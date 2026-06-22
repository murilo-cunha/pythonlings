# I AM NOT DONE


def add(a, b):
    return a + b


def is_palindrome(s):
    return s == s  # Fix: should check s == s[::-1]


# Fix the failing test — the function is buggy, not the test
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("level") is True


# DON'T EDIT BELOW
import sys
import pytest
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
