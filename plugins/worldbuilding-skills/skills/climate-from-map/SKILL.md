---
name: climate-from-map
description: "Generate climate, biomes, prevailing winds, and seasons for a fantasy world from its map. Use when the user wants to work out climate, weather, biomes, rainfall, deserts, seasons, or \"what grows where\" for their world or continent — triggers include \"generate the climate\", \"climate from my map\", \"what biomes\", \"where are the deserts\", \"prevailing winds\", \"is this climate realistic\", \"climate check\". Reads worldstate/world.v1.md and writes worldstate/climate.v1.md, establishing the canonical region registry (reg- IDs) that every downstream skill depends on. Applies Köppen zones, three-cell circulation, lapse rate, rain shadow, ocean currents, continentality, and monsoon rules. Do NOT use for resources/trade goods, peoples, history, realms, politics, religion — those read climate but have their own skills."
---

# /climate-from-map — derive climate and the region registry

World foundation (must exist):
!`cat worldstate/world.v1.md 2>/dev/null || echo "MISSING world.v1 — run /worldbuild-init first"`
Existing climate (regenerating overwrites the region registry):
!`head -40 worldstate/climate.v1.md 2>/dev/null`

You are producing `climate.v1` AND the master **region registry**. Every downstream skill references regions by the `reg-` IDs you mint here, so name them well and never rename them later. Contract: `worldstate/SCHEMA.md` (`climate.v1` block). Physical rules and the Köppen-14 table: `references/climate-rules.md` — read it before assigning zones.

## Step 1 — Guard

If `world.v1.md` is missing, STOP: tell the user to run `/worldbuild-init`. If `climate.v1.md` already exists, warn that regenerating changes region IDs and invalidates every downstream file; confirm before overwriting.

## Step 2 — Divide the continent into regions

Read `map.description`, `planet` (tilt, rotation, sea level), and the latitude range from `world.v1`. Partition the land into 6–15 coherent regions. A region is a patch with one dominant climate — split on the drivers that change climate: latitude band, the windward vs. leeward side of each mountain range, coastal vs. deep interior, and any island group. Give each a `reg-` id and human name.

## Step 3 — Assign climate to each region (apply the rules in order)

For every region, work through `references/climate-rules.md`:

1. **Base temperature** from latitude band.
2. **Prevailing wind** from the three-cell model (mirror the bands if `rotation: retrograde`): easterlies 0–30°, westerlies 30–60°, polar easterlies 60–90°.
3. **Elevation** — apply the 6.5 °C/km lapse rate; shift highland/mountain regions toward their colder biome.
4. **Moisture**: is the region windward (wet) or leeward (rain-shadow dry) of a range? How far from the sea (continentality — interiors drier/more extreme)? Any ocean current warming or cooling the coast?
5. **ITCZ / monsoon** for low latitudes: seasonal wind reversal → summer-wet/winter-dry.
6. Resolve to a **Köppen-14 zone**, biome, temp (summer/winter), precip (amount + pattern), winds, current.

Record `adjacent:` for each region (symmetric — if A lists B, B lists A). The adjacency graph must be **connected** (no region unreachable) — downstream migration and trade skills walk it.

Resolve any `open_questions` from `world.v1` that concern climate (e.g. "is there a cold current here?") and note the decision.

## Step 4 — Consistency check (mandatory — do not skip)

Verify against `worldstate/SCHEMA.md` §4, then echo ≥3 concrete results into the header `consistency_check:`:

- **Global rule 1**: no desert (`arid`) region adjacent to open water unless justified by a `cold` current or a `rain shadow` recorded in `notes`.
- **Global rule 2**: windward slopes wetter than leeward at the same latitude; interior regions drier and more temperature-extreme than coastal regions at the same latitude.
- Prevailing winds follow the latitude band and match `rotation`.
- Elevation cooling applied to every highland/mountain region.
- `adjacent:` is symmetric and the graph is connected.

Fix violations before writing. If a region breaks a rule and you keep it, it MUST carry an explicit justification in `notes` (e.g. a cold current, a magical anomaly flagged in `world.v1`).

## Step 5 — Earth sanity option

If the user asks to validate the method, run it on a described Earth region and confirm it reproduces the real biome (e.g. "Sahara latitude + subtropical high + leeward → hot desert"; "UK 50–58°N + westerlies + warm current → temperate oceanic"). See `references/climate-rules.md` worked examples.

## Step 6 — Write and hand off

1. Write `worldstate/climate.v1.md`: the `climate.v1` YAML block, then prose — a `## Region tour` and a `## Seasons` note.
2. Append to `worldstate/LOG.md`: `[<date>] /climate-from-map — N regions, registry established`.
3. Next step: `/resource-map` (reads climate.v1 to place goods).
