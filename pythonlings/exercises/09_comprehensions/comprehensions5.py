"""
Nested comprehensions: [expr for outer in iterable for inner in outer]
Each additional 'for' clause is a nested loop — read left to right.
Keep nesting to 2 levels maximum; deeper nesting hurts readability quickly.

Fix the comprehension to flatten the 3x3 matrix into a single list.
"""

# I AM NOT DONE


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [matrix[i][j] for i in range(3)]
