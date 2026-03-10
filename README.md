# BinaryOrNot

Python library and CLI tool to check if a file is binary or text. Zero dependencies.

```python
from binaryornot.check import is_binary

is_binary("image.png")    # True
is_binary("README.md")    # False
is_binary("data.sqlite")  # True
is_binary("report.csv")   # False
```

```sh
$ binaryornot image.png
True
```

## Install

```sh
pip install binaryornot
```

## Why not just check for null bytes?

That's the first thing everyone tries. It works until it doesn't:

- A UTF-16 text file is full of null bytes. Your tool thinks it's binary and corrupts it.
- A Big5 or GB2312 text file has high-ASCII bytes everywhere. Looks binary by byte ratios alone.
- A font file (.woff, .eot) is clearly binary but might not have null bytes in the first chunk.

BinaryOrNot reads the first 512 bytes and runs them through a trained decision tree that considers byte ratios, Shannon entropy, encoding validity, BOM detection, and more. It handles all the edge cases above correctly, with zero dependencies.

Tested against [37 text encodings and 49 binary formats](https://binaryornot.github.io/binaryornot/usage/), verified by parametrized tests driven from coverage CSVs.

## API

One function:

```python
from binaryornot.check import is_binary

is_binary(filename)  # returns True or False
```

There's also `is_binary_string()` if you already have bytes:

```python
from binaryornot.helpers import is_binary_string

# Read a chunk from a file and classify it
with open("mystery_file", "rb") as f:
    chunk = f.read(512)
is_binary_string(chunk)
```

[Full documentation](https://binaryornot.github.io/binaryornot/) covers the detection algorithm in detail.

## Credits

Created by [Audrey Roy Greenfeld](https://audrey.feldroy.com).
