#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
binaryornot.check
-----------------

Main code for checking if a file is binary or text.
"""

from __future__ import unicode_literals
import six

from .helpers import get_starting_chunk, is_binary_string, FileNotReadableAsText


def is_binary(filename):
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """

    try:
        chunk = get_starting_chunk(filename)
        return is_binary_string(chunk)
    except FileNotReadableAsText:
        return True
