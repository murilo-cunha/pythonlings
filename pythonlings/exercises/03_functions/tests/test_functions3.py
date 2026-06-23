from functions3 import make_multiplier


def test_double():
    double = make_multiplier(2)
    assert double(5) == 10

def test_triple():
    triple = make_multiplier(3)
    assert triple(5) == 15

def test_composed():
    double = make_multiplier(2)
    triple = make_multiplier(3)
    assert double(triple(4)) == 24

def test_one():
    identity = make_multiplier(1)
    assert identity(7) == 7
