---
name: faction-turn
description: "Advance the world between solo-play sessions — tick faction progress clocks, resolve completed clocks, and evolve the political situation over in-world time. Use ONLY when the user explicitly asks to advance factions, run a faction turn, pass time, do downtime, or \"move the world forward\" — triggers include \"faction turn\", \"advance the clocks\", \"run downtime\", \"pass a month\", \"move the world on\", \"what did the factions do\". This skill has side effects: it edits worldstate/politics.v1.md in place and appends to LOG.md. Reads politics.v1 and solo.v1 (chaos factor). Do NOT use for one-off oracle questions (/oracle) or rumour tables (/rumour-table); do NOT trigger automatically on narrative mentions of factions."
disable-model-invocation: true
---

# /faction-turn — advance the clocks (deliberate, side-effecting)

Current board:
!`grep -E '- id: fac|name:|tier:|status:|goal:|conflicts_with:|clock:' worldstate/politics.v1.md 2>/dev/null || echo "MISSING politics.v1 — run /political-intrigue first"`
Chaos level:
!`grep -E 'chaos_factor' worldstate/solo.v1.md 2>/dev/null || echo "chaos_factor 5 (default)"`

You move the world forward in time. This is a DELIBERATE side-effecting step — it rewrites `politics.v1.md`. Contract: `worldstate/SCHEMA.md` (`politics.v1`). Confirm the amount of in-world time to advance (default: one month) before running.

## Step 1 — Guard
politics.v1 must exist. Confirm the time span with the user. Note the current in-world date (world.v1 + LOG.md) so you can date the turn.

## Step 2 — Advance each faction's clock
For each faction, roll its **Tier as a fortune die** (Blades-style: roll dTier, higher Tier = more progress) to decide how many segments its clock ticks this turn — roughly: Tier 0–1 → 0–1 segment, Tier 2–3 → 1–2, Tier 4–5 → 2–3. Add ±1 for the Chaos Factor (high chaos = more movement). A faction actively opposed by another whose clock also advanced makes less progress (they check each other — use `conflicts_with`).

## Step 3 — Resolve full clocks
When a clock fills, resolve its goal IN WORLD and cascade the consequences:
- Update `status`/`tier` where the outcome warrants (a faction that achieved its goal may rise a tier or shift status toward/against the player).
- Update the relevant `situations` (a resolved situation closes or transforms; a new one may open).
- Update `relations` if the outcome changes a stance (a won succession can turn tension into war or alliance).
- Reset or replace the clock with the faction's next goal, still `conflicts_with` someone.

## Step 4 — Consistency check (mandatory)
Before writing, verify and echo ≥3 into the politics.v1 `consistency_check` header (add entries):
- Every faction still has a goal that `conflicts_with` a real faction (SCHEMA rule 6) — new/replacement goals included.
- Every bordering realm pair still has a `relations` entry (SCHEMA rule 6) after any changes.
- Outcomes are consistent with upstream facts (a faction can't achieve something geography/resources forbid).
- Clock/tier/status changes are internally consistent (no tier above 5, status in −3..+3).

## Step 5 — Write and log
- Overwrite `worldstate/politics.v1.md` with the advanced state (bump `updated:`).
- Append a narrative summary to `LOG.md`: `[<new in-world date>] /faction-turn — <what each clock did, what resolved>`.
- Report to the user what changed and surface any newly live situations for the next scene.
