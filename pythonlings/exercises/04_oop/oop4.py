"""
@classmethod receives the class (cls) as first argument — use it for alternative
constructors: Temperature.from_fahrenheit(212). @staticmethod has no implicit
first argument; it's a plain function namespaced inside the class.

Implement from_fahrenheit (formula: C = (F - 32) * 5/9) and is_freezing (True if <= 0).
"""

# I AM NOT DONE


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        return cls(0)

    @staticmethod
    def is_freezing(celsius):
        return False

    def __repr__(self):
        return f"Temperature({self.celsius})"
