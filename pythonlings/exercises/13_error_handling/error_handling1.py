# I AM NOT DONE


def safe_divide(a, b):
    # Fix: implement using try/except/else/finally
    # - catch ZeroDivisionError and return None
    # - else block: return the result
    # - finally block: always executed (no return needed there)
    return 0.0  # Fix this into a try/except/else/finally structure


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
        log.append("done")  # Runs whether or not an exception occurred


# DON'T EDIT THE TESTS
assert safe_divide(10, 2) == 5.0
assert safe_divide(10, 0) is None

assert logged_divide(10, 2) == 5.0
assert log == ["ok", "done"]

log.clear()
assert logged_divide(10, 0) is None
assert log == ["error", "done"]
