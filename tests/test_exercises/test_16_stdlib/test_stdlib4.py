from stdlib4 import json_str, restored, pretty


def test_json_str():
    assert json_str == '{"name": "Ada", "scores": [95, 87, 92], "active": true}'

def test_restored():
    assert restored == {"name": "Ada", "scores": [95, 87, 92], "active": True}

def test_pretty_format():
    assert pretty.startswith("{\n  ")
