"""
Dict comprehensions: {key_expr: value_expr for item in iterable}
Use them to build dicts from sequences without a loop and .update().

Fix the value expression to map each word to its length.
"""

# I AM NOT DONE


words = ["hello", "world", "python", "code"]
word_lengths = {w: 0 for w in words}
