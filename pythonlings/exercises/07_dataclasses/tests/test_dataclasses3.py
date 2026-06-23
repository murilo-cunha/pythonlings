import pytest
from dataclasses3 import Coordinate


def test_fields():
    c = Coordinate(51.5, -0.1)
    assert c.lat == 51.5
    assert c.lon == -0.1

def test_frozen_raises():
    c = Coordinate(51.5, -0.1)
    with pytest.raises(Exception):
        c.lat = 99.0

def test_hashable():
    c = Coordinate(51.5, -0.1)
    assert hash(c) is not None
