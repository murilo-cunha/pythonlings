# I AM NOT DONE


class Timer:
    """Context manager that records elapsed time."""
    import time as _time

    def __enter__(self):
        self.start = self._time.monotonic()
        return self  # returning self lets users write: with Timer() as t:

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Fix: compute self.elapsed as the time since self.start
        self.elapsed = 0.0  # Fix this
        return False  # Don't suppress exceptions


import time


# DON'T EDIT THE TESTS
with Timer() as t:
    time.sleep(0.05)

assert t.elapsed >= 0.05
assert t.elapsed < 1.0  # Sanity bound
