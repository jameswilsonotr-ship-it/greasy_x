# Spec 10 — Obsidian vault hydrate (pipeline step 10 / GVG Phase 4)

## Status

**Planned**

## Goal

Turn mediated/stage records into vault notes with YAML frontmatter + wikilinks.  
Pairs with `/recipe-connect-vault-mcp` Obsidian skills.

## Acceptance

- [ ] `greasy-x hydrate --vault PATH --input stage.jsonl`  
- [ ] Frontmatter includes chat_id, tags, create_time  
- [ ] Safe filenames (reuse exporter sanitizer)  
