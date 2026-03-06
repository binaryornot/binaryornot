# BinaryOrNot

Ultra-lightweight pure Python package to guess whether a file is binary or text, using a heuristic similar to Perl's `pp_fttext` and its [analysis by Eli Bendersky](http://eli.thegreenplace.net/2011/10/19/perls-guess-if-file-is-text-or-binary-implemented-in-python/).

```python
>>> from binaryornot.check import is_binary
>>> is_binary('README.md')
False
>>> is_binary('logo.png')
True
```

## Why?

You may be thinking, "I can write this in 2 lines of code?!"

It's actually not that easy. Reliable binary detection needs to handle edge cases across encodings (UTF-16, GB2312, Big5, EUC-KR, Latin-1), file types (fonts, images, compiled bytecode, SQLite databases), and the boundary between "high-ASCII text" and "binary with printable bytes." BinaryOrNot saves you from writing and thoroughly testing that code across all these cases yourself.

## Getting started

- [Installation](installation.md) - how to install BinaryOrNot
- [Usage](usage.md) - Python API, command line, and how the detection works
- [API Reference](api.md) - auto-generated API documentation

## Credits

- Created by [Audrey Roy Greenfeld](https://github.com/audreyfeldroy)
- Special thanks to [Eli Bendersky](https://eli.thegreenplace.net/) for his writeup explaining the Perl heuristic and his Python implementation, which BinaryOrNot is largely based on
- Perl's `pp_fttext` source: [perl5/pp_sys.c](https://github.com/Perl/perl5/blob/v5.23.1/pp_sys.c#L3527-L3587)
