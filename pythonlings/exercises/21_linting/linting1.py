# Ruff's formatter enforces a consistent code style: spacing around
# operators and commas, no extra spaces inside parentheses, and so on.
# The code below is VALID Python but messily formatted.
# Reformat it so that `ruff format --check` reports nothing to change.
# Tip: let the tool do the work for you (see the hint).

# I AM NOT DONE

def add(a,b ):
    result=a+b
    return  result


def greet( name ):
    return "Hello, "+name+"!"


values = [1,2 ,3,4]
total = add( 10,20 )
