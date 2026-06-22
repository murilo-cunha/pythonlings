# I AM NOT DONE

from collections import Counter, defaultdict, deque

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

# Fix: use Counter to count word frequencies
counts = {}  # Fix: use Counter(words)

# Fix: use defaultdict(list) to group words by first letter
by_letter = {}  # Fix: use defaultdict(list)
for word in words:
    pass  # Fix: append to by_letter[word[0]]

# Fix: use deque with maxlen=3 as a sliding window
window = []  # Fix: use deque(maxlen=3)
for n in [1, 2, 3, 4, 5]:
    window.append(n)  # Once fixed, window auto-discards the oldest item

# DON'T EDIT THE TESTS
assert counts["apple"] == 3
assert counts["banana"] == 2
assert counts["cherry"] == 1
assert counts.most_common(1) == [("apple", 3)]

assert sorted(by_letter["a"]) == ["apple", "apple", "apple"]
assert sorted(by_letter["b"]) == ["banana", "banana"]

assert list(window) == [3, 4, 5]  # Only last 3 elements kept
