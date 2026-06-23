import math
import pytest
from decorators4 import Circle


def test_initial_radius():
    c = Circle(5)
    assert c.radius == 5

def test_area():
    c = Circle(5)
    assert abs(c.area - math.pi * 25) < 1e-9

def test_set_radius():
    c = Circle(5)
    c.radius = 10
    assert c.radius == 10

def test_negative_radius_raises():
    c = Circle(5)
    with pytest.raises(ValueError):
        c.radius = -1
