from enums1 import Direction


def test_values():
    assert Direction.NORTH.value == 1
    assert Direction.SOUTH.value == 2
    assert Direction.EAST.value == 3
    assert Direction.WEST.value == 4

def test_identity():
    assert Direction.NORTH == Direction.NORTH
    assert Direction.NORTH != Direction.SOUTH

def test_access_by_name():
    assert Direction["NORTH"] is Direction.NORTH

def test_access_by_value():
    assert Direction(2) is Direction.SOUTH
