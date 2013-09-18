#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import six
import sys

if six.PY2:
    import codecs


class FileNotReadableAsText(Exception):
    """
    The opened file could not be read as a text file.
    """


def unicode_open(filename, *args, **kwargs):
    """
    Opens a file as usual on Python 3, and with UTF-8 encoding on Python 2.

    :param filename: Name of file to open.
    """
    kwargs['encoding'] = "utf-8"
    if six.PY3:
        return open(filename, *args, **kwargs)
    return codecs.open(filename, *args, **kwargs)


def get_starting_chunk(filename):
    """
    :param filename: File to open and get the first little chunk of.
    :returns: Starting chunk of bytes.
    """
    try:
        with unicode_open(filename, 'r') as f:
            chunk = f.read(1024)
            return chunk
    except UnicodeDecodeError as e:
        logging.debug("get_starting_chunk() couldn't read the file")
        logging.debug(e)
        raise FileNotReadableAsText


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

    text_ascii_codes = range(32, 256)
    textchars = b''.join([six.int2byte(i) for i in text_ascii_codes]) + b'\n\r\t\f\b'

    if six.PY2:
        # Remove the non-text chars from the bytes
        nontext = bytes_to_check.translate(None, textchars)
        logging.debug("nontext:")
        logging.debug(nontext)
        # Binary if non-text chars are > 30% of the string
        nontext_ratio = len(nontext) // len(bytes_to_check)
        logging.debug(nontext_ratio)
        return nontext_ratio > 0.3

    if six.PY3:
        # Count the text chars
        textchar_count = sum([bytes(c, "utf-8") in textchars for c in bytes_to_check])
        logging.debug("textchar_count:")
        logging.debug(textchar_count)
        logging.debug("bytes_to_check:")
        logging.debug(bytes_to_check)
        logging.debug("len(bytes_to_check):")
        logging.debug(len(bytes_to_check))
        # Binary if text chars are <= 30% of the string
        text_ratio = textchar_count / len(bytes_to_check)
        logging.debug(text_ratio)
        return text_ratio <= 0.3


def is_binary(filename):
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """

    # PNGs start with bytes that appear to be text
    # See PNG Specification, section 12.11 http://www.w3.org/TR/PNG-Rationale.html
    if filename.endswith('png'):
        return True

    try:
        chunk = get_starting_chunk(filename)
        return is_binary_string(chunk)
    except FileNotReadableAsText:
        return True

