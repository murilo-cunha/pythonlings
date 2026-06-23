from error_handling1 import safe_divide, logged_divide, log


def test_safe_divide_ok():
    assert safe_divide(10, 2) == 5.0

def test_safe_divide_zero():
    assert safe_divide(10, 0) is None

def test_logged_ok():
    log.clear()
    assert logged_divide(10, 2) == 5.0
    assert log == ["ok", "done"]

def test_logged_zero():
    log.clear()
    assert logged_divide(10, 0) is None
    assert log == ["error", "done"]
