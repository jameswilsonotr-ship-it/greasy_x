# 01 — Explore map — greasy_x

**mode=basic**  
**recipe=one-repo-one-pass (6)**  
**path=`/mnt/c/out/grokbuild/greasy_x`**  
**focus=export, stage-jsonl, ingestion**

## What it is

Python package **greasy_x**: offline CLI that reads xAI **account export** `prod-grok-backend.json`, exports conversations to human formats (MD/TXT/JSONL) with optional **thinking traces**, and emits **Stage JSONL v0** for bunker ingestion handoff.

**Lineage:** Easy Grok Chat Exporter (`Owlock/easy-grok-chat-exporter` → local `easy-grok-chat-exporter-main`).  
**Extended by:** meta-extraction GVG five-pass notes + `Grok Ingestion Work` Stage/memory design.

## Tree (product-relevant)

```text
greasy_x/
  README.md · PIPELINE.md · RECIPE-RUNBOOK.md · AGENTS.md
  pyproject.toml          # package greasy-x, entry greasy-x
  src/greasy_x/
    __init__.py · __main__.py
    exporter.py           # Easy lineage: parse, MD/TXT/JSONL, thinking
    cli.py                # CLI + Stage JSONL + interactive
  specs/                  # 00, 06, 07, 08, 10 stubs
  tests/
    test_stage_jsonl.py
    fixtures/mini-backend.json
  docs/UPSTREAM-EASY-EXPORTER-README.md
```

## Entrypoints

| Entry | Role |
|-------|------|
| `python -m greasy_x` / `greasy-x` | CLI (`cli.main`) |
| `exporter.load_conversations` | Load `conversations[]` |
| `exporter.process_conversation` | One chat → structured dict |
| `cli.convert_to_stage_jsonl` | Stage handoff |

## Languages / deps

- Python ≥3.9, **stdlib only** for current features  
- Optional `dev`: pytest  

## Related bunker systems

- Tags: `#backend-export` `#stage-jsonl` `#ingestion-pipeline`  
- Meta: `/mnt/c/out/grok-meta-extraction/`  
- Design: `grokbuild/Grok Ingestion Work/`  
- Sample giant JSON: `grokbuild/working/prod-grok-backend.json` (do not load whole into agent)  
