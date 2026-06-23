"""
itertools is a stdlib toolbox for efficient lazy iteration.
chain(*iterables) concatenates iterables. groupby(it) groups consecutive equal elements.
islice(it, n) takes the first n items from any iterator, including infinite ones.

Fix combined, grouped, and first_five using itertools functions.
"""

# I AM NOT DONE

import itertools

combined = list([1, 2, 3]) + list([4, 5, 6])

data = [1, 1, 2, 2, 2, 3, 1, 1]
grouped = [(k, list(v)) for k, v in []]

first_five = []
