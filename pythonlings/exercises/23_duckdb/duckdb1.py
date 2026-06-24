"""
DuckDB is an in-process SQL database. `duckdb.sql(...)` runs a query and
returns a relation you can fetch results from.

`.fetchone()` returns the first row as a tuple, so the first column is `[0]`.

Run a query that selects the value 42 (aliased as `answer`) and assign the
single returned value to `answer` so that `answer == 42`.
"""

# I AM NOT DONE

import duckdb

# TODO: run a SELECT with duckdb.sql(...) and fetch the value
answer = ...
