import types
from itertools import islice
from generators4 import naturals


def test_is_generator():
    assert isinstance(naturals(), types.GeneratorType)

def test_first_five():
    assert list(islice(naturals(), 5)) == [1, 2, 3, 4, 5]

def test_start_from_ten():
    assert list(islice(naturals(10), 4)) == [10, 11, 12, 13]
