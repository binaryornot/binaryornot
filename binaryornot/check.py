#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_starting_chunk(filename):
    with(filename, 'r') as f:
        chunk = open(filename).read(1024)
        return chunk


def is_binary_string(bytes_to_check):
    """
    :param bytes: A chunk of bytes to check.
    :returns: True if appears to be a binary, otherwise False.
    """
    
    textchars = ''.join(map(chr, [7,8,9,10,12,13,27] + range(0x20, 0x100)))
    result = bytes_to_check.translate(None, textchars)
    return bool(result)


def is_binary(filename):
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """
    
    chunk = get_starting_chunk(filename)
    return is_binary_string(chunk)
