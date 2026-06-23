from type_hints3 import first, T


def test_return_annotation_is_T():
    assert first.__annotations__.get("return") is T

def test_first_int():
    assert first([1, 2, 3]) == 1

def test_first_str():
    assert first(["a", "b"]) == "a"
