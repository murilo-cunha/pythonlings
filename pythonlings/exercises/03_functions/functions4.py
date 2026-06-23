# I AM NOT DONE

# Fix each lambda to do what the comment says:

# Compute the square of a number
square = lambda x: x  # Fix this

# Return True if the number is even
is_even = lambda x: True  # Fix this

# Sort key: sort by the second element of a tuple
second = lambda t: t  # Fix this


# DON'T EDIT THE TESTS
assert square(4) == 16
assert square(7) == 49
assert is_even(4) is True
assert is_even(7) is False
pairs = [(3, 1), (1, 3), (2, 2)]
assert sorted(pairs, key=second) == [(3, 1), (2, 2), (1, 3)]
