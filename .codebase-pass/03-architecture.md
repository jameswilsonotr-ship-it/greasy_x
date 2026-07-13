# 03 — Architecture — greasy_x

## C4 context

```text
[User] --requests export--> [xAI / Grok]
[User] --downloads--> prod-grok-backend.json
[User] --runs--> [greasy_x CLI]
[greasy_x] --writes--> files (MD/TXT/JSONL/Stage)
[Stage JSONL] --feeds--> [Ingestion / GVG / Letta] (downstream, mostly out of process today)
```

## C4 container

```text
┌─────────────────────────────────────────┐
│ greasy_x (Python package)               │
│  cli.py     — argparse, stage, UX       │
│  exporter.py— parse + format writers    │
└─────────────────────────────────────────┘
         │
         ▼
   filesystem outputs
```

## Data flow (as-is)

1. `json.load` entire file → `data["conversations"]`  
2. For each conv: require `conversation` + `responses`; skip empty title/responses  
3. Optional: extract `agent_thinking_traces` → thinking text  
4. Write per-format files under `-o` dir  
5. Stage: header record + turn records (`greasy_x.stage_jsonl.v0`)

## To-be (planned containers)

| Component | Pipeline step | Notes |
|-----------|---------------|--------|
| Validator / streamer | 0 | Avoid full-load GB JSON |
| Distiller | 7 | GVG phase 1 |
| Scorer | 8 | optional NLP extra |
| Hydrator | 10 | Obsidian notes |
| Memory bridge | 12 | MCP / Letta |

## Risks

- Full `json.load` on ~1GB export  
- Upstream export schema drift  
- Double-count metrics in original Easy loop (exported formats × conv) — greasy_x counts conversations with any write  
