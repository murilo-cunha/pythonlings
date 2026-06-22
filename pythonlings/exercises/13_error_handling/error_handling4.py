# I AM NOT DONE


def validate_all(data: dict) -> None:
    errors = []
    if "name" not in data:
        errors.append(ValueError("missing field: name"))
    if "age" not in data:
        errors.append(ValueError("missing field: age"))
    if errors:
        # Fix: raise an ExceptionGroup("validation errors", errors)
        raise Exception("validation errors")  # Fix this


# DON'T EDIT THE TESTS
try:
    validate_all({})
except ExceptionGroup as eg:
    assert eg.message == "validation errors"
    assert len(eg.exceptions) == 2

try:
    validate_all({"name": "Ada"})
except ExceptionGroup as eg:
    assert len(eg.exceptions) == 1
    assert "age" in str(eg.exceptions[0])

# No exception when all fields present
validate_all({"name": "Ada", "age": 30})
