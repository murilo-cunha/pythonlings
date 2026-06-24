# Public classes and their public methods should each have a docstring.
# Ruff's pydocstyle rules D101 (class) and D102 (method) flag missing ones.
#
# Add a one-line docstring to the `Counter` class AND to its `increment`
# method. Each docstring must end with a period.

# I AM NOT DONE


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value
