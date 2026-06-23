from oop4 import Temperature


def test_from_fahrenheit_boiling():
    assert Temperature.from_fahrenheit(212).celsius == 100.0

def test_from_fahrenheit_freezing():
    assert Temperature.from_fahrenheit(32).celsius == 0.0

def test_is_freezing_zero():
    assert Temperature.is_freezing(0) is True

def test_is_freezing_negative():
    assert Temperature.is_freezing(-10) is True

def test_is_not_freezing():
    assert Temperature.is_freezing(1) is False
