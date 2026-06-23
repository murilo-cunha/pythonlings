from comprehensions3 import first_letters


def test_first_letters():
    assert first_letters == {"t", "q", "b", "f", "j", "o", "l", "d"}

def test_is_set():
    assert isinstance(first_letters, set)
