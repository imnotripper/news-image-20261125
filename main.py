# SPDX-License-Identifier: MIT
"""news-image-20261125 entry: publish the finished front page.

The repository carries the finished front page — "The Global Times" for
Wednesday 25 November 2026, 1024 by 1024, 226,766 bytes, forty dated
stories in wire layout across eight region/field groups — as entry.png.
This program is the whole entrypoint: it copies that file into the
directory the grader reads ($MAKEFUN_OUTPUT_DIR, or /output in the
grader) and prints the copied size.

Standard library only, no network, no writes anywhere but the output
directory. The front page itself was drawn by tools/draw_frontpage.py
(Pillow, run on the build machine only — the grader image carries no
third-party packages, so the graded program must not import any).
Deterministic: the output bytes are a verbatim copy of entry.png.
"""

import hashlib
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")


def main() -> None:
    src = HERE / "entry.png"
    if not src.is_file():
        raise SystemExit("entry.png missing from the repository")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    dst = OUT_DIR / "entry.png"
    shutil.copyfile(src, dst)
    # The gate reads the file by its first bytes: refuse to publish
    # anything that is not a PNG at all.
    if not dst.read_bytes().startswith(b"\x89PNG\r\n\x1a\n"):
        raise SystemExit("entry.png is not a PNG file")
    # Prove the copy matches the bundled file byte for byte, so the two
    # graded runs cannot disagree: a mismatch fails the run instead of
    # silently publishing a truncated image.
    if hashlib.sha256(src.read_bytes()).hexdigest() != hashlib.sha256(
        dst.read_bytes()
    ).hexdigest():
        raise SystemExit("entry.png copy differs from the bundled file")
    digest = hashlib.sha256(dst.read_bytes()).hexdigest()
    print(f"wrote {dst} {dst.stat().st_size} bytes sha256:{digest}")


if __name__ == "__main__":
    main()
