# BinaryOrNot

![PyPI version](https://img.shields.io/pypi/v/binaryornot.svg)

Ultra-lightweight pure Python package to guess whether a file is binary or text, using a heuristic similar to Perl's `pp_fttext`.

* PyPI package: https://pypi.org/project/binaryornot/
* Documentation: https://binaryornot.github.io/binaryornot/
* Free software: MIT License

## Quickstart

```python
>>> from binaryornot.check import is_binary
>>> is_binary('README.md')
False
>>> is_binary('logo.png')
True
```

Or from the command line:

```sh
$ binaryornot README.md
False
```

## Why?

You may be thinking, "I can write this in 2 lines of code?!"

It's actually not that easy. Reliable binary detection needs to handle edge cases across encodings (UTF-16, GB2312, Big5, EUC-KR, Latin-1), file types (fonts, images, compiled bytecode, SQLite databases), and the boundary between "high-ASCII text" and "binary with printable bytes." BinaryOrNot saves you from writing and thoroughly testing that code across all these cases yourself.

For the full story, see Eli Bendersky's [writeup on Perl's heuristic](http://eli.thegreenplace.net/2011/10/19/perls-guess-if-file-is-text-or-binary-implemented-in-python/).

## Features

Has tests for these file types:

* **Text**: .txt, .css, .json, .svg, .js, .lua, .pl, .rst, .py
* **Binary**: .png, .gif, .jpg, .tiff, .bmp, .rgb, .DS_Store, .eot, .otf, .ttf, .woff, .pyc, .sqlite

Has tests for numerous encodings: UTF-8, UTF-16, UTF-32, GB2312, Big5, EUC-KR, Latin-1, Shift-JIS.

## Development

```bash
git clone git@github.com:binaryornot/binaryornot.git
cd binaryornot
uv sync
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Credits

* Created by [Audrey Roy Greenfeld](https://github.com/audreyfeldroy)
* Special thanks to [Eli Bendersky](https://eli.thegreenplace.net/) for his writeup and implementation, which BinaryOrNot is largely based on
* Perl's `pp_fttext` source: [perl5/pp_sys.c](https://github.com/Perl/perl5/blob/v5.23.1/pp_sys.c#L3527-L3587)

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage).
