# I AM NOT DONE

from contextlib import contextmanager


@contextmanager
def managed_list():
    # Fix: yield an empty list, then sort it in place after the with block
    items = []
    yield items
    # Fix: sort items here (after yield)


# DON'T EDIT THE TESTS
with managed_list() as lst:
    lst.append(3)
    lst.append(1)
    lst.append(2)

assert lst == [1, 2, 3]  # sorted after the with block
