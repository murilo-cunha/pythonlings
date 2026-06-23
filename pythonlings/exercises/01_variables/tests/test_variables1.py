from variables1 import a_integer, a_float, a_string, a_bytes, a_boolean, a_tuple


def test_integer_type():
    assert isinstance(a_integer, int)

def test_float_type():
    assert isinstance(a_float, float)

def test_string_type():
    assert isinstance(a_string, str)

def test_bytes_type():
    assert isinstance(a_bytes, bytes)

def test_boolean_type():
    assert isinstance(a_boolean, bool)

def test_tuple_type():
    assert isinstance(a_tuple, tuple)
