"""Generate minimal binary test fixtures for formats lacking real files.

Usage:
    uv run python scripts/generate_fixtures.py

Creates files in tests/files/ for each format that can be generated
either from command-line tools or from minimal valid headers.
"""

import os
import struct
import subprocess
import tempfile

FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "..", "tests", "files")


def write_fixture(name, data):
    path = os.path.join(FIXTURES_DIR, name)
    with open(path, "wb") as f:
        f.write(data)
    print(f"  {name} ({len(data)} bytes)")
    return path


def generate_with_tool(name, cmd, input_data=None):
    """Run a shell command to generate a fixture."""
    path = os.path.join(FIXTURES_DIR, name)
    try:
        result = subprocess.run(cmd, input=input_data, capture_output=True, timeout=10)
        if result.returncode == 0 and os.path.exists(path):
            size = os.path.getsize(path)
            print(f"  {name} ({size} bytes) [tool]")
            return path
        elif result.stdout:
            with open(path, "wb") as f:
                f.write(result.stdout)
            print(f"  {name} ({len(result.stdout)} bytes) [tool/stdout]")
            return path
        else:
            print(f"  {name} FAILED: {result.stderr.decode()[:100]}")
            return None
    except FileNotFoundError:
        print(f"  {name} SKIPPED (tool not found)")
        return None


# --- Tool-generated fixtures ---


def gen_bzip2():
    return generate_with_tool(
        "test.bz2",
        ["bzip2", "-c"],
        input_data=b"Hello, this is test data for binaryornot.\n" * 10,
    )


def gen_zstd():
    return generate_with_tool(
        "test.zst",
        ["zstd", "-c", "-q"],
        input_data=b"Hello, this is test data for binaryornot.\n" * 10,
    )


def gen_webp():
    png_path = os.path.join(FIXTURES_DIR, "logo.png")
    out_path = os.path.join(FIXTURES_DIR, "logo.webp")
    return generate_with_tool(
        "logo.webp",
        ["cwebp", "-q", "50", png_path, "-o", out_path],
    )


def gen_mp4():
    """Generate a minimal MP4 with ffmpeg (1 frame, tiny resolution)."""
    out_path = os.path.join(FIXTURES_DIR, "test.mp4")
    return generate_with_tool(
        "test.mp4",
        [
            "ffmpeg",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "color=c=red:s=8x8:d=0.1",
            "-c:v",
            "libx264",
            "-pix_fmt",
            "yuv420p",
            out_path,
        ],
    )


def gen_mp3():
    """Generate a minimal MP3 with ffmpeg (short sine wave)."""
    out_path = os.path.join(FIXTURES_DIR, "test.mp3")
    return generate_with_tool(
        "test.mp3",
        [
            "ffmpeg",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "sine=frequency=440:duration=0.1",
            "-c:a",
            "libmp3lame",
            "-b:a",
            "32k",
            out_path,
        ],
    )


def gen_matroska():
    """Generate a minimal WebM with ffmpeg."""
    out_path = os.path.join(FIXTURES_DIR, "test.webm")
    return generate_with_tool(
        "test.webm",
        [
            "ffmpeg",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "color=c=blue:s=8x8:d=0.1",
            "-c:v",
            "libvpx-vp9",
            out_path,
        ],
    )


def gen_heif():
    """Generate a minimal HEIF with heif-enc if available."""
    png_path = os.path.join(FIXTURES_DIR, "logo.png")
    out_path = os.path.join(FIXTURES_DIR, "logo.heic")
    result = generate_with_tool(
        "logo.heic",
        ["heif-enc", "-q", "50", png_path, "-o", out_path],
    )
    if result:
        return result
    # Fallback: minimal ftyp box
    ftyp = struct.pack(">I", 24) + b"ftyp" + b"heic" + struct.pack(">I", 0) + b"heic"
    mdat = struct.pack(">I", 16) + b"mdat" + b"\x00" * 8
    return write_fixture("logo.heic", ftyp + mdat + b"\x00" * 80)


def gen_git_pack():
    """Generate a real git pack file from a temporary repo."""
    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.run(["git", "init", tmpdir], capture_output=True)
        test_file = os.path.join(tmpdir, "test.txt")
        with open(test_file, "w") as f:
            f.write("test content\n")
        subprocess.run(["git", "-C", tmpdir, "add", "."], capture_output=True)
        subprocess.run(
            ["git", "-C", tmpdir, "commit", "-m", "test", "--allow-empty"],
            capture_output=True,
            env={
                **os.environ,
                "GIT_AUTHOR_NAME": "test",
                "GIT_AUTHOR_EMAIL": "test@test",
                "GIT_COMMITTER_NAME": "test",
                "GIT_COMMITTER_EMAIL": "test@test",
            },
        )
        # Pack all objects
        result = subprocess.run(
            ["git", "-C", tmpdir, "pack-objects", "--all", "--stdout"],
            capture_output=True,
        )
        if result.stdout[:4] == b"PACK":
            return write_fixture("test.pack", result.stdout)
    print("  test.pack FAILED")
    return None


# --- Python-generated minimal fixtures ---


