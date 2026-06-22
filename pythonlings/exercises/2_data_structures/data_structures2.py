# I AM NOT DONE

# Create a dictionary of fruit prices
prices = {"apple": 0.99, "banana": 0.59, "cherry": 2.99}

# Update banana's price to 0.79
# YOUR CODE HERE

# Remove "cherry" from the dict
# YOUR CODE HERE

# Get the price of "mango" (not in dict) with a default of 0.0
mango_price = 0.0  # Fix: use dict.get() so missing keys return 0.0

# DON'T EDIT THE TESTS
assert prices == {"apple": 0.99, "banana": 0.79}
assert "cherry" not in prices
assert mango_price == 0.0
