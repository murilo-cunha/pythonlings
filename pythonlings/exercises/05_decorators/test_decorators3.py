from decorators3 import repeat


def test_call_count():
    count = 0
    def track():
        nonlocal count
        count += 1
    repeat(3)(track)()
    assert count == 3

def test_returns_last_result():
    @repeat(3)
    def echo(msg):
        return msg
    assert echo("hello") == "hello"

def test_repeat_once():
    calls = []
    @repeat(1)
    def append_one():
        calls.append(1)
    append_one()
    assert len(calls) == 1
