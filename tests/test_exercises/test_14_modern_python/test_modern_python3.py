from modern_python3 import http_status


def test_200():
    assert http_status(200) == "OK"

def test_404():
    assert http_status(404) == "Not Found"

def test_500():
    assert http_status(500) == "Internal Server Error"

def test_default():
    assert http_status(418) == "Unknown"
