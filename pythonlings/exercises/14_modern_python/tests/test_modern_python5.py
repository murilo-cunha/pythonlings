from modern_python5 import describe, Point, Circle, Rectangle


def test_point():
    assert describe(Point(0.0, 0.0)) == "point at (0.0, 0.0)"

def test_circle():
    assert describe(Circle(Point(1.0, 2.0), 5.0)) == "circle at (1.0, 2.0) r=5.0"

def test_rectangle():
    assert describe(Rectangle(Point(0.0, 4.0), Point(3.0, 0.0))) == "rect from (0.0, 4.0) to (3.0, 0.0)"

def test_unknown():
    assert describe("other") == "unknown shape"
