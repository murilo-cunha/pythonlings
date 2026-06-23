"""
Always use timezone-aware datetimes in production to avoid ambiguity.
Create aware datetimes with tzinfo=timezone.utc. Add time with timedelta.
Subtraction of two datetimes returns a timedelta; use .days to get the count.

Fix utc_noon to be timezone-aware, compute later by adding 2h 30m, and set days_between.
"""

# I AM NOT DONE

from datetime import datetime, timezone, timedelta

utc_noon = datetime(2024, 1, 1, 12, 0, 0)
later = utc_noon

start = datetime(2024, 1, 1, tzinfo=timezone.utc)
end = datetime(2024, 12, 31, tzinfo=timezone.utc)
days_between = 0
