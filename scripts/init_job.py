#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--reference", required=True)
    p.add_argument("--product", required=True)
    p.add_argument("--mode", required=True, choices=["precision_clone", "style_rebuild"])
    p.add_argument("--purpose", default="taobao_main_image")
    p.add_argument("--output", default="outputs/job.json")
    args = p.parse_args()
    data = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "reference": args.reference,
        "product": args.product,
        "mode": args.mode,
        "purpose": args.purpose,
        "status": "initialized"
    }
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(str(out))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
