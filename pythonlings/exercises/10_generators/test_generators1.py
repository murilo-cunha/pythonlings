import types
from generators1 import countdown


def test_is_generator():
    assert isinstance(countdown(5), types.GeneratorType)

def test_countdown_five():
    assert list(countdown(5)) == [5, 4, 3, 2, 1]

def test_countdown_three():
    assert list(countdown(3)) == [3, 2, 1]

def test_countdown_one():
    assert list(countdown(1)) == [1]

def test_countdown_zero():
    assert list(countdown(0)) == []
