from polars3 import result


def test_teams():
    assert result.sort("team")["team"].to_list() == ["x", "y"]

def test_totals():
    assert result.sort("team")["total"].to_list() == [3, 3]
