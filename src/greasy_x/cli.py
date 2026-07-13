"""greasy_x CLI — Grok export + extended pipeline steps."""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any

from greasy_x import exporter as ex
from greasy_x.stage_jsonl import convert_to_stage_jsonl, write_export_manifest


def load_backend(json_file: str) -> tuple[list | None, str | None]:
    """
    Load and validate backend JSON once.
    Returns (conversations, error_message). conversations is None on failure.
    """
    path = Path(json_file)
    if not path.is_file():
        return None, f"Error: file not found: {json_file}"
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return None, f"Error: invalid JSON: {e}"
    except OSError as e:
        return None, f"Error: cannot read file: {e}"
    if not isinstance(data, dict):
        return None, "Error: root JSON value must be an object"
    if "conversations" not in data:
        return (
            None,
            "Error: missing 'conversations' key — not a prod-grok-backend-style export "
            "(do not use Prometheus grok_exporter logs here)",
        )
    if not isinstance(data["conversations"], list):
        return None, "Error: 'conversations' must be a list"
    return data["conversations"], None


def validate_backend_path(json_file: str) -> int:
    """Light validate: file exists and top-level looks like backend export."""
    conversations, err = load_backend(json_file)
    if err:
        print(err)
        return 1
    assert conversations is not None
    print(f"[greasy_x] validate OK: {json_file}  conversations={len(conversations)}")
    return 0


def run_export(
    json_file: str,
    formats: list[str],
    include_thinking: bool,
    output_dir: str,
    sample: int | None = None,
    stage_version: str = "v1",
    write_manifest: bool = True,
) -> int:
    os.makedirs(output_dir, exist_ok=True)
    conversations, err = load_backend(json_file)
    if err:
        print(err)
        return 1
    assert conversations is not None

    total_all = len(conversations)
    print(f"[greasy_x] validate OK: {json_file}  conversations={total_all}")
    if sample is not None:
        if sample < 0:
            print("Error: --sample N must be >= 0")
            return 2
        conversations = conversations[:sample]
        print(f"[greasy_x] --sample {sample}: using {len(conversations)} of {total_all}")

    total = len(conversations)
    ok_conv = 0
    skipped = 0
    exported_meta: list[dict[str, Any]] = []
    print()
    print(f"[greasy_x] Processing {total} conversations...")
    print(f"  formats: {', '.join(formats)}")
    print(f"  thinking: {'yes' if include_thinking else 'no'}")
    if "stage" in formats:
        print(f"  stage schema: {stage_version}")
    print(f"  out: {output_dir}")
    print()

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
                wrote = (
                    convert_to_stage_jsonl(
                        processed_conv, output_dir, version=stage_version
                    )
                    or wrote
                )
        if wrote:
            ok_conv += 1
            exported_meta.append(
                {
                    "chat_id": processed_conv["chat_id"],
                    "title": processed_conv["title"],
                    "title_sanitized": processed_conv["title_sanitized"],
                    "stage_file": f"{processed_conv['title_sanitized']}.stage.jsonl"
                    if "stage" in formats
                    else None,
                }
            )
        else:
            skipped += 1

    manifest_path = None
    if write_manifest and exported_meta:
        manifest_path = write_export_manifest(
            output_dir,
            source_json=os.path.abspath(json_file),
            exported=exported_meta,
            stage_version=stage_version if "stage" in formats else "n/a",
            sample=sample,
        )

    print("--- greasy_x export report ---")
    print(f"Total conversations: {total}")
    print(f"Exported OK: {ok_conv}")
    print(f"Skipped: {skipped}")
    print(f"Output directory: {output_dir}")
    if manifest_path:
        print(f"Manifest: {manifest_path}")
    return 0


def interactive() -> tuple[str, list[str], bool]:
    print("=" * 60)
    print("greasy_x — Grok export pipeline")
    print("=" * 60)
    default_path = str(Path.cwd() / "prod-grok-backend.json")
    json_file = input(f"Path to prod-grok-backend.json\n[default: {default_path}]: ").strip()
    if not json_file:
        json_file = default_path
    if not os.path.exists(json_file):
        print(f"Error: File '{json_file}' not found.")
        sys.exit(1)
    print()
    print("Select output format:")
    print("1. Markdown (.md)")
    print("2. Plain Text (.txt)")
    print("3. JSON Lines (.jsonl) — per-turn flat")
    print("4. Stage JSONL (.stage.jsonl) — ingestion handoff")
    print("5. All formats (md + txt + jsonl + stage)")
    choice = input("Enter choice [1-5] (default: 1): ").strip()
    if choice == "2":
        formats = ["txt"]
    elif choice == "3":
        formats = ["jsonl"]
    elif choice == "4":
        formats = ["stage"]
    elif choice == "5":
        formats = ["md", "txt", "jsonl", "stage"]
    else:
        formats = ["md"]
    print()
    print("Include AI thinking traces?")
    print("1. No")
    print("2. Yes")
    thinking_choice = input("Enter choice [1-2] (default: 1): ").strip()
    include_thinking = thinking_choice == "2"
    return json_file, formats, include_thinking


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="greasy-x",
        description="greasy_x: Grok backend JSON export + Stage JSONL handoff (Easy Exporter lineage)",
    )
    parser.add_argument("json_file", nargs="?", help="Path to prod-grok-backend.json")
    parser.add_argument("-o", "--output-dir", help="Output directory")
    parser.add_argument("-md", "--markdown", action="store_true")
    parser.add_argument("-txt", "--text", action="store_true")
    parser.add_argument("-jsonl", "--jsonlines", action="store_true")
    parser.add_argument(
        "-stage",
        "--stage-jsonl",
        action="store_true",
        help="Emit Stage JSONL for ingestion (#stage-jsonl)",
    )
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
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Only validate backend JSON shape (requires conversations[]); do not export",
    )
    parser.add_argument(
        "--stage-version",
        choices=("v0", "v1"),
        default="v1",
        help="Stage JSONL schema version (default: v1, STAGE_JSONL-aligned)",
    )
    parser.add_argument(
        "--no-manifest",
        action="store_true",
        help="Do not write greasy_x_manifest.json sidecar",
    )
    args = parser.parse_args(argv)

    if args.validate_only:
        if not args.json_file:
            print("Error: json_file required with --validate-only")
            return 2
        return validate_backend_path(args.json_file)

    if args.interactive or not args.json_file:
        json_file, formats, include_thinking = interactive()
        sample = args.sample
    else:
        json_file = args.json_file
        include_thinking = args.thinking
        sample = args.sample
        if args.all_formats:
            formats = ["md", "txt", "jsonl", "stage"]
        else:
            formats = []
            if args.markdown:
                formats.append("md")
            if args.text:
                formats.append("txt")
            if args.jsonlines:
                formats.append("jsonl")
            if args.stage_jsonl:
                formats.append("stage")
            if not formats:
                formats = ["md"]

    output_dir = args.output_dir or os.path.dirname(os.path.abspath(json_file)) or "."
    return run_export(
        json_file,
        formats,
        include_thinking,
        output_dir,
        sample=sample,
        stage_version=args.stage_version,
        write_manifest=not args.no_manifest,
    )


if __name__ == "__main__":
    raise SystemExit(main())
