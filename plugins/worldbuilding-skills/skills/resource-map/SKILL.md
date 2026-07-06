---
name: resource-map
description: "Assign natural resources, trade goods, and economic needs to every region of a fantasy world. Use when the user wants to work out what each region produces, what goods come from where, resources, raw materials, exports, imports, or \"what's this place rich in\" — triggers include \"resource map\", \"what does this region produce\", \"assign resources\", \"trade goods\", \"what are the exports\", \"economy of my world\". Reads worldstate/climate.v1.md and writes worldstate/resources.v1.md, tagging every region (by reg- id) with produces/needs/special using climate-and-terrain logic and the primary/secondary/tertiary sector model. Guarantees full coverage — no region left blank. Do NOT use for trade ROUTES between regions (that is /trade-routes), peoples, realms, or politics."
---

# /resource-map — what each region produces and needs

Climate registry (must exist):
!`cat worldstate/climate.v1.md 2>/dev/null || echo "MISSING climate.v1 — run /climate-from-map first"`
Existing resources:
!`head -20 worldstate/resources.v1.md 2>/dev/null`

You are tagging every region with its economy. Contract: `worldstate/SCHEMA.md` (`resources.v1`). Resource-by-climate mappings and sector logic: `references/resource-by-climate.md` — read it first.

## Step 1 — Guard
If `climate.v1.md` is missing, STOP and send the user to `/climate-from-map`. Use ONLY the `reg-` ids that exist in climate.v1 — never invent regions.

## Step 2 — Pass 1: assign by climate (organic)
For each region in `climate.v1`, read its `koppen`, `biome`, `elevation`, `position`, and `current`, and assign `produces:` using `references/resource-by-climate.md` (e.g. taiga→furs/timber, mountains→metals/stone, plains/steppe→grain/horses, hot-humid→spices, coast→fish/salt, rivers→trade/flax). Tag each good with `sector` (primary/secondary/tertiary) and `abundance` (rich/adequate/scarce). Manufacturing (secondary) belongs where raw materials OR population concentrate; note the combining rule (e.g. tin + imported copper → bronze).

## Step 3 — Pass 2: needs and coverage fill (guaranteed)
- For every region, list `needs:` — staple or strategic goods it can't produce locally (a taiga region needs grain; a desert needs almost everything but salt/minerals).
- **Coverage guarantee (SCHEMA rule 3 + rule 10):** confirm EVERY region in climate.v1 has an entry with at least one `produces` item. If any region came out empty (e.g. ice cap, open desert), force-fill a plausible marginal good (ice→nothing but a strategic chokepoint; desert→salt pans, gems, a caravan toll economy). Report in prose what the fill pass added.
- Mark `special:` for unique/strategic goods that will drive trade and conflict later (a lone silver mountain, the only saltpan, spice islands).

## Step 4 — Consistency check (mandatory)
Verify, then echo ≥3 results into header `consistency_check:`:
- Every climate.v1 region id appears exactly once (full coverage — SCHEMA rule 3).
- No good contradicts climate (no tropical spices from tundra; no vast grain surplus from arid desert without an irrigated river region to justify it).
- `special:` goods are genuinely scarce elsewhere (so trade/politics have something to fight over).
- Report the two-pass result: which regions were force-filled.

## Step 5 — Write and hand off
Write `worldstate/resources.v1.md` (YAML block + `## Economy tour` prose). Append to `LOG.md`. Next: `/populate`.
