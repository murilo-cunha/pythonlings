# I AM NOT DONE


class Fibonacci:
    """Iterator that yields Fibonacci numbers."""

    def __init__(self, limit):
        self.limit = limit
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self  # This is correct

    def __next__(self):
        # Fix: yield a, advance (a, b) → (b, a+b), stop when a > limit
        raise StopIteration  # Fix this


# DON'T EDIT THE TESTS
fibs = list(Fibonacci(20))
assert fibs == [0, 1, 1, 2, 3, 5, 8, 13]
assert list(Fibonacci(1)) == [0, 1, 1]
