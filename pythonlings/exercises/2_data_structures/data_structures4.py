# I AM NOT DONE

numbers = [1, 2, 3, 4, 5]

# Unpack: first element into `first`, rest into `rest`
# Fix: use a single starred unpacking assignment: first, *rest = numbers
first = None   # Fix: use unpacking assignment instead
rest = None    # Fix: use unpacking assignment instead

# Unpack: first, last, and everything in between
# Fix: use a single starred unpacking assignment: first2, *middle, last = numbers
first2 = None    # Fix: use unpacking assignment
middle = None    # Fix: use unpacking assignment
last = None      # Fix: use unpacking assignment

# DON'T EDIT THE TESTS
assert first == 1
assert rest == [2, 3, 4, 5]
assert first2 == 1
assert middle == [2, 3, 4]
assert last == 5
