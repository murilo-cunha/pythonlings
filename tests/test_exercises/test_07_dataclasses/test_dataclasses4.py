from dataclasses4 import BoundedInt


def test_within_range():
    assert BoundedInt(50).value == 50

def test_clamp_low():
    assert BoundedInt(-10).value == 0

def test_clamp_high():
    assert BoundedInt(200).value == 100

def test_custom_bounds():
    assert BoundedInt(5, minimum=10, maximum=20).value == 10
