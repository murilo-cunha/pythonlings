from type_hints1 import add, greet


def test_add_annotations():
    hints = add.__annotations__
    assert hints.get("a") is int
    assert hints.get("b") is int
    assert hints.get("return") is int

def test_greet_annotations():
    hints = greet.__annotations__
    assert hints.get("name") is str
    assert hints.get("return") is str

def test_add_result():
    assert add(2, 3) == 5
