"""
binaryornot.helpers
-------------------

Helper utilities used by BinaryOrNot.
"""

import logging
import math
from pathlib import Path
from string.templatelib import Template

from binaryornot.tree import is_binary as _is_binary_by_features

logger = logging.getLogger(__name__)

type FeatureVector = list[float]


def _render_features(template: Template) -> str:
    """Render a template string of feature values as name=value pairs."""
    parts = []
    for interpolation in template.interpolations:
        parts.append(f"{interpolation.expression}={interpolation.value:.3f}")
    return ", ".join(parts)


def print_as_hex(s: str) -> None:
    """
    Print a string as hex bytes.
    """
    print(":".join(f"{ord(c):x}" for c in s))


def get_starting_chunk(filename: str | bytes | Path, length: int = 128) -> bytes:
    """
    :param filename: File to open and get the first little chunk of.
    :param length: Number of bytes to read, default 128.
    :returns: Starting chunk of bytes.
    """
    with open(filename, "rb") as f:
        chunk = f.read(length)
        return chunk


# Bytes considered non-text control characters (excluding \t \n \r)
_CONTROL_BYTES = frozenset(range(0, 32)) - {9, 10, 13}


def _compute_features(chunk: bytes) -> FeatureVector:
    """Compute 23 features from a byte chunk for the binary/text decision tree."""
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

    def _try_decode(encoding: str) -> float:
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

    features = _compute_features(bytes_to_check)
    [
        null, ctrl, ascii_, high, utf8, even0, odd0, entropy,
        bom32le, bom32be, bom16le, bom16be, bom8,
        try16le, try16be, try32le, try32be,
        run, gb2312, big5, shiftjis, eucjp, euckr,
    ] = features
    result = _is_binary_by_features(features)
    logger.debug(
        "is_binary_string: %r (%s)",
        result,
        _render_features(
            t"{null} {ctrl} {ascii_} {high} {utf8} {even0} {odd0} {entropy} "
            t"{bom32le} {bom32be} {bom16le} {bom16be} {bom8} "
            t"{try16le} {try16be} {try32le} {try32be} "
            t"{run} {gb2312} {big5} {shiftjis} {eucjp} {euckr}"
        ),
    )
    return result
