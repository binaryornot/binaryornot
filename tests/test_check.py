#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_binaryornot
------------------

Tests for `binaryornot` module.
"""

import logging
try:
    from unittest.case import expectedFailure
    import unittest
except ImportError:
    from unittest2.case import expectedFailure
    import unittest2 as unittest

import os
from contextlib import contextmanager
from tempfile import mkstemp

from hypothesis import given
from hypothesis.strategies import binary

from binaryornot.check import is_binary


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


class TestIsBinary(unittest.TestCase):
    """Test is_binary() with various files."""

    def test_empty(self):
        self.assertFalse(is_binary('tests/files/empty.txt'))

    def test_triggers_decoding_error(self):
        self.assertTrue(is_binary('tests/files/decoding-error'))

    def test_triggers_lookup_error(self):
        self.assertTrue(is_binary('tests/files/lookup-error'))

    def test_ds_store(self):
        self.assertTrue(is_binary('tests/files/.DS_Store'))

    def test_txt(self):
        self.assertFalse(is_binary('tests/files/robots.txt'))

    def test_txt_unicode(self):
        self.assertFalse(is_binary('tests/files/unicode.txt'))

    @expectedFailure
    def test_binary_pdf2(self):
        self.assertTrue(is_binary('tests/isBinaryFile/pdf.pdf'))

    def test_text_russian2(self):
        self.assertFalse(is_binary('tests/isBinaryFile/russian_file.rst'))

    def test_binary_exe2(self):
        self.assertTrue(is_binary('tests/isBinaryFile/grep'))


class TestFontFiles(unittest.TestCase):
    """Test is_binary() with various font file types."""

    def test_eot(self):
        self.assertTrue(
            is_binary('tests/files/glyphiconshalflings-regular.eot'))

    def test_otf(self):
        self.assertTrue(
            is_binary('tests/files/glyphiconshalflings-regular.otf'))

    def test_ttf(self):
        self.assertTrue(
            is_binary('tests/files/glyphiconshalflings-regular.ttf'))

    def test_woff(self):
        self.assertTrue(
            is_binary('tests/files/glyphiconshalflings-regular.woff'))


class TestImageFiles(unittest.TestCase):
    """Test is_binary() with various image file types."""

    def test_png(self):
        self.assertTrue(is_binary('tests/files/logo.png'))

    def test_gif(self):
        self.assertTrue(is_binary('tests/files/lena.gif'))

    def test_jpg(self):
        self.assertTrue(is_binary('tests/files/lena.jpg'))

    def test_tiff(self):
        self.assertTrue(is_binary('tests/files/palette-1c-8b.tiff'))

    def test_bmp(self):
        self.assertTrue(is_binary('tests/files/rgb-3c-8b.bmp'))

    def test_binary_rgb_stream(self):
        self.assertTrue(is_binary('tests/files/pixelstream.rgb'))

    def test_binary_gif2(self):
        self.assertFalse(is_binary('tests/isBinaryFile/null_file.gif'))

    def test_binary_gif3(self):
        self.assertTrue(is_binary('tests/isBinaryFile/trunks.gif'))

    def test_svg(self):
        self.assertFalse(
            is_binary('tests/files/glyphiconshalflings-regular.svg'))


class TestEncodings(unittest.TestCase):
    """Test is_binary() with files containing various encodings."""

    def test_text_utf16(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/bom_utf-16.txt'))

    def test_text_utf16le(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/bom_utf-16le.txt'))

    def test_text_utf16be(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/test-utf16be.txt'))

    def test_text_utf32le(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/bom_utf-32le.txt'))

    def test_text_utf82(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/utf_8.txt'))

    def test_text_gb2(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/test-gb2.txt'))

    def test_text_kr(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/test-kr.txt'))

    def test_text_latin(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/test-latin.txt'))

    def test_text_big5(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/big5.txt'))

    def test_text_gb(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/test-gb.txt'))

    def test_text_utf32(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/bom_utf-32.txt'))

    def test_text_utf8(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/bom_utf-8.txt'))

    def test_text_big5b(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/big5_B.txt'))

    def test_text_shishi(self):
        self.assertFalse(
            is_binary('tests/isBinaryFile/encodings/test-shishi.txt'))

    def test_text_utfcn(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/utf8cn.txt'))


class TestCodeFiles(unittest.TestCase):
    """Test is_binary() with various code file types."""

    def test_css(self):
        self.assertFalse(is_binary('tests/files/bootstrap-glyphicons.css'))

    def test_json(self):
        self.assertFalse(is_binary('tests/files/cookiecutter.json'))

    def test_text_perl2(self):
        self.assertFalse(is_binary('tests/isBinaryFile/perl_script'))

    def test_text_js(self):
        self.assertFalse(is_binary('tests/isBinaryFile/index.js'))

    def test_text_lua(self):
        self.assertFalse(is_binary('tests/isBinaryFile/no.lua'))


class TestProgrammingArtifacts(unittest.TestCase):
    """Test is_binary() with various leftover byproducts from running or
    building programs."""

    def test_binary_pyc(self):
        self.assertTrue(is_binary('tests/files/hello_world.pyc'))

    def test_binary_empty_pyc(self):
        self.assertTrue(is_binary('tests/files/empty.pyc'))

    def test_binary_troublesome_pyc(self):
        self.assertTrue(is_binary('tests/files/troublesome.pyc'))


@contextmanager
def bytes_in_file(data):
    o, f = mkstemp()
    try:
        os.write(o, data)
        os.close(o)
        yield f
    finally:
        os.unlink(f)


class TestDetectionProperties(unittest.TestCase):
    @given(binary(average_size=512))
    def test_never_crashes(self, data):
        with bytes_in_file(data) as f:
            is_binary(f)


if __name__ == '__main__':
    unittest.main()
