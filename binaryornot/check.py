# -*- coding: utf-8 -*-

"""
binaryornot.check
-----------------

Main code for checking if a file is binary or text.
"""

import logging

from .helpers import get_starting_chunk, is_binary_string


logger = logging.getLogger(__name__)


def is_binary(filename):
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """
    logger.debug('is_binary: %(filename)r' % locals())
    chunk = get_starting_chunk(filename)
    return is_binary_string(chunk)
