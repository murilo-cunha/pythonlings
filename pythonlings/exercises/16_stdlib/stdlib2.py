# I AM NOT DONE

from datetime import datetime, timezone, timedelta

# Fix: create a timezone-aware UTC datetime for 2024-01-01 12:00:00
utc_noon = datetime(2024, 1, 1, 12, 0, 0)  # Fix: add tzinfo=timezone.utc

# Fix: add 2 hours and 30 minutes to utc_noon using timedelta
later = utc_noon  # Fix: use timedelta

# Fix: compute the number of days between two dates
start = datetime(2024, 1, 1, tzinfo=timezone.utc)
end = datetime(2024, 12, 31, tzinfo=timezone.utc)
days_between = 0  # Fix: compute (end - start).days

# DON'T EDIT THE TESTS
assert utc_noon.tzinfo == timezone.utc
assert utc_noon.hour == 12

assert later.hour == 14
assert later.minute == 30

assert days_between == 365
