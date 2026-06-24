import subprocess
import sys


def test_module_has_docstring():
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "--select", "D100", "--no-cache", "docstrings3.py"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
