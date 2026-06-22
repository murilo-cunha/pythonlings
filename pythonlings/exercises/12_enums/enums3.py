# I AM NOT DONE

from enum import Enum


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    def to_hex(self) -> str:
        # Fix: return the color as a hex string like "#ff0000"
        r, g, b = self.value
        return ""  # Fix: use f"#{r:02x}{g:02x}{b:02x}"

    @classmethod
    def from_hex(cls, hex_str: str):
        # Fix: look up a Color member by hex string
        # hex_str is like "#ff0000"
        for member in cls:
            if member.to_hex() == hex_str:
                return member
        raise ValueError(f"No color for {hex_str}")


# DON'T EDIT THE TESTS
assert Color.RED.to_hex() == "#ff0000"
assert Color.GREEN.to_hex() == "#00ff00"
assert Color.BLUE.to_hex() == "#0000ff"

assert Color.from_hex("#ff0000") is Color.RED
assert Color.from_hex("#0000ff") is Color.BLUE
