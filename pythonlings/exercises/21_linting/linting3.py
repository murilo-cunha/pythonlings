# Pyflakes (ruff's "F" rule family) catches dead code such as unused
# imports (F401) and unused local variables (F841).
# This file imports `math` but never uses it, and `compute` assigns a
# local `unused` that is never read.
# Remove the unused import and the unused variable so `ruff check
# --select F` passes. Keep everything that is actually used.

# I AM NOT DONE

import json
import math


def compute(x):
    unused = x * 2
    return x + 1


print(json.dumps({"result": compute(10)}))
