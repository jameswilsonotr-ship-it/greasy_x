# Three concrete PRs (stacked)

All implemented on working tree 2026-07-13. Split into git branches if/when publishing:

1. `feat/pr-01-sample-n` → docs/prs/PR-01-sample-n.md  
2. `feat/pr-02-validate-only` → docs/prs/PR-02-validate-only.md  
3. `feat/pr-03-stage-jsonl-v1` → docs/prs/PR-03-stage-jsonl-v1.md  

Suggested stack order: 01 → 02 → 03 (02 shares load_backend with 01; 03 depends on export path).
