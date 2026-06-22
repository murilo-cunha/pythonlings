# I AM NOT DONE


def chain(*iterables):
    # Fix: yield all items from each iterable using "yield from"
    for it in iterables:
        pass  # Fix: use yield from


# DON'T EDIT THE TESTS
result = list(chain([1, 2], [3, 4], [5]))
assert result == [1, 2, 3, 4, 5]
assert list(chain("ab", "cd")) == ["a", "b", "c", "d"]
