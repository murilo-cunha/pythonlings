import subprocess
import sys


def test_class_and_method_have_docstrings():
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--select", "D101,D102", "--no-cache", "docstrings2.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
