"""
To create an abstract property, stack @property and @abstractmethod (property first).
Subclasses must define it with @property, not just a plain attribute.
The speak() template method calls self.sound, which subclasses must provide.

Implement sound as a property on Cat (returns "meow") and Dog (returns "woof").
"""

# I AM NOT DONE

from abc import ABC, abstractmethod


class Animal(ABC):
    @property
    @abstractmethod
    def sound(self) -> str: ...

    def speak(self) -> str:
        return f"I say: {self.sound}"


class Cat(Animal):
    @property
    def sound(self) -> str:
        return ""


class Dog(Animal):
    @property
    def sound(self) -> str:
        return ""
