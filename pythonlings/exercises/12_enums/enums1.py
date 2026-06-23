"""
Enum creates a set of named constants. Members are singletons compared with `is`.
Access by name: Direction["NORTH"], by value: Direction(1), or: Direction.NORTH.
Enums prevent magic numbers and make code self-documenting.

Add NORTH=1, SOUTH=2, EAST=3, WEST=4 members to Direction.
"""

# I AM NOT DONE

from enum import Enum


class Direction(Enum):
    pass
