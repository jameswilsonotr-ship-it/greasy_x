# 06 — Iteration loop — greasy_x

## Branch strategy

- `main` / local master: always runnable fixture export  
- Feature branches: `feat/sample-n`, `feat/stage-v1`, `feat/distill-stub`  

## Definition of done (per PR)

1. Spec section updated or checkbox ticked  
2. Fixture still exports  
3. New tests if behavior added  
4. README/PIPELINE one-line if user-facing flag  

## Verify

```bash
cd /mnt/c/out/grokbuild/greasy_x
PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json -all -t -o /tmp/greasy-out
PYTHONPATH=src python3 -m greasy_x tests/fixtures/mini-backend.json --sample 1 -stage -o /tmp/greasy-s
# pytest when available
PYTHONPATH=src python3 -m pytest -q tests/
```

## After plan approval

```text
/recipe-before-change /mnt/c/out/grokbuild/greasy_x
```

First concrete feature: **M2 `--sample N` + validate**.  
