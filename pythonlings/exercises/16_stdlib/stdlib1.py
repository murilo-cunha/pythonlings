"""
pathlib.Path provides an object-oriented interface to filesystem paths.
Use / to join paths: base / "sub" / "file.txt". Key methods: .mkdir(),
.read_text(), .write_text(), .exists(), .is_dir(), .suffix, .stem.

Create data_dir inside tmp_dir using /, then write "Hello, pathlib!" to hello.txt.
"""

# I AM NOT DONE

from pathlib import Path
import tempfile

tmp_dir = Path(tempfile.mkdtemp())

data_dir = tmp_dir
hello_file = data_dir / "hello.txt"
