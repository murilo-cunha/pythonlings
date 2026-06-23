from functional5 import combined, grouped, first_five


def test_combined():
    assert combined == [1, 2, 3, 4, 5, 6]

def test_grouped():
    assert grouped == [(1, [1, 1]), (2, [2, 2, 2]), (3, [3]), (1, [1, 1])]

def test_first_five():
    assert first_five == [1, 2, 3, 4, 5]
