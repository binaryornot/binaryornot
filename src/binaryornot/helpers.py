"""
binaryornot.helpers
-------------------

Helper utilities used by BinaryOrNot.
"""

import csv
import logging
import math
import os
from importlib.resources import files
from pathlib import Path

from binaryornot.tree import is_binary as _is_binary_by_features

logger = logging.getLogger(__name__)


def _load_binary_signatures() -> tuple[bytes, ...]:
    """Load known binary file signatures from binary_formats.csv."""
    csv_path = files("binaryornot.data").joinpath("binary_formats.csv")
    sigs = []
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            magic_hex = row["magic_hex"].strip()
            if magic_hex:
                sigs.append(bytes.fromhex(magic_hex))
    return tuple(sigs)


_BINARY_SIGNATURES = _load_binary_signatures()


def _has_known_binary_signature(chunk: bytes) -> bool:
    """Check if a byte chunk starts with a known binary file signature."""
    for sig in _BINARY_SIGNATURES:
        if chunk[: len(sig)] == sig:
            return True
    return False


def _load_binary_extensions() -> frozenset[str]:
    """Load known binary file extensions from binary_extensions.csv."""
    csv_path = files("binaryornot.data").joinpath("binary_extensions.csv")
    exts = set()
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            exts.add(row["extension"].strip().lower())
    return frozenset(exts)


BINARY_EXTENSIONS = _load_binary_extensions()


def has_binary_extension(filename: str | bytes | Path) -> bool:
    """Check if a filename has a known binary file extension.

    :param filename: File path to check.
    :returns: True if the extension is in the known binary list.
    """
    # bytes filenames matter for CJK locales (Shift-JIS, GBK, EUC-KR):
    # files created on Windows with a CJK locale produce non-UTF-8 names
    # that os.listdir() returns as bytes on Linux/Docker/WSL.
    if isinstance(filename, bytes):
        filename = os.fsdecode(filename)
    p = Path(filename) if not isinstance(filename, Path) else filename
    ext = p.suffix.lower().lstrip(".")
    return ext in BINARY_EXTENSIONS


def print_as_hex(s: str) -> None:
    """
    Print a string as hex bytes.
    """
    print(":".join(f"{ord(c):x}" for c in s))


CHUNK_SIZE = 512


def get_starting_chunk(filename: str | bytes | Path, length: int = CHUNK_SIZE) -> bytes:
    """
    :param filename: File to open and get the first little chunk of.
    :param length: Number of bytes to read, default 512.
    :returns: Starting chunk of bytes.
    """
    # Ensure we open the file in binary mode
    with open(filename, "rb") as f:
        chunk = f.read(length)
        return chunk


# Bytes considered non-text control characters (excluding \t \n \r)
_CONTROL_BYTES = frozenset(range(0, 32)) - {9, 10, 13}


