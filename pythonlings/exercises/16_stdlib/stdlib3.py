"""
Counter(iterable) counts occurrences; .most_common(n) returns the top-n pairs.
defaultdict(list) auto-creates a list for missing keys — no KeyError on first append.
deque(maxlen=n) is a fixed-size sliding window; oldest items are auto-discarded.

Fix counts (use Counter), by_letter (use defaultdict), and window (use deque).
"""

# I AM NOT DONE

from collections import Counter, defaultdict, deque

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = {}

by_letter = {}
for word in words:
    pass

window = []
for n in [1, 2, 3, 4, 5]:
    window.append(n)
