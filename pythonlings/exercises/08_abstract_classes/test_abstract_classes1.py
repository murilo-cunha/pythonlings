import pytest
from abstract_classes1 import Rectangle, Shape


def test_area():
    assert Rectangle(4, 5).area() == 20.0

def test_perimeter():
    assert Rectangle(4, 5).perimeter() == 18.0

def test_abstract_not_instantiable():
    with pytest.raises(TypeError):
        Shape()
