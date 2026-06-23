"""
@property turns a method into a read-only attribute. Add a setter with
@name.setter to allow assignment, and add validation logic there.
Use properties to keep a clean attribute API while enforcing constraints.

Add ValueError on negative radius and compute area = pi * r^2.
"""

# I AM NOT DONE

import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def area(self):
        return 0.0
