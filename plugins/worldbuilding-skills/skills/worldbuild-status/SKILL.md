---
name: worldbuild-status
description: "Show worldbuilding progress and what to do next. Use when the user asks where they are in building their world, what to run next, what's missing, whether anything is out of date, or wants a progress overview or checklist — triggers include \"where am I\", \"what's next\", \"what should I run next\", \"worldbuild status\", \"world progress\", \"what's left to build\", \"did I miss a step\", \"is anything stale\", \"guide me through worldbuilding\". Read-only: inspects worldstate/ and reports a phase-by-phase checklist, the recommended next skill and why, and flags any missing prerequisites or stale downstream files. Does NOT generate or edit any world content — it only points you to the right generation skill (/worldbuild-init, /climate-from-map, etc.) to run next."
---

# /worldbuild-status — where you are and what's next

Current world bible (files + last-modified):
!`ls -la --time-style=+%Y-%m-%d\ %H:%M worldstate/*.md 2>/dev/null | awk '{print $6, $7, $8}' || echo "(no worldstate/ — start with /worldbuild-init)"`
Declared update dates inside each file:
!`for f in world climate resources peoples history realms politics trade pantheon calendar mythology naming solo; do d=$(grep -m1 'updated:' worldstate/$f.v1.md 2>/dev/null | awk '{print $2}'); [ -n "$d" ] && echo "$f.v1: $d"; done`
Recent activity:
!`tail -5 worldstate/LOG.md 2>/dev/null`

You are a READ-ONLY guide. You NEVER write or edit world files. You inspect the world bible, report progress, and tell the user exactly which generation skill to run next and why. If they want to proceed, point them to the skill (e.g. "run `/resource-map`") — you do not run it or generate its content yourself.

## The pipeline (dependency order + what each needs)

| # | Skill | Writes | Requires |
|---|-------|--------|----------|
| 0 | `/worldbuild-init` | world.v1 | — |
| 1 | `/climate-from-map` | climate.v1 | world.v1 |
| 2 | `/resource-map` | resources.v1 | climate.v1 |
| 3 | `/populate` | peoples.v1 | climate.v1, resources.v1 |
| 4 | `/history-and-migration` | history.v1 | peoples.v1, climate.v1 |
| 5 | `/realms-and-borders` | realms.v1 | climate.v1, resources.v1, peoples.v1, history.v1 |
| 6 | `/political-intrigue` | politics.v1 | realms.v1, resources.v1, history.v1 |
| 7 | `/trade-routes` | trade.v1 | resources.v1, realms.v1, climate.v1 |
| 7b | `/travel-calculator` | trade.v1 (fills days) | trade.v1, world.v1 |
| 8 | `/pantheon` | pantheon.v1 | realms.v1, peoples.v1 |
| 9 | `/calendar` | calendar.v1 | world.v1 (climate/pantheon/history enrich) |
| 10 | `/mythology` | mythology.v1 | peoples.v1 (pantheon/climate/history enrich) |
| 11 | `/naming` | naming.v1 | peoples.v1 (realms.v1 enriches) |
| 12 | `/oracle` | solo.v1 | politics.v1 + all |
| 13 | `/rumour-table` | solo.v1 (rumours) | politics.v1 (trade/history enrich) |
| 14 | `/faction-turn` | politics.v1 (in place) | politics.v1 (solo.v1 enriches) |

Phases: **0** Foundation · **1** Climate · **2** Causal chain (2–7b) · **3** Cultural (8–11, any order) · **4** Solo play (12–14).

## What to report

1. **Checklist** — for each phase, mark each file: ✅ present · ▶️ next up · ⛔ blocked (missing prereq) · ⬜ not started. Base "present" on the file existing in worldstate/.

2. **Recommended next step** — the earliest skill in pipeline order whose output is missing AND whose requirements are all present. Name it and give a one-line reason ("climate.v1 exists, so `/resource-map` can run"). If a later file exists but an earlier prereq doesn't, flag the gap.

3. **Staleness check** — compare declared `updated:` dates (and file mtimes as tiebreaker). If any file is OLDER than a file it depends on, warn that it may be stale and should be regenerated. Example: if climate.v1 was updated after resources.v1, resources.v1 (and everything downstream of it) is potentially stale. List the affected downstream chain in pipeline order.

4. **Optional-layer note** — remind the user the cultural layer (Phase 3) and solo layer (Phase 4) are optional; a world is playable after the causal chain. Solo skills only make sense once politics.v1 exists.

## Style
Be brief and scannable — a short checklist plus one clear "do this next" line. Do not dump file contents. Do not invent world facts. Do not modify anything. If worldstate/ is empty or missing, the answer is simply: start with `/worldbuild-init`.
