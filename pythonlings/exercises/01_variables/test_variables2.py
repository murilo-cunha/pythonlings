from variables2 import x, y, z


def test_x_is_int():
    assert isinstance(x, int)

def test_y_is_float():
    assert isinstance(y, float)

def test_z_is_bytes():
    assert isinstance(z, bytes)
