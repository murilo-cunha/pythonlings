"""
A Protocol defines an interface structurally — any class with the right methods
automatically satisfies it without explicit inheritance. This is "duck typing"
formalised: if it has a .draw() method, it's Drawable.

Implement Square.draw() to return f"Square(s={self.side})".
"""

# I AM NOT DONE

from typing import Protocol


class Drawable(Protocol):
    def draw(self) -> str: ...


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def draw(self) -> str:
        return f"Circle(r={self.radius})"


class Square:
    def __init__(self, side: float):
        self.side = side

    def draw(self) -> str:
        return ""


def render(shape: Drawable) -> str:
    return shape.draw()
