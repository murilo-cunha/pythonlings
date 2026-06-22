# I AM NOT DONE

from enum import IntEnum, auto


class Priority(IntEnum):
    # Fix: use auto() for values — LOW, MEDIUM, HIGH, CRITICAL
    # auto() assigns 1, 2, 3, 4 automatically
    pass


# DON'T EDIT THE TESTS
assert Priority.LOW == 1
assert Priority.MEDIUM == 2
assert Priority.HIGH == 3
assert Priority.CRITICAL == 4

# IntEnum members are ints — arithmetic works
assert Priority.HIGH > Priority.LOW
assert Priority.CRITICAL - Priority.LOW == 3
