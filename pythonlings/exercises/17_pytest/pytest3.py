"""
@pytest.mark.parametrize("names", [...]) runs the same test function with multiple inputs.
Each tuple becomes one test case with its own pass/fail result.

Fix celsius_to_fahrenheit and the expected values in the parametrize decorator.
"""

# I AM NOT DONE

import pytest


def celsius_to_fahrenheit(c):
    return c * 9 / 5


@pytest.mark.parametrize("celsius,expected", [
    (0, 31),
    (100, 211),
    (-40, -40),
])
def test_conversion(celsius, expected):
    assert celsius_to_fahrenheit(celsius) == expected
