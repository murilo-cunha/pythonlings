from abstract_classes2 import Cat, Dog


def test_cat_sound():
    assert Cat().sound == "meow"

def test_dog_sound():
    assert Dog().sound == "woof"

def test_cat_speak():
    assert Cat().speak() == "I say: meow"

def test_dog_speak():
    assert Dog().speak() == "I say: woof"
