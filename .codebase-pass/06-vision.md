# 06 — Vision — greasy_x

**mode=medium** (vision/spec/plan)  
**Intent (stated):** Export → Stage JSONL → GVG phases 1–2 MVP; later vault/memory.

## North star

**greasy_x** is the local, offline **first mile** of bunker Grok memory:

1. Reliably ingest **official account exports** (including thinking traces).  
2. Emit **Stage JSONL** that the rest of the ingestion stack can consume without re-parsing GB JSON.  
3. Grow **optional** post-export phases (distill, score, vault) behind clear specs—without turning the core CLI into a mandatory ML stack.

## Users

| User | Need |
|------|------|
| Operator (you) | One command: export + stage from download zip |
| Ingestion / Letta work | Stable stage records, tags, chat ids |
| Agents (Grok Build) | Specs + small fixtures; never require loading full export |

## Non-goals (near term)

- Live browser scrape (use enhanced-grok-export)  
- Android offline zip suite (Groxxporter)  
- Full multi-Letta orchestration inside greasy_x process  
- Composio required for core path  

## Success metrics

- Fixture + sample path always green in <1s  
- Real export: produce stage files without OOM on workstation (stream/sample strategy)  
- Stage schema documented and linked from INGESTION-TAG-INDEX  
- MVP: steps **0, 5, 6, 7 stub, 8 dry scorer** before vault  
