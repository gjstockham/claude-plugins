---
name: rumour-table
description: "Generate setting-consistent rumour and gossip tables for the regions and towns of a fantasy world, for solo or GM play. Use when the user wants rumours, gossip, tavern talk, hooks, \"what are people saying\", overheard news, or a rumour table for a place — triggers include \"rumour table\", \"rumours\", \"gossip\", \"tavern talk\", \"what are people saying in\", \"word on the street\", \"hooks for this town\", \"overheard\". Reads the whole worldstate (politics.v1 situations, history.v1, trade.v1, pantheon.v1) and updates worldstate/solo.v1.md with a d6 rumour table per requested region, where every rumour cites a real source id (situation, event, faction, route) and is tagged for truth (yes/mostly/twisted/false). Do NOT use for the yes/no oracle (that is /oracle) or advancing faction clocks (that is /faction-turn)."
---

# /rumour-table — setting-consistent rumours

World hooks to draw on:
!`grep -E '- \{id: sit|title:|hook:|involves:' worldstate/politics.v1.md 2>/dev/null | head -40 || echo "run /political-intrigue first for the richest rumours"`
!`grep -E 'id:|name:|hubs:|hazards:' worldstate/trade.v1.md 2>/dev/null | head -30`
!`grep -E 'id:|type:|effect:' worldstate/history.v1.md 2>/dev/null | head -20`
Existing solo state (preserve it):
!`grep -E 'chaos_factor|threads:|rumour_tables:' worldstate/solo.v1.md 2>/dev/null || echo "(no solo.v1 yet — will create, preserving any oracle state)"`

You write rumours that are always about the real world. Contract: `worldstate/SCHEMA.md` (`solo.v1` `rumour_tables`). Principle: a rumour table is a mirror of the setting's live tensions, so every entry must trace to something that exists.

## Step 1 — Choose the region(s)
Ask which region/town if unspecified. Rumours should reflect WHERE they're heard — a caravan-hub rumour is about tolls and silver; a port rumour about the sea route; a steppe-edge rumour about raids.

## Step 2 — Build a d6 table per region
For each region, write 6 rumours (`roll: 1..6`). Each entry:
- `rumour`: what's being said, in-voice, local to that place.
- `source`: a REQUIRED real id — a `sit-` situation, `evt-` event, `fac-` faction, `route-` route, or `god-`/festival. This is what makes it setting-consistent.
- `true`: one of `yes` (accurate), `mostly` (true, distorted), `twisted` (a real thing, wrong conclusion), `false` (rival propaganda / superstition).
Mix truth levels (roughly 2 accurate, 2 distorted, 1 twisted, 1 false) so players can't trust everything. Bias content toward the nearest live `situations` so rumours double as adventure hooks.

## Step 3 — Consistency check (mandatory)
Verify, then echo ≥3 into the solo.v1 `consistency_check` header (add, don't remove existing):
- Every rumour `source` is a real id present in the world state (SCHEMA rule 9).
- Rumours fit the region's culture/economy and the peoples who live there.
- Truth tags are mixed (not all true, not all false).
- False/twisted rumours are still plausible in-world (rival factions' spin, local superstition tied to a real god/omen).

## Step 4 — Write and log
Create or update `worldstate/solo.v1.md`, adding/replacing only the `rumour_tables:` entries for the chosen regions and PRESERVING `chaos_factor`, `threads`, and `npcs` from /oracle. Append to `LOG.md`: `[<date>] /rumour-table — <region> d6 rumours`.
