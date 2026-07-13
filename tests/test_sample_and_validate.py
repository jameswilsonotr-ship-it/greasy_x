from pathlib import Path
from greasy_x.cli import main, validate_backend_path

FIX = Path(__file__).resolve().parent / "fixtures" / "mini-backend.json"

def test_validate_ok():
    assert validate_backend_path(str(FIX)) == 0

def test_validate_missing_conversations(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text('{"nope": 1}', encoding="utf-8")
    assert validate_backend_path(str(bad)) == 1

def test_sample_limits_export(tmp_path):
    out = tmp_path / "o"
    out.mkdir()
    rc = main([str(FIX), "--sample", "1", "-stage", "-o", str(out)])
    assert rc == 0
    assert len(list(out.glob("*.stage.jsonl"))) == 1
