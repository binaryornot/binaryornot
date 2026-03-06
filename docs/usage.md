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

BinaryOrNot uses a heuristic similar to Perl's `pp_fttext`, based on [Eli Bendersky's translation to Python](http://eli.thegreenplace.net/2011/10/19/perls-guess-if-file-is-text-or-binary-implemented-in-python/). The detection runs in three stages:

1. **Byte ratio analysis**: checks the ratio of ASCII control characters and high-ASCII characters in the first 1024 bytes. Files that are overwhelmingly control characters are binary. Files with a high ratio of control characters and very few high-ASCII characters are flagged as "likely binary."

2. **Charset detection**: runs [chardet](https://github.com/chardet/chardet) on the chunk. If chardet identifies an encoding with >90% confidence (and it's not plain ASCII), the chunk is decoded to verify.

3. **Final decision**: combines the byte ratio flag with the charset detection result. Files flagged as likely binary that can't be decoded as Unicode are binary. Files not flagged as likely binary but containing null bytes (`\x00`) or `\xff` are binary. Everything else is text.

## Tested file types

BinaryOrNot has tests covering:

**Text**: .txt, .css, .json, .svg, .js, .lua, .pl, .rst, .py

**Binary**: .png, .gif, .jpg, .tiff, .bmp, .rgb, .DS_Store, .eot, .otf, .ttf, .woff, .pyc, .sqlite

**Encodings**: UTF-8, UTF-16 (BE/LE/BOM), UTF-32 (LE/BOM), GB2312, Big5, EUC-KR, Latin-1, Shift-JIS
