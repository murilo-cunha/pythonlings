"""
monkeypatch is a built-in pytest fixture for temporarily overriding environment state.
monkeypatch.setenv("KEY", "value") sets an env variable for the duration of the test.
All patches are automatically undone after each test — no cleanup needed.

Use monkeypatch.setenv so test_custom_greeting passes without affecting other tests.
"""

# I AM NOT DONE

import pytest


def get_greeting(name):
    import os
    env_greeting = os.environ.get("GREETING", "Hello")
    return f"{env_greeting}, {name}!"


def test_default_greeting():
    assert get_greeting("Alice") == "Hello, Alice!"


def test_custom_greeting(monkeypatch):
    assert get_greeting("Bob") == "Hi, Bob!"
