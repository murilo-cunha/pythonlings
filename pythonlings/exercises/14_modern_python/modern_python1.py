# I AM NOT DONE

name = "Ada"
value = 3.14159
items = [1, 2, 3]

# Fix each variable to produce the expected string using f-strings:

# Format value to 2 decimal places inside an f-string
formatted = f"{value}"  # Fix: should produce "3.14"

# Left-pad name to width 10 with dashes
padded = f"{name}"  # Fix: should produce "-------Ada"

# Use an expression inside the f-string (no pre-computation)
count = f"{items}"  # Fix: should produce "3 items" using len(items) in the f-string

# DON'T EDIT THE TESTS
assert formatted == "3.14"
assert padded == "-------Ada"
assert count == "3 items"
