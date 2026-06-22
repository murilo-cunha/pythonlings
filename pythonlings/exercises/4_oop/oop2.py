# I AM NOT DONE


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        # Two Colors are equal if all three channels match
        return False  # Fix this

    def __hash__(self):
        # Hash based on all three channels
        return 0  # Fix this


# DON'T EDIT THE TESTS
red = Color(255, 0, 0)
also_red = Color(255, 0, 0)
blue = Color(0, 0, 255)

assert red == also_red
assert red != blue
assert hash(red) == hash(also_red)
colors = {red, also_red, blue}
assert len(colors) == 2  # red and also_red are the same
