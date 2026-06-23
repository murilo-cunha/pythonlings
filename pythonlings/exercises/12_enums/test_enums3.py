from enums3 import Color


def test_to_hex():
    assert Color.RED.to_hex() == "#ff0000"
    assert Color.GREEN.to_hex() == "#00ff00"
    assert Color.BLUE.to_hex() == "#0000ff"

def test_from_hex():
    assert Color.from_hex("#ff0000") is Color.RED
    assert Color.from_hex("#0000ff") is Color.BLUE
