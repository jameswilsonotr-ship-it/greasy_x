# PR-01 — `--sample N`

## Summary

Add/document **`--sample N`** so greasy_x only processes the first N conversations. Safe for multi-GB exports and agent loops.

## Motivation

Full `prod-grok-backend.json` can be ~1GB. Agents and quick tests must not always walk every conversation.

## Changes

- CLI: `--sample N` (N ≥ 0)
- Logs: `using K of TOTAL`
- Docs: README flag table
- Test: sample limits export count

## Acceptance

- [x] `--sample 1` on fixture with 2 convs exports exactly 1 chat’s files  
- [x] Documented in README  
- [x] Invalid negative N rejected  

## Test

```bash
cd /mnt/c/out/grokbuild/greasy_x
PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json --sample 1 -stage -o /tmp/pr01
# expect 1 conversation worth of stage file + manifest count 1
```

## Out of scope

- Streaming parse (later)
- Random sampling
