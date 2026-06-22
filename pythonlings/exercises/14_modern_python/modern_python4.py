# I AM NOT DONE


def classify(n):
    # Fix: implement using match/case with guards (if conditions in case clauses)
    # The current implementation always returns "unknown"
    return "unknown"


# DON'T EDIT THE TESTS
assert classify(-5) == "negative"
assert classify(0) == "zero"
assert classify(3) == "small positive"   # 1-9
assert classify(10) == "large positive"  # 10+
