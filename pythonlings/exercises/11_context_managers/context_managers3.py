"""
@contextmanager turns a generator function into a context manager.
Write setup code, then yield the value (the body of the with block runs here),
then teardown code. Code after yield always runs, even if an exception occurs.

Yield an empty list from managed_list(), then sort it in place after the yield.
"""

# I AM NOT DONE

from contextlib import contextmanager


@contextmanager
def managed_list():
    items = []
    yield items
