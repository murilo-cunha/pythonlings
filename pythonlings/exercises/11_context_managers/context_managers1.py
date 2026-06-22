# I AM NOT DONE

import tempfile
import os

# Write "Hello, World!" to a temp file and read it back using with/open
tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
tmp_path = tmp.name
tmp.close()

# Fix: write "Hello, World!" to tmp_path using `with open(...) as f`
# YOUR CODE HERE

# Fix: read the content back using `with open(...) as f`
content = ""  # Fix this

# DON'T EDIT THE TESTS
assert content == "Hello, World!"
os.unlink(tmp_path)
