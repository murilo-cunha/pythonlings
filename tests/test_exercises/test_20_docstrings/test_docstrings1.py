import subprocess
import sys


def test_function_has_docstring():
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--select", "D103", "--no-cache", "docstrings1.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
