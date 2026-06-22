# I AM NOT DONE

from pathlib import Path
import tempfile

# Work with a temporary directory
tmp_dir = Path(tempfile.mkdtemp())

# Fix: create a subdirectory called "data" inside tmp_dir using the / operator
# then call .mkdir() to create it on disk
data_dir = tmp_dir  # Fix: use / operator and .mkdir()

# Fix: create a file "hello.txt" inside data_dir with content "Hello, pathlib!"
hello_file = data_dir / "hello.txt"
# Fix: write "Hello, pathlib!" to hello_file using .write_text()

# DON'T EDIT THE TESTS
assert data_dir.is_dir()
assert hello_file.exists()
assert hello_file.read_text() == "Hello, pathlib!"
assert hello_file.suffix == ".txt"
assert hello_file.stem == "hello"

# Cleanup
import shutil
shutil.rmtree(tmp_dir)
