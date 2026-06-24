"""
Polars expressions transform DataFrames. `with_columns` adds or replaces
columns, `pl.col(...)` references a column, and `filter` keeps matching rows.

Starting from `df`, add a column "with_tax" equal to "price" * 1.21, then
keep only the rows where "price" is greater than 15. Assign the result to
`result`. It should contain the "with_tax" column, have height 2, and its
with_tax values (rounded to 2 decimals) should be [24.2, 36.3].
"""

# I AM NOT DONE

import polars as pl

df = pl.DataFrame({"name": ["A", "B", "C"], "price": [10, 20, 30]})

# TODO: add the "with_tax" column, filter price > 15, assign to `result`
result = ...
