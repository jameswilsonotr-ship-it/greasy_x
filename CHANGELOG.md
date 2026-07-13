# Changelog — greasy_x

## [0.2.0] - 2026-07-13

### Added — three concrete PRs

- **PR-01** `--sample N` (docs + tests): `docs/prs/PR-01-sample-n.md`
- **PR-02** `--validate-only` + shared `load_backend()`: `docs/prs/PR-02-validate-only.md`
- **PR-03** Stage JSONL **v1** (STAGE_JSONL_SCHEMA-aligned) + manifest + field map:  
  `docs/prs/PR-03-stage-jsonl-v1.md`, `docs/STAGE_FIELD_MAP.md`, `stage_jsonl.py`  
  `--stage-version v0|v1` (default v1), `--no-manifest`

## [0.1.1] - 2026-07-13

### Added

- `--sample N` — process only first N conversations (agent-safe).
- `--validate-only` — shape check for `conversations` list.
- Fixture `tests/fixtures/mini-backend.json`.
- Full Recipe 6+5 pass under `.codebase-pass/`.

## [0.1.0] - 2026-07-13

### Added

- Project **greasy_x** forked conceptually from Easy Grok Chat Exporter (`grok_exporter.py`).
- CLI: MD/TXT/JSONL export with thinking traces (upstream behavior).
- **Stage JSONL v0** export (`-stage` / included in `-all`) for `#stage-jsonl` handoff.
- `PIPELINE.md` — Easy steps 1–5 + extended steps 0, 6–13 from meta/GVG notes.
- `RECIPE-RUNBOOK.md` — Recipe 6 → 5 → before-change → implement.
- Spec stubs: `specs/00`, `06`, `07`, `08`, `10`.
- Smoke test for stage JSONL.
