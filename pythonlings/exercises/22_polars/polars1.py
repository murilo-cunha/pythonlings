"""
Polars is a fast DataFrame library. A pl.DataFrame is built from a dict
mapping column names to lists of values.

The dict below has two columns. Build a DataFrame from it and assign it
to `df` so that df.columns == ["name", "age"], df.height == 2, and the
"age" column holds [30, 25].
"""

# I AM NOT DONE

import polars as pl

data = {"name": ["Alice", "Bob"], "age": [30, 25]}

# TODO: build a pl.DataFrame from `data` and assign it to `df`
df = ...
