# I AM NOT DONE


def countdown(n):
    # Fix: make this a generator that yields n, n-1, ..., 1
    return []  # Change to yield statements


# DON'T EDIT THE TESTS
import types

gen = countdown(5)
assert isinstance(gen, types.GeneratorType)
assert list(gen) == [5, 4, 3, 2, 1]
assert list(countdown(3)) == [3, 2, 1]
