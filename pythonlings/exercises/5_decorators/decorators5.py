# I AM NOT DONE

import functools


def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


# Currently produces <i><b>hello</b></i> — fix the decorator order
# so the output becomes <b><i>hello</i></b>
@italic
@bold
def hello():
    return "hello"


# DON'T EDIT THE TESTS
assert hello() == "<b><i>hello</i></b>"
