# 06 — Plan — greasy_x phased work

## Phase MVP (now → next sessions)

| # | Task | Spec | Depends |
|---|------|------|---------|
| M1 | Fixture mini-backend + e2e smoke | — | done |
| M2 | `--sample N` + light validate | 00 | M1 |
| M3 | Stage v0 tests in pytest + e2e | 06 | M1 |
| M4 | Register greasy_x in INGESTION-TAG-INDEX | meta | M3 |
| M5 | Update meta COMPARISON (done row) | meta | done |

## Phase v0.2 — Stage v1 + safe load

| # | Task | Spec |
|---|------|------|
| V1 | Align stage fields with STAGE_JSONL_SCHEMA | 06 |
| V2 | Streaming/ijson **or** documented chunk strategy | 00 |
| V3 | Manifest sidecar listing chats | 06 |

## Phase v0.3 — GVG 1–2 stubs

| # | Task | Spec |
|---|------|------|
| G1 | Distill stub CLI | 07 |
| G2 | Dry-run scorer interface | 08 |

## Phase later

| # | Task | Spec |
|---|------|------|
| L1 | Obsidian hydrate | 10 |
| L2 | Overnight resume scaffold | PIPELINE 13 |
| L3 | Memory MCP handoff docs only or thin bridge | 12 |

## Dependencies / order

```text
M1 → M2 → M3 → M4
M3 → V1 → V2
M3 → G1 → G2
G2 → L1 (optional)
```

## Effort guess

- M2–M3: small (hours)  
- V1–V2: medium  
- G1–G2: medium  
- L*: large / optional  
