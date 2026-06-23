"""
match/case is Python's structural pattern matching (3.10+).
match value: case 200: ... case 404: ... case _: (wildcard/default)
Unlike if/elif, it supports destructuring, guards, and class patterns.

Rewrite http_status() using match/case to handle 200, 404, 500, and a default.
"""

# I AM NOT DONE


def http_status(code):
    if code == 200:
        return "OK"
    elif code == 500:
        return "Internal Server Error"
