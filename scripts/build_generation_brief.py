#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path

VALID_MODES = {"precision_clone", "style_rebuild"}

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", required=True, choices=sorted(VALID_MODES))
    p.add_argument("--visual-dna", required=True)
    p.add_argument("--product-name", default="user product")
    p.add_argument("--selling-point", action="append", default=[])
    p.add_argument("--output", required=True)
    args = p.parse_args()
    dna = load_json(Path(args.visual_dna))

    if args.mode == "precision_clone":
        mode_text = (
            "Preserve the reference's broad spatial hierarchy, camera relationship, lighting logic, "
            "background category, negative-space distribution, and commercial emphasis. Rebuild rather "
            "than literally copy branded/protected details."
        )
    else:
        mode_text = (
            "Preserve the visual DNA (palette, mood, lighting, density, perceived price tier and product "
            "presentation language) while creating a meaningfully new composition and scene."
        )

    selling_points = "\n".join(f"- {x}" for x in args.selling_point) or "- No unverified claims."
    palette = ", ".join(dna.get("palette", [])) or "derive from reference"
    exclusions = "\n".join(f"- {x}" for x in dna.get("literal_copy_exclusions", [])) or "- Third-party logos / protected unique artwork"

    brief = f"""# Ecommerce Image Generation Brief\n\n## Mode\n{args.mode}\n\n{mode_text}\n\n## Product\n{args.product_name}\n\nThe user's product image is the identity source. Preserve its geometry, color, pattern, material cues, proportions and key construction details. Do not beautify by changing the product itself.\n\n## Reference Visual DNA\n- Style: {dna.get('style_name', 'derived from reference')}\n- Mood: {dna.get('mood', 'derived from reference')}\n- Background: {dna.get('background', 'derived from reference')}\n- Palette: {palette}\n- Price tier: {dna.get('perceived_price_tier', 'derived from reference')}\n\n## Verified selling points\n{selling_points}\n\n## Literal-copy exclusions\n{exclusions}\n\n## Generation priorities\n1. Product fidelity.\n2. Correct perspective and physically plausible contact/shadows.\n3. Commercial-quality composition.\n4. Mode fidelity.\n5. Clean background with no accidental text or logos.\n\n## Text rule\nDo not render dense Chinese marketing copy inside the generated image. Leave intended text zones clean for deterministic text composition later.\n\n## Output\nGenerate a clean ecommerce-ready main image. Do not add unsupported specifications, certifications, discount claims, brand logos, watermarks or third-party marks.\n"""
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(brief, encoding="utf-8")
    print(str(out))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
