from decorators1 import greet


def test_shout_world():
    assert greet("world") == "HELLO, WORLD"

def test_shout_python():
    assert greet("python") == "HELLO, PYTHON"

def test_shout_mixed_case():
    assert greet("Alice") == "HELLO, ALICE"
