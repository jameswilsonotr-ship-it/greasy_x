# 06 — Design summary — greasy_x

## Module boundaries

| Module | Responsibility | Stability |
|--------|----------------|-----------|
| `exporter.py` | Pure parse + writers; minimal CLI-free API | Keep Easy behavior; avoid big rewrites |
| `cli.py` | Argparse, formats list, stage, interactive, future subcommands | Grow carefully |
| Future `validate.py` | Shape checks, sample slicing | New |
| Future `distill.py` / `score.py` / `hydrate.py` | Pipeline stages | New packages under `greasy_x/` |

## Stage JSONL v0 record types

1. `conversation_header` — once per chat  
2. `turn` — once per response  

Schema string: `greasy_x.stage_jsonl.v0` — bump to `.v1` on breaking field renames.

## Large file strategy (chosen for MVP)

1. **`--sample N`** for agent/dev loops (implement next).  
2. Document that production full export should run as a **batch job** with enough RAM or a later ijson path.  
3. Do **not** block MVP on streaming.

## Subcommand migration (future)

When adding distill/hydrate, prefer:

```text
greasy-x export ...   # current default
greasy-x validate ...
greasy-x distill ...
```

Keep bare `greasy-x file.json -md` working for Easy UX.

## Security

- Sanitize titles for filenames (existing)  
- Refuse absolute path injection in titles  
- Never log full message bodies at debug by default  
