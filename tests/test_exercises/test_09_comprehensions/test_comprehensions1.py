from comprehensions1 import squares_of_evens


def test_squares_of_evens():
    assert squares_of_evens == [4, 16, 36, 64, 100]

def test_length():
    assert len(squares_of_evens) == 5
