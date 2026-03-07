"""Train a decision tree to classify byte chunks as text or binary.

Training data comes from two sources:
  1. Hypothesis text() strategy, encoded via Python's stdlib codecs
  2. Hypothesis binary() strategy for synthetic binary patterns
  3. binaryornot's own test files (MIT-licensed), weighted for validation

The encoding list is read from binaryornot/data/encodings.csv.

Usage:
    uv run --with 'scikit-learn>=1.4,numpy,hypothesis' python scripts/train_detector.py
"""

import csv
import os
import struct
from importlib.resources import files

import numpy as np
from hypothesis import HealthCheck, Phase, assume, settings
from hypothesis import strategies as st
from hypothesis.core import given
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier, export_text

from binaryornot.helpers import _compute_features

FEATURE_NAMES = [
    "null_ratio",
    "control_ratio",
    "printable_ascii_ratio",
    "high_byte_ratio",
    "utf8_valid",
    "even_null_ratio",
    "odd_null_ratio",
    "byte_entropy",
    "bom_utf32le",
    "bom_utf32be",
    "bom_utf16le",
    "bom_utf16be",
    "bom_utf8",
    "try_utf16le",
    "try_utf16be",
    "try_utf32le",
    "try_utf32be",
    "longest_printable_run",
    "try_gb2312",
    "try_big5",
    "try_shift_jis",
    "try_euc_jp",
    "try_euc_kr",
]


def _load_encodings_from_csv():
    """Load encoding list from the coverage CSV (single source of truth)."""
    csv_path = files("binaryornot.data").joinpath("encodings.csv")
    with csv_path.open() as f:
        return [row["encoding"] for row in csv.DictReader(f)]


def _load_csv_samples():
    """Load per-encoding sample text from the CSV as training data."""
    csv_path = files("binaryornot.data").joinpath("encodings.csv")
    samples = []
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            text = (row["sample_text"] + " ") * 20
            try:
                chunk = text.encode(row["encoding"])[:128]
            except (UnicodeEncodeError, LookupError):
                continue
            if len(chunk) >= 4:
                samples.append((chunk, 0))
    return samples


# ---------------------------------------------------------------------------
# Training data generation via Hypothesis strategies
# ---------------------------------------------------------------------------

TEXT_ENCODINGS = _load_encodings_from_csv()


def _load_binary_headers_from_csv():
    """Load binary format magic bytes from the coverage CSV."""
    csv_path = files("binaryornot.data").joinpath("binary_formats.csv")
    headers = []
    with csv_path.open() as f:
        for row in csv.DictReader(f):
            magic_hex = row["magic_hex"].strip()
            if magic_hex:
                headers.append(bytes.fromhex(magic_hex))
    return headers


BINARY_HEADERS = _load_binary_headers_from_csv()


# --- Hypothesis strategies ---


def encoded_text_strategy(min_size=5, max_size=64):
    """Strategy: generate Unicode text, encode it in a random encoding."""

    @st.composite
    def strat(draw):
        t = draw(st.text(min_size=min_size, max_size=max_size))
        enc = draw(st.sampled_from(TEXT_ENCODINGS))
        try:
            chunk = t.encode(enc)[:128]
        except (UnicodeEncodeError, UnicodeDecodeError, LookupError):
            assume(False)
        assume(len(chunk) >= 4)
        return chunk

    return strat()


def binary_random_strategy():
    """Strategy: random bytes at various lengths."""
    return st.binary(min_size=10, max_size=128)


def binary_with_header_strategy():
    """Strategy: known file format header + random padding."""

    @st.composite
    def strat(draw):
        header = draw(st.sampled_from(BINARY_HEADERS))
        padding = draw(st.binary(min_size=20, max_size=500))
        return (header + padding)[:128]

    return strat()


def binary_control_chars_strategy():
    """Strategy: bytes made entirely of control characters."""
    return st.binary(min_size=10, max_size=300).map(
        lambda b: bytes(x % 31 + 1 for x in b)  # map to 0x01-0x1F
    )


