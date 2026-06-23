# I AM NOT DONE

sentence = "the quick brown fox jumps over the lazy dog"

# Fix: create a set of unique first-letters using a set comprehension
first_letters = {word for word in sentence.split()}  # Fix the expression

# DON'T EDIT THE TESTS
assert first_letters == {"t", "q", "b", "f", "j", "o", "l", "d"}
assert isinstance(first_letters, set)
