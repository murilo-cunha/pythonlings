"""
@dataclass(frozen=True) makes instances immutable — any attribute assignment
raises FrozenInstanceError. Frozen dataclasses are also hashable by default,
making them usable as dict keys or set members.

Add frozen=True to the @dataclass decorator on Coordinate.
"""

# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class Coordinate:
    lat: float
    lon: float
