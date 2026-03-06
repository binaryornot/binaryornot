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


def encode_sample(row):
    # Repeat sample text to produce a chunk well above detection thresholds
    text = (row["sample_text"] + " ") * 20
    return text.encode(row["encoding"])[:1024]


def make_id(row):
    return f"{row['encoding']}-{row['status']}"


rows = load_encoding_rows()


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

    assert is_binary_string(chunk) is False, (
        f"Text encoded as {encoding} was misclassified as binary"
    )
