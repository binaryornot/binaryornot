# -*- coding: utf-8 -*-

"""
binaryornot.check
-----------------

Main code for checking if a file is binary or text.
"""

import logging
import argparse

from binaryornot.helpers import get_starting_chunk, is_binary_string


logger = logging.getLogger(__name__)


def is_binary(filename):
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """
    logger.debug('is_binary: %(filename)r', locals())
    # Check if the file extension is in a list of known binary types
#     binary_extensions = ['.pyc', ]
#     for ext in binary_extensions:
#         if filename.endswith(ext):
#             return True

    # Check if the starting chunk is a binary string
    chunk = get_starting_chunk(filename)
    return is_binary_string(chunk)

def file_type(filename):
    chunk = get_starting_chunk(filename)
    image_data = chunk
    header_byte = image_data[0:3].hex().lower()
    types = {'474946': 'image/gif', '89504e': 'image/png', 'ffd8ff': 'image/jpeg',
             '667479':' video/mp4', '494433':'audio/mp3', '4d4d00': 'tiff', '424d00':' bmp',
             '01da01': 'rgb', 'd0cf11':'file/doc', '255044':'filepdf', '53514c':'file/db'}
    return types.get(header_byte, "Binary file")


def main():
    parser = argparse.ArgumentParser(description="Check if a "
                                                 "file passed as argument is "
                                                 "binary or not")

    parser.add_argument("filename", help="File name to check for. If "
                                         "the file is not in the same folder, "
                                         "include full path")

    args = parser.parse_args()

    print(is_binary(**vars(args)))


if __name__ == "__main__":
    main()
