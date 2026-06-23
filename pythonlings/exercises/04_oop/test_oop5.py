import pytest
from oop5 import Vector


def test_x():
    v = Vector(3, 4)
    assert v.x == 3

def test_y():
    v = Vector(3, 4)
    assert v.y == 4

def test_slots_prevents_new_attrs():
    v = Vector(1, 2)
    with pytest.raises(AttributeError):
        v.z = 5
