# I AM NOT DONE

from enum import Enum


class Direction(Enum):
    # Fix: add four members NORTH, SOUTH, EAST, WEST with values 1, 2, 3, 4
    pass


# DON'T EDIT THE TESTS
assert Direction.NORTH.value == 1
assert Direction.SOUTH.value == 2
assert Direction.EAST.value == 3
assert Direction.WEST.value == 4

# Enums support comparison by identity, not value
assert Direction.NORTH == Direction.NORTH
assert Direction.NORTH != Direction.SOUTH

# Access by name and by value
assert Direction["NORTH"] is Direction.NORTH
assert Direction(2) is Direction.SOUTH
