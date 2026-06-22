# I AM NOT DONE


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        # Fix: raise ValueError if value is negative
        self._radius = value

    @property
    def area(self):
        # Fix: return pi * r^2 (use math.pi)
        return 0.0


import math


# DON'T EDIT THE TESTS
c = Circle(5)
assert c.radius == 5
assert abs(c.area - math.pi * 25) < 1e-9

c.radius = 10
assert c.radius == 10

try:
    c.radius = -1
    assert False, "Expected ValueError"
except ValueError:
    pass
