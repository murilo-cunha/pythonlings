"""
ExceptionGroup (Python 3.11+) groups multiple exceptions raised simultaneously.
raise ExceptionGroup("label", [err1, err2])
Useful for validation that should report ALL failures, not just the first one.

Fix validate_all() to raise ExceptionGroup("validation errors", errors) instead of Exception.
"""

# I AM NOT DONE


def validate_all(data: dict) -> None:
    errors = []
    if "name" not in data:
        errors.append(ValueError("missing field: name"))
    if "age" not in data:
        errors.append(ValueError("missing field: age"))
    if errors:
        raise Exception("validation errors")
