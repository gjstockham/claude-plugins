---
name: mythology
description: "Write myths, legends, creation stories, and folklore for a fantasy world's cultures. Use when the user wants myths, legends, creation stories, folklore, culture-hero tales, or asks \"what's their creation myth\", \"legends of this people\", \"how they explain the flood/mountain/stars\" — triggers include \"mythology\", \"creation myth\", \"legends\", \"folklore\", \"hero cycle\", \"origin story\", \"what myths\". Reads worldstate/pantheon.v1.md, peoples.v1.md, climate.v1.md, and history.v1.md and writes worldstate/mythology.v1.md: creation, etiological, hero-cycle, and eschatological myths, each tied to an existing deity, people, and a real geographic/climatic fact or historical event. Do NOT use for the gods' stat-blocks (that is /pantheon), the calendar, or naming."
---

# /mythology — the stories cultures tell

Inputs (pantheon + peoples strongly recommended):
!`grep -E '- id:|name:|domains:|patron_of:' worldstate/pantheon.v1.md 2>/dev/null | head -40 || echo "run /pantheon first for god-linked myths"`
!`grep -E '- id:|name:|traits:|migration_seed:' worldstate/peoples.v1.md 2>/dev/null | head -40 || echo "MISSING peoples.v1"`
!`grep -E 'id:|notes:|biome:' worldstate/climate.v1.md 2>/dev/null | head -40`
!`grep -E 'id:|type:|effect:|justifies:' worldstate/history.v1.md 2>/dev/null | head -30`

You write myths that explain the world's real features. Contract: `worldstate/SCHEMA.md` (`mythology.v1`). Principle: a coastal culture has a flood myth; a mountain culture a forge myth; a people born from catastrophe has a myth of that catastrophe. Every myth `explains:` something that actually exists in the world state.

## Step 1 — Guard
peoples.v1 required. pantheon.v1 lets myths name real gods; climate.v1/history.v1 give the facts to explain. Use only existing `ppl-`/`god-`/`reg-`/`evt-` ids; mint `myth-` ids.

## Step 2 — Pick facts that beg explanation
Scan the world state for striking facts: a dramatic biome (a desert on open water, a lone green river through dead land), a people's origin/migration (a drought-scattered diaspora, a seafaring colonisation), a historical trauma (a collapse, a great war), a distinctive custom (river burials). Each is a seed for a myth.

## Step 3 — Write myths (mix the four types)
For each seed, write a myth with a `type`:
- **creation** — how the world/this land/this people began.
- **etiological** — why a specific feature is the way it is (why the desert is dry, why the river floods, why the north is cold).
- **hero-cycle** — a culture hero's deeds (founding a city, crossing the desert, defeating a rival people — often mirroring a real history event).
- **eschatological** — how it will end (a returning drought, a final flood).
Tie each to `peoples`, `deities`, and set `explains:` to the concrete fact (reference a reg- or evt- id where possible). Different peoples may explain the SAME fact differently — contradictory myths are realistic and a feature.

## Step 4 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Every myth `explains:` a fact that actually exists in climate.v1/history.v1/peoples.v1 (SCHEMA rule 9 — cite real ids).
- Deities named are real pantheon.v1 gods with fitting domains (a flood myth invokes a water/river god).
- Myths fit each people's environment and history (no desert people with a native ice-giant creation myth unless justified by migration).
- Where two peoples explain one fact, the versions are consistent with their differing values.

## Step 5 — Write and hand off
Write `worldstate/mythology.v1.md` (YAML + `## Myths of the peoples` prose). Append to `LOG.md`.
