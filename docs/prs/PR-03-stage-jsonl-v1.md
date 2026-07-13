# PR-03 — Stage JSONL v1 (STAGE_JSONL_SCHEMA-aligned)

## Summary

Emit **Stage JSONL v1** chunks shaped like `Grok Ingestion Work/STAGE_JSONL_SCHEMA.md` (CreativeWork / chunk fields), plus export **manifest** sidecar. Keep **v0** via `--stage-version v0`.

## Mapping (Easy → Stage v1)

| Easy / greasy field | Stage v1 field |
|---------------------|----------------|
| conversation.id | `conversation_id` |
| chat_id + `#turn-i` | `id` |
| message text | `content` |
| create_time | `timestamp` |
| — | `source_platform`: `"grok"` |
| turn vs full | `chunk_type`: `atomic_message` / `full_conversation` |
| thinking traces | `thinking` (greasy extension) |
| — | `scoring` / `grok_personality_markers` placeholders for later sieve |
| — | `provenance.processing_pipeline`: `greasy_x` |
| follows previous | `relationships[]` `follows_from` |

## Changes

- New module `src/greasy_x/stage_jsonl.py`
- Default `--stage-version v1`
- Optional `--stage-version v0` legacy
- `greasy_x_manifest.json` listing exported chats (disable with `--no-manifest`)
- Spec `specs/06-stage-jsonl.md` updated
- Mapping doc `docs/STAGE_FIELD_MAP.md`
- Tests for v1 shape + v0 still works

## Acceptance

- [x] Fixture `-stage` produces lines with `@type`, `chunk_type`, `conversation_id`, `content`  
- [x] Mapping table documented  
- [x] Fixture round-trip / shape tests  
- [x] greasy_x listed under ingestion tags  

## Test

```bash
PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json -stage -t -o /tmp/pr03
head -1 /tmp/pr03/*.stage.jsonl | python3 -m json.tool | head -40
cat /tmp/pr03/greasy_x_manifest.json
PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json -stage --stage-version v0 -o /tmp/pr03v0
```
