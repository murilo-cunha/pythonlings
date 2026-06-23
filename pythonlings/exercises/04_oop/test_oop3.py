from oop3 import Dog, Animal


def test_name_inherited():
    d = Dog("Rex", "Labrador")
    assert d.name == "Rex"

def test_breed():
    d = Dog("Rex", "Labrador")
    assert d.breed == "Labrador"

def test_speak():
    d = Dog("Rex", "Labrador")
    assert d.speak() == "Rex makes a sound — Woof!"

def test_is_animal():
    d = Dog("Rex", "Labrador")
    assert isinstance(d, Animal)
