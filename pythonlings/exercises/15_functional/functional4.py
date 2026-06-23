"""
partial(func, *args, **kwargs) returns a new callable with some args pre-filled.
square = partial(power, exponent=2) — then square(4) calls power(4, exponent=2).
Useful for adapting functions to callbacks or APIs that expect a simpler signature.

Use partial() to create square, cube, and format_2dp.
"""

# I AM NOT DONE

from functools import partial


def power(base, exponent):
    return base ** exponent


square = power
cube = power


def format_number(value, decimals=0):
    return f"{value:.{decimals}f}"


format_2dp = format_number
