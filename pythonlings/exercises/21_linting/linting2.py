# Ruff can sort imports for you (the "I" rule family, same as isort).
# The two standard-library imports below are USED, but they are NOT in
# alphabetical order, so `ruff check --select I` flags them.
# Reorder the imports so they are sorted and the check passes.
# Tip: let the tool do the work for you (see the hint).

# I AM NOT DONE

import sys
import os

print(os.getcwd())
print(sys.version)
