# AGENTS — greasy_x

## Product

Offline Grok **backend JSON** exporter → human formats + **Stage JSONL** for ingestion.  
Composio/Rube not required for core parse. Optional later: Drive for archive drop (`#overnight-sync`).

## Before changing code

1. Read `PIPELINE.md` and the matching `specs/*.md`.
2. Prefer smallest PR from RECIPE-RUNBOOK order.
3. Do not load multi-GB `prod-grok-backend.json` into agents whole — use samples or streaming design (spec 00).
4. Thinking-trace extraction is a **flagship** feature — regression tests should cover it.

## Recipe chain

- Familiarize: `/recipe-one-repo-one-pass`  
- Future plan: `/recipe-vision-spec-plan`  
- Per feature: `/recipe-before-change` → implement → `/review`  
- Optional: `/recipe-security-quality` on parsers

## Related bunker paths

- Meta: `/mnt/c/out/grok-meta-extraction/`  
- Ingestion design: `/mnt/c/out/grokbuild/Grok Ingestion Work/`  
- Sample data: `/mnt/c/out/grokbuild/working/prod-grok-backend.json` (huge)
