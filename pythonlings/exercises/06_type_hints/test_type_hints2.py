from type_hints2 import double, parse_id


def test_double_annotation():
    hints = double.__annotations__
    assert str(hints.get("value")) in ("int | float", "float | int")
    assert str(hints.get("return")) in ("int | float", "float | int")

def test_parse_id_valid():
    assert parse_id("42") == 42

def test_parse_id_invalid():
    assert parse_id("abc") is None
