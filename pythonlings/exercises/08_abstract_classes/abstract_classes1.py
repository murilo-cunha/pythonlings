# I AM NOT DONE

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...

    @abstractmethod
    def perimeter(self) -> float:
        ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return 0.0  # Fix this

    def perimeter(self) -> float:
        return 0.0  # Fix this


# DON'T EDIT THE TESTS
r = Rectangle(4, 5)
assert r.area() == 20.0
assert r.perimeter() == 18.0

# Abstract classes cannot be instantiated directly
try:
    Shape()
    assert False, "Expected TypeError"
except TypeError:
    pass
