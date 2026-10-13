---
name: ecommerce-visual-clone
description: Analyze premium ecommerce reference images and rebuild product visuals for Taobao-style main images and detail-page sections. Supports precision_clone and style_rebuild. Prioritizes product fidelity, editable Chinese text, and repeatable visual DNA.
---

# Ecommerce Visual Clone Skill

Use this skill when the user provides a **premium ecommerce reference image** plus their **own product image(s)** and wants a new ecommerce visual based on the reference.

## V1 scope

V1 is optimized for **Taobao product main images**. Detail-page generation is scaffolded but should not be claimed complete until its editable-text pipeline is implemented and tested.

Two modes are supported:

- `precision_clone`: preserve the reference image's broad composition, lighting direction, visual hierarchy, spacing logic, and product presentation while rebuilding the scene around the user's own product. Do not copy third-party logos, trademarked identifiers, or unique protected decorative artwork.
- `style_rebuild`: extract the reference image's visual DNA and create a new composition with the same overall design language, mood, palette, lighting, density, and commercial intent.

## Required inputs

1. Reference image path.
2. User-owned product image path.
3. Mode: `precision_clone` or `style_rebuild`.
4. Output purpose: default `taobao_main_image`.
5. Optional product facts / selling points.

If any required image is missing, stop and ask for the missing asset. Do not invent a file path.

## Preferred image generation path

Use Codex's built-in `image_gen` tool by default for image generation/editing. Do not ask for `OPENAI_API_KEY` for the built-in path.

Only use an API/CLI fallback when the user explicitly asks for it.

## Workflow

### 1. Validate inputs

Run:

```bash
python scripts/validate_inputs.py --reference <reference> --product <product>
```

Reject unreadable images and report exact errors.

### 2. Analyze the reference into Visual DNA

Inspect the reference image and product image. Create `outputs/visual_dna.json` using the schema in `references/visual_dna_schema.json`.

Capture at minimum:

- canvas ratio and dimensions
- composition / camera angle
- product placement and scale
- palette
- background type
- lighting direction / softness
- shadow characteristics
- typography zones (if present)
- negative space
- decorative elements
- perceived price tier / mood
- what must NOT be copied literally

Do not transcribe or reproduce third-party brand marks unless the user owns or explicitly authorizes them.

### 3. Build a generation brief

Run:

```bash
python scripts/build_generation_brief.py \
  --mode precision_clone \
  --visual-dna outputs/visual_dna.json \
  --product-name "<name>" \
  --output outputs/generation_brief.md
```

For `precision_clone`, instruct generation to preserve the *layout logic* while rebuilding protected or branded elements.

For `style_rebuild`, intentionally vary composition details while preserving the extracted visual language.

### 4. Generate / edit the image

Call built-in `image_gen` using:

- the reference image as visual reference;
- the user's product image as the product identity source;
- `outputs/generation_brief.md` as the structured generation instruction.

Priorities, in order:

1. Product identity and geometry.
2. Product color/pattern/material fidelity.
3. Commercial visual quality.
4. Requested mode fidelity.
5. Decorative similarity.

Never sacrifice product accuracy just to make the image prettier.

### 5. Text handling

For Chinese ecommerce text, prefer **separate editable text layout** rather than asking the image model to render dense Chinese copy.

V1 main-image rule:

- If the reference contains simple decorative text, first generate the clean visual background/product composite without that text.
- Then create a text-layout JSON from `references/text_layout_schema.json` and use a deterministic layout/compositing step where possible.
- If exact font is unavailable, choose a visually similar licensed/system font and record the substitution.

Do not invent product claims, specifications, certifications, or discounts.

### 6. Quality check

Compare generated output against the user's source product image.

Create `outputs/quality_report.json` using `references/quality_report_schema.json`.

Check:

- product shape
- product color
- product pattern / logo owned by user
- key structural details
- perspective plausibility
- background artifacts
- text accuracy
- resolution

For phone cases, explicitly check camera cutout, border, pattern placement, color, and case geometry.
For apparel, explicitly check silhouette, neckline, sleeve type, material impression, color, print, buttons and key construction details.

A result that looks attractive but materially changes the product must be marked `needs_revision`.

### 7. Save outputs

Store project assets under `outputs/` without overwriting existing files. Use versioned filenames when needed.

Recommended structure:

```text
outputs/
  visual_dna.json
  generation_brief.md
  quality_report.json
  main-image-v1.png
```

## Detail page status

`detail_page_generator` is **Phase 2**. Until implemented, analyze detail-page references and produce a structured section plan, but do not claim a complete editable long-page generator exists.

Phase 2 should use:

OCR / layout analysis → clean image generation → editable text layer → section render → long-page stitching.

## Safety / ownership / integrity

- Work from user-owned or authorized product assets.
- Do not remove watermarks or ownership marks to facilitate unauthorized reuse.
- Do not reproduce third-party brand marks or unique protected artwork as if owned by the user.
- Do not fabricate product facts.
- Clearly distinguish generated results from source/reference assets in filenames and logs.

## Completion report

At the end, report:

1. mode used;
2. files generated;
3. product-fidelity risks found;
4. any text/font substitutions;
5. whether the result is `pass`, `needs_revision`, or `manual_review`.
