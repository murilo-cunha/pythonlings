# I AM NOT DONE


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, f):
        # Create a Temperature from a Fahrenheit value
        # Formula: C = (F - 32) * 5/9
        return cls(0)  # Fix this

    @staticmethod
    def is_freezing(celsius):
        # Return True if temperature is at or below 0°C
        return False  # Fix this

    def __repr__(self):
        return f"Temperature({self.celsius})"


# DON'T EDIT THE TESTS
t = Temperature.from_fahrenheit(212)
assert t.celsius == 100.0

t2 = Temperature.from_fahrenheit(32)
assert t2.celsius == 0.0

assert Temperature.is_freezing(0) is True
assert Temperature.is_freezing(-10) is True
assert Temperature.is_freezing(1) is False
