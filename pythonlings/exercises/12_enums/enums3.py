"""
Enum members can store tuple values and you can add methods to an Enum class.
Methods can use self.value to access the stored value.
This lets you attach behavior (conversion, formatting) directly to enum members.

Implement to_hex() to return f"#{r:02x}{g:02x}{b:02x}" (e.g. Color.RED.to_hex() == "#ff0000"). from_hex() is already written for you and relies on to_hex().
"""

# I AM NOT DONE

from enum import Enum


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def to_hex(self) -> str:
        r, g, b = self.value
        return ""

    @classmethod
    def from_hex(cls, hex_str: str):
        for member in cls:
            if member.to_hex() == hex_str:
                return member
        raise ValueError(f"No color for {hex_str}")
