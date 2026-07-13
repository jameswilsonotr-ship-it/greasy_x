"""Base: stage v0 only."""
from __future__ import annotations
import json, tempfile
from pathlib import Path
from greasy_x.cli import convert_to_stage_jsonl

def test_stage_v0():
    conv = {
        "chat_id": "c1", "title": "T", "title_sanitized": "T",
        "create_time": "", "include_thinking": True,
        "responses": [{"response": {"sender": "a", "message": "m", "create_time": "", "model": "",
            "agent_thinking_traces": [{"thinking_trace": "x"}]}}],
    }
    with tempfile.TemporaryDirectory() as td:
        assert convert_to_stage_jsonl(conv, td)
        lines = (Path(td)/"T.stage.jsonl").read_text().strip().splitlines()
        assert json.loads(lines[0])["schema"] == "greasy_x.stage_jsonl.v0"
