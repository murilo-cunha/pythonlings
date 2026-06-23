"""
Class patterns match dataclass instances by field name:
    case Circle(center=Point(x=cx, y=cy), radius=r):
Fields are matched structurally; unmatched fields are ignored.
Matched field values are bound as local variables in the case body.

Implement describe(shape) using match/case with dataclass patterns: a Point(x, y) -> f"point at ({x}, {y})"; a Circle with center Point(cx, cy) and radius r -> f"circle at ({cx}, {cy}) r={r}"; a Rectangle with top_left Point(x1, y1) and bottom_right Point(x2, y2) -> f"rect from ({x1}, {y1}) to ({x2}, {y2})"; and "unknown shape" otherwise (case _).
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
