---
name: naming
description: "Create naming conventions and a name-generating grammar for a fantasy world's peoples, places, and characters. Use when the user wants names, naming conventions, a naming system, place-names, person-names, or asks \"what should I call this city/character\", \"generate names\", \"how do these people name things\", \"make it sound consistent\" — triggers include \"naming conventions\", \"generate names\", \"name grammar\", \"place names\", \"character names\", \"what to call\", \"sounds for this culture\". Reads worldstate/peoples.v1.md (and existing names in realms.v1.md) and writes worldstate/naming.v1.md: a phonaesthetic grammar per people (syllable inventory, permitted clusters, person vs place patterns) plus sample names. Not a full conlang. Do NOT use for the gods, myths, or calendar."
---

# /naming — a naming grammar per people

Inputs:
!`grep -E '- id:|name:|traits:|subsistence:' worldstate/peoples.v1.md 2>/dev/null | head -50 || echo "MISSING peoples.v1 — run /populate first"`
Existing names to stay consistent with:
!`grep -E 'name:|- \{id: (city|realm)' worldstate/realms.v1.md 2>/dev/null | head -40`

You build a lightweight phonaesthetic grammar (not a conlang) so new names sound like they belong. Contract: `worldstate/SCHEMA.md` (`naming.v1`). Reference: `references/naming-grammar.md`.

## Step 1 — Guard
peoples.v1 required. If realms.v1 exists, EXTRACT the existing names (cities, realms, NPCs) for each people and reverse-engineer the grammar so new names match what's already canon — do not contradict established names.

## Step 2 — Build a grammar per people
For each `ppl-` id, define:
- `syllables`: `onsets` (permitted initial consonants/clusters), `nuclei` (vowels/diphthongs), `codas` (permitted final consonants). Pick a phonaesthetic that fits the culture (harsh stops for a harsh people; liquid/open sounds for a maritime one) and matches existing canon names.
- `forbidden_clusters`: combinations that never occur (keeps output consistent).
- `person_pattern`: syllable shape + morphology (patronymics, honorifics, gendered endings).
- `place_pattern`: place-name morphology (geography suffixes like -mark/-fjord/-gate; compound patterns).
- `samples`: 4–6 `people` names and 4–6 `places`, generated from the grammar, including at least the already-canon ones to prove consistency.

## Step 3 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Every people in peoples.v1 has a grammar.
- Existing canon names (from realms.v1) are GENERATED-COMPATIBLE with their people's grammar — flag and reconcile any that aren't.
- Distinct peoples have distinguishable phonaesthetics (you can tell at a glance which people a name belongs to).
- Samples actually obey the stated onsets/nuclei/codas and forbidden clusters.

## Step 4 — Write and hand off
Write `worldstate/naming.v1.md` (YAML + `## Naming by people` prose with a note on how to coin a new name). Append to `LOG.md`. Downstream skills (`/oracle`, `/rumour-table`) can use these grammars to name new NPCs and places consistently.
