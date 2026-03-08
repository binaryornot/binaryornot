# BinaryOrNot 0.6.0: Three Layers of Detection

BinaryOrNot identifies binary files three ways: by extension, by file signature, and by content analysis. Pass it any file path and it tells you binary or text, accurately, across PNGs, PDFs, executables, archives, fonts, CJK-encoded text, and hundreds of other formats.

```
uv pip install --upgrade binaryornot
```

### What's new

**131 file types recognized by name.** `is_binary()` checks the filename extension against a curated list of binary types (images, audio, video, archives, executables, fonts, documents, databases, 3D models, CAD files, scientific data formats, game ROMs) before reading any bytes. A `.png` or `.mp4` is classified instantly with zero file I/O. The extension list ships as `binary_extensions.csv` and is easy to inspect or extend. ([#648](https://github.com/binaryornot/binaryornot/pull/648))

If you need pure content-based classification, pass `check_extensions=False`:

```python
from binaryornot.check import is_binary

# Extension says binary, but let's check the actual bytes
is_binary("mystery_file.pyc", check_extensions=False)
```

**55 binary format signatures.** The detector checks file headers against known magic bytes for PNG, JPEG, PDF, ZIP, ELF, Mach-O, WebAssembly, SQLite, Parquet, Arrow IPC, and 45 more formats. Files that match a known signature are classified as binary immediately, before the statistical model runs. The signature table ships as `binary_formats.csv`. ([#647](https://github.com/binaryornot/binaryornot/pull/647))

**Type annotations on the public API.** `is_binary()`, `is_binary_string()`, and `get_starting_chunk()` all have inline type annotations. Editors and type checkers know that `is_binary()` accepts `str`, `bytes`, or `pathlib.Path` and returns `bool`. Credit to [@smheidrich](https://github.com/smheidrich) for the initial type stubs proposal (#627) and [@AlJohri](https://github.com/AlJohri) for requesting `pathlib.Path` support (#628). ([#643](https://github.com/binaryornot/binaryornot/pull/643))

### What's better

**Completely retrained decision tree on 4x more data.** The detector reads 512 bytes per file instead of 128, and the decision tree was rebuilt from scratch on those larger samples. A new feature, `has_magic_signature`, gives the tree a second path to the right answer when statistical features are ambiguous. Byte ratios and entropy calculations reflect actual file content rather than header artifacts. ([#647](https://github.com/binaryornot/binaryornot/pull/647))

**Python 3.10+ compatibility.** BinaryOrNot installs on Python 3.10 through 3.14, supporting Cookiecutter, cookieplone, and other tools that run on older interpreters. Thanks [@wesleybl](https://github.com/wesleybl) for raising this. ([#645](https://github.com/binaryornot/binaryornot/pull/645))

**Test fixtures ship in the sdist.** `.pyc` and `.DS_Store` test fixtures are force-included in the source distribution so tests pass when run from the sdist. ([#646](https://github.com/binaryornot/binaryornot/pull/646))

### What's fixed

**PNGs with ambiguous headers are correctly classified.** A 512x512 grayscale+alpha PNG has an IHDR chunk with enough null bytes that the first 128 bytes accidentally decode as UTF-16. Extension checking, signature matching, and the retrained tree each independently prevent this misclassification. Closes [#642](https://github.com/binaryornot/binaryornot/issues/642). ([#647](https://github.com/binaryornot/binaryornot/pull/647))

### What's changed

**`is_binary()` has a new keyword argument.** `check_extensions` (default `True`) controls whether the extension check runs. Existing code that calls `is_binary(path)` gets the extension check automatically. Code that passes `check_extensions=False` gets the previous content-only behavior.

### Contributors

[@audreyfeldroy](https://github.com/audreyfeldroy) (Audrey M. Roy Greenfeld) designed and built this release: the extension detection system, file signature matching, decision tree retraining, type annotations, Python 3.10 compatibility, and sdist fixes.

Thanks to [@smheidrich](https://github.com/smheidrich) for the type stubs proposal, [@AlJohri](https://github.com/AlJohri) for requesting pathlib.Path support, and [@wesleybl](https://github.com/wesleybl) for raising Python 3.10 compatibility.
