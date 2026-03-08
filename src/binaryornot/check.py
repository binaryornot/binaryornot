"""
binaryornot.check
-----------------

Main code for checking if a file is binary or text.
"""

import argparse
import logging
from pathlib import Path

from binaryornot.helpers import get_starting_chunk, is_binary_string

logger = logging.getLogger(__name__)


def is_binary(filename: str | bytes | Path) -> bool:
    """
    :param filename: File to check.
    :returns: True if it's a binary file, otherwise False.
    """
    logger.debug("is_binary: %(filename)r", locals())

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
