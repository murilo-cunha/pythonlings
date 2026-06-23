"""
itertools is a stdlib toolbox for efficient lazy iteration.
chain(*iterables) concatenates iterables. groupby(it) groups consecutive equal elements.
islice(it, n) takes the first n items from any iterator, including infinite ones.

Set combined = list(itertools.chain([1, 2, 3], [4, 5, 6])) -> [1, 2, 3, 4, 5, 6]; grouped = [(k, list(v)) for k, v in itertools.groupby(data)] -> [(1, [1, 1]), (2, [2, 2, 2]), (3, [3]), (1, [1, 1])]; and first_five = list(itertools.islice(itertools.count(1), 5)) -> [1, 2, 3, 4, 5].
"""

# I AM NOT DONE

import itertools

combined = list([1, 2, 3]) + list([4, 5, 6])

data = [1, 1, 2, 2, 2, 3, 1, 1]
grouped = [(k, list(v)) for k, v in []]

first_five = []
