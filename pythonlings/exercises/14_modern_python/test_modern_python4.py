from modern_python4 import classify


def test_negative():
    assert classify(-5) == "negative"

def test_zero():
    assert classify(0) == "zero"

def test_small_positive():
    assert classify(3) == "small positive"

def test_large_positive():
    assert classify(10) == "large positive"
