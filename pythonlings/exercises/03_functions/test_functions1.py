from functions1 import greet


def test_default_greeting():
    assert greet("Alice") == "Hello, Alice!"

def test_custom_greeting_positional():
    assert greet("Bob", "Hi") == "Hi, Bob!"

def test_custom_greeting_keyword():
    assert greet("Carol", greeting="Hey") == "Hey, Carol!"
