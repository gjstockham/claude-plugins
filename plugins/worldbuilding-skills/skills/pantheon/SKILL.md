---
name: pantheon
description: "Create gods, deities, religions, and a pantheon for a fantasy world, with domains, temples, and patron realms. Use when the user wants gods, deities, a pantheon, religion, faiths, divine domains, temples, or asks \"who do they worship\", \"create the gods\", \"design a religion\" — triggers include \"pantheon\", \"create gods\", \"deities\", \"religion\", \"what gods\", \"divine domains\", \"temples\", \"who do people pray to\". Reads worldstate/realms.v1.md and worldstate/peoples.v1.md and writes worldstate/pantheon.v1.md: deities with 1d4 shared-able domains, values, symbols, patron realms/peoples, and temples. Guarantees every realm and people has at least one patron deity and every capital a temple. Do NOT use for myths and creation stories (that is /mythology), the calendar, or naming."
---

# /pantheon — the gods and who worships them

Inputs (must exist):
!`grep -E 'id:|name:|capital:|peoples:|government:' worldstate/realms.v1.md 2>/dev/null | head -60 || echo "MISSING realms.v1 — run /realms-and-borders first"`
!`grep -E 'id:|name:|subsistence:|traits:' worldstate/peoples.v1.md 2>/dev/null | head -50 || echo "MISSING peoples.v1"`
World tone/focus:
!`grep -E 'tone|focus|physical|cultural' worldstate/world.v1.md 2>/dev/null | head`

You build a coverage-guaranteed pantheon. Contract: `worldstate/SCHEMA.md` (`pantheon.v1`). Domain lists and the values-based "color pie" scaffold: `references/pantheon-design.md`. Religions "explain the unexplainable" and "provide hope and purpose" — tie each god to real world facts (a people's subsistence, a region's danger, a historical trauma).

## Step 1 — Guard
If realms.v1 or peoples.v1 is missing, STOP and name the skill. Use only existing `realm-`/`ppl-`/`city-` ids; mint `god-` ids.

## Step 2 — Pass 1: create gods organically
Create 5–9 deities rooted in the world. For each, roll/pick **1d4 domains** (see reference) — domains MAY be shared across gods and a god may hold several, so avoid the "one god per domain" cliché. Give `values` (an ethos, not a D&D alignment), a `symbol`, and initial `patron_of` (the realms/peoples to whom this god is central, based on their subsistence and history — a seafaring people gets a sea/storm god; a people with river burials gets a river/death god).

## Step 3 — Pass 2: coverage fill (guaranteed)
- **SCHEMA rule 5 + rule 10:** every realm AND every people must appear in at least one god's `patron_of`. Sweep the lists; for any realm/people with no patron, either extend an existing god's patronage or add a local deity. No atheistic realms.
- Every capital city must have ≥1 temple: fill `temples:` so each realm capital (from realms.v1) hosts at least one. Place additional temples in favored realms.
- Add a few `relations` between gods (kinship, rivalry, marriage) to make the pantheon a system, not a list.
- Report what the fill pass added.

## Step 4 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Every realm and every people has ≥1 patron deity (SCHEMA rule 5) — list any that needed fill.
- Every capital has ≥1 temple (SCHEMA rule 5).
- Domains are distributed (shared/multiple), not one-to-one.
- Each god's portfolio fits the worshippers' environment/history (no purely maritime god patronising a landlocked steppe people without a reason).
- Pantheon matches world tone (a grim low-magic world doesn't get a jolly cornucopia of benevolent gods).

## Step 5 — Write and hand off
Write `worldstate/pantheon.v1.md` (YAML + `## The gods` prose). Append to `LOG.md`. Next cultural skills: `/calendar`, `/mythology`, `/naming` (any order).
