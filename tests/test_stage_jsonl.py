"""PR-03 Stage JSONL v0/v1 tests."""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from greasy_x.stage_jsonl import convert_to_stage_jsonl


def _conv(include_thinking: bool = True) -> dict:
    return {
        "chat_id": "c1",
        "title": "Hello World",
        "title_sanitized": "Hello World",
        "create_time": "2026-01-01T00:00:00Z",
        "include_thinking": include_thinking,
        "responses": [
            {
                "response": {
                    "sender": "user",
                    "message": "hi",
                    "create_time": "2026-01-01T00:00:01Z",
                    "model": "",
                    "agent_thinking_traces": [],
                }
            },
            {
                "response": {
                    "sender": "assistant",
                    "message": "hello",
                    "create_time": "2026-01-01T00:00:02Z",
                    "model": "grok",
                    "agent_thinking_traces": [{"thinking_trace": "reason..."}],
                }
            },
        ],
    }


def test_stage_v0_header_and_turn():
    with tempfile.TemporaryDirectory() as td:
        assert convert_to_stage_jsonl(_conv(), td, version="v0")
        path = Path(td) / "Hello World.stage.jsonl"
        lines = path.read_text(encoding="utf-8").strip().splitlines()
        assert len(lines) == 3
        h = json.loads(lines[0])
        assert h["record_type"] == "conversation_header"
        assert h["schema"] == "greasy_x.stage_jsonl.v0"
        t1 = json.loads(lines[2])
        assert t1["thinking"] == "reason..."


def test_stage_v1_creative_work_shape():
    with tempfile.TemporaryDirectory() as td:
        assert convert_to_stage_jsonl(_conv(), td, version="v1")
        path = Path(td) / "Hello World.stage.jsonl"
        lines = path.read_text(encoding="utf-8").strip().splitlines()
        # full + 2 turns
        assert len(lines) == 3
        full = json.loads(lines[0])
        assert full["@type"] == "CreativeWork"
        assert full["chunk_type"] == "full_conversation"
        assert full["conversation_id"] == "c1"
        assert full["source_platform"] == "grok"
        assert "scoring" in full and "provenance" in full
        turn = json.loads(lines[2])
        assert turn["chunk_type"] == "atomic_message"
        assert turn["content"] == "hello"
        assert turn["thinking"] == "reason..."
        assert turn["relationships"][0]["relation"] == "follows_from"
