# greasy_x

**Grok** account-export pipeline: **thinking-aware** parse of `prod-grok-backend.json` → human formats **and** **Stage JSONL** for bunker ingestion.

| | |
|--|--|
| **Was** | [Easy Grok Chat Exporter](https://github.com/Owlock/easy-grok-chat-exporter) (`easy-grok-chat-exporter-main`) |
| **Is** | `greasy_x` under `/mnt/c/out/grokbuild/greasy_x` |
| **Meta basis** | `grok-meta-extraction` + GVG five-pass notes + `Grok Ingestion Work` |

```text
prod-grok-backend.json
        │
        ▼
   greasy_x (steps 5–6)
   MD / TXT / JSONL / Stage JSONL  (+ thinking)
        │
        ▼
   planned GVG / ingestion steps 7–13
   distill → score → graph → vault → memory
```

## Why greasy_x

Easy Exporter already did something no browser tool did well: **export thinking traces** offline from official backend JSON. Meta conversation + ingestion tags say the **next** job is not more formats alone — it is **handoff into Stage JSONL / memory pipeline**. greasy_x keeps the Easy core and **adds those steps** as product surface + specs.

## Quick start

```bash
cd /mnt/c/out/grokbuild/greasy_x
PYTHONPATH=src python3 -m greasy_x -i
# or
PYTHONPATH=src python3 -m greasy_x /path/to/prod-grok-backend.json -stage -t -o ./out
PYTHONPATH=src python3 -m greasy_x /path/to/prod-grok-backend.json -all -t -o ./out
```

| Flag | Meaning |
|------|---------|
| `-md` / `-txt` / `-jsonl` | Human / flat AI import formats (Easy lineage) |
| `-stage` | **Stage JSONL** for `#stage-jsonl` handoff (default **v1**) |
| `--stage-version v0\|v1` | Stage schema (v1 = STAGE_JSONL_SCHEMA-aligned) |
| `-all` | md + txt + jsonl + stage |
| `-t` | Include thinking traces |
| `-i` | Interactive |
| `--sample N` | Only first N conversations (**PR-01**) |
| `--validate-only` | Check `conversations[]` shape; no export (**PR-02**) |
| `--no-manifest` | Skip `greasy_x_manifest.json` sidecar |

Concrete PR write-ups: [`docs/prs/`](./docs/prs/).

**Zero runtime dependencies** for current features (stdlib only).

## Docs

| Doc | Purpose |
|-----|---------|
| [`PIPELINE.md`](./PIPELINE.md) | Full step list (Easy 1–5 + greasy 0,5–13) |
| [`RECIPE-RUNBOOK.md`](./RECIPE-RUNBOOK.md) | Recipe 6 → 5 → C → implement |
| [`specs/`](./specs/) | Spec-driven feature stubs |
| [`docs/UPSTREAM-EASY-EXPORTER-README.md`](./docs/UPSTREAM-EASY-EXPORTER-README.md) | Original Easy guide |
| Meta | `/mnt/c/out/grok-meta-extraction/` |
| Tags | `grokbuild/TAG-TOC.md` · `INGESTION-TAG-INDEX.md` |

## Full recipe process

```text
/recipe-one-repo-one-pass /mnt/c/out/grokbuild/greasy_x --mode basic
/recipe-vision-spec-plan /mnt/c/out/grokbuild/greasy_x --from .codebase-pass --mode medium
```

Then implement per `RECIPE-RUNBOOK.md` + `specs/`.

## License

MIT (upstream Easy Exporter lineage).
