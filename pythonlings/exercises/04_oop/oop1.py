# I AM NOT DONE


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # Return a string like: Point(1, 2)
        return ""  # Fix this

    def __str__(self):
        # Return a human-friendly string like: (1, 2)
        return ""  # Fix this


# DON'T EDIT THE TESTS
p = Point(1, 2)
assert repr(p) == "Point(1, 2)"
assert str(p) == "(1, 2)"
assert f"{p}" == "(1, 2)"
