import subprocess
import sys


def test_one_line_docstring_style():
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--select", "D200,D210,D400", "--no-cache", "docstrings4.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
