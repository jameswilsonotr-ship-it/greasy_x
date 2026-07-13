"""PR-01 / PR-02 tests."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from greasy_x.cli import main, validate_backend_path

FIX = Path(__file__).resolve().parent / "fixtures" / "mini-backend.json"


def test_validate_ok():
    assert validate_backend_path(str(FIX)) == 0


def test_validate_missing_conversations(tmp_path: Path):
    bad = tmp_path / "bad.json"
    bad.write_text('{"nope": 1}', encoding="utf-8")
    assert validate_backend_path(str(bad)) == 1


def test_validate_only_cli():
    assert main([str(FIX), "--validate-only"]) == 0
    assert main(["/tmp/does-not-exist-greasy.json", "--validate-only"]) == 1


def test_sample_limits_export(tmp_path: Path):
    out = tmp_path / "o"
    out.mkdir()
    rc = main(
        [
            str(FIX),
            "--sample",
            "1",
            "-stage",
            "-t",
            "-o",
            str(out),
            "--no-manifest",
        ]
    )
    assert rc == 0
    stages = list(out.glob("*.stage.jsonl"))
    assert len(stages) == 1
