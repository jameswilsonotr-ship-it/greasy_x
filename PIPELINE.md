# greasy_x — full pipeline steps

**Lineage:** Easy Grok Chat Exporter (`grok_exporter.py`) + meta-extraction notes  
**Tags:** `#backend-export` `#stage-jsonl` `#ingestion-pipeline` `#memory-architecture`  
**Sources:**  
- `/mnt/c/out/easy-grok-chat-exporter-main`  
- `/mnt/c/out/grok-meta-extraction/` (esp. `approaches/02`, `05`, `ingestison neotes.txt` GVG five passes)  
- `/mnt/c/out/grokbuild/Grok Ingestion Work/` (STAGE_JSONL, scoring, multi-Letta)

---

## A. User export path (upstream of code) — Easy Exporter steps 1–5

These remain the **human** prerequisites (from upstream README):

| Step | Action |
|-----:|--------|
| **1** | Request data from Grok (settings → export) |
| **2** | Download + unzip account export package |
| **3** | Locate `prod-grok-backend.json` |
| **4** | Install greasy_x (this repo) |
| **5** | Run export CLI (MD / TXT / JSONL / Stage, ± thinking) |

---

## B. greasy_x product steps (code) — **extended** from meta notes

| Step | Name | Status | Output / tag |
|-----:|------|--------|--------------|
| **0** | **Validate backend JSON** | **partial** (`--validate-only`, `--sample N`) | Full stream still planned |
| **5** | **Parse + export human formats** | **implemented** (Easy lineage) | `.md` / `.txt` / `.jsonl` + thinking |
| **6** | **Emit Stage JSONL** | **implemented (v1 default, v0 flag)** | `*.stage.jsonl` + manifest → `#stage-jsonl` |
| **7** | **Distillation (backward-first)** | planned | `phase_1_distilled_state.jsonl` — GVG Phase 1 |
| **8** | **Mediation / scoring sieve** | planned | `phase_2_mediated_corpus.jsonl` — essence axes (`SCORING_AND_AXES`) |
| **9** | **Chunk + graph extract** | planned | `phase_3_knowledge_graph.json` — optional |
| **10** | **Vault hydrate (Obsidian)** | planned | frontmatter MD notes — `#obsidian-vault` |
| **11** | **Rule / negative mining + visual anchors** | planned | golden rules JSON — GVG Phase 5 |
| **12** | **Memory handoff** | planned | Letta / multi-silo / MCP — `#memory-architecture` `#mcp-orchestration` |
| **13** | **Overnight / resume scaffold** | planned | cron + `RESUME_SCAFFOLD_*.md` — `#overnight-sync` |

**Implemented today:** steps **0 (partial), 5–6** (validate/sample, parse/export, stage v1).  
**Spec-driven roadmap:** stream load + steps **7–13** in `specs/` + Recipe 5/6 artifacts.

---

## C. Mapping to meta conversation (GVG five passes)

| GVG pass | greasy_x step | Notes |
|----------|---------------|--------|
| Phase 1 Distillation | 7 | After Stage JSONL exists |
| Phase 2 Mediation / NLP | 8 | RoBERTa/essence > 0.5 concepts from notes |
| Phase 3 Graph | 9 | Optional neuro-symbolic |
| Phase 4 Obsidian hydrate | 10 | Pairs with recipe Obsidian skills |
| Phase 5 Rules / visuals | 11 | Optional; not MVP |

Easy Exporter alone stopped at “pretty files.” greasy_x **starts the handoff** into the ingestion/memory stack.

---

## CLI (current)

```bash
# from repo
PYTHONPATH=src python3 -m greasy_x /path/to/prod-grok-backend.json --validate-only
PYTHONPATH=src python3 -m greasy_x /path/to/prod-grok-backend.json --sample 5 -stage -t -o ./out
PYTHONPATH=src python3 -m greasy_x /path/to/prod-grok-backend.json -md -t
PYTHONPATH=src python3 -m greasy_x /path/to/prod-grok-backend.json -stage --stage-version v1 -t -o ./out
PYTHONPATH=src python3 -m greasy_x /path/to/prod-grok-backend.json -all -t -o ./out
PYTHONPATH=src python3 -m greasy_x -i
```

Zero extra runtime deps for steps 5–6 (stdlib only).

---

## D. Full **recipe process** for this repo (agent workflow)

See [`RECIPE-RUNBOOK.md`](./RECIPE-RUNBOOK.md).

Order:

1. Recipe **A** or **6** — familiarize greasy_x  
2. Recipe **5** — vision/spec/plan for steps 0 + 7–13  
3. Spec-driven coding (`specs/` + `/design` + `/execute-plan` or recipe **C** per feature)  
4. Recipe **D** optional — security/quality before shipping parsers of GB-scale JSON  
