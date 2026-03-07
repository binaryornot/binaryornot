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

BinaryOrNot reads the first 128 bytes and classifies them with a trained decision tree. The tree operates on 23 features: byte class ratios, Shannon entropy, encoding validity checks (UTF-8, UTF-16, UTF-32, GB2312, Big5, Shift-JIS, EUC-JP, EUC-KR), BOM detection, and longest printable run. It handles all the edge cases above correctly, with zero dependencies.

Tested against 37 text encodings and 49 binary formats, verified by parametrized tests driven from coverage CSVs. Fuzz-tested with [Hypothesis](https://hypothesis.readthedocs.io/).

## API

One function:

```python
from binaryornot.check import is_binary

is_binary(filename)  # returns True or False
```

There's also `is_binary_string()` if you already have bytes:

```python
from binaryornot.helpers import is_binary_string

is_binary_string(b"\x00\x01\x02")  # True
is_binary_string(b"hello world")   # False
```

[Full documentation](https://binaryornot.github.io/binaryornot/) covers the detection algorithm in detail.

## Credits

Created by [Audrey Roy Greenfeld](https://github.com/audreyfeldroy). Based on [Eli Bendersky's analysis](http://eli.thegreenplace.net/2011/10/19/perls-guess-if-file-is-text-or-binary-implemented-in-python/) of Perl's [`pp_fttext`](https://github.com/Perl/perl5/blob/v5.23.1/pp_sys.c#L3527-L3587).
