"""
pytest collects functions whose names start with test_ and runs them automatically.
Use plain assert statements — pytest rewrites them to show actual vs expected values on failure.

The is_palindrome function has a bug. Fix it, then make all three test functions pass.
"""

# I AM NOT DONE


def add(a, b):
    return a + b


def is_palindrome(s):
    return s == s


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_is_palindrome_true():
    assert is_palindrome("racecar") is True
    assert is_palindrome("level") is True


def test_is_palindrome_false():
    assert is_palindrome("hello") is False
