from functions2 import total, describe


def test_total_three():
    assert total(1, 2, 3) == 6

def test_total_two():
    assert total(10, 20) == 30

def test_total_empty():
    assert total() == 0

def test_describe():
    assert describe(name="Ada", lang="Python") == {"name": "Ada", "lang": "Python"}

def test_describe_empty():
    assert describe() == {}
