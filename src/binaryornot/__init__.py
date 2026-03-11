"""BinaryOrNot: ultra-lightweight pure Python package to check if a file is binary or text."""


class NotARegularFileError(OSError):
    """Raised when a path points to a non-regular file (FIFO, socket, device node)."""
