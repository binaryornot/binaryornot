#!/usr/bin/env python

"""
test_binaryornot
------------------

Tests for `binaryornot` module.
"""

import logging
import os
import unittest
from contextlib import contextmanager
from pathlib import Path
from tempfile import mkstemp

from hypothesis import given
from hypothesis.strategies import binary

from binaryornot.check import is_binary

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)


class TestIsBinary(unittest.TestCase):
    """Test is_binary() with various files."""

    def test_empty(self):
        self.assertFalse(is_binary("tests/files/empty.txt"))

    def test_triggers_decoding_error(self):
        self.assertTrue(is_binary("tests/files/decoding-error"))

    def test_triggers_lookup_error(self):
        self.assertTrue(is_binary("tests/files/lookup-error"))

    def test_ds_store(self):
        self.assertTrue(is_binary("tests/files/.DS_Store"))

    def test_txt(self):
        self.assertFalse(is_binary("tests/files/robots.txt"))

    def test_txt_unicode(self):
        self.assertFalse(is_binary("tests/files/unicode.txt"))

    def test_binary_pdf2(self):
        self.assertTrue(is_binary("tests/isBinaryFile/pdf.pdf"))

    def test_text_russian2(self):
        self.assertFalse(is_binary("tests/isBinaryFile/russian_file.rst"))

    def test_binary_exe2(self):
        self.assertTrue(is_binary("tests/isBinaryFile/grep"))

    def test_negative_binary(self):
        # A text file named .pyc is detected as binary by extension.
        # With check_extensions=False, content detection classifies it as text.
        self.assertTrue(is_binary("tests/isBinaryFile/this_is_not_a_bin.pyc"))
        self.assertFalse(is_binary("tests/isBinaryFile/this_is_not_a_bin.pyc", check_extensions=False))

    def test_binary_sqlite(self):
        self.assertTrue(is_binary("tests/isBinaryFile/test.sqlite"))

    def test_binary_png_issue_642(self):
        self.assertTrue(is_binary("tests/files/issue-642.png"))


class TestFontFiles(unittest.TestCase):
    """Test is_binary() with various font file types."""

    def test_eot(self):
        self.assertTrue(is_binary("tests/files/glyphiconshalflings-regular.eot"))

    def test_otf(self):
        self.assertTrue(is_binary("tests/files/glyphiconshalflings-regular.otf"))

    def test_ttf(self):
        self.assertTrue(is_binary("tests/files/glyphiconshalflings-regular.ttf"))

    def test_woff(self):
        self.assertTrue(is_binary("tests/files/glyphiconshalflings-regular.woff"))


class TestImageFiles(unittest.TestCase):
    """Test is_binary() with various image file types."""

    def test_png(self):
        self.assertTrue(is_binary("tests/files/logo.png"))

    def test_gif(self):
        self.assertTrue(is_binary("tests/files/lena.gif"))

    def test_jpg(self):
        self.assertTrue(is_binary("tests/files/lena.jpg"))

    def test_tiff(self):
        self.assertTrue(is_binary("tests/files/palette-1c-8b.tiff"))

    def test_bmp(self):
        self.assertTrue(is_binary("tests/files/rgb-3c-8b.bmp"))

    def test_binary_rgb_stream(self):
        self.assertTrue(is_binary("tests/files/pixelstream.rgb"))

    def test_binary_gif2(self):
        # Empty file named .gif: extension check says binary, content check says text.
        self.assertTrue(is_binary("tests/isBinaryFile/null_file.gif"))
        self.assertFalse(is_binary("tests/isBinaryFile/null_file.gif", check_extensions=False))

    def test_binary_gif3(self):
        self.assertTrue(is_binary("tests/isBinaryFile/trunks.gif"))

    def test_svg(self):
        self.assertFalse(is_binary("tests/files/glyphiconshalflings-regular.svg"))


