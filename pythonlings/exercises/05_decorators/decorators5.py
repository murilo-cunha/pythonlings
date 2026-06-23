"""
Decorators stack bottom-up: the decorator closest to def runs first.
@A @B def f(): ... is equivalent to f = A(B(f)).
So calling f() runs A's wrapper, which calls B's wrapper, which calls f.

Fix the decorator order on hello() so the output is <b><i>hello</i></b>.
"""

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


@italic
@bold
def hello():
    return "hello"
