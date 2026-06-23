from generators2 import chain


def test_chain_lists():
    assert list(chain([1, 2], [3, 4], [5])) == [1, 2, 3, 4, 5]

def test_chain_strings():
    assert list(chain("ab", "cd")) == ["a", "b", "c", "d"]

def test_chain_empty():
    assert list(chain([], [])) == []
