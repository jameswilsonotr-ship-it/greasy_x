# 02 — Onboarding — greasy_x

## Day-1

1. **Install / run**
   ```bash
   cd /mnt/c/out/grokbuild/greasy_x
   PYTHONPATH=src python3 -m greasy_x -h
   PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json -all -t -o /tmp/greasy-out
   ```
2. **Get real data:** Grok settings → request export → unzip → `prod-grok-backend.json`.
3. **Read:** `README.md`, `PIPELINE.md` (steps), `RECIPE-RUNBOOK.md` (how agents work this repo).
4. **Do not** open the full GB sample in an editor; use fixtures or `--sample` (planned, spec 00).

## Mental model

| Layer | Job |
|-------|-----|
| Human steps 1–4 | Obtain export file |
| Step 5 (code) | Pretty export + thinking |
| Step 6 (code) | Stage JSONL for memory pipeline |
| Steps 7–13 | Spec-driven future (GVG / vault / Letta) |

## Success criteria for a new contributor

- Export fixture with `-stage -t` and open `*.stage.jsonl`  
- Know where Easy code lives (`exporter.py`) vs extensions (`cli.py`)  
- Can name next PR from RECIPE-RUNBOOK table  
