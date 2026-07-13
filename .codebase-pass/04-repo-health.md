# 04 — Repo health — greasy_x

## Strengths

- Zero runtime deps for core path  
- Clear product docs (`PIPELINE`, `RECIPE-RUNBOOK`)  
- Spec stubs already present  
- Fixture + stage smoke path  
- Single module split: legacy exporter vs new CLI  

## Gaps / risks

| Item | Severity | Note |
|------|----------|------|
| No streaming load | **High** for production use | Spec 00 |
| Few tests | Medium | Only stage unit smoke; need fixture end-to-end in CI |
| No packaging install verify in CI | Low | pyproject present, no workflow yet |
| Empty Olivia-ish dirs absent (good) | — | Cleaner than many bunker clones |
| `git` local only | Low | fine for bunker |

## Verify commands

```bash
cd /mnt/c/out/grokbuild/greasy_x
PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json -all -t -o /tmp/greasy-out
PYTHONPATH=src python3 -c "from greasy_x.cli import convert_to_stage_jsonl; print('ok')"
# when pytest installed:
# PYTHONPATH=src pytest -q
```

## Smallest safe next PR

**Spec 00 + fixture e2e test + optional `--sample N`** without NLP.  
