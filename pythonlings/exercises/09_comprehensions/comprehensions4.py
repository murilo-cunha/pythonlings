"""
Generator expressions look like list comprehensions but use () instead of [].
They don't build the whole sequence in memory — they yield values lazily on demand.
Use them when you only need to iterate once or when the sequence could be large.

Change the [] brackets to () to make cubes_gen a generator expression.
"""

# I AM NOT DONE

import types

numbers = range(1, 11)
cubes_gen = [n ** 3 for n in numbers]
