# Spec 08 — Mediation / scoring (pipeline step 8 / GVG Phase 2)

## Status

**Planned**

## Goal

Score segments (essence / emotion axes) using local models where possible; emit `phase_2_mediated_corpus.jsonl`.  
Align with `Grok Ingestion Work/SCORING_AND_AXES.md` and meta essence > 0.5 threshold concept.

## Constraints

- Optional heavy deps behind extra extras (`pip install greasy-x[nlp]`)  
- Core greasy_x remains zero-dep without this feature  

## Acceptance

- [ ] Pluggable scorer interface  
- [ ] Dry-run scorer that tags all turns score=1.0 for plumbing tests  
