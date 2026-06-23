"""
Set comprehensions: {expression for item in iterable}
Like list comprehensions but produce a set — duplicates are removed automatically.
The only difference from a list comprehension is the curly braces.

Fix the comprehension to collect unique first letters of words, not the words themselves.
"""

# I AM NOT DONE


sentence = "the quick brown fox jumps over the lazy dog"
first_letters = {word for word in sentence.split()}
