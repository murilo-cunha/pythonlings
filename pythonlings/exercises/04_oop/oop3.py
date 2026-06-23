"""
Use super().__init__(...) inside a child class to call the parent __init__.
This ensures the parent initialises its own state before you add child-specific state.
super() also works for regular method calls, not just __init__.

Fix Dog.__init__ to call super().__init__(name) and fix speak() to extend the parent's result.
"""

# I AM NOT DONE


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        self.breed = breed

    def speak(self):
        return "Woof!"
