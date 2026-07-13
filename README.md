# greasy_x

Offline Grok export CLI: `prod-grok-backend.json` → MD/TXT/JSONL + Stage JSONL v0 (thinking traces).

```bash
cd /mnt/c/out/grokbuild/greasy_x
PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json -all -t -o ./out
PYTHONPATH=src python3 -m greasy_x -i
```

| Flag | Meaning |
|------|---------|
| `-md` / `-txt` / `-jsonl` | Human / flat formats |
| `-stage` | Stage JSONL v0 handoff |
| `-all` | md + txt + jsonl + stage |
| `-t` | Thinking traces |
| `-i` | Interactive |

See `PIPELINE.md`, `RECIPE-RUNBOOK.md`.
