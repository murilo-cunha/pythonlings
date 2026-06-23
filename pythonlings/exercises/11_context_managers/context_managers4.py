"""
contextlib.suppress(*exceptions) silently ignores the listed exception types.
with suppress(FileNotFoundError): os.remove(path) — no try/except needed.
Only use it when ignoring the exception is actually the right behavior.

Rewrite the result2 assignment using contextlib.suppress(ZeroDivisionError).
"""

# I AM NOT DONE

from contextlib import suppress

result = None
try:
    result = 1 / 0
except ZeroDivisionError:
    pass

result2 = None
result2 = 1 / 0
