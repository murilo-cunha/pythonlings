from functional4 import square, cube, format_2dp


def test_square():
    assert square(4) == 16
    assert square(5) == 25

def test_cube():
    assert cube(3) == 27

def test_format_2dp():
    assert format_2dp(3.14159) == "3.14"
    assert format_2dp(1.0) == "1.00"
