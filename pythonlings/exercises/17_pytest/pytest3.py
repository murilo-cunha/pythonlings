# I AM NOT DONE

import pytest


def celsius_to_fahrenheit(c):
    return c * 9 / 5  # Fix: missing + 32


# Fix the parametrize decorator — it currently has wrong expected values
@pytest.mark.parametrize("celsius,expected", [
    (0, 31),    # Fix: 0°C should be 32°F
    (100, 211), # Fix: 100°C should be 212°F
    (-40, -40), # This one is actually correct
])
def test_conversion(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == expected


# DON'T EDIT BELOW
import sys
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
