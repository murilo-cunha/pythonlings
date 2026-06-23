from functional3 import fib
import functional3


def test_fib_10():
    assert fib(10) == 55

def test_call_count():
    functional3.call_count = 0
    fib(10)
    assert functional3.call_count <= 11
