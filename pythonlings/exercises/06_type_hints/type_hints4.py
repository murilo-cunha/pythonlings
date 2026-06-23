"""
TypedDict creates a dict subtype with specific required keys and value types.
from typing import TypedDict; class Movie(TypedDict): title: str; year: int
Great for typing JSON-like data without full dataclass overhead.

Add title: str, year: int, and rating: float fields to Movie.
"""

# I AM NOT DONE

from typing import TypedDict


class Movie(TypedDict):
    pass
