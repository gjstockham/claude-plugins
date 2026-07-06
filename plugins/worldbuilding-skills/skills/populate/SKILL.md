---
name: populate
description: "Place peoples and cultures across a fantasy world and explain where they live and why. Use when the user wants to add peoples, cultures, ethnic groups, tribes, or populations to their world, or asks \"who lives here\", \"what cultures\", \"populate my world\", \"where do people settle\" — triggers include \"populate the world\", \"add peoples\", \"what cultures live where\", \"distribute populations\", \"cultural groups\". Reads worldstate/climate.v1.md and worldstate/resources.v1.md and writes worldstate/peoples.v1.md, giving each people a homeland, current range (by reg- id), subsistence, traits, migration seed, and neighbour stances. Guarantees every region is inhabited or explicitly wilderness. Do NOT use for realms/borders/governments (that is /realms-and-borders), history, religion, or naming."
---

# /populate — who lives where, and why

Inputs (must exist):
!`cat worldstate/climate.v1.md 2>/dev/null | head -80 || echo "MISSING climate.v1"`
!`cat worldstate/resources.v1.md 2>/dev/null | head -60 || echo "MISSING resources.v1 — run /resource-map first"`
World premise/tone:
!`sed -n '/premise:/,/planet:/p' worldstate/world.v1.md 2>/dev/null`

You place cultures according to geography and economy. Contract: `worldstate/SCHEMA.md` (`peoples.v1`). Guiding principle: cultures diverge at natural barriers (mountains, seas, deserts), "nature abhors straight lines," and people live where climate + resources support their subsistence.

## Step 1 — Guard
If climate.v1 or resources.v1 is missing, STOP and name the skill to run. Use only existing `reg-` ids.

## Step 2 — Pass 1: seed cultures at natural cores
Identify natural culture cores — a fertile valley, a coastal strip, a steppe, an island chain — each separated from others by a barrier region (mountain crest, desert, sea). Create 3–7 peoples (fewer is better early). For each: `homeland` (origin reg-ids), `subsistence` fitted to the biome and resources (farming in river valleys, pastoral on steppe, fishing/trade on coasts and isles), 2–4 `traits` that flow from environment and the world's cultural focus, and a `migration_seed` — a climate/resource reason they might move (drought, crowding, a coveted resource elsewhere).

## Step 3 — Pass 2: spread and coverage fill (guaranteed)
- Spread each people into adjacent regions they can plausibly use (follow climate.v1 `adjacent`), setting `range`.
- **Coverage guarantee (SCHEMA rule 3 + rule 10):** every region must appear in at least one people's `range`, OR be explicitly declared uninhabited wilderness in prose with a reason (ice cap, deep desert). Force-fill any orphan region — assign a sparse population (nomads crossing the desert, hunters in the taiga) or mark it wilderness. Report what the fill pass added.
- Set `neighbours` stances (kin/trade/rivalry/hostile) between peoples who share or border regions — these seed history and politics.

## Step 4 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Every climate.v1 region is in ≥1 `range` or declared wilderness (SCHEMA rule 3).
- Subsistence matches biome/resources (no farmers homelanded in open desert; pastoralists on steppe/plains).
- Barriers separate distinct cultures (peoples on opposite sides of the mountain crest differ); ranges follow the adjacency graph (no people teleporting across a barrier region they don't inhabit).
- Migration seeds cite a real climate/resource cause (sets up /history-and-migration).

## Step 5 — Write and hand off
Write `worldstate/peoples.v1.md` (YAML + `## Peoples of the world` prose). Append to `LOG.md`. Next: `/history-and-migration`.
