from exercise_with_failing_test import add


def test_add_wrong():
    assert add(2, 3) == 999  # intentionally wrong
