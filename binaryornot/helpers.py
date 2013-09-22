#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

def print_as_hex(s):
    """
    Print a string as colon separated hex sequences.
    """
    print(":".join("{0:x}".format(ord(c)) for c in s))
