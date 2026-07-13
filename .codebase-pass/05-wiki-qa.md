# 05 — Wiki Q&A (evidence-based)

**Q1. What file is the main input?**  
`prod-grok-backend.json` with top-level `conversations` array (`exporter.load_conversations`).

**Q2. Where are thinking traces read from?**  
Each response dict: `agent_thinking_traces` → `extract_thinking_text` looking for `thinking_trace` fields.

**Q3. What is Stage JSONL for?**  
Handoff to bunker ingestion (`#stage-jsonl`): conversation header + per-turn records (`cli.convert_to_stage_jsonl`), schema `greasy_x.stage_jsonl.v0`.

**Q4. What is implemented vs planned?**  
Implemented: human export + stage v0 (steps 5–6). Planned: validate/stream (0), GVG distill/score/graph/vault/rules/memory/overnight (7–13) per `PIPELINE.md`.

**Q5. How does greasy_x relate to Easy Exporter?**  
Same parse/export core (copied to `exporter.py`); rebranded product with pipeline + specs + stage output; upstream README preserved under `docs/`.

**Q6. What should not be confused with this tool?**  
Prometheus `grok_exporter` (metrics) — `#name-collision-not-chat`. Live DOM userscripts (enhanced-grok-export). Offline zip Android suite (Groxxporter).
