#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_binaryornot
------------------

Tests for `binaryornot` module.
"""

import unittest

from binaryornot.check import is_binary


class TestIsBinary(unittest.TestCase):

    def test_css(self):
        self.assertFalse(is_binary('tests/files/bootstrap-glyphicons.css'))

    def test_json(self):
        self.assertFalse(is_binary('tests/files/cookiecutter.json'))

    def test_png(self):
        self.assertTrue(is_binary('tests/files/logo.png'))

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


if __name__ == '__main__':
    unittest.main()
