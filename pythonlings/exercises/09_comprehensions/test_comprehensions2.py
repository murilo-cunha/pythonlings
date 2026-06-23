from comprehensions2 import word_lengths


def test_lengths():
    assert word_lengths == {"hello": 5, "world": 5, "python": 6, "code": 4}

def test_keys():
    assert set(word_lengths.keys()) == {"hello", "world", "python", "code"}
