from enums2 import Priority


def test_values():
    assert Priority.LOW == 1
    assert Priority.MEDIUM == 2
    assert Priority.HIGH == 3
    assert Priority.CRITICAL == 4

def test_comparison():
    assert Priority.HIGH > Priority.LOW

def test_arithmetic():
    assert Priority.CRITICAL - Priority.LOW == 3
