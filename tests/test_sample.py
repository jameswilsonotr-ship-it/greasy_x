from pathlib import Path
from greasy_x.cli import main

FIX = Path(__file__).resolve().parent / "fixtures" / "mini-backend.json"

def test_sample_limits(tmp_path):
    out = tmp_path / "o"
    out.mkdir()
    assert main([str(FIX), "--sample", "1", "-stage", "-o", str(out)]) == 0
    assert len(list(out.glob("*.stage.jsonl"))) == 1
