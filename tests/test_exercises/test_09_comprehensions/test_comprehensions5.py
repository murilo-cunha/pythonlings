from comprehensions5 import flat, matrix


def test_flat():
    assert flat == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_length():
    assert len(flat) == 9

def test_transposed():
    transposed = [[row[i] for row in matrix] for i in range(3)]
    assert transposed == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
