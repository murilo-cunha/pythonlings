# I AM NOT DONE

numbers = [1, 2, 3, 4, 5]

# Unpack: first element into `first`, rest into `rest`
first = numbers[0]   # Fix: use unpacking assignment instead
rest = numbers[1:]   # Fix: use unpacking assignment instead

# Unpack: first, last, and everything in between
first2 = numbers[0]    # Fix: use unpacking assignment
middle = numbers[1:4]  # Fix: use unpacking assignment
last = numbers[-1]     # Fix: use unpacking assignment

# DON'T EDIT THE TESTS
assert first == 1
assert rest == [2, 3, 4, 5]
assert first2 == 1
assert middle == [2, 3, 4]
assert last == 5
