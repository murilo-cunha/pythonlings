# I AM NOT DONE

import pytest


@pytest.fixture
def sample_data():
    # Fix: return a dict with keys "name" (str), "scores" (list of ints), "active" (bool)
    return {}  # Fix this


def test_name(sample_data):
    assert sample_data["name"] == "Alice"


def test_scores(sample_data):
    assert len(sample_data["scores"]) == 3
    assert sum(sample_data["scores"]) == 270


def test_active(sample_data):
    assert sample_data["active"] is True


# DON'T EDIT BELOW
import sys
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
