# I AM NOT DONE

from typing import NamedTuple


class Point(NamedTuple):
    # Fix: add fields x: float and y: float
    pass


# DON'T EDIT THE TESTS
p = Point(1.0, 2.0)
assert p.x == 1.0
assert p.y == 2.0
assert p[0] == 1.0  # NamedTuple supports index access
assert isinstance(p, tuple)

# Immutable — assignment should raise
try:
    p.x = 9.0
    assert False, "Expected AttributeError"
except AttributeError:
    pass
