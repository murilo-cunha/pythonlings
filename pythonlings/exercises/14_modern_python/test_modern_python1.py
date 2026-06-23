from modern_python1 import formatted, padded, count


def test_formatted():
    assert formatted == "3.14"

def test_padded():
    assert padded == "-------Ada"

def test_count():
    assert count == "3 items"
