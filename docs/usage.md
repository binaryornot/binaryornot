# Usage

## Python API

Use `is_binary()` to guess whether a file is binary or text:

```python
from binaryornot.check import is_binary

is_binary("README.md")
# False

is_binary("logo.png")
# True
```

## Command line

The `binaryornot` command takes a filename and prints `True` or `False`:

```sh
$ binaryornot README.md
False

$ binaryornot logo.png
True
```

Run `binaryornot --help` for usage details.

## How it works

BinaryOrNot reads the first 1024 bytes of a file and classifies them as binary or text using a trained decision tree. The tree operates on 18 features computed from the byte chunk:

- **Byte class ratios**: null bytes, control characters, printable ASCII, high bytes (0x80-0xFF)
- **Encoding validity**: whether the chunk decodes as UTF-8, UTF-16-LE/BE, or UTF-32-LE/BE
- **Positional null ratios**: fraction of even-index and odd-index bytes that are 0x00 (detects BOM-less UTF-16)
- **BOM flags**: presence of UTF-8, UTF-16, or UTF-32 byte order marks
- **Shannon entropy**: byte distribution randomness (structured text vs random binary)
- **Longest printable run**: longest streak of printable ASCII + whitespace relative to chunk length

The decision tree was trained on Hypothesis-generated data (Unicode text encoded via Python's stdlib codecs, plus synthetic binary patterns) and the project's own test files. The training script lives in `scripts/train_detector.py` and can be re-run to retrain the model.

## Encoding coverage

BinaryOrNot ships an encoding coverage matrix at `binaryornot/data/encodings.csv` that lists every encoding family, whether the detection covers it, known gaps, and sample text for testing. The test suite reads this CSV to verify coverage claims: each encoding marked "covered" becomes a passing test, each "gap" becomes an expected failure. When someone improves the model and a gap starts passing, the test tells them to update the CSV.

## Tested file types

BinaryOrNot has tests covering:

**Text**: .txt, .css, .json, .svg, .js, .lua, .pl, .rst, .py

**Binary**: .png, .gif, .jpg, .tiff, .bmp, .rgb, .DS_Store, .eot, .otf, .ttf, .woff, .pyc, .sqlite

**Encodings**: UTF-8, UTF-16 (BE/LE/BOM), UTF-32 (LE/BOM), GB2312, Big5, EUC-KR, Latin-1, Shift-JIS
