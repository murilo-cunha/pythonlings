import subprocess
import sys


def test_multi_line_docstring_style():
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--select", "D205,D212", "--no-cache", "docstrings5.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
