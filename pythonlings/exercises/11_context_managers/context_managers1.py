"""
The with statement ensures a resource is properly closed after use, even if
an exception occurs. open() returns a context manager that closes the file
on __exit__. Pattern: with open(path, "w") as f: f.write("...")

Write "Hello, World!" to tmp_path using with/open, then read it back.
"""

# I AM NOT DONE

import tempfile
import os

tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
tmp_path = tmp.name
tmp.close()

content = ""
