"""
Polars can aggregate with group_by(...).agg(...). Each group produces one
row, and aggregation expressions like pl.col("x").sum() summarize values.

Starting from `df`, group by "team" and compute the sum of "points" as a
column named "total". Assign the result to `result`. After sorting by
"team", the "team" column should be ["x", "y"] and "total" should be [3, 3].
"""

# I AM NOT DONE

import polars as pl

df = pl.DataFrame({"team": ["x", "x", "y"], "points": [1, 2, 3]})

# TODO: group by "team", sum "points" into a "total" column, assign to `result`
result = ...
