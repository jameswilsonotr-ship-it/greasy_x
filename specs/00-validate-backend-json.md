# Spec 00 — Validate backend JSON (pipeline step 0)

## Status

**Partial — implemented:** `--validate-only`, shape check, `--sample N`  
**Still planned:** streaming / ijson for GB files  

## Problem

`prod-grok-backend.json` can be GB-scale and schema-drifting. Loading full file with `json.load` is fragile for agents and laptops.

## Requirements

1. Detect presence of `conversations` key (or document alternate shapes). **done**
2. Optional `--sample N` first N conversations for dry runs. **done**
3. Optional streaming / ijson path for large files (may add optional dep). **open**
4. Clear errors for wrong file type (e.g. Prometheus grok_exporter logs). **done**

## Acceptance

- [x] CLI exits non-zero with readable message on bad shape  
- [x] Unit tests with tiny fixture under `tests/fixtures/`  
- [x] Doc link from PIPELINE.md step 0 / README  
- [ ] Streaming load without full RAM  

## PRs

- `docs/prs/PR-01-sample-n.md`  
- `docs/prs/PR-02-validate-only.md`  

## References

- `grok-meta-extraction/DATA-SHAPES.md`  
- `grok-meta-extraction/approaches/02-official-backend-json.md`  
