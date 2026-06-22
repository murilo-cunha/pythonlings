# I AM NOT DONE

from itertools import islice


def naturals(start=1):
    # Fix: make an infinite generator yielding start, start+1, start+2, ...
    return  # Fix: use yield in a while loop


# DON'T EDIT THE TESTS
import types
gen = naturals()
assert isinstance(gen, types.GeneratorType)

# Take the first 5 natural numbers
first_five = list(islice(naturals(), 5))
assert first_five == [1, 2, 3, 4, 5]

# Start from 10
from_ten = list(islice(naturals(10), 4))
assert from_ten == [10, 11, 12, 13]
