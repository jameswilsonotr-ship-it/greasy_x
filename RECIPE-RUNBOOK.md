# greasy_x — full recipe runbook (onboarding → spec-driven coding)

**Repo:** `/mnt/c/out/grokbuild/greasy_x`  
**Intent:** Evolve Easy Grok Chat Exporter into the **greasy_x** export→Stage→ingestion handoff tool, driven by meta-extraction + Grok Ingestion Work notes.

Default modes: `--mode basic` unless stated.

---

## Phase 0 — One-time setup

```bash
cd /mnt/c/out/grokbuild/greasy_x
python3 -m pip install -e ".[dev]"   # optional
python3 -m greasy_x -h
```

Read: `README.md`, `PIPELINE.md`, `docs/UPSTREAM-EASY-EXPORTER-README.md`,  
meta: `/mnt/c/out/grok-meta-extraction/README.md`, `Grok Ingestion Work/STAGE_JSONL_SCHEMA.md`.

---

## Phase 1 — Familiarize (Recipe 6 or A)

```text
/recipe-one-repo-one-pass /mnt/c/out/grokbuild/greasy_x --mode basic --focus export,stage-jsonl,ingestion
```

Or light:

```text
/recipe-new-fork-onboarding /mnt/c/out/grokbuild/greasy_x --mode basic
```

**Artifacts:** `.codebase-pass/01`–`05` (or `.fork-onboarding/`).

**Future intent to pass into Recipe 5:**

> greasy_x becomes the local CLI that (1) validates and parses `prod-grok-backend.json` with thinking traces, (2) emits Stage JSONL compatible with bunker ingestion tags, (3) optionally runs distillation/scoring/vault hydrate stubs aligned with GVG meta notes—without requiring browser automation.

---

## Phase 2 — Vision / Spec / Plan (Recipe 5)

```text
/recipe-vision-spec-plan /mnt/c/out/grokbuild/greasy_x \
  --from .codebase-pass \
  --mode medium \
  --intent "export → stage JSONL → GVG phases 1–2 MVP; later vault/memory"
```

**Artifacts:** `06-vision.md`, `06-spec.md`, `06-plan.md`, `06-design.md`, `06-iteration-loop.md`  
Seed specs already stubbed under `specs/` — **refine** them in this phase; do not invent conflicting product goals.

---

## Phase 3 — Spec-driven coding loop (per feature)

For each planned PR (e.g. “step 0 validate”, “step 7 distill stub”):

```text
/recipe-before-change /mnt/c/out/grokbuild/greasy_x
```

Then:

1. Update `specs/<feature>.md` acceptance criteria  
2. `/design` if multi-module  
3. TDD / implement (tests under `tests/`)  
4. `/review`  
5. Verify: `python -m greasy_x …` on a **small** JSON sample (never load full 1GB into flaky sessions without streaming plan)

**Suggested PR order (MVP):**

| PR | Pipeline step | Spec file |
|----|---------------|-----------|
| 1 | Step 0 validate + streaming load plan | `specs/00-validate-backend-json.md` |
| 2 | Harden Stage JSONL v0 → v1 | `specs/06-stage-jsonl.md` |
| 3 | Step 7 distillation stub | `specs/07-distillation.md` |
| 4 | Step 8 scoring hooks (optional local) | `specs/08-mediation-scoring.md` |
| 5 | Step 10 Obsidian hydrate thin | `specs/10-vault-hydrate.md` |

---

## Phase 4 — Quality / security (Recipe D, optional)

```text
/recipe-security-quality /mnt/c/out/grokbuild/greasy_x --mode basic
```

Focus: path traversal in output names, huge JSON DoS, no secret logging.

---

## Phase 5 — Integration with bunker tags

After Stage JSONL works:

- Tag outputs / docs with `#backend-export` `#stage-jsonl`  
- Link from `INGESTION-TAG-INDEX.md` under easy/greasy  
- Pair sample: `grokbuild/working/prod-grok-backend.json` (or a **slice**)

---

## Definition of done (MVP greasy_x)

- [x] Renamed product identity **greasy_x**  
- [x] Easy Exporter parse/export preserved  
- [x] Stage JSONL v0 export  
- [x] Pipeline + recipe runbook documented  
- [ ] Specs refined via Recipe 5  
- [ ] Streaming/safe load for large exports  
- [ ] At least one GVG post-export phase stub with tests  

---

## Slash cheat sheet

```text
/recipe-one-repo-one-pass /mnt/c/out/grokbuild/greasy_x --mode basic
/recipe-vision-spec-plan /mnt/c/out/grokbuild/greasy_x --from .codebase-pass --mode medium
/recipe-before-change /mnt/c/out/grokbuild/greasy_x
/recipe-security-quality /mnt/c/out/grokbuild/greasy_x
/design
/execute-plan
/review
```
