# Easy backend JSON → Stage JSONL v1 field map

Canonical stage shape: `Grok Ingestion Work/STAGE_JSONL_SCHEMA.md` (v2.0 concepts).  
Emitter: `greasy_x.stage_jsonl` schema id `greasy_x.stage_jsonl.v1`.

## Per atomic_message chunk

| Stage field | Source |
|-------------|--------|
| `@context` | constant `https://schema.org` |
| `@type` | constant `CreativeWork` |
| `id` | `{conversation_id}#turn-{i}` |
| `conversation_id` | `conversation.id` |
| `chunk_type` | `atomic_message` |
| `source_platform` | `grok` |
| `timestamp` | response `create_time` or conversation `create_time` |
| `content` | response `message` |
| `metadata.sender` | response `sender` |
| `metadata.model` | response `model` |
| `metadata.turn_index` | loop index |
| `metadata.title` | conversation `title` |
| `metadata.entities` | `[]` (later extractors) |
| `metadata.coven_tags` | `[]` |
| `scoring.*` | empty placeholders (Phase 2 sieve) |
| `grok_personality_markers.*` | null placeholders |
| `routing_signals` | default priority `normal` |
| `relationships` | link to previous chunk `follows_from` |
| `provenance` | greasy_x + stage canon ref |
| `thinking` | `agent_thinking_traces` (extension) |

## Per full_conversation chunk

| Stage field | Source |
|-------------|--------|
| `id` | `{conversation_id}#full` |
| `chunk_type` | `full_conversation` |
| `content` | joined `sender: message` turns |
| `timestamp` | conversation `create_time` |

## Manifest

`greasy_x_manifest.json`: list of exported chats, source path, stage version, sample N.