def gen_woff2():
    """Minimal WOFF2: signature + valid header fields."""
    # WOFF2 header: signature(4) + flavor(4) + length(4) + numTables(2) + ...
    data = b"wOF2"  # signature
    data += b"\x00\x01\x00\x00"  # flavor (TrueType)
    data += struct.pack(">I", 128)  # length
    data += struct.pack(">H", 1)  # numTables
    data += b"\x00" * 110  # padding to 128 bytes
    return write_fixture("test.woff2", data)


def gen_ole2():
    """Minimal OLE2/CFB header."""
    # CFB header is 512 bytes, first 8 are the signature
    data = bytes.fromhex("d0cf11e0a1b11ae1")  # signature
    data += struct.pack("<H", 0x003E)  # minor version
    data += struct.pack("<H", 0x0003)  # major version
    data += struct.pack("<H", 0xFFFE)  # byte order (little-endian)
    data += struct.pack("<H", 0x0009)  # sector size power (512)
    data += b"\x00" * (128 - len(data))  # pad to 128
    return write_fixture("test.doc", data)


def gen_rar():
    """Minimal RAR5 signature + archive header."""
    data = bytes.fromhex("526172211a0700")  # RAR5 signature
    data += b"\x00" * (128 - len(data))
    return write_fixture("test.rar", data)


def gen_midi():
    """Minimal valid MIDI file: header + one empty track."""
    # MThd chunk
    data = b"MThd"
    data += struct.pack(">I", 6)  # header length
    data += struct.pack(">H", 0)  # format 0
    data += struct.pack(">H", 1)  # 1 track
    data += struct.pack(">H", 96)  # 96 ticks per quarter
    # MTrk chunk (empty track with end-of-track event)
    track_data = b"\x00\xff\x2f\x00"  # delta=0, meta event, end of track
    data += b"MTrk"
    data += struct.pack(">I", len(track_data))
    data += track_data
    return write_fixture("test.mid", data)


def gen_psd():
    """Minimal PSD header."""
    data = b"8BPS"  # signature
    data += struct.pack(">H", 1)  # version
    data += b"\x00" * 6  # reserved
    data += struct.pack(">H", 3)  # channels (RGB)
    data += struct.pack(">I", 1)  # height
    data += struct.pack(">I", 1)  # width
    data += struct.pack(">H", 8)  # bits per channel
    data += struct.pack(">H", 3)  # color mode (RGB)
    data += b"\x00" * (128 - len(data))
    return write_fixture("test.psd", data)


def gen_parquet():
    """Minimal Parquet file: magic + empty metadata + magic."""
    data = b"PAR1"  # magic
    # Minimal footer (empty schema, 0 rows)
    footer = b"\x00" * 50
    data += footer
    data += struct.pack("<I", len(footer))  # footer length
    data += b"PAR1"  # trailing magic
    data += b"\x00" * (128 - len(data))
    return write_fixture("test.parquet", data)


def gen_dex():
    """Minimal DEX header."""
    data = b"dex\n039\x00"  # magic (DEX version 039)
    data += struct.pack("<I", 0)  # checksum
    data += b"\x00" * 20  # SHA-1 hash
    data += struct.pack("<I", 128)  # file size
    data += struct.pack("<I", 0x70)  # header size
    data += b"\x00" * (128 - len(data))
    return write_fixture("test.dex", data)


def gen_llvm_bc():
    """Minimal LLVM bitcode wrapper."""
    data = bytes.fromhex("4243c0de")  # magic
    data += b"\x00" * 124  # padding
    return write_fixture("test.bc", data)


def gen_7z():
    """Try 7z tool, fall back to minimal header."""
    with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as f:
        f.write(b"test content\n")
        tmp = f.name
    out_path = os.path.join(FIXTURES_DIR, "test.7z")
    result = generate_with_tool("test.7z", ["7z", "a", out_path, tmp])
    os.unlink(tmp)
    if result:
        return result
    # Fallback: minimal 7z signature
    data = bytes.fromhex("377abcaf271c")  # signature
    data += b"\x00" * (128 - len(data))
    return write_fixture("test.7z", data)


def main():
    print("Generating test fixtures...")
    results = {}

    generators = [
        ("woff2", gen_woff2),
        ("webp", gen_webp),
        ("mp4", gen_mp4),
        ("mp3_id3", gen_mp3),
        ("bzip2", gen_bzip2),
        ("7z", gen_7z),
        ("ole2", gen_ole2),
        ("zstd", gen_zstd),
        ("rar", gen_rar),
        ("matroska", gen_matroska),
        ("midi", gen_midi),
        ("psd", gen_psd),
        ("heif", gen_heif),
        ("parquet", gen_parquet),
        ("dex", gen_dex),
        ("llvm_bc", gen_llvm_bc),
        ("git_pack", gen_git_pack),
    ]

    for name, gen in generators:
        path = gen()
        if path:
            # Store relative path from project root
            results[name] = os.path.relpath(path, os.path.join(FIXTURES_DIR, "..", ".."))

    print(f"\nGenerated {len(results)}/{len(generators)} fixtures.")
    print("\nCSV test_file values:")
    for name, path in results.items():
        print(f"  {name}: {path}")


if __name__ == "__main__":
    main()
