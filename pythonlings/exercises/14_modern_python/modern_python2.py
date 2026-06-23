"""
The walrus operator := assigns AND returns a value in one expression.
It lets you compute a value inside a comprehension filter and reuse it
in the expression, avoiding computing it twice.

Rewrite the comprehension using walrus so root := math.isqrt(n) is used
in both the filter (root**2 == n) and the result (collect root, not n).
"""

# I AM NOT DONE

import math

numbers = [2, 3, 4, 8, 9, 15, 16, 25]
whole_roots = [n for n in numbers if math.isqrt(n) ** 2 == n]
