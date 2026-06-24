"""
SQL `GROUP BY` collapses rows that share a value and lets you aggregate the
rest with functions like `SUM(...)`.

The `sales` table below is already created and populated for you. Write a
query that returns each region together with the total of its `amount`,
ordered by region, and assign the fetched rows to `totals`.

`.fetchall()` returns a list of tuples, one per group. The test expects:
    totals == [('north', 30), ('south', 5)]
"""

# I AM NOT DONE

import duckdb

con = duckdb.connect()
con.execute("CREATE TABLE sales (region VARCHAR, amount INTEGER)")
con.execute("INSERT INTO sales VALUES ('north', 10), ('north', 20), ('south', 5)")

# TODO: aggregate amount per region with GROUP BY, ordered by region
totals = ...
