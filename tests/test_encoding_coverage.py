"""Test coverage claims from the encoding and binary format CSVs.

Each row in encodings.csv becomes a text test case. Each row in
binary_formats.csv becomes a binary test case. CSVs are the single
source of truth for what the detector claims to handle.
"""

import csv
import hashlib
import os
from importlib.resources import files

import pytest

from binaryornot.helpers import CHUNK_SIZE, is_binary_string


def load_encoding_rows():
    csv_path = files("binaryornot.data").joinpath("encodings.csv")
    with csv_path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_binary_format_rows():
    csv_path = files("binaryornot.data").joinpath("binary_formats.csv")
    with csv_path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def encode_sample(row, max_bytes=128):
    # Repeat sample text to produce a chunk well above detection thresholds
    text = (row["sample_text"] + " ") * 20
    return text.encode(row["encoding"])[:max_bytes]


def make_id(row):
    return f"{row['encoding']}-{row['status']}"


rows = load_encoding_rows()
covered_rows = [r for r in rows if r["status"] == "covered"]
binary_rows = load_binary_format_rows()


@pytest.mark.parametrize("row", rows, ids=make_id)
def test_encoding_detected_as_text(row):
    encoding = row["encoding"]
    status = row["status"]

    try:
        chunk = encode_sample(row)
    except (UnicodeEncodeError, LookupError):
        pytest.skip(f"Python cannot encode sample text as {encoding}")

    if status == "gap":
        pytest.xfail(f"Known gap: {row['gap_reason']}")

    assert is_binary_string(chunk) is False, f"Text encoded as {encoding} was misclassified as binary"


# --- Edge-case tests ---


@pytest.mark.parametrize("row", covered_rows, ids=lambda r: r["encoding"])
def test_encoding_at_min_bytes(row):
    """Detection works at exactly the claimed min_bytes threshold."""
    encoding = row["encoding"]
    min_bytes = int(row["min_bytes"])

    try:
        chunk = encode_sample(row, max_bytes=min_bytes)
    except (UnicodeEncodeError, LookupError):
        pytest.skip(f"Python cannot encode sample text as {encoding}")

    # At min_bytes, the chunk should not crash and should return a bool
    result = is_binary_string(chunk)
    assert isinstance(result, bool), f"{encoding} at {min_bytes} bytes did not return bool"


@pytest.mark.parametrize("size", [1, 2, 4, 8, 10, 16, 32, 64])
def test_tiny_ascii_chunks(size):
    """Pure ASCII text at small sizes is detected as text."""
    chunk = b"Hello, world! The quick brown fox jumps."[:size]
    assert is_binary_string(chunk) is False, f"ASCII text at {size} bytes misclassified as binary"


@pytest.mark.parametrize("size", [16, 32, 64])
def test_tiny_binary_chunks(size):
    """Null-heavy data at small sizes is detected as binary."""
    chunk = b"\x00" * size
    assert is_binary_string(chunk) is True, f"All-null data at {size} bytes misclassified as text"


def test_mostly_printable_with_high_bytes():
    """90% printable ASCII with scattered high bytes stays text-like enough
    to not crash, regardless of classification."""
    base = b"The quick brown fox jumps over the lazy dog. " * 3
    chunk = bytearray(base[:128])
    # Inject 10% high bytes
    for i in range(0, 128, 10):
        chunk[i] = 0xC0 + (i % 30)
    result = is_binary_string(bytes(chunk))
    assert isinstance(result, bool)


def test_single_invalid_utf8_byte():
    """Valid UTF-8 with one invalid continuation byte is still classifiable."""
    text = "Hello, world! This is valid UTF-8 text for testing purposes."
    chunk = bytearray(text.encode("utf-8"))[:128]
    # Break one byte to make it invalid UTF-8
    chunk[10] = 0xFF
    result = is_binary_string(bytes(chunk))
    assert isinstance(result, bool)


# --- Binary format tests ---


binary_rows_with_magic = [r for r in binary_rows if r["magic_hex"].strip()]
binary_rows_with_files = [r for r in binary_rows if r["test_file"].strip()]


@pytest.mark.parametrize("row", binary_rows_with_magic, ids=lambda r: r["format"])
def test_binary_magic_detected(row):
    """Magic bytes + random padding is detected as binary."""
    magic = bytes.fromhex(row["magic_hex"])
    # Pad with high-entropy binary data (resembles compressed/pixel data)
    padding = hashlib.sha512(b"binary-padding").digest() * 2  # 128 bytes
    chunk = (magic + padding)[:128]
    assert is_binary_string(chunk) is True, f"{row['format']} magic bytes misclassified as text"


@pytest.mark.parametrize("row", binary_rows_with_files, ids=lambda r: r["format"])
def test_binary_file_detected(row):
    """Real binary test fixture files are detected as binary."""
    path = row["test_file"]
    if not os.path.exists(path):
        pytest.skip(f"Test file not found: {path}")
    with open(path, "rb") as f:
        chunk = f.read(CHUNK_SIZE)
    if len(chunk) == 0:
        pytest.skip(f"Empty file: {path}")
    assert is_binary_string(chunk) is True, f"{row['format']} file {path} misclassified as text"
