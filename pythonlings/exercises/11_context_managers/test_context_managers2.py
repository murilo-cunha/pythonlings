import time
from context_managers2 import Timer


def test_elapsed():
    with Timer() as t:
        time.sleep(0.05)
    assert t.elapsed >= 0.05
    assert t.elapsed < 1.0
