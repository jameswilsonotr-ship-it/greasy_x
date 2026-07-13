# Spec 06 — Stage JSONL (pipeline step 6)

## Status

- **v0** — implemented (legacy header/turn)  
- **v1** — implemented (STAGE_JSONL_SCHEMA-aligned CreativeWork chunks) — **default**

## v0 behavior

- Per conversation: one `conversation_header` line + N `turn` lines  
- Schema id: `greasy_x.stage_jsonl.v0`  
- Optional `thinking` on turns when `-t`  
- CLI: `--stage-version v0`

## v1 behavior

- Per conversation: one `full_conversation` chunk + N `atomic_message` chunks  
- Schema id: `greasy_x.stage_jsonl.v1`  
- Core fields from `STAGE_JSONL_SCHEMA.md`: id, conversation_id, chunk_type, source_platform, timestamp, content, metadata, scoring placeholders, personality placeholders, routing_signals, relationships, provenance  
- `thinking` extension when `-t`  
- Manifest: `greasy_x_manifest.json`  
- Mapping: `docs/STAGE_FIELD_MAP.md`  
- PR: `docs/prs/PR-03-stage-jsonl-v1.md`

## Acceptance (v1)

- [x] Documented mapping table Easy JSON → Stage fields  
- [x] Fixture / unit tests for shape  
- [x] Entry in INGESTION-TAG-INDEX under greasy_x  

## References

- `Grok Ingestion Work/STAGE_JSONL_SCHEMA.md`  
- Meta GVG Phase 1 blueprint (distilled state block)  
