# I AM NOT DONE

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Fix: use map() to square each number (convert result to list)
squares = list(numbers)  # Fix this

# Fix: use filter() to keep only even numbers (convert result to list)
evens = list(numbers)  # Fix this

# Fix: chain map and filter — squares of even numbers only
even_squares = list(numbers)  # Fix this

# DON'T EDIT THE TESTS
assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
assert evens == [2, 4, 6, 8, 10]
assert even_squares == [4, 16, 36, 64, 100]
