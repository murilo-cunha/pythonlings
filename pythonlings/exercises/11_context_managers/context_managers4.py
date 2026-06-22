# I AM NOT DONE

from contextlib import suppress


# Fix: use contextlib.suppress so the ZeroDivisionError is silently ignored
result = None
try:
    result = 1 / 0
except ZeroDivisionError:
    pass

# Rewrite the above using contextlib.suppress
result2 = None
# Fix: use `with suppress(ZeroDivisionError):`
result2 = 1 / 0  # This will raise — wrap it with suppress


# DON'T EDIT THE TESTS
assert result is None  # Not set because of the error
assert result2 is None  # Also not set — suppress silenced the error
