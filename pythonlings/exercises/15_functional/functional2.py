"""
reduce(func, iterable) accumulates items left-to-right.
reduce(lambda a, b: a * b, [1,2,3]) = (1*2)*3 = 6
For simple reductions, prefer sum(), max(), or min() when available.

Use reduce() to compute the product and the maximum of numbers.
"""

# I AM NOT DONE

from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = 0
maximum = numbers[0]
