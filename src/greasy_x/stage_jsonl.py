"""Stage JSONL writers — v0 (legacy) and v1 (aligned with STAGE_JSONL_SCHEMA concepts)."""
from __future__ import annotations

import json
import os
from typing import Any

from greasy_x import exporter as ex

SCHEMA_V0 = "greasy_x.stage_jsonl.v0"
SCHEMA_V1 = "greasy_x.stage_jsonl.v1"
# Conceptual alignment with Grok Ingestion Work STAGE_JSONL_SCHEMA.md v2.0 fields
STAGE_CANON_REF = "Grok Ingestion Work/STAGE_JSONL_SCHEMA.md#v2.0"


def convert_to_stage_jsonl_v0(processed_conv: dict, output_dir: str) -> bool:
    """Legacy header + turn records (pre-v1)."""
    if not processed_conv:
        return False
    title_sanitized = processed_conv["title_sanitized"]
    path = os.path.join(output_dir, f"{title_sanitized}.stage.jsonl")
    include_thinking = processed_conv["include_thinking"]
    try:
        with open(path, "w", encoding="utf-8") as f:
            header = {
                "record_type": "conversation_header",
                "schema": SCHEMA_V0,
                "chat_id": processed_conv["chat_id"],
                "title": processed_conv["title"],
                "create_time": processed_conv.get("create_time", ""),
                "pipeline": "greasy_x",
                "tags": ["#backend-export", "#stage-jsonl"],
            }
            f.write(json.dumps(header, ensure_ascii=False) + "\n")
            for i, resp_wrapper in enumerate(processed_conv["responses"]):
                resp = resp_wrapper.get("response", {})
                if not isinstance(resp, dict):
                    continue
                row: dict[str, Any] = {
                    "record_type": "turn",
                    "schema": SCHEMA_V0,
                    "chat_id": processed_conv["chat_id"],
                    "turn_index": i,
                    "sender": resp.get("sender", "unknown"),
                    "message": resp.get("message", ""),
                    "create_time": resp.get("create_time", ""),
                    "model": resp.get("model", ""),
                }
                if include_thinking:
                    thinking_traces = resp.get("agent_thinking_traces", [])
                    row["thinking"] = ex.extract_thinking_text(thinking_traces)
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
        return True
    except OSError as e:
        print(f"Error writing {path}: {e}")
        return False


def _empty_scoring() -> dict[str, Any]:
    return {
        "positive": {},
        "negative_flags": [],
        "overall_quality": None,
    }


def _default_personality() -> dict[str, Any]:
    return {
        "receptivity": None,
        "uninhibited_heat": None,
        "statefulness": None,
        "emotional_availability": None,
    }


