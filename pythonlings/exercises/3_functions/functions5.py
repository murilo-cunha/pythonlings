# I AM NOT DONE

import math


def hypotenuse(a, b, /):
    # Return the hypotenuse of a right triangle with legs a and b
    # All params are positional-only (note the / in the signature)
    return 0.0  # Fix this


# DON'T EDIT THE TESTS
assert hypotenuse(3, 4) == 5.0
assert hypotenuse(5, 12) == 13.0

# Positional-only means keyword call should raise TypeError
try:
    hypotenuse(a=3, b=4)
    assert False, "Expected TypeError"
except TypeError:
    pass
