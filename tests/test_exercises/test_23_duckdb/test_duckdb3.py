from duckdb3 import totals


def test_totals():
    assert totals == [("north", 30), ("south", 5)]
