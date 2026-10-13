#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path
from PIL import Image

ALLOWED = {"JPEG", "PNG", "WEBP"}

def inspect(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    if not path.is_file():
        raise ValueError(f"Not a file: {path}")
    with Image.open(path) as im:
        im.verify()
    with Image.open(path) as im:
        fmt = (im.format or "").upper()
        if fmt not in ALLOWED:
            raise ValueError(f"Unsupported image format {fmt!r}: {path}")
        width, height = im.size
    if width < 128 or height < 128:
        raise ValueError(f"Image too small ({width}x{height}): {path}")
    return {"path": str(path), "format": fmt, "width": width, "height": height}

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--reference", required=True)
    p.add_argument("--product", required=True)
    args = p.parse_args()
    result = {
        "ok": True,
        "reference": inspect(Path(args.reference)),
        "product": inspect(Path(args.product)),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
