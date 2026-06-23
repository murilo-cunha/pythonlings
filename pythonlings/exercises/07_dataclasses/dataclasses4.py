# I AM NOT DONE

from dataclasses import dataclass


@dataclass
class BoundedInt:
    value: int
    minimum: int = 0
    maximum: int = 100

    def __post_init__(self):
        # Fix: clamp self.value to be between minimum and maximum
        pass


# DON'T EDIT THE TESTS
b = BoundedInt(50)
assert b.value == 50

b_low = BoundedInt(-10)
assert b_low.value == 0  # Clamped to minimum

b_high = BoundedInt(200)
assert b_high.value == 100  # Clamped to maximum

b_custom = BoundedInt(5, minimum=10, maximum=20)
assert b_custom.value == 10  # Clamped to minimum=10
