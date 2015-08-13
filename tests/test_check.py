#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_binaryornot
------------------

Tests for `binaryornot` module.
"""

import logging
import unittest

from binaryornot.check import is_binary
from unittest.case import expectedFailure

#logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)


class TestIsBinary(unittest.TestCase):

    def test_empty(self):
        self.assertFalse(is_binary('tests/files/empty.txt'))

    def test_css(self):
        self.assertFalse(is_binary('tests/files/bootstrap-glyphicons.css'))

    def test_json(self):
        self.assertFalse(is_binary('tests/files/cookiecutter.json'))

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

    # @expectedFailure
    def test_ds_store(self):
        self.assertTrue(is_binary('tests/files/.DS_Store'))

    def test_eot(self):
        self.assertTrue(
            is_binary('tests/files/glyphiconshalflings-regular.eot'))

    def test_otf(self):
        self.assertTrue(
            is_binary('tests/files/glyphiconshalflings-regular.otf'))

    def test_svg(self):
        self.assertFalse(
            is_binary('tests/files/glyphiconshalflings-regular.svg'))

    def test_ttf(self):
        self.assertTrue(
            is_binary('tests/files/glyphiconshalflings-regular.ttf'))

    def test_woff(self):
        self.assertTrue(
            is_binary('tests/files/glyphiconshalflings-regular.woff'))

    def test_txt(self):
        self.assertFalse(is_binary('tests/files/robots.txt'))

    def test_txt_unicode(self):
        self.assertFalse(is_binary('tests/files/unicode.txt'))

    def test_is_binary_js(self):
        self.assertFalse(is_binary('tests/isBinaryFile/index.js'))

    def test_is_binary_gif2(self):
        self.assertFalse(is_binary('tests/isBinaryFile/null_file.gif'))

    def test_is_binary_gif3(self):
        self.assertTrue(is_binary('tests/isBinaryFile/trunks.gif'))

    def test_is_binary_lua(self):
        self.assertFalse(is_binary('tests/isBinaryFile/no.lua'))

    @expectedFailure
    def test_is_binary_pdf2(self):
        self.assertTrue(is_binary('tests/isBinaryFile/pdf.pdf'))

    def test_is_binary_perl2(self):
        self.assertFalse(is_binary('tests/isBinaryFile/perl_script'))

    def test_is_binary_russian2(self):
        self.assertFalse(is_binary('tests/isBinaryFile/russian_file.rst'))

    def test_is_binary_exe2(self):
        self.assertTrue(is_binary('tests/isBinaryFile/grep'))

    def test_is_binary_utf16(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/bom_utf-16.txt'))

    def test_is_binary_utf16le(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/bom_utf-16le.txt'))

    def test_is_binary_utf16be(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/test-utf16be.txt'))

    def test_is_binary_utf32le(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/bom_utf-32le.txt'))

    def test_is_binary_utf82(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/utf_8.txt'))

    def test_is_binary_gb2(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/test-gb2.txt'))

    def test_is_binary_kr(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/test-kr.txt'))

    def test_is_binary_latin(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/test-latin.txt'))

    def test_is_binary_big5(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/big5.txt'))

    def test_is_binary_gb(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/test-gb.txt'))

    def test_is_binary_utf32(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/bom_utf-32.txt'))

    def test_is_binary_utf8(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/bom_utf-8.txt'))

    def test_is_binary_big5b(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/big5_B.txt'))

    def test_is_binary_shishi(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/test-shishi.txt'))

    def test_is_binary_utfcn(self):
        self.assertFalse(is_binary('tests/isBinaryFile/encodings/utf8cn.txt'))

    def test_is_binary_rgb_stream(self):
        self.assertTrue(is_binary('tests/files/pixelstream.rgb'))


if __name__ == '__main__':
    unittest.main()
