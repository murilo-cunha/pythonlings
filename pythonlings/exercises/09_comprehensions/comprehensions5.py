# I AM NOT DONE

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Fix: flatten the matrix into a single list using a nested comprehension
flat = [matrix[i][j] for i in range(3)]  # Fix: add the inner loop

# DON'T EDIT THE TESTS
assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Also: transpose the matrix (rows become columns)
transposed = [[row[i] for row in matrix] for i in range(3)]  # This is correct — study it
assert transposed == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
