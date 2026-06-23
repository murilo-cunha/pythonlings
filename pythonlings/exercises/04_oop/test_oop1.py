from oop1 import Point


def test_repr():
    p = Point(1, 2)
    assert repr(p) == "Point(1, 2)"

def test_str():
    p = Point(1, 2)
    assert str(p) == "(1, 2)"

def test_fstring():
    p = Point(3, 4)
    assert f"{p}" == "(3, 4)"
