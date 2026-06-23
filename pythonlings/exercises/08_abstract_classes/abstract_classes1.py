"""
ABC (Abstract Base Class) forces subclasses to implement specific methods.
Decorate abstract methods with @abstractmethod — instantiating a subclass
that skips any abstract method raises TypeError.

Implement Rectangle.area() (width * height) and Rectangle.perimeter() (2*(w+h)).
"""

# I AM NOT DONE

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

    @abstractmethod
    def perimeter(self) -> float: ...


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0
