from datetime import timezone
from stdlib2 import utc_noon, later, days_between


def test_utc_aware():
    assert utc_noon.tzinfo == timezone.utc

def test_later_time():
    assert later.hour == 14
    assert later.minute == 30

def test_days_between():
    assert days_between == 365
