"""
@lru_cache() memoises a function — it caches results keyed by arguments.
Repeated calls with the same args return the cached result instantly.
Without cache, fib(10) makes 177 calls; with cache it makes just 11.

Add @lru_cache() above def fib to enable memoisation.
"""

# I AM NOT DONE

from functools import lru_cache

call_count = 0


def fib(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
