import types
from comprehensions4 import cubes_gen


def test_is_generator():
    assert isinstance(cubes_gen, types.GeneratorType)

def test_values():
    assert list(cubes_gen) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
