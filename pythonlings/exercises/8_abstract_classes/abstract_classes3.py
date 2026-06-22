# I AM NOT DONE

from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> str:
        ...


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"Circle(r={self.radius})"  # This is correct — study it


class Square:
    def __init__(self, side: float):
        self.side = side

    def draw(self) -> str:
        return ""  # Fix: return f"Square(s={self.side})"


def render(shape: Drawable) -> str:
    return shape.draw()


# DON'T EDIT THE TESTS
c = Circle(5.0)
s = Square(3.0)

assert render(c) == "Circle(r=5.0)"
assert render(s) == "Square(s=3.0)"

# Protocol without @runtime_checkable raises TypeError for issubclass
try:
    issubclass(Circle, Drawable)
    assert False, "Expected TypeError"
except TypeError:
    pass  # Correct — Protocol needs @runtime_checkable for isinstance/issubclass
