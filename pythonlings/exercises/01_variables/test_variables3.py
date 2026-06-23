from variables3 import x, y, z, a, b, c


def test_chained_assignment():
    assert x == y == z == "Hello!"

def test_unpacking_a():
    assert a == "a"

def test_unpacking_b():
    assert b == "b"

def test_unpacking_c():
    assert c == "c"
