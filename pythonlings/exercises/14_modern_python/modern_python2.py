# I AM NOT DONE

# The walrus operator := assigns and returns a value in one expression.
# It lets you assign inside a comprehension filter and reuse the value.

import math

numbers = [2, 3, 4, 8, 9, 15, 16, 25]

# Fix: rewrite using walrus so sqrt is computed once per number:
#   whole_roots = [root for n in numbers if (root := math.isqrt(n)) ** 2 == n]
# The broken version below collects n (the original number) instead of
# the integer square root, producing the wrong list.
whole_roots = [n for n in numbers if math.isqrt(n) ** 2 == n]

# DON'T EDIT THE TESTS
# After the fix, whole_roots should contain the square roots (2, 3, 4, 5)
# not the original perfect-square numbers (4, 9, 16, 25)
assert whole_roots == [2, 3, 4, 5]
