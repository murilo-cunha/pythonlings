from oop2 import Color


def test_equal_colors():
    assert Color(255, 0, 0) == Color(255, 0, 0)

def test_unequal_colors():
    assert Color(255, 0, 0) != Color(0, 0, 255)

def test_hash_equal():
    assert hash(Color(255, 0, 0)) == hash(Color(255, 0, 0))

def test_set_dedup():
    red = Color(255, 0, 0)
    also_red = Color(255, 0, 0)
    blue = Color(0, 0, 255)
    assert len({red, also_red, blue}) == 2