def convert_to_stage_jsonl_v1(processed_conv: dict, output_dir: str) -> bool:
    """
    Emit Stage JSONL v1: one CreativeWork-shaped chunk per turn, plus optional
    full_conversation summary line. Fields map to STAGE_JSONL_SCHEMA.md core structure.
    """
    if not processed_conv:
        return False
    title_sanitized = processed_conv["title_sanitized"]
    path = os.path.join(output_dir, f"{title_sanitized}.stage.jsonl")
    include_thinking = processed_conv["include_thinking"]
    conv_id = processed_conv["chat_id"]
    title = processed_conv["title"]
    create_time = processed_conv.get("create_time") or ""

    try:
        with open(path, "w", encoding="utf-8") as f:
            # Optional conversation-level chunk (chunk_type=full_conversation)
            full_parts: list[str] = []
            for resp_wrapper in processed_conv["responses"]:
                resp = resp_wrapper.get("response", {})
                if isinstance(resp, dict) and resp.get("message"):
                    full_parts.append(
                        f"{resp.get('sender', 'unknown')}: {resp.get('message', '')}"
                    )
            full_content = "\n\n".join(full_parts)
            full_rec = {
                "@context": "https://schema.org",
                "@type": "CreativeWork",
                "id": f"{conv_id}#full",
                "conversation_id": conv_id,
                "chunk_type": "full_conversation",
                "source_platform": "grok",
                "timestamp": create_time,
                "content": full_content,
                "title": title,
                "metadata": {
                    "entities": [],
                    "coven_tags": [],
                    "date_range_active": [create_time, create_time] if create_time else [],
                    "topic_pivot_detected": False,
                    "turn_count": len(processed_conv["responses"]),
                },
                "scoring": _empty_scoring(),
                "grok_personality_markers": _default_personality(),
                "routing_signals": {
                    "suggested_silos": [],
                    "priority": "normal",
                },
                "relationships": [],
                "provenance": {
                    "ingestion_version": SCHEMA_V1,
                    "processing_pipeline": "greasy_x",
                    "axis_version": None,
                    "stage_canon_ref": STAGE_CANON_REF,
                    "tags": ["#backend-export", "#stage-jsonl"],
                },
            }
            f.write(json.dumps(full_rec, ensure_ascii=False) + "\n")

            prev_id: str | None = f"{conv_id}#full"
            for i, resp_wrapper in enumerate(processed_conv["responses"]):
                resp = resp_wrapper.get("response", {})
                if not isinstance(resp, dict):
                    continue
                msg = resp.get("message", "") or ""
                ts = resp.get("create_time", "") or create_time
                chunk_id = f"{conv_id}#turn-{i}"
                thinking = ""
                if include_thinking:
                    thinking = ex.extract_thinking_text(
                        resp.get("agent_thinking_traces", [])
                    )
                # content = spoken message; thinking kept separate for non-lossy handoff
                relationships = []
                if prev_id:
                    relationships.append(
                        {
                            "@type": "Link",
                            "target_id": prev_id,
                            "relation": "follows_from",
                            "strength": 1.0,
                        }
                    )
                rec = {
                    "@context": "https://schema.org",
                    "@type": "CreativeWork",
                    "id": chunk_id,
                    "conversation_id": conv_id,
                    "chunk_type": "atomic_message",
                    "source_platform": "grok",
                    "timestamp": ts,
                    "content": msg,
                    "metadata": {
                        "entities": [],
                        "coven_tags": [],
                        "date_range_active": [ts, ts] if ts else [],
                        "topic_pivot_detected": False,
                        "sender": resp.get("sender", "unknown"),
                        "model": resp.get("model", ""),
                        "turn_index": i,
                        "title": title,
                    },
                    "scoring": _empty_scoring(),
                    "grok_personality_markers": _default_personality(),
                    "routing_signals": {
                        "suggested_silos": [],
                        "priority": "normal",
                    },
                    "relationships": relationships,
                    "provenance": {
                        "ingestion_version": SCHEMA_V1,
                        "processing_pipeline": "greasy_x",
                        "axis_version": None,
                        "stage_canon_ref": STAGE_CANON_REF,
                        "tags": ["#backend-export", "#stage-jsonl"],
                    },
                }
                if thinking:
                    rec["thinking"] = thinking  # greasy extension (not in canon table yet)
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                prev_id = chunk_id
        return True
    except OSError as e:
        print(f"Error writing {path}: {e}")
        return False


def convert_to_stage_jsonl(
    processed_conv: dict,
    output_dir: str,
    *,
    version: str = "v1",
) -> bool:
    if version in ("v0", "0"):
        return convert_to_stage_jsonl_v0(processed_conv, output_dir)
    return convert_to_stage_jsonl_v1(processed_conv, output_dir)


def write_export_manifest(
    output_dir: str,
    *,
    source_json: str,
    exported: list[dict[str, Any]],
    stage_version: str,
    sample: int | None,
) -> str:
    """Sidecar manifest listing chats written (PR-03 / stage v1 acceptance)."""
    path = os.path.join(output_dir, "greasy_x_manifest.json")
    payload = {
        "schema": "greasy_x.export_manifest.v1",
        "source_json": source_json,
        "stage_version": stage_version,
        "sample": sample,
        "count": len(exported),
        "conversations": exported,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return path