class TestEncodings(unittest.TestCase):
    """Test is_binary() with files containing various encodings."""

    def test_text_utf16(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/bom_utf-16.txt"))

    def test_text_utf16le(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/bom_utf-16le.txt"))

    def test_text_utf16be(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/test-utf16be.txt"))

    def test_text_utf32le(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/bom_utf-32le.txt"))

    def test_text_utf82(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/utf_8.txt"))

    def test_text_gb2(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/test-gb2.txt"))

    def test_text_kr(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/test-kr.txt"))

    def test_text_latin(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/test-latin.txt"))

    def test_text_big5(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/big5.txt"))

    def test_text_gb(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/test-gb.txt"))

    def test_text_utf32(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/bom_utf-32.txt"))

    def test_text_utf8(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/bom_utf-8.txt"))

    def test_text_big5b(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/big5_B.txt"))

    def test_text_shishi(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/test-shishi.txt"))

    def test_text_utfcn(self):
        self.assertFalse(is_binary("tests/isBinaryFile/encodings/utf8cn.txt"))


class TestCodeFiles(unittest.TestCase):
    """Test is_binary() with various code file types."""

    def test_css(self):
        self.assertFalse(is_binary("tests/files/bootstrap-glyphicons.css"))

    def test_json(self):
        self.assertFalse(is_binary("tests/files/cookiecutter.json"))

    def test_text_perl2(self):
        self.assertFalse(is_binary("tests/isBinaryFile/perl_script"))

    def test_text_js(self):
        self.assertFalse(is_binary("tests/isBinaryFile/index.js"))

    def test_text_lua(self):
        self.assertFalse(is_binary("tests/isBinaryFile/no.lua"))


class TestProgrammingArtifacts(unittest.TestCase):
    """Test is_binary() with various leftover byproducts from running or
    building programs."""

    def test_binary_pyc(self):
        self.assertTrue(is_binary("tests/files/hello_world.pyc"))

    def test_binary_empty_pyc(self):
        self.assertTrue(is_binary("tests/files/empty.pyc"))

    def test_binary_troublesome_pyc(self):
        self.assertTrue(is_binary("tests/files/troublesome.pyc"))


@contextmanager
def bytes_in_file(data):
    o, f = mkstemp()
    try:
        os.write(o, data)
        os.close(o)
        yield f
    finally:
        os.unlink(f)


class TestErrorHandling(unittest.TestCase):
    """Test is_binary() error behavior."""

    def test_nonexistent_file_raises(self):
        with self.assertRaises(OSError):
            is_binary("tests/files/this_file_does_not_exist.txt")

    def test_unreadable_file_raises(self):
        _, path = mkstemp()
        try:
            os.chmod(path, 0o000)
            with self.assertRaises(OSError):
                is_binary(path)
        finally:
            os.chmod(path, 0o600)
            os.unlink(path)


class TestMagicBytesGuard(unittest.TestCase):
    """Test that known binary file signatures bypass the decision tree."""

    def test_png_signature_with_adversarial_content(self):
        from binaryornot.helpers import is_binary_string

        # First 128 bytes of issue-642.png — the tree misclassifies this as text
        chunk = (
            b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x00"
            b"\x00\x00\x02\x00\x08\x04\x00\x00\x00^q\x1cq\x00\x00"
            b"\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00"
            b"\x00 cHRM\x00\x00z&\x00\x00\x80\x84\x00\x00\xfa\x00"
            b"\x00\x00\x80\xe8\x00\x00u0\x00\x00\xea`\x00\x00:\x98"
            b"\x00\x00\x17p\x9c\xbaQ<\x00\x00\x00\x02bKGD\x00\xff"
            b"\x87\x8f\xcc\xbf\x00\x00\x00\x07tIME\x07\xe4\x07\x0e"
            b"\x0b\x07\t)6\x99\x95\x00\x00"
        )
        self.assertTrue(is_binary_string(chunk))

    def test_plain_text_not_caught(self):
        from binaryornot.helpers import is_binary_string

        chunk = b"Hello, world! This is a plain text file with enough content.\n" * 2
        self.assertFalse(is_binary_string(chunk[:128]))


class TestFeatureVector(unittest.TestCase):
    """Test that the feature vector includes all expected features."""

    def test_feature_count_includes_magic_signature(self):
        from binaryornot.helpers import _compute_features

        chunk = b"\x89PNG\r\n\x1a\n" + b"\x00" * 504
        features = _compute_features(chunk)
        self.assertEqual(len(features), 24)

    def test_magic_signature_feature_set_for_png(self):
        from binaryornot.helpers import _compute_features

        chunk = b"\x89PNG\r\n\x1a\n" + b"\x00" * 504
        features = _compute_features(chunk)
        self.assertEqual(features[23], 1.0)

    def test_magic_signature_feature_unset_for_text(self):
        from binaryornot.helpers import _compute_features

        chunk = b"Hello, world! This is plain text." * 16
        features = _compute_features(chunk[:512])
        self.assertEqual(features[23], 0.0)


class TestExtensionCheck(unittest.TestCase):
    """Test that known binary extensions are detected without reading the file."""

    def test_pyc_detected_by_extension(self):
        """A .pyc file is detected as binary by its extension."""
        with bytes_in_file(b"This is plain text content, not real bytecode.") as f:
            # Rename to .pyc
            pyc_path = f + ".pyc"
            os.rename(f, pyc_path)
            try:
                self.assertTrue(is_binary(pyc_path))
            finally:
                os.rename(pyc_path, f)

    def test_png_detected_by_extension(self):
        """A .png file is detected as binary by its extension."""
        with bytes_in_file(b"Not actually a PNG, just text.") as f:
            png_path = f + ".png"
            os.rename(f, png_path)
            try:
                self.assertTrue(is_binary(png_path))
            finally:
                os.rename(png_path, f)

    def test_extension_check_disabled(self):
        """With check_extensions=False, a text file with a binary extension is classified by content."""
        with bytes_in_file(b"This is plain text content, not real bytecode.\n" * 5) as f:
            pyc_path = f + ".pyc"
            os.rename(f, pyc_path)
            try:
                self.assertFalse(is_binary(pyc_path, check_extensions=False))
            finally:
                os.rename(pyc_path, f)

    def test_text_extensions_not_affected(self):
        """Text file extensions like .txt and .py are not in the binary list."""
        self.assertFalse(is_binary("tests/files/robots.txt"))
        self.assertFalse(is_binary("tests/isBinaryFile/index.js"))

    def test_no_extension_falls_through(self):
        """Files without extensions fall through to content detection."""
        self.assertTrue(is_binary("tests/isBinaryFile/grep"))

    def test_pathlib_path_works(self):
        """Extension check works with pathlib.Path objects."""
        self.assertTrue(is_binary(Path("tests/files/logo.png")))

    def test_extension_case_insensitive(self):
        """Extension check is case-insensitive (.PNG == .png)."""
        with bytes_in_file(b"Not actually a PNG.") as f:
            upper_path = f + ".PNG"
            os.rename(f, upper_path)
            try:
                self.assertTrue(is_binary(upper_path))
            finally:
                os.rename(upper_path, f)


class TestDetectionProperties(unittest.TestCase):
    @given(binary(max_size=512))
    def test_never_crashes(self, data):
        with bytes_in_file(data) as f:
            is_binary(f)


if __name__ == "__main__":
    unittest.main()
