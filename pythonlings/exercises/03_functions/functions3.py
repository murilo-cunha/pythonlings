"""
A closure is an inner function that remembers variables from the enclosing scope,
even after the outer function has returned. The inner function "closes over" those
variables — they stay alive as long as the inner function exists.

Implement make_multiplier() so it returns a function that multiplies its argument
by the captured factor.
"""

# I AM NOT DONE


def make_multiplier(factor):
    def multiply(x):
        return x
    return multiply
