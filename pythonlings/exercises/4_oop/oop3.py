# I AM NOT DONE


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent __init__ using super()
        self.breed = breed  # Fix: also initialise name via super().__init__

    def speak(self):
        # Override speak — call super().speak() and append " — Woof!"
        return "Woof!"  # Fix this


# DON'T EDIT THE TESTS
d = Dog("Rex", "Labrador")
assert d.name == "Rex"
assert d.breed == "Labrador"
assert d.speak() == "Rex makes a sound — Woof!"
assert isinstance(d, Animal)
