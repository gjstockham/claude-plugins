---
name: calendar
description: "Design a calendar and timekeeping system for a fantasy world — months, weeks, moons, seasons, leap days, and festivals. Use when the user wants a calendar, months, weeks, seasons, moon cycles, holidays, festivals, or asks \"how do they measure time\", \"what are the months\", \"when are the holy days\" — triggers include \"calendar\", \"months and weeks\", \"moons\", \"festivals\", \"holidays\", \"how they tell time\", \"leap year\", \"seasonal cycle\". Reads worldstate/world.v1.md (planet, year), climate.v1.md (seasons), pantheon.v1.md (gods for months/festivals), and history.v1.md (events to commemorate) and writes worldstate/calendar.v1.md. Do NOT use for the gods themselves (that is /pantheon), myths, or naming."
---

# /calendar — months, moons, and festivals

Inputs:
!`grep -E 'axial_tilt|rotation|year_zero|current_year|scale' worldstate/world.v1.md 2>/dev/null || echo "MISSING world.v1 — run /worldbuild-init first"`
!`grep -E '- id:|name:|domains:' worldstate/pantheon.v1.md 2>/dev/null | head -40 || echo "(no pantheon.v1 yet — months can still be secular; run /pantheon to tie months to gods)"`
!`grep -E 'id:|name:|type:|year:' worldstate/history.v1.md 2>/dev/null | head -30`
!`grep -E '- id:|temp:|precip:' worldstate/climate.v1.md 2>/dev/null | head -30 || echo "(no climate.v1 — seasons will be assumed)"`

You build a calendar that reveals worldbuilding (naming a rest day "Saintsday" implies saints). Contract: `worldstate/SCHEMA.md` (`calendar.v1`). Reference template: Gnome Stew "realistic enough" (13×28-day months + 1 intercalary day; map gods to months).

## Step 1 — Guard
world.v1 must exist. climate.v1, pantheon.v1, and history.v1 are recommended (they let you match the seasons, tie months to gods, and festivals to real events); if absent, note that months/festivals will be provisional.

## Step 2 — Build the year
- Set `year_length_days` (default 365 for an Earth-like orbit; adjust if the premise says otherwise).
- Divide into `months`. A clean template: 12–13 months of ~28–30 days. If pantheon.v1 exists, dedicate each month to a god (`god:` per month) so the calendar teaches the pantheon.
- Define the `week` (length + `day_names`) — day names should reveal culture (gods, trades, the dead).
- Add `moons` with independent `cycle_days` (multiple moons with different cycles create rare alignments — good for prophecy/festivals). Use world.v1 if it specified moons; otherwise propose 1–2.
- Set `intercalation`: how the leftover days are handled (leap day, festival days outside the months).

## Step 3 — Festivals
Create `festivals` tied to (a) seasons/agriculture from climate.v1 seasons, (b) gods from pantheon.v1 (`honors:`), and (c) historical events from history.v1 (`commemorates:` an evt- id — e.g. a day of mourning for a collapse, a founding day). Anchor each festival to a `date` in the new calendar.

## Step 4 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Month/day count sums to `year_length_days` (including intercalation).
- Seasons implied by the calendar match climate.v1 (monsoon/dry, summer/winter placement) — if climate.v1 is absent, state the assumption.
- Every `honors:` points to a real god id and every `commemorates:` to a real evt id.
- The calendar reflects the world's focus/tone (a caravan or monsoon culture times its year by the trade season or the rains).

## Step 5 — Write and hand off
Write `worldstate/calendar.v1.md` (YAML + `## The year` prose). Append to `LOG.md`.
