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

BinaryOrNot reads the first 512 bytes of a file and classifies them as binary or text using a trained decision tree. The tree operates on 24 features computed from the byte chunk:

- **Byte class ratios**: null bytes, control characters, printable ASCII, high bytes (0x80-0xFF)
- **Encoding validity**: whether the chunk decodes as UTF-8, UTF-16-LE/BE, UTF-32-LE/BE, GB2312, Big5, Shift-JIS, EUC-JP, or EUC-KR
- **Positional null ratios**: fraction of even-index and odd-index bytes that are 0x00 (detects BOM-less UTF-16)
- **BOM flags**: presence of UTF-8, UTF-16, or UTF-32 byte order marks
- **Shannon entropy**: byte distribution randomness (structured text vs random binary)
- **Longest printable run**: longest streak of printable ASCII + whitespace relative to chunk length
- **Magic signature match**: whether the chunk starts with a known binary file signature

The decision tree was trained on Hypothesis-generated data (Unicode text encoded via Python's stdlib codecs, plus synthetic binary patterns) and the project's own test files. The training script lives in `scripts/train_detector.py` and can be re-run to retrain the model.

## Encoding coverage

BinaryOrNot ships an encoding coverage matrix at `binaryornot/data/encodings.csv` that lists every encoding family, whether the detection covers it, known gaps, and sample text for testing. The test suite reads this CSV to verify coverage claims: each encoding marked "covered" becomes a passing test, each "gap" becomes an expected failure.

37 encodings are covered, including UTF-8, UTF-16, UTF-32, all major single-byte encodings (ISO-8859, Windows code pages, KOI8-R, Mac encodings), and CJK encodings (GB2312, GBK, GB18030, Big5, Shift-JIS, EUC-JP, EUC-KR, ISO-2022-JP). 4 gaps are documented with reasons: ISO-2022-KR and three EBCDIC code pages.

## Binary format coverage

Binary format detection is tracked in `binaryornot/data/binary_formats.csv`. Each row lists the format name, its magic bytes in hex, an optional path to a real test fixture, and the specification where the magic value is defined.

49 formats are covered across images (PNG, JPEG, GIF, BMP, TIFF, ICO, WebP, PSD, HEIF), documents (PDF, OLE2), databases (SQLite), archives (ZIP, gzip, xz, bzip2, 7z, RAR, Zstandard), executables (ELF, Mach-O, MZ/PE, Java class, WebAssembly, Dalvik DEX), media (RIFF, Ogg, FLAC, MP4/MOV, MP3, Matroska/WebM, MIDI), fonts (WOFF, WOFF2, OTF, TTF, EOT), data (Apache Parquet), and compiled artifacts (.pyc, .DS_Store, LLVM bitcode, Git packfiles).

