from functional1 import squares, evens, even_squares


def test_squares():
    assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

def test_evens():
    assert evens == [2, 4, 6, 8, 10]

def test_even_squares():
    assert even_squares == [4, 16, 36, 64, 100]
