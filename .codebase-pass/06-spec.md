# 06 — Spec — greasy_x requirements

## Functional

### F1 — Parse official backend JSON (as-is + harden)

- **Given** a path to JSON with `conversations`  
- **When** user runs greasy_x  
- **Then** conversations with title + responses export; others skipped with counts  

### F2 — Thinking traces

- **Given** `-t` and `agent_thinking_traces`  
- **Then** MD/TXT/JSONL/Stage include thinking text  

### F3 — Human formats

- MD, TXT, flat JSONL as Easy Exporter  

### F4 — Stage JSONL v0 (done) / v1

- Header + turns; schema id; tags; chat_id  
- v1: map to `STAGE_JSONL_SCHEMA.md` fields where possible  

### F5 — Validate / sample (MVP next)

- `--sample N` process only first N conversations  
- Validate shape before full work; non-zero exit on bad file  

### F6 — Distillation stub (post-MVP)

- CLI subcommand or `greasy-x distill` reading stage → phase_1 jsonl skeleton  

### F7 — Scoring dry-run (post-MVP)

- Pluggable scorer; default pass-through  

### F8 — Vault hydrate (later)

- Optional notes with frontmatter  

## Non-functional

- Core path: **no required third-party deps**  
- NLP/graph: optional extras only  
- Safe filenames (no path traversal)  
- Deterministic CLI for scripting  

## Interfaces

```text
greasy-x INPUT.json [-md|-txt|-jsonl|-stage|-all] [-t] [-o DIR] [--sample N]
greasy-x -i
# future:
greasy-x validate INPUT.json
greasy-x distill --input DIR_OR_FILE --output DIR
greasy-x hydrate --vault PATH --input STAGE
```
