from polars2 import result


def test_has_with_tax_column():
    assert "with_tax" in result.columns

def test_filtered_height():
    assert result.height == 2

def test_with_tax_values():
    assert [round(v, 2) for v in result["with_tax"].to_list()] == [24.2, 36.3]
