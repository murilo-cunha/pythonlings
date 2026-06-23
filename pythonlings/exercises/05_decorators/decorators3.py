# I AM NOT DONE


def repeat(n):
    # Return a decorator that calls the decorated function n times
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            # Fix: call func exactly n times, keeping the last result
            return result
        return wrapper
    return decorator


@repeat(3)
def say(msg):
    return msg


# DON'T EDIT THE TESTS
results = []
call_count = 0

def count_calls(msg):
    global call_count
    call_count += 1
    return msg

count_calls = repeat(3)(count_calls)
count_calls("hi")
assert call_count == 3

assert say("echo") == "echo"
