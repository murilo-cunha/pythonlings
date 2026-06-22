# I AM NOT DONE

from functools import lru_cache

call_count = 0


# Fix: add @lru_cache() to cache results and avoid recomputation
def fib(n):
    global call_count
    call_count += 1
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# DON'T EDIT THE TESTS
call_count = 0
assert fib(10) == 55

# With lru_cache, computing fib(10) should call fib at most 11 times (fib(0) through fib(10))
# Without cache, it calls fib 177 times for n=10
assert call_count <= 11
