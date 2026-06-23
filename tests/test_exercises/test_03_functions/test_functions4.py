from functions4 import square, is_even, second


def test_square():
    assert square(4) == 16
    assert square(7) == 49

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(7) is False

def test_second_sort_key():
    pairs = [(3, 1), (1, 3), (2, 2)]
    assert sorted(pairs, key=second) == [(3, 1), (2, 2), (1, 3)]
