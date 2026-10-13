import json
import subprocess
import sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

def run(*args):
    return subprocess.run([sys.executable, *map(str, args)], cwd=ROOT, capture_output=True, text=True)

def test_validate_inputs(tmp_path):
    a = tmp_path / "a.png"
    b = tmp_path / "b.png"
    Image.new("RGB", (800, 800), "white").save(a)
    Image.new("RGB", (900, 900), "black").save(b)
    r = run(ROOT / "scripts/validate_inputs.py", "--reference", a, "--product", b)
    assert r.returncode == 0, r.stderr
    data = json.loads(r.stdout)
    assert data["ok"] is True
    assert data["reference"]["width"] == 800

def test_build_generation_brief(tmp_path):
    dna = ROOT / "examples/visual_dna.example.json"
    out = tmp_path / "brief.md"
    r = run(ROOT / "scripts/build_generation_brief.py", "--mode", "style_rebuild", "--visual-dna", dna, "--product-name", "test product", "--output", out)
    assert r.returncode == 0, r.stderr
    text = out.read_text(encoding="utf-8")
    assert "style_rebuild" in text
    assert "test product" in text
    assert "Product fidelity" in text
