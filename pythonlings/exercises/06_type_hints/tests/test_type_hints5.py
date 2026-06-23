import pytest
from type_hints5 import Point


def test_named_access():
    p = Point(1.0, 2.0)
    assert p.x == 1.0
    assert p.y == 2.0

def test_index_access():
    p = Point(1.0, 2.0)
    assert p[0] == 1.0

def test_is_tuple():
    p = Point(1.0, 2.0)
    assert isinstance(p, tuple)

def test_immutable():
    p = Point(1.0, 2.0)
    with pytest.raises(AttributeError):
        p.x = 9.0
