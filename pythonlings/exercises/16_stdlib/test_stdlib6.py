from stdlib6 import output


def test_debug_present():
    assert "starting up" in output

def test_info_present():
    assert "processing item 1" in output

def test_warning_present():
    assert "low disk space" in output
