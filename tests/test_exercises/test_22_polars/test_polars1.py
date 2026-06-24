import polars as pl
from polars1 import df


def test_is_dataframe():
    assert isinstance(df, pl.DataFrame)

def test_columns():
    assert df.columns == ["name", "age"]

def test_height():
    assert df.height == 2

def test_age_values():
    assert df["age"].to_list() == [30, 25]
