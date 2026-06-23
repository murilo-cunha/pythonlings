"""
Class patterns match dataclass instances by field name:
    case Circle(center=Point(x=cx, y=cy), radius=r):
Fields are matched structurally; unmatched fields are ignored.
Matched field values are bound as local variables in the case body.

Implement describe() using match/case with dataclass patterns for Point, Circle, Rectangle.
"""

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
    return "unknown shape"
