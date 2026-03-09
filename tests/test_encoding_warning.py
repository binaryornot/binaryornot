"""Verify that binaryornot does not trigger EncodingWarning.

Python 3.10+ emits EncodingWarning when open() is called without an
explicit encoding argument, if -X warn_default_encoding is active.
CI environments that treat warnings as errors would crash on import.
"""

import subprocess
import sys


def test_no_encoding_warning_on_import():
    """Importing binaryornot with warn_default_encoding raises no warnings."""
    result = subprocess.run(
        [
            sys.executable,
            "-X",
            "warn_default_encoding",
            "-W",
            "error::EncodingWarning",
            "-c",
            "import binaryornot.check",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"EncodingWarning triggered on import:\n{result.stderr}"


def test_no_encoding_warning_in_tests():
    """Running the test suite with warn_default_encoding raises no warnings."""
    result = subprocess.run(
        [
            sys.executable,
            "-X",
            "warn_default_encoding",
            "-m",
            "pytest",
            "tests/test_encoding_coverage.py",
            "-W",
            "error::EncodingWarning",
            "-q",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"EncodingWarning triggered in test suite:\n{result.stderr}"
