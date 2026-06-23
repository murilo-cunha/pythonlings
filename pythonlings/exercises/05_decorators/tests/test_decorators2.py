from decorators2 import add


def test_add_result():
    assert add(2, 3) == 5

def test_preserves_name():
    assert add.__name__ == "add"

def test_preserves_doc():
    assert add.__doc__ == "Add two numbers."
