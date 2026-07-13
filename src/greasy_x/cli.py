"""greasy_x CLI — base (export + stage v0)."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from greasy_x import exporter as ex


def convert_to_stage_jsonl(processed_conv: dict, output_dir: str) -> bool:
    if not processed_conv:
        return False
    title_sanitized = processed_conv["title_sanitized"]
    path = os.path.join(output_dir, f"{title_sanitized}.stage.jsonl")
    include_thinking = processed_conv["include_thinking"]
    try:
        with open(path, "w", encoding="utf-8") as f:
            header = {
                "record_type": "conversation_header",
                "schema": "greasy_x.stage_jsonl.v0",
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
                row = {
                    "record_type": "turn",
                    "schema": "greasy_x.stage_jsonl.v0",
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


def run_export(json_file, formats, include_thinking, output_dir, sample=None):
    os.makedirs(output_dir, exist_ok=True)
    conversations = ex.load_conversations(json_file)
    if not conversations:
        return 1
    total_all = len(conversations)
    if sample is not None:
        if sample < 0:
            print("Error: --sample N must be >= 0")
            return 2
        conversations = conversations[:sample]
        print(f"[greasy_x] --sample {sample}: using {len(conversations)} of {total_all}")
    total = len(conversations)
    ok_conv = skipped = 0
    print(f"[greasy_x] Processing {total} conversations...")
    for conv in conversations:
        processed_conv = ex.process_conversation(conv, include_thinking)
        if not processed_conv:
            skipped += 1
            continue
        wrote = False
        for fmt in formats:
            if fmt == "md":
                wrote = ex.convert_to_markdown(processed_conv, output_dir) or wrote
            elif fmt == "txt":
                wrote = ex.convert_to_text(processed_conv, output_dir) or wrote
            elif fmt == "jsonl":
                wrote = ex.convert_to_jsonl(processed_conv, output_dir) or wrote
            elif fmt == "stage":
                wrote = convert_to_stage_jsonl(processed_conv, output_dir) or wrote
        if wrote:
            ok_conv += 1
        else:
            skipped += 1
    print(f"Exported OK: {ok_conv}  Skipped: {skipped}  Out: {output_dir}")
    return 0


def interactive():
    print("greasy_x interactive")
    default_path = str(Path.cwd() / "prod-grok-backend.json")
    json_file = input(f"JSON path [{default_path}]: ").strip() or default_path
    formats = ["md"]
    include_thinking = False
    return json_file, formats, include_thinking


def main(argv=None):
    parser = argparse.ArgumentParser(prog="greasy-x")
    parser.add_argument("json_file", nargs="?")
    parser.add_argument("-o", "--output-dir")
    parser.add_argument("-md", "--markdown", action="store_true")
    parser.add_argument("-txt", "--text", action="store_true")
    parser.add_argument("-jsonl", "--jsonlines", action="store_true")
    parser.add_argument("-stage", "--stage-jsonl", action="store_true")
    parser.add_argument("-all", "--all-formats", action="store_true")
    parser.add_argument("-t", "--thinking", action="store_true")
    parser.add_argument("-i", "--interactive", action="store_true")
    parser.add_argument(
        "--sample",
        type=int,
        default=None,
        metavar="N",
        help="Only process first N conversations (safe for large exports / agent loops)",
    )
    args = parser.parse_args(argv)
    sample = args.sample
    if args.interactive or not args.json_file:
        json_file, formats, include_thinking = interactive()
    else:
        json_file = args.json_file
        include_thinking = args.thinking
        if args.all_formats:
            formats = ["md", "txt", "jsonl", "stage"]
        else:
            formats = []
            if args.markdown: formats.append("md")
            if args.text: formats.append("txt")
            if args.jsonlines: formats.append("jsonl")
            if args.stage_jsonl: formats.append("stage")
            if not formats: formats = ["md"]
    output_dir = args.output_dir or os.path.dirname(os.path.abspath(json_file)) or "."
    return run_export(json_file, formats, include_thinking, output_dir, sample=sample)


if __name__ == "__main__":
    raise SystemExit(main())
