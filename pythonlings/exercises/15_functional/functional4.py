# I AM NOT DONE

from functools import partial


def power(base, exponent):
    return base ** exponent


# Fix: use partial to create specialised versions
square = power  # Fix: use partial to fix exponent=2
cube = power    # Fix: use partial to fix exponent=3


# Fix: create a partial that always formats a number with 2 decimal places
def format_number(value, decimals=0):
    return f"{value:.{decimals}f}"


format_2dp = format_number  # Fix: use partial to fix decimals=2


# DON'T EDIT THE TESTS
assert square(4) == 16
assert square(5) == 25
assert cube(3) == 27
assert format_2dp(3.14159) == "3.14"
assert format_2dp(1.0) == "1.00"
