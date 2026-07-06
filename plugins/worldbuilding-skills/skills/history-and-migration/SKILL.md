---
name: history-and-migration
description: "Generate a world's history, timeline, migrations, wars, foundings, golden ages, and collapses. Use when the user wants history, a timeline, backstory, lore, past events, migrations, or \"what happened here before\" — triggers include \"generate history\", \"world timeline\", \"migration history\", \"past wars\", \"how did we get here\", \"world backstory\", \"eras and events\". Reads worldstate/peoples.v1.md and worldstate/climate.v1.md (and resources.v1 if present) and writes worldstate/history.v1.md as eras plus dated events, each retro-fitting a present-day fact. Uses the generate-present-then-explain method: decide what the world looks like now, then invent the history that justifies it. Do NOT use for current politics/factions (that is /political-intrigue), realms, religion, or the live solo campaign log."
---

# /history-and-migration — invent the past that explains the present

Inputs (must exist):
!`cat worldstate/peoples.v1.md 2>/dev/null | head -80 || echo "MISSING peoples.v1 — run /populate first"`
!`sed -n '/regions:/,/^`/p' worldstate/climate.v1.md 2>/dev/null | grep -E 'id:|name:|notes:' | head -60`
World anchor:
!`grep -E 'year_zero_label|current_year|premise' worldstate/world.v1.md 2>/dev/null`

You write history BACKWARD from the present. Contract: `worldstate/SCHEMA.md` (`history.v1`). Core rule (SCHEMA rule 7): every event must `justifies` a present-day fact already established in peoples.v1 / climate.v1. Do not simulate forward from year zero.

## Step 1 — Guard
If peoples.v1 or climate.v1 is missing, STOP and name the skill to run. Use only existing `reg-`/`ppl-` ids.

## Step 2 — List the present-day facts that need explaining
Scan peoples.v1 and climate.v1 for facts a history must justify: each people's current `range` vs `homeland` (every mismatch = a migration to explain), each `migration_seed`, each `neighbours` rivalry/hostility, distinctive settlements-to-be (the caravan cities on the river, the isolated highland folk), and any resource concentration worth a past war.

## Step 3 — Build eras (sparse early, dense near the present)
Define 3–5 `eras` spanning up to `current_year`. Older eras get one-line summaries; the era nearest the present is detailed. This matches how real settings feel — myth-dim past, well-lit present.

## Step 4 — Write events that retro-fit those facts
For each present-day fact from Step 2, author one or more `events` (migration/founding/war/collapse/golden-age/disaster/succession-crisis/conversion). Each event needs `actors`, `regions`, a `cause` from the SCHEMA list (drought, warfare, competition, inequality, trade-collapse, succession, territory, religion, opportunity), an `effect`, and a REQUIRED `justifies:` naming the present fact it explains. Use rise-and-fall drivers (drought/warfare extrinsic; inequality/competition/trade-collapse intrinsic) for collapses. Migrations must follow a plausible route through `adjacent` regions — no crossing a barrier the people never inhabited.

## Step 5 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Every people whose `range` ≠ `homeland` has a migration event justifying the move (SCHEMA rule 7).
- Every migration route steps through adjacent regions (no teleporting across barriers).
- Every event's `cause` is climate/resource/political-plausible (a collapse has a real driver; a golden age has a resource or trade basis).
- Every rivalry/hostility in peoples.v1 has a historical root event.
- Chronology is internally consistent (no effect before its cause; foundings before the realms that will inherit them).

## Step 6 — Write and hand off
Write `worldstate/history.v1.md` (YAML + `## Chronicle` prose narrating the eras). Append to `LOG.md`. Next: `/realms-and-borders`.
