# I AM NOT DONE


def http_status(code):
    # Fix: implement using match/case instead of if/elif
    # The current implementation is missing the 404 and default cases
    if code == 200:
        return "OK"
    elif code == 500:
        return "Internal Server Error"


# DON'T EDIT THE TESTS
assert http_status(200) == "OK"
assert http_status(404) == "Not Found"
assert http_status(500) == "Internal Server Error"
assert http_status(418) == "Unknown"
