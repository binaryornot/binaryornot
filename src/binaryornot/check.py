"""
binaryornot.check
-----------------

Main code for checking if a file is binary or text.
"""

import argparse
import logging
from pathlib import Path

from binaryornot.helpers import get_starting_chunk, has_binary_extension, is_binary_string

logger = logging.getLogger(__name__)


def is_binary(filename: str | bytes | Path, *, check_extensions: bool = True) -> bool:
    """
    :param filename: File to check.
    :param check_extensions: If True (default), check the file extension
        against a list of known binary types before reading the file.
        Set to False to classify purely by file contents.
    :returns: True if it's a binary file, otherwise False.
    """
    logger.debug("is_binary: %(filename)r", locals())

    if check_extensions and has_binary_extension(filename):
        logger.debug("is_binary: True (matched binary extension)")
        return True

    # Check if the starting chunk is a binary string
    chunk = get_starting_chunk(filename)
    return is_binary_string(chunk)


def main() -> None:
    parser = argparse.ArgumentParser(description="Check if a file passed as argument is binary or not")

    parser.add_argument(
        "filename", help="File name to check for. If the file is not in the same folder, include full path"
    )

    args = parser.parse_args()

    print(is_binary(**vars(args)))


if __name__ == "__main__":
    main()
