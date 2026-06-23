from variables4 import hello_world, one_plus_two


def test_string_concat():
    assert hello_world == "Hello World!"

def test_integer_addition():
    assert one_plus_two == 3

def test_result_is_int():
    assert isinstance(one_plus_two, int)
