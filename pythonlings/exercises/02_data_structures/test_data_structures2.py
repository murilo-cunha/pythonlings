from data_structures2 import prices, mango_price


def test_banana_updated():
    assert prices["banana"] == 0.79

def test_cherry_removed():
    assert "cherry" not in prices

def test_apple_unchanged():
    assert prices["apple"] == 0.99

def test_mango_default():
    assert mango_price == 0.0
