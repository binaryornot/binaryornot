"""Verify that test fixtures are included in the sdist."""

import subprocess
import tarfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestSdistContents(unittest.TestCase):
    def test_sdist_includes_pyc_fixtures(self):
        """The .pyc test fixtures must survive hatchling's sdist build."""
        result = subprocess.run(
            ["uv", "build", "--sdist", "--out-dir", "dist"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

        sdists = sorted(ROOT.glob("dist/*.tar.gz"))
        self.assertTrue(sdists, "No sdist found in dist/")
        sdist_path = sdists[-1]

        with tarfile.open(sdist_path) as tar:
            names = tar.getnames()

        expected = [
            "tests/files/.DS_Store",
            "tests/files/empty.pyc",
            "tests/files/hello_world.pyc",
            "tests/files/troublesome.pyc",
        ]
        for fixture in expected:
            matching = [n for n in names if n.endswith(fixture)]
            self.assertTrue(matching, f"{fixture} not found in sdist")
