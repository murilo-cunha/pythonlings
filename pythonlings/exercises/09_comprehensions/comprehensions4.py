# I AM NOT DONE

numbers = range(1, 11)

# Fix: create a generator expression (use () not []) that yields cubes
cubes_gen = [n ** 3 for n in numbers]  # Fix: make this a generator, not a list

# DON'T EDIT THE TESTS
import types
assert isinstance(cubes_gen, types.GeneratorType)
assert list(cubes_gen) == [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
