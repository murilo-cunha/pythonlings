# I AM NOT DONE


class ValidationError(ValueError):
    # Fix: add __init__ that accepts field: str and message: str
    # Store both as instance attributes
    pass


def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("age", "must be an integer")
    if age < 0 or age > 150:
        raise ValidationError("age", "must be between 0 and 150")
    return age


# DON'T EDIT THE TESTS
try:
    validate_age(-1)
    assert False, "Should raise"
except ValidationError as e:
    assert e.field == "age"
    assert e.message == "must be between 0 and 150"
    assert isinstance(e, ValueError)  # Inherits from ValueError

assert validate_age(25) == 25
