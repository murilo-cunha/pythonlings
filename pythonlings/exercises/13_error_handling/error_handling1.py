"""
try runs the risky code. except catches a specific exception type.
else runs only if NO exception was raised. finally ALWAYS runs (cleanup).
Pattern: try: result = op() except Err: handle() else: use(result) finally: cleanup()

Implement safe_divide() using try/except/else/finally — return None on ZeroDivisionError,
otherwise return the result.
"""

# I AM NOT DONE


def safe_divide(a, b):
    return 0.0


log = []


def logged_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        log.append("error")
        return None
    else:
        log.append("ok")
        return result
    finally:
        log.append("done")
