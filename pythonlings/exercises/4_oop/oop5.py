# I AM NOT DONE


class Vector:
    # Add __slots__ to restrict attributes to x and y only
    # This saves memory and prevents adding arbitrary attributes

    def __init__(self, x, y):
        self.x = x
        self.y = y


# DON'T EDIT THE TESTS
v = Vector(3, 4)
assert v.x == 3
assert v.y == 4

# __slots__ should prevent adding new attributes
try:
    v.z = 5
    assert False, "Expected AttributeError"
except AttributeError:
    pass
