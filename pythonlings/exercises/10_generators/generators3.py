"""
To make a class iterable, implement __iter__ (returns self) and __next__
(returns the next value or raises StopIteration when exhausted).
for x in obj: calls iter(obj) then repeatedly calls next() until StopIteration.

Fix __next__ to return the current Fibonacci number and advance the sequence.
"""

# I AM NOT DONE


class Fibonacci:
    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
