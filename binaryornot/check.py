#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import sys

PY3 = sys.version > '3'
if not PY3:
    import codecs


def unicode_open(filename, *args, **kwargs):
    """
    Opens a file as usual on Python 3, and with UTF-8 encoding on Python 2.

    :param filename: Name of file to open.
    """
    if PY3:
        return open(filename, *args, **kwargs)
    kwargs['encoding'] = "utf-8"
    return codecs.open(filename, *args, **kwargs)


def get_starting_chunk(filename):
    """
    :param filename: File to open and get the first little chunk of.
    :returns: Starting chunk of bytes.
    """
    with open(filename, 'r') as f:
        chunk = f.read(1024)
        return chunk

def print_as_hex(s):
    """
    Print a string as hex bytes.
    """

    print(":".join("{0:x}".format(ord(c)) for c in s))


def is_binary_string(bytes_to_check):
    """
    :param bytes: A chunk of bytes to check.
    :returns: True if appears to be a binary, otherwise False.
    """

    # Use file(1)'s choices for what's text and what's not.
    textchars = ''.join(
        map(chr, [7, 8, 9, 10, 12, 13, 27] + range(0x20, 0x100)))
    result = bool(bytes_to_check.translate(None, textchars))        
    return result

def is_binary_alt(filename):
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """

    chunk = get_starting_chunk(filename)
    return is_binary_string(chunk)


def is_binary(filename):
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """

    # PNGs start with bytes that appear to be text
    # See PNG Specification, section 12.11 http://www.w3.org/TR/PNG-Rationale.html
    if filename.endswith('png'):
        return True

    # HACK: Works for now, but it would be nice to improve this
    try:
        chunk = get_starting_chunk(filename)
        if not PY3:
            return is_binary_string(chunk)
    except UnicodeDecodeError:
        return True

