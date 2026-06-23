from generators3 import Fibonacci


def test_fib_20():
    assert list(Fibonacci(20)) == [0, 1, 1, 2, 3, 5, 8, 13]

def test_fib_1():
    assert list(Fibonacci(1)) == [0, 1, 1]

def test_fib_0():
    assert list(Fibonacci(0)) == [0]
