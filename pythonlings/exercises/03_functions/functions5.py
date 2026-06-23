"""
Parameters before / in a function signature are positional-only — they cannot
be passed by keyword. Calling func(a=1) raises TypeError when a is positional-only.
This is useful for built-in-like APIs where keyword names are implementation details.

Implement hypotenuse(a, b, /) to return sqrt(a^2 + b^2).
"""

# I AM NOT DONE

import math


def hypotenuse(a, b, /):
    return 0.0
