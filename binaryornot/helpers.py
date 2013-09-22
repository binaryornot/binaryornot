#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
binaryornot.helpers
-------------------

Helper utilities used by BinaryOrNot.
"""

from __future__ import unicode_literals

import six

if six.PY2:
    import codecs


class FileNotReadableAsText(Exception):

    """
    The opened file could not be read as a text file.
    """


def unicode_open(filename, *args, **kwargs):
    """
    Opens a file with UTF-8 encoding, in a Python 2- and 3-compatible way.

    :param filename: Name of file to open.
    :param *args: Optional args to be passed on to `open()`.
    :param **kwargs: Optional kwargs to be passed on to `open()`.
    """

    kwargs['encoding'] = "utf-8"
    if six.PY3:
        return open(filename, *args, **kwargs)
    return codecs.open(filename, *args, **kwargs)


def print_as_hex(s):
    """
    Print a string as hex bytes.
    """

    print(":".join("{0:x}".format(ord(c)) for c in s))


def get_starting_chunk(filename):
    """
    :param filename: File to open and get the first little chunk of.
    :returns: Starting chunk of bytes.
    """
    try:
        with unicode_open(filename, 'r') as f:
            chunk = f.read(1024)
            return chunk
    except UnicodeDecodeError:
        raise FileNotReadableAsText


def is_binary_string(bytes_to_check):
    """
    :param bytes: A chunk of bytes to check.
    :returns: True if appears to be a binary, otherwise False.
    """

    text_ascii_codes = range(32, 256)
    textchars = b''.join([six.int2byte(i)
                         for i in text_ascii_codes]) + b'\n\r\t\f\b'

    # Create a translation table
    delete_chars = dict.fromkeys(bytearray(textchars))

    # Remove the non-text chars from the bytes
    nontext = bytes_to_check.translate(delete_chars)

    # Binary if non-text chars are > 30% of the string
    nontext_ratio = float(len(nontext)) / float(len(bytes_to_check))
    return nontext_ratio > 0.3
