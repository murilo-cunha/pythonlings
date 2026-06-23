import pytest
from functions5 import hypotenuse


def test_3_4_5():
    assert hypotenuse(3, 4) == 5.0

def test_5_12_13():
    assert hypotenuse(5, 12) == 13.0

def test_positional_only():
    with pytest.raises(TypeError):
        hypotenuse(a=3, b=4)
