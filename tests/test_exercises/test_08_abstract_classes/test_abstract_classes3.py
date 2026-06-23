import pytest
from abstract_classes3 import Circle, Square, render


def test_circle_draw():
    assert render(Circle(5.0)) == "Circle(r=5.0)"

def test_square_draw():
    assert render(Square(3.0)) == "Square(s=3.0)"

def test_protocol_no_runtime_check():
    from abstract_classes3 import Drawable
    with pytest.raises(TypeError):
        issubclass(Circle, Drawable)
