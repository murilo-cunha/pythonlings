# I AM NOT DONE

import pytest


def get_greeting(name):
    import os
    env_greeting = os.environ.get("GREETING", "Hello")
    return f"{env_greeting}, {name}!"


def test_default_greeting():
    assert get_greeting("Alice") == "Hello, Alice!"


def test_custom_greeting(monkeypatch):
    # Fix: use monkeypatch.setenv to set GREETING="Hi" for this test
    # (currently this test doesn't patch anything so it also returns "Hello")
    assert get_greeting("Bob") == "Hi, Bob!"


# DON'T EDIT BELOW
import sys
if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
