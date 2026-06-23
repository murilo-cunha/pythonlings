"""
Custom exceptions inherit from built-in exception classes (ValueError, RuntimeError, etc.).
Add __init__ to attach structured data (field name, error code, etc.).
Raising specific exception types lets callers catch exactly what they expect.

Add __init__(self, field, message) to ValidationError and store both as attributes.
"""

# I AM NOT DONE


class ValidationError(ValueError):
    pass


def validate_age(age):
    if not isinstance(age, int):
        raise ValidationError("age", "must be an integer")
    if age < 0 or age > 150:
        raise ValidationError("age", "must be between 0 and 150")
    return age
