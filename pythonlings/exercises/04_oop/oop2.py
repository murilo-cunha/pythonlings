"""
__eq__ defines the == operator between instances. If you define __eq__, also
define __hash__ — without it your class becomes unhashable (can't be used in
sets or as dict keys). Base the hash on the same fields you compare in __eq__.

Implement __eq__ and __hash__ for Color using its (r, g, b) channels.
"""

# I AM NOT DONE


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return False

    def __hash__(self):
        return 0
