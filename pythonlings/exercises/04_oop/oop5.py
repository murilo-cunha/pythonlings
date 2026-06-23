"""
__slots__ = ('x', 'y') tells Python to allocate only those specific attributes.
Benefits: lower memory per instance, faster attribute access, and typos become
AttributeErrors immediately instead of silently creating new attributes.

Add __slots__ to Vector to restrict it to x and y only.
"""

# I AM NOT DONE


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
