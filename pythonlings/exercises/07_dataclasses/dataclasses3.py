# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class Coordinate:
    # Fix: make this dataclass frozen (immutable)
    lat: float
    lon: float


# DON'T EDIT THE TESTS
c = Coordinate(51.5, -0.1)
assert c.lat == 51.5

raised = False
try:
    c.lat = 99.0  # Should raise FrozenInstanceError
except Exception:
    raised = True  # Any exception counts — frozen dataclasses raise FrozenInstanceError

assert raised, "Assignment should have raised an exception (make the dataclass frozen)"
