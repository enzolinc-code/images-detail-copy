# Ecommerce Visual Clone Skill

Codex Skill prototype for rebuilding premium ecommerce visuals from a reference image while preserving the user's own product identity.

## V0.1 focus

- Taobao-style main images
- `precision_clone` and `style_rebuild`
- Visual DNA JSON
- generation brief builder
- deterministic input validation
- quality-report schema
- Phase-2 scaffold for editable-text detail pages

## Why this architecture

V0.1 intentionally uses Codex's built-in image generation/editing path first. It avoids forcing a heavy local diffusion stack before the workflow has been validated on real ecommerce samples.

Optional future enhancement layers:

- IP-Adapter for stronger reference-image style/subject guidance
- ControlNet for depth/edge/layout structure control
- ComfyUI for local graph-based batch pipelines
- Fabric.js/Vue editor for editable visual/text templates

## Quick start in Codex

1. Put the skill folder in a Codex-accessible workspace/repository.
2. Provide a premium reference image and your own product image.
3. Ask:

```text
Use ecommerce-visual-clone in precision_clone mode.
Reference: references/my-reference.jpg
Product: references/my-product.png
Purpose: Taobao main image.
Keep my product geometry/color/pattern accurate. Do not copy third-party logos.
```

4. Codex should validate assets, create Visual DNA, build a generation brief, call built-in image generation/editing, and generate a quality report.

## Development status

- [x] Skill orchestration specification
- [x] Dual-mode definitions
- [x] Input validation script
- [x] Visual DNA schema
- [x] generation brief builder
- [x] quality report schema
- [x] basic automated tests
- [ ] real reference/product pair image-generation acceptance test
- [ ] deterministic Chinese text compositor
- [ ] OCR + long detail-page section reconstruction
- [ ] batch mode
- [ ] visual style library UI

## Important

This repository does not claim that pixel-perfect product fidelity can be guaranteed by a generative model. Product fidelity is treated as a quality gate and may require iterative generation or manual review.
