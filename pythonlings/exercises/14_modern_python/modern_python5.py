# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Circle:
    center: Point
    radius: float


@dataclass
class Rectangle:
    top_left: Point
    bottom_right: Point


def describe(shape):
    # Fix: implement using match/case with dataclass patterns
    return "unknown shape"


# DON'T EDIT THE TESTS
p = Point(0.0, 0.0)
c = Circle(center=Point(1.0, 2.0), radius=5.0)
r = Rectangle(top_left=Point(0.0, 4.0), bottom_right=Point(3.0, 0.0))

assert describe(p) == "point at (0.0, 0.0)"
assert describe(c) == "circle at (1.0, 2.0) r=5.0"
assert describe(r) == "rect from (0.0, 4.0) to (3.0, 0.0)"
assert describe("other") == "unknown shape"
