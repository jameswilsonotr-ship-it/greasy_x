# PR-02 — `--validate-only`

## Summary

Add **`--validate-only`**: load JSON, require root object with **`conversations` list**, exit non-zero otherwise. No export.

## Motivation

Catch wrong files early (e.g. Prometheus `grok_exporter` logs, empty dumps) without writing outputs.

## Changes

- CLI: `--validate-only` (requires `json_file`)
- Shared `load_backend()` used by validate + export (single validation path)
- Clear error if `conversations` missing
- Test: bad JSON / missing key

## Acceptance

- [x] Valid fixture → exit 0 + `validate OK` line with count  
- [x] `{"nope":1}` → exit 1, mentions missing `conversations`  
- [x] Missing file → exit 1  
- [x] Documented in README  

## Test

```bash
PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json --validate-only
echo '{"nope":1}' > /tmp/bad.json
PYTHONPATH=src python3 -m greasy_x /tmp/bad.json --validate-only ; echo exit=$?
```

## Out of scope

- Deep per-conversation schema validation  
- Streaming validate without full load  
