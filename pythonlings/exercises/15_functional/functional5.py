# I AM NOT DONE

import itertools

# Fix each expression using itertools:

# Chain two lists into one iterator (convert to list for the assertion)
combined = list([1, 2, 3]) + list([4, 5, 6])  # Fix: use itertools.chain

# Group consecutive equal elements
data = [1, 1, 2, 2, 2, 3, 1, 1]
grouped = [(k, list(v)) for k, v in []]  # Fix: use itertools.groupby

# Take the first 5 elements of an infinite count starting at 1
first_five = []  # Fix: use itertools.islice(itertools.count(1), 5)

# DON'T EDIT THE TESTS
assert combined == [1, 2, 3, 4, 5, 6]
assert grouped == [(1, [1, 1]), (2, [2, 2, 2]), (3, [3]), (1, [1, 1])]
assert first_five == [1, 2, 3, 4, 5]
