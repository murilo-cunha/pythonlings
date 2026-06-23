"""
Implement __enter__ (called on entering the with block — return the resource)
and __exit__ (called on exit — receives exception info, return False to re-raise).
Use time.monotonic() for elapsed time: self.elapsed = time.monotonic() - self.start.

Fix Timer.__exit__ to record self.elapsed as the time since self.start.
"""

# I AM NOT DONE

import time


class Timer:
    def __enter__(self):
        self.start = time.monotonic()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = 0.0
        return False
