from stdlib3 import counts, by_letter, window


def test_counts():
    assert counts["apple"] == 3
    assert counts["banana"] == 2
    assert counts["cherry"] == 1

def test_most_common():
    assert counts.most_common(1) == [("apple", 3)]

def test_by_letter():
    assert sorted(by_letter["a"]) == ["apple", "apple", "apple"]
    assert sorted(by_letter["b"]) == ["banana", "banana"]

def test_window():
    assert list(window) == [3, 4, 5]
