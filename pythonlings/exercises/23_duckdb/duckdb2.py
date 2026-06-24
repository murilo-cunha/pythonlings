"""
A DuckDB connection lets you run statements with `con.execute(...)`.

Using the in-memory connection `con` below:
  1. create a table `fruits` with columns `id INTEGER` and `name VARCHAR`,
  2. insert two rows into it,
  3. assign the number of rows in the table to `n_rows`.

`con.execute("SELECT ...").fetchone()` returns a tuple, so the count is `[0]`.
The test expects `n_rows == 2`.
"""

# I AM NOT DONE

import duckdb

con = duckdb.connect()

# TODO: create the table, insert 2 rows, then count them
n_rows = ...