def binary_scattered_nulls_strategy():
    """Strategy: random bytes with null bytes injected."""

    @st.composite
    def strat(draw):
        data = bytearray(draw(st.binary(min_size=50, max_size=128)))
        n = len(data)
        null_count = draw(st.integers(min_value=n // 20, max_value=n // 5))
        positions = draw(st.lists(st.integers(min_value=0, max_value=n - 1), min_size=null_count, max_size=null_count))
        for pos in positions:
            data[pos] = 0
        return bytes(data)

    return strat()


def binary_high_bytes_strategy():
    """Strategy: bytes only in the 0x80-0xFF range."""
    return st.binary(min_size=10, max_size=500).map(lambda b: bytes((x % 128) + 128 for x in b))


def binary_pyc_strategy():
    """Strategy: simulated .pyc file (magic + random)."""

    @st.composite
    def strat(draw):
        magic_val = draw(st.integers(min_value=0x0A0D, max_value=0x0FFF))
        magic = struct.pack("<H", magic_val) + b"\r\n"
        rest = draw(st.binary(min_size=50, max_size=500))
        return (magic + rest)[:128]

    return strat()


def binary_mixed_printable_strategy():
    """Strategy: alternating ASCII text and binary segments."""

    @st.composite
    def strat(draw):
        n_parts = draw(st.integers(min_value=3, max_value=8))
        parts = []
        for _ in range(n_parts):
            if draw(st.booleans()):
                draw(st.binary(min_size=3, max_size=20)).translate(bytes(range(256)), bytes(0 for _ in range(256)))
                # Map to printable ASCII range
                parts.append(bytes((b % 95) + 32 for b in draw(st.binary(min_size=3, max_size=20))))
            else:
                parts.append(draw(st.binary(min_size=10, max_size=100)))
        chunk = b"".join(parts)[:128]
        assume(len(chunk) >= 10)
        return chunk

    return strat()


def binary_structured_strategy():
    """Strategy: repeating byte patterns like struct-packed records.

    Binary files often contain structured data (pixel rows, database
    records, protocol buffers) with repeating patterns, not random bytes.
    """

    @st.composite
    def strat(draw):
        # Generate a short pattern (2-8 bytes) and repeat it
        pattern_len = draw(st.integers(min_value=2, max_value=8))
        pattern = draw(st.binary(min_size=pattern_len, max_size=pattern_len))
        repeats = 128 // pattern_len + 1
        chunk = (pattern * repeats)[:128]
        # Inject some variation (field values change across records)
        data = bytearray(chunk)
        n_mutations = draw(st.integers(min_value=1, max_value=len(data) // 4))
        for _ in range(n_mutations):
            pos = draw(st.integers(min_value=0, max_value=len(data) - 1))
            data[pos] = draw(st.integers(min_value=0, max_value=255))
        return bytes(data)

    return strat()


def binary_with_strings_strategy():
    """Strategy: binary data with embedded ASCII strings.

    Real executables and object files contain string tables, error
    messages, and symbol names surrounded by non-printable bytes.
    """

    @st.composite
    def strat(draw):
        parts = []
        for _ in range(draw(st.integers(min_value=2, max_value=5))):
            # Binary segment
            parts.append(draw(st.binary(min_size=5, max_size=30)))
            # Embedded ASCII string (null-terminated)
            word = draw(st.from_regex(r"[a-z_]{3,15}", fullmatch=True))
            parts.append(word.encode("ascii") + b"\x00")
        chunk = b"".join(parts)[:128]
        assume(len(chunk) >= 20)
        return chunk

    return strat()


def binary_compressed_strategy():
    """Strategy: high-entropy bytes that fail all encoding checks.

    Compressed and encrypted data has near-uniform byte distribution
    but doesn't decode as any text encoding.
    """

    @st.composite
    def strat(draw):
        # Generate bytes spanning the full 0x00-0xFF range
        data = bytearray(draw(st.binary(min_size=64, max_size=128)))
        # Ensure invalid UTF-8 sequences by inserting bare continuation bytes
        for i in range(0, len(data) - 1, 7):
            data[i] = draw(st.sampled_from([0x80, 0xBF, 0xFE, 0xFF]))
        return bytes(data)

    return strat()


def collect_samples(strategy, label, count, seed=42):
    """Draw `count` examples from a Hypothesis strategy with a fixed seed."""
    collected = []

    @given(data=strategy)
    @settings(
        max_examples=count,
        database=None,
        phases=[Phase.generate],
        derandomize=True,
        suppress_health_check=[HealthCheck.too_slow, HealthCheck.filter_too_much],
    )
    def collector(data):
        collected.append((data, label))

    collector()
    return collected


def cjk_text_strategy():
    """Strategy: CJK characters encoded in CJK encodings.

    These are the main source of false positives (text misclassified as
    binary) because CJK encodings produce high-byte-ratio chunks with
    low printable ASCII ratios, looking binary by surface statistics.
    """
    cjk_encodings = ["gb2312", "gbk", "gb18030", "big5", "shift_jis", "euc-jp", "euc-kr"]

    @st.composite
    def strat(draw):
        # CJK Unified Ideographs (U+4E00-U+9FFF) + punctuation
        chars = draw(st.text(
            alphabet=st.characters(whitelist_categories=("Lo", "Zs"), whitelist_characters="，。！？、"),
            min_size=5, max_size=40,
        ))
        enc = draw(st.sampled_from(cjk_encodings))
        try:
            chunk = chars.encode(enc)[:128]
        except (UnicodeEncodeError, UnicodeDecodeError, LookupError):
            assume(False)
        assume(len(chunk) >= 8)
        return chunk

    return strat()


def text_with_whitespace_strategy():
    """Strategy: text with realistic whitespace (tabs, newlines, CRs).

    Real text files have control characters that are still text: \\t,
    \\n, \\r. These inflate control_ratio without being binary.
    """

    @st.composite
    def strat(draw):
        words = draw(st.lists(
            st.from_regex(r"[A-Za-z0-9_]{1,12}", fullmatch=True),
            min_size=5, max_size=20,
        ))
        separators = [" ", "\t", "\n", "\r\n", "  "]
        parts = []
        for word in words:
            parts.append(word)
            parts.append(draw(st.sampled_from(separators)))
        return "".join(parts).encode("utf-8")[:128]

    return strat()


def generate_text_samples() -> list[tuple[bytes, int]]:
    """Generate labeled text samples using Hypothesis strategies."""
    samples = []

    # Main text generation: Hypothesis text() -> encode in random encoding
    # Full-length chunks
    samples.extend(collect_samples(encoded_text_strategy(5, 64), label=0, count=800))

    # Short text for edge cases
    samples.extend(collect_samples(encoded_text_strategy(1, 20), label=0, count=200))

    # Near-max-length chunks
    samples.extend(collect_samples(encoded_text_strategy(30, 64), label=0, count=200))

    # CJK text (targets the main false positive source)
    samples.extend(collect_samples(cjk_text_strategy(), label=0, count=200))

    # Text with realistic whitespace
    samples.extend(collect_samples(text_with_whitespace_strategy(), label=0, count=100))

    print(f"  Text samples generated: {len(samples)}")
    return samples


def generate_binary_samples() -> list[tuple[bytes, int]]:
    """Generate labeled binary samples using Hypothesis strategies."""
    samples = []

    samples.extend(collect_samples(binary_random_strategy(), label=1, count=300))
    samples.extend(collect_samples(binary_with_header_strategy(), label=1, count=250))
    samples.extend(collect_samples(binary_control_chars_strategy(), label=1, count=30))
    samples.extend(collect_samples(binary_scattered_nulls_strategy(), label=1, count=50))
    samples.extend(collect_samples(binary_high_bytes_strategy(), label=1, count=30))
    samples.extend(collect_samples(binary_pyc_strategy(), label=1, count=30))
    samples.extend(collect_samples(binary_mixed_printable_strategy(), label=1, count=30))
    samples.extend(collect_samples(binary_structured_strategy(), label=1, count=150))
    samples.extend(collect_samples(binary_with_strings_strategy(), label=1, count=100))
    samples.extend(collect_samples(binary_compressed_strategy(), label=1, count=100))

    print(f"  Binary samples generated: {len(samples)}")
    return samples


# ---------------------------------------------------------------------------
# Tree export
# ---------------------------------------------------------------------------


TREE_MODULE_PATH = os.path.join(os.path.dirname(__file__), "..", "src", "binaryornot", "tree.py")


def export_tree_as_python(tree, feature_names, indent="    ", start_depth=0):
    """Export a fitted DecisionTreeClassifier as Python if/else code."""
    tree_ = tree.tree_
    feature_name = [feature_names[i] if i >= 0 else "undefined" for i in tree_.feature]

    lines = []

    def recurse(node, depth):
        prefix = indent * depth
        if tree_.feature[node] >= 0:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            lines.append(f"{prefix}if features[{tree_.feature[node]}] <= {threshold:.6f}:  # {name}")
            recurse(tree_.children_left[node], depth + 1)
            lines.append(f"{prefix}else:")
            recurse(tree_.children_right[node], depth + 1)
        else:
            # Leaf node
            counts = tree_.value[node][0]
            prediction = 1 if counts[1] > counts[0] else 0
            total = counts[0] + counts[1]
            confidence = max(counts) / total
            label = "binary" if prediction == 1 else "text"
            lines.append(f"{prefix}return {bool(prediction)}  # {label} ({confidence:.1%}, n={int(total)})")

    recurse(0, start_depth)
    return "\n".join(lines)


def write_tree_module(tree, feature_names):
    """Write the trained tree as src/binaryornot/tree.py."""
    body = export_tree_as_python(tree, feature_names, indent="    ", start_depth=1)
    module = f'''\
"""Auto-generated decision tree for binary/text classification.

Do not edit by hand. Regenerate with:
    uv run --with 'scikit-learn,numpy,hypothesis' python scripts/train_detector.py
"""


def is_binary(features):
    """Classify a byte chunk as binary or text.

    Takes the feature list from helpers._compute_features().
    Returns True for binary.
    """
{body}
'''
    path = os.path.normpath(TREE_MODULE_PATH)
    with open(path, "w") as f:
        f.write(module)
    print(f"\nWrote tree to {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def validate_against_test_files(model):
    """Check model predictions against binaryornot's existing test files."""
    expected = {
        "tests/files/empty.txt": False,
        "tests/files/robots.txt": False,
        "tests/files/unicode.txt": False,
        "tests/files/bootstrap-glyphicons.css": False,
        "tests/files/cookiecutter.json": False,
        "tests/files/glyphiconshalflings-regular.svg": False,
        "tests/isBinaryFile/russian_file.rst": False,
        "tests/isBinaryFile/perl_script": False,
        "tests/isBinaryFile/index.js": False,
        "tests/isBinaryFile/no.lua": False,
        "tests/isBinaryFile/null_file.gif": False,
        "tests/isBinaryFile/encodings/bom_utf-16.txt": False,
        "tests/isBinaryFile/encodings/bom_utf-16le.txt": False,
        "tests/isBinaryFile/encodings/bom_utf-32.txt": False,
        "tests/isBinaryFile/encodings/bom_utf-32le.txt": False,
        "tests/isBinaryFile/encodings/bom_utf-8.txt": False,
        "tests/isBinaryFile/encodings/test-utf16be.txt": False,
        "tests/isBinaryFile/encodings/utf_8.txt": False,
        "tests/isBinaryFile/encodings/utf8cn.txt": False,
        "tests/isBinaryFile/encodings/big5.txt": False,
        "tests/isBinaryFile/encodings/big5_B.txt": False,
        "tests/isBinaryFile/encodings/test-gb.txt": False,
        "tests/isBinaryFile/encodings/test-gb2.txt": False,
        "tests/isBinaryFile/encodings/test-kr.txt": False,
        "tests/isBinaryFile/encodings/test-latin.txt": False,
        "tests/isBinaryFile/encodings/test-shishi.txt": False,
        "tests/files/.DS_Store": True,
        "tests/files/decoding-error": True,
        "tests/files/lookup-error": True,
        "tests/files/logo.png": True,
        "tests/files/lena.gif": True,
        "tests/files/lena.jpg": True,
        "tests/files/palette-1c-8b.tiff": True,
        "tests/files/rgb-3c-8b.bmp": True,
        "tests/files/pixelstream.rgb": True,
        "tests/files/hello_world.pyc": True,
        "tests/files/empty.pyc": True,
        "tests/files/troublesome.pyc": True,
        "tests/files/glyphiconshalflings-regular.eot": True,
        "tests/files/glyphiconshalflings-regular.otf": True,
        "tests/files/glyphiconshalflings-regular.ttf": True,
        "tests/files/glyphiconshalflings-regular.woff": True,
        "tests/isBinaryFile/grep": True,
        "tests/isBinaryFile/test.sqlite": True,
        "tests/isBinaryFile/trunks.gif": True,
    }

    passed = 0
    failed = 0
    for path, expected_binary in expected.items():
        if not os.path.exists(path):
            print(f"  SKIP (not found): {path}")
            continue

        with open(path, "rb") as f:
            chunk = f.read(128)

        if len(chunk) == 0:
            predicted_binary = False
        else:
            features = np.array([_compute_features(chunk)])
            predicted_binary = bool(model.predict(features)[0])

        if predicted_binary == expected_binary:
            passed += 1
        else:
            failed += 1
            direction = "should be binary" if expected_binary else "should be text"
            if len(chunk) > 0:
                prob = model.predict_proba(features)[0]
                print(f"  FAIL: {path} ({direction}, prob_binary={prob[1]:.3f})")
            else:
                print(f"  FAIL: {path} ({direction})")

    total = passed + failed
    print(f"  Validation: {passed}/{total} passed ({failed} failures)")
    return failed


def load_test_file_samples() -> list[tuple[bytes, int]]:
    """Load the real binaryornot test files as training data."""
    samples = []
    text_files = [
        "tests/files/empty.txt",
        "tests/files/robots.txt",
        "tests/files/unicode.txt",
        "tests/files/bootstrap-glyphicons.css",
        "tests/files/cookiecutter.json",
        "tests/files/glyphiconshalflings-regular.svg",
        "tests/files/hello_world.py",
        "tests/isBinaryFile/russian_file.rst",
        "tests/isBinaryFile/perl_script",
        "tests/isBinaryFile/index.js",
        "tests/isBinaryFile/no.lua",
        "tests/isBinaryFile/encodings/bom_utf-16.txt",
        "tests/isBinaryFile/encodings/bom_utf-16le.txt",
        "tests/isBinaryFile/encodings/bom_utf-32.txt",
        "tests/isBinaryFile/encodings/bom_utf-32le.txt",
        "tests/isBinaryFile/encodings/bom_utf-8.txt",
        "tests/isBinaryFile/encodings/test-utf16be.txt",
        "tests/isBinaryFile/encodings/utf_8.txt",
        "tests/isBinaryFile/encodings/utf8cn.txt",
        "tests/isBinaryFile/encodings/big5.txt",
        "tests/isBinaryFile/encodings/big5_B.txt",
        "tests/isBinaryFile/encodings/test-gb.txt",
        "tests/isBinaryFile/encodings/test-gb2.txt",
        "tests/isBinaryFile/encodings/test-kr.txt",
        "tests/isBinaryFile/encodings/test-latin.txt",
        "tests/isBinaryFile/encodings/test-shishi.txt",
    ]
    binary_files = [
        "tests/files/.DS_Store",
        "tests/files/decoding-error",
        "tests/files/lookup-error",
        "tests/files/logo.png",
        "tests/files/lena.gif",
        "tests/files/lena.jpg",
        "tests/files/palette-1c-8b.tiff",
        "tests/files/rgb-3c-8b.bmp",
        "tests/files/pixelstream.rgb",
        "tests/files/hello_world.pyc",
        "tests/files/empty.pyc",
        "tests/files/troublesome.pyc",
        "tests/files/glyphiconshalflings-regular.eot",
        "tests/files/glyphiconshalflings-regular.otf",
        "tests/files/glyphiconshalflings-regular.ttf",
        "tests/files/glyphiconshalflings-regular.woff",
        "tests/isBinaryFile/grep",
        "tests/isBinaryFile/pdf.pdf",
        "tests/isBinaryFile/test.sqlite",
        "tests/isBinaryFile/trunks.gif",
    ]
    for path in text_files:
        if os.path.exists(path):
            with open(path, "rb") as f:
                chunk = f.read(128)
            if len(chunk) > 0:
                # Add multiple times to weight real files more heavily
                for _ in range(10):
                    samples.append((chunk, 0))
    for path in binary_files:
        if os.path.exists(path):
            with open(path, "rb") as f:
                chunk = f.read(128)
            if len(chunk) > 0:
                for _ in range(10):
                    samples.append((chunk, 1))
    return samples


def main():
    print("Generating training data via Hypothesis strategies...")
    text_samples = generate_text_samples()
    binary_samples = generate_binary_samples()
    real_samples = load_test_file_samples()
    csv_samples = _load_csv_samples()
    all_samples = text_samples + binary_samples + real_samples + csv_samples
    print(f"  Real file samples: {len(real_samples)}")
    print(f"  CSV encoding samples: {len(csv_samples)}")

    print(f"  Text samples:   {len(text_samples)}")
    print(f"  Binary samples: {len(binary_samples)}")
    print(f"  Total:          {len(all_samples)}")

    print("\nExtracting features...")
    X = np.array([_compute_features(chunk) for chunk, _ in all_samples])
    y = np.array([label for _, label in all_samples])

    print(f"  Feature matrix: {X.shape}")
    print(f"  Class balance:  {sum(y == 0)} text, {sum(y == 1)} binary")

    # Try different tree depths
    best_depth = None
    best_score = 0
    print("\nSearching for best tree depth...")
    for depth in range(5, 15):
        model = DecisionTreeClassifier(max_depth=depth, random_state=42, class_weight="balanced")
        scores = cross_val_score(model, X, y, cv=5, scoring="accuracy")
        mean_score = scores.mean()
        print(f"  depth={depth:2d}  CV={mean_score:.4f} (+/- {scores.std():.4f})")
        if mean_score > best_score:
            best_score = mean_score
            best_depth = depth

    print(f"\nBest depth: {best_depth} (CV={best_score:.4f})")

    # Train final model
    model = DecisionTreeClassifier(max_depth=best_depth, random_state=42, class_weight="balanced")
    model.fit(X, y)

    train_acc = model.score(X, y)
    preds = model.predict(X)
    fp = sum((preds == 1) & (y == 0))
    fn = sum((preds == 0) & (y == 1))
    print(f"  Training accuracy: {train_acc:.4f}")
    print(f"  False positives (text->binary): {fp}")
    print(f"  False negatives (binary->text): {fn}")

    if fp > 0 or fn > 0:
        print("\n  Misclassified training samples:")
        for i, (chunk, label) in enumerate(all_samples):
            if preds[i] != label:
                direction = "text->binary" if label == 0 else "binary->text"
                preview = repr(chunk[:50])
                prob = model.predict_proba(X[i : i + 1])[0]
                print(f"    [{direction}] prob={prob[1]:.3f} {preview}")

    # Feature importance
    print("\nFeature importance:")
    importances = list(zip(FEATURE_NAMES, model.feature_importances_, strict=True))
    importances.sort(key=lambda x: x[1], reverse=True)
    for name, imp in importances:
        if imp > 0.001:
            print(f"  {name:25s} {imp:.4f}")

    # Validate
    print("\nValidating against binaryornot test files...")
    failures = validate_against_test_files(model)

    # Show the tree
    print("\nDecision tree (sklearn format):")
    print(export_text(model, feature_names=FEATURE_NAMES, max_depth=10))

    # Write tree module
    write_tree_module(model, FEATURE_NAMES)

    if failures == 0:
        print("\n*** All validation tests passed! ***")
    else:
        print(f"\n*** {failures} validation failures - model needs improvement ***")


if __name__ == "__main__":
    main()
