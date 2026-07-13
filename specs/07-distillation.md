# Spec 07 — Distillation (pipeline step 7 / GVG Phase 1)

## Status

**Planned**

## Goal

Backward-first chronological pass over Stage JSONL → `phase_1_distilled_state.jsonl`  
(PII sanitize hooks, unified blocks — per meta notes.)

## Non-goals (MVP)

- Full RoBERTa scoring (step 8)  
- Graph extraction (step 9)

## Acceptance

- [ ] Stub CLI `greasy-x distill --input ... --output ...`  
- [ ] Blueprint fields documented vs meta conversation example  
- [ ] Tests on synthetic stage lines  
