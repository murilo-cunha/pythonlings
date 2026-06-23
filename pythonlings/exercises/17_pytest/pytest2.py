"""
Fixtures are functions decorated with @pytest.fixture that provide reusable test data.
Tests declare them as parameters — pytest injects the return value automatically.
Use fixtures to avoid repeating setup code across test functions.

Fix the sample_data fixture so all three tests pass.
"""

# I AM NOT DONE

import pytest


@pytest.fixture
def sample_data():
    return {}


def test_name(sample_data):
    assert sample_data["name"] == "Alice"


def test_scores(sample_data):
    assert len(sample_data["scores"]) == 3
    assert sum(sample_data["scores"]) == 270


def test_active(sample_data):
    assert sample_data["active"] is True
