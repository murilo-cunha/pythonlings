# I AM NOT DONE

from abc import ABC, abstractmethod


class Animal(ABC):
    @property
    @abstractmethod
    def sound(self) -> str:
        ...

    def speak(self) -> str:
        return f"I say: {self.sound}"


class Cat(Animal):
    @property
    def sound(self) -> str:
        return ""  # Fix: return "meow"


class Dog(Animal):
    @property
    def sound(self) -> str:
        return ""  # Fix: return "woof"


# DON'T EDIT THE TESTS
c = Cat()
d = Dog()
assert c.sound == "meow"
assert d.sound == "woof"
assert c.speak() == "I say: meow"
assert d.speak() == "I say: woof"
