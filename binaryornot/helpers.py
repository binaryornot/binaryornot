#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import six

if six.PY2:
    import codecs


def unicode_open(filename, *args, **kwargs):
    """
    Opens a file as usual on Python 3, and with UTF-8 encoding on Python 2.

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
