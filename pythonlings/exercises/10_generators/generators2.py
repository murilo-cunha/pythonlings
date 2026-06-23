"""
"yield from iterable" delegates to another iterable, yielding each of its items.
It's equivalent to: for item in iterable: yield item
It also works with other generators, flattening them without extra loops.

Use yield from inside chain() to yield all items from each iterable in turn.
"""

# I AM NOT DONE


def chain(*iterables):
    for it in iterables:
        pass