def _compute_features(chunk: bytes) -> list[float]:
    """Compute features for the binary/text decision tree.

    Feature indices:
      0: null_ratio           - fraction of 0x00 bytes
      1: control_ratio        - fraction of control chars (0x01-0x08, 0x0E-0x1F)
      2: printable_ascii_ratio - fraction of 0x20-0x7E
      3: high_byte_ratio      - fraction of 0x80-0xFF
      4: utf8_valid           - 1.0 if chunk decodes as UTF-8
      5: even_null_ratio      - fraction of even-index bytes that are 0x00
      6: odd_null_ratio       - fraction of odd-index bytes that are 0x00
      7: byte_entropy         - Shannon entropy of byte distribution
      8-12: BOM flags         - UTF-32 LE/BE, UTF-16 LE/BE, UTF-8 BOM
      13: try_utf16le         - 1.0 if chunk decodes as UTF-16-LE
      14: try_utf16be         - 1.0 if chunk decodes as UTF-16-BE
      15: try_utf32le         - 1.0 if chunk decodes as UTF-32-LE
      16: try_utf32be         - 1.0 if chunk decodes as UTF-32-BE
      17: longest_printable_run - longest run of printable chars / length
      18: try_gb2312          - 1.0 if chunk decodes as GB2312
      19: try_big5            - 1.0 if chunk decodes as Big5
      20: try_shift_jis       - 1.0 if chunk decodes as Shift-JIS
      21: try_euc_jp          - 1.0 if chunk decodes as EUC-JP
      22: try_euc_kr          - 1.0 if chunk decodes as EUC-KR
      23: has_magic_signature  - 1.0 if chunk starts with a known binary signature
    """
    n = len(chunk)

    null_count = chunk.count(0)
    control_count = sum(1 for b in chunk if b in _CONTROL_BYTES)
    printable_count = sum(1 for b in chunk if 0x20 <= b <= 0x7E)
    high_count = sum(1 for b in chunk if b >= 0x80)

    null_ratio = null_count / n
    control_ratio = control_count / n
    printable_ascii_ratio = printable_count / n
    high_byte_ratio = high_count / n

    try:
        chunk.decode("utf-8")
        utf8_valid = 1.0
    except (UnicodeDecodeError, ValueError):
        utf8_valid = 0.0

    even_total = (n + 1) // 2
    odd_total = n // 2
    even_nulls = sum(1 for i in range(0, n, 2) if chunk[i] == 0)
    odd_nulls = sum(1 for i in range(1, n, 2) if chunk[i] == 0)
    even_null_ratio = even_nulls / even_total if even_total else 0
    odd_null_ratio = odd_nulls / odd_total if odd_total else 0

    hist = [0] * 256
    for b in chunk:
        hist[b] += 1
    entropy = 0.0
    for count in hist:
        if count > 0:
            p = count / n
            entropy -= p * math.log2(p)

    bom_utf32le = 1.0 if chunk[:4] == b"\xff\xfe\x00\x00" else 0.0
    bom_utf32be = 1.0 if chunk[:4] == b"\x00\x00\xfe\xff" else 0.0
    bom_utf16le = 1.0 if chunk[:2] == b"\xff\xfe" and chunk[:4] != b"\xff\xfe\x00\x00" else 0.0
    bom_utf16be = 1.0 if chunk[:2] == b"\xfe\xff" else 0.0
    bom_utf8 = 1.0 if chunk[:3] == b"\xef\xbb\xbf" else 0.0

    try_utf16le = 0.0
    try_utf16be = 0.0
    try_utf32le = 0.0
    try_utf32be = 0.0
    if n >= 10:
        try:
            chunk.decode("utf-16-le")
            try_utf16le = 1.0
        except (UnicodeDecodeError, ValueError):
            pass
        try:
            chunk.decode("utf-16-be")
            try_utf16be = 1.0
        except (UnicodeDecodeError, ValueError):
            pass
    if n >= 16:
        try:
            chunk.decode("utf-32-le")
            try_utf32le = 1.0
        except (UnicodeDecodeError, ValueError):
            pass
        try:
            chunk.decode("utf-32-be")
            try_utf32be = 1.0
        except (UnicodeDecodeError, ValueError):
            pass

    max_run = 0
    current_run = 0
    for b in chunk:
        if 0x20 <= b <= 0x7E or b in (9, 10, 13):
            current_run += 1
            if current_run > max_run:
                max_run = current_run
        else:
            current_run = 0
    longest_printable_run = max_run / n

    def _try_decode(encoding):
        try:
            chunk.decode(encoding)
            return 1.0
        except (UnicodeDecodeError, ValueError):
            return 0.0

    try_gb2312 = _try_decode("gb2312") if n >= 10 else 0.0
    try_big5 = _try_decode("big5") if n >= 10 else 0.0
    try_shift_jis = _try_decode("shift_jis") if n >= 10 else 0.0
    try_euc_jp = _try_decode("euc-jp") if n >= 10 else 0.0
    try_euc_kr = _try_decode("euc-kr") if n >= 10 else 0.0

    has_magic_signature = 1.0 if _has_known_binary_signature(chunk) else 0.0

    return [
        null_ratio,
        control_ratio,
        printable_ascii_ratio,
        high_byte_ratio,
        utf8_valid,
        even_null_ratio,
        odd_null_ratio,
        entropy,
        bom_utf32le,
        bom_utf32be,
        bom_utf16le,
        bom_utf16be,
        bom_utf8,
        try_utf16le,
        try_utf16be,
        try_utf32le,
        try_utf32be,
        longest_printable_run,
        try_gb2312,
        try_big5,
        try_shift_jis,
        try_euc_jp,
        try_euc_kr,
        has_magic_signature,
    ]


def is_binary_string(bytes_to_check: bytes) -> bool:
    """
    Check if a chunk of bytes appears to be binary or text.

    Uses a trained decision tree on byte statistics including entropy,
    character class ratios, encoding validity checks, and BOM detection.

    :param bytes_to_check: A chunk of bytes to check.
    :returns: True if appears to be a binary, otherwise False.
    """
    if not bytes_to_check:
        return False

    if _has_known_binary_signature(bytes_to_check):
        return True

    features = _compute_features(bytes_to_check)
    result = _is_binary_by_features(features)
    logger.debug(
        "is_binary_string: %r (features=%r)",
        result,
        dict(
            zip(
                [
                    "null",
                    "ctrl",
                    "ascii",
                    "high",
                    "utf8",
                    "even0",
                    "odd0",
                    "entropy",
                    "bom32le",
                    "bom32be",
                    "bom16le",
                    "bom16be",
                    "bom8",
                    "try16le",
                    "try16be",
                    "try32le",
                    "try32be",
                    "run",
                    "gb2312",
                    "big5",
                    "shiftjis",
                    "eucjp",
                    "euckr",
                    "magic",
                ],
                [f"{v:.3f}" for v in features],
                strict=True,
            )
        ),
    )
    return result
