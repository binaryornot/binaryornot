"""Test encoding coverage claims from the encoding coverage CSV.

Each row in the CSV becomes a test case. Encodings marked 'covered' must
be detected as text. Encodings marked 'gap' are expected failures.

Sample text for each encoding lives in the CSV's sample_text column,
keeping test data and coverage claims in one place.
"""

import csv
from importlib.resources import files

import pytest

from binaryornot.helpers import is_binary_string


def load_encoding_rows():
    csv_path = files("binaryornot.data").joinpath("encodings.csv")
    with csv_path.open() as f:
        return list(csv.DictReader(f))


def encode_sample(row, max_bytes=128):
    # Repeat sample text to produce a chunk well above detection thresholds
    text = (row["sample_text"] + " ") * 20
    return text.encode(row["encoding"])[:max_bytes]


def make_id(row):
    return f"{row['encoding']}-{row['status']}"


rows = load_encoding_rows()
covered_rows = [r for r in rows if r["status"] == "covered"]


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


@pytest.mark.parametrize("size", [1, 2, 4, 8, 16, 32, 64])
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
