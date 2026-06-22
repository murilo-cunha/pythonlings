# I AM NOT DONE

def make_multiplier(factor):
    # Return a function that multiplies its argument by factor
    def multiply(x):
        return x  # Fix: use factor here
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

# DON'T EDIT THE TESTS
assert double(5) == 10
assert triple(5) == 15
assert double(triple(4)) == 24
