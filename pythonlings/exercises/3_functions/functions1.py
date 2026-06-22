# I AM NOT DONE

def greet(name, greeting="Hello"):
    # Currently ignores the greeting parameter — fix it
    return f"Hello, {name}!"


# DON'T EDIT THE TESTS
assert greet("Alice") == "Hello, Alice!"
assert greet("Bob", "Hi") == "Hi, Bob!"
assert greet("Carol", greeting="Hey") == "Hey, Carol!"
