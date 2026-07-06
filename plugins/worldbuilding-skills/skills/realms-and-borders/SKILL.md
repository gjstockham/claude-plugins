---
name: realms-and-borders
description: "Define the polities, kingdoms, realms, borders, capitals, and settlements of a fantasy world. Use when the user wants to create kingdoms, nations, states, realms, borders, capitals, cities, or asks \"who rules where\", \"draw the borders\", \"what countries\", \"place the cities\" — triggers include \"realms and borders\", \"create kingdoms\", \"political map\", \"where are the cities\", \"capitals\", \"draw borders\", \"found settlements\". Reads worldstate/climate.v1.md, resources.v1.md, peoples.v1.md, and history.v1.md and writes worldstate/realms.v1.md containing both realms (with borders at natural barriers) and settlements (capitals/cities/towns on justified sites). Every region is owned, disputed, or explicitly unclaimed. Do NOT use for faction relationships/intrigue (that is /political-intrigue), trade routes, religion, or history."
---

# /realms-and-borders — polities, borders, and settlements

Inputs (all must exist):
!`grep -E 'id:|name:|position:|elevation:|adjacent:' worldstate/climate.v1.md 2>/dev/null | head -80 || echo "MISSING climate.v1"`
!`grep -E 'id:|special:|produces:' worldstate/resources.v1.md 2>/dev/null | head -50 || echo "MISSING resources.v1"`
!`grep -E 'id:|name:|range:|homeland:' worldstate/peoples.v1.md 2>/dev/null | head -50 || echo "MISSING peoples.v1"`
!`grep -E 'type:|actors:|regions:|justifies:' worldstate/history.v1.md 2>/dev/null | head -40 || echo "MISSING history.v1 — run /history-and-migration first"`

You draw the political map AND place settlements in one file. Contract: `worldstate/SCHEMA.md` (`realms.v1`). Principles: borders follow natural barriers ("nature abhors straight lines" — straight borders imply artificial/colonial imposition); leave some buffer/disputed zones for intrigue; settlements sit on justified sites.

## Step 1 — Guard
If any of climate/resources/peoples/history is missing, STOP and name the earliest missing skill. Use only existing ids.

## Step 2 — Pass 1: paint realms onto regions
Group regions into realms along cultural (`peoples.v1` ranges) and geographic lines, respecting history.v1 foundings/collapses. Assign each realm `government`, member `regions`, `peoples`, and a `founded:` event id. Define `borders`: for each neighbouring realm, name the `nature` (river/mountain/sea/desert/forest/disputed/artificial). Prefer natural-barrier borders; mark any straight/artificial border deliberately (it implies conquest or treaty — a hook). Deliberately leave 1+ buffer/disputed zone.

## Step 3 — Pass 2: coverage + settlements
- **Coverage (SCHEMA rule 3 + rule 10):** every region must be in a realm's `regions`, in `unclaimed[]` with a reason, or explicitly disputed. Force-fill orphans (wilderness → unclaimed with `why`). Report the fill.
- **Settlements:** place a `capital` per realm plus key `city`/`town` settlements. Each settlement needs a `site` justified by SCHEMA rule 4 — water (harbor, river-crossing, oasis), resource (mine, saltpan), or a route chokepoint (mountain pass, ford). No city in a resource void without a route reason. Put capitals in defensible, well-resourced, well-connected regions.

## Step 4 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Every region owned / disputed / explicitly unclaimed (SCHEMA rule 3).
- Every settlement `site` justified by water, resource, or route (SCHEMA rule 4) — flag any that isn't.
- Borders prefer natural barriers; every artificial/straight border has an in-world justification (conquest/treaty from history.v1).
- Realm membership matches peoples' ranges (a realm's peoples actually live in its regions).
- Every `founded:` points to a real history.v1 event id.

## Step 5 — Write and hand off
Write `worldstate/realms.v1.md` (YAML with `realms:`, `unclaimed:`, `settlements:` + `## The realms` and `## Cities` prose). Append to `LOG.md`. Next: `/political-intrigue`, then `/trade-routes`.
