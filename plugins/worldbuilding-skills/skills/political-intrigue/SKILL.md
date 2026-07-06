---
name: political-intrigue
description: "Build factions, political relationships, rivalries, alliances, wars, and live intrigue for a fantasy world. Use when the user wants politics, factions, intrigue, alliances, rivalries, wars, plots, court politics, or asks \"who's fighting whom\", \"what are the factions\", \"political situation\", \"add intrigue\" — triggers include \"political intrigue\", \"create factions\", \"faction relationships\", \"who's allied\", \"casus belli\", \"power struggles\", \"court plots\". Reads worldstate/realms.v1.md, resources.v1.md, and history.v1.md and writes worldstate/politics.v1.md: factions with Blades-style Tier/Status/progress-clocks and face/favour/fight, a relationship matrix over every bordering realm pair with casus-belli causes, and 3-5 live situations. Do NOT use to advance clocks over time (that is /faction-turn), or for realms/borders, trade, or religion."
---

# /political-intrigue — factions, relationships, live situations

Inputs (must exist):
!`grep -E 'id:|name:|government:|capital:|peoples:|with:|nature:' worldstate/realms.v1.md 2>/dev/null | head -80 || echo "MISSING realms.v1 — run /realms-and-borders first"`
!`grep -E 'id:|special:' worldstate/resources.v1.md 2>/dev/null | head -40`
!`grep -E 'type:|actors:|cause:|justifies:' worldstate/history.v1.md 2>/dev/null | head -40`
World tone:
!`grep -E 'tone|tech_level' worldstate/world.v1.md 2>/dev/null`

You make the world politically alive. Contract: `worldstate/SCHEMA.md` (`politics.v1`). Mechanics and casus-belli list: `references/faction-toolkit.md` — read it first. Engine of intrigue: every faction's goal conflicts with at least one other's.

## Step 1 — Guard
If realms.v1 is missing, STOP and send to `/realms-and-borders`. Use only existing `realm-`/`reg-`/`evt-` ids; mint new `fac-`/`sit-` ids.

## Step 2 — Build factions
Create factions for each realm's crown PLUS non-state actors (guilds, cults, orders, companies, court-parties, criminal networks) — draw them from resources.v1 `special` goods (who controls the silver? the saltpan? the caravan tolls?) and history.v1 grievances. For each: `tier` (0–5 reach/power), `status` (−3..+3 toward the player), `type`, a **face** (named leader + role), a **favour** (something useful it can offer), a **fight** (its conflict), a `goal`, a required `conflicts_with:` (another faction id), and a `clock` (name + 4/6/8 segments + filled). Start with 4–8 factions, not twenty. Give at least one realm two internal factions (e.g. idealist vs. cynic) for court tension.

## Step 3 — Relationship matrix
For EVERY pair of bordering realms (from realms.v1 `borders`), add a `relations` entry: `stance` (alliance/trade/tension/rivalry/war) and a `cause` from the casus-belli categories (territory/state-creation/state-integrity/succession/co-religionists/trade), with a one-line `detail` rooted in history.v1 or resources.v1. Calibrate a pre-modern setting toward dynastic/succession and territorial causes over nationalist ones.

## Step 4 — Live situations
Write 3–5 `situations` a solo player can engage now: `title`, `involves` (faction ids), `stakes`, `hook`. Each should sit at the intersection of conflicting goals so player action tips a balance.

## Step 5 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Every faction `goal` has a `conflicts_with` naming a real faction whose goal genuinely opposes it (SCHEMA rule 6).
- Every pair of bordering realms in realms.v1 appears in `relations` with a casus-belli cause (SCHEMA rule 6).
- Every faction has a face, favour, AND fight (no inert lore-only factions).
- Faction power (`tier`) is consistent with the realm's resources/size from upstream files.
- Situations reference only existing faction ids and real tensions.

## Step 6 — Write and hand off
Write `worldstate/politics.v1.md` (YAML + `## The board` prose). Append to `LOG.md`. Advance the world later with `/faction-turn`; next pipeline step is `/trade-routes`.
