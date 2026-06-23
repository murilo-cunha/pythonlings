"""
IntEnum members are both Enum members AND integers — comparisons and arithmetic work.
auto() assigns incrementing integer values starting at 1.
Use IntEnum when you need integer-compatible members (e.g. for database storage).

Add LOW, MEDIUM, HIGH, CRITICAL members to Priority using auto().
"""

# I AM NOT DONE

from enum import IntEnum, auto


class Priority(IntEnum):
    pass
