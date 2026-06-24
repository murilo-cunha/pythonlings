# A multi-line docstring should start its summary on the FIRST line (right
# after the opening """), then have a blank line before the rest.
# Ruff's pydocstyle rules check this:
#   D212 - the multi-line summary starts on the first line,
#   D205 - there is one blank line between the summary and the description.
#
# Fix the docstring below: move the summary up onto the first line and add a
# blank line between the summary and the description.

# I AM NOT DONE


def greet(name):
    """
    Return a greeting for name.
    The greeting is a friendly hello.
    """
    return f"Hello, {name}!"
