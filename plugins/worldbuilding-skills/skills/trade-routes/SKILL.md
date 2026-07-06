---
name: trade-routes
description: "Design trade routes, caravan and shipping lanes, hub cities, and price gradients for a fantasy world. Use when the user wants trade routes, commerce, caravans, shipping lanes, merchant networks, trade hubs, or asks \"how do goods move\", \"where's the trade\", \"which cities are rich\", \"trade network\" — triggers include \"trade routes\", \"caravan routes\", \"shipping lanes\", \"trade hubs\", \"how goods flow\", \"commerce map\", \"price of goods\". Reads worldstate/resources.v1.md, realms.v1.md, and climate.v1.md and writes worldstate/trade.v1.md: routes with legs (mode, distance, goods, hazards), hub cities where routes cross, and price-gradient notes. Routes follow cheap paths (water, valleys) and avoid mountains/forest. Pair with /travel-calculator to fill travel days. Do NOT use for the peoples, realms, politics, or religion themselves."
---

# /trade-routes — how goods move and who gets rich

Inputs (must exist):
!`grep -E 'id:|produces:|needs:|special:' worldstate/resources.v1.md 2>/dev/null | head -70 || echo "MISSING resources.v1 — run /resource-map first"`
!`grep -E 'id:|name:|region:|realm:|size:|site:' worldstate/realms.v1.md 2>/dev/null | head -70 || echo "MISSING realms.v1 — run /realms-and-borders first"`
!`grep -E 'id:|position:|elevation:|biome:|adjacent:' worldstate/climate.v1.md 2>/dev/null | head -70`

You connect supply to demand along the cheapest paths. Contract: `worldstate/SCHEMA.md` (`trade.v1`). Routing logic and travel speeds: `references/trade-and-travel.md` — read it first. Security enables trade (Pax Mongolica → Silk Road); note where a route is unsafe.

## Step 1 — Guard
If resources.v1 or realms.v1 is missing, STOP and name the earliest missing skill. Use only existing `city-`/`reg-` ids; mint `route-` ids.

## Step 2 — Match supply to demand
Cross resources.v1 `produces`/`special` against `needs`. Each strong supply→demand pair is a candidate route between the settlements nearest each end. Prioritise `special`/high-value goods (salt, metals, spices, horses) and staples that regions genuinely lack.

## Step 3 — Route the legs along cheap paths
Build each route as a chain of `legs` between settlements. Pick `mode` by geography (SCHEMA rule 8): **sea** along coasts, **river** down navigable rivers, **road** across plains/valleys, **caravan** across desert/steppe. Avoid crossing mountain crests and dense forest — route through passes and valleys instead (a settlement on a pass or ford exists precisely to tax the route). Estimate `distance_km` from world.v1 `map.scale`. List `goods` per leg with direction (`"wool>"` from→to, `"<salt"` to→from) and any `hazards` (bandits, pirates, monsoon closure, desert).

## Step 4 — Hubs and price gradients
Mark `hubs:` where routes cross or transfer mode (river→sea port, desert-edge caravanserai) — these are the wealthy centers. In `notes:`, sketch price gradients (a good is cheap at source, dear far away; the markup funds the hubs) and note that routes also carry ideas, religions, and disease, not just goods.

## Step 5 — Consistency check (mandatory)
Verify, then echo ≥3 into `consistency_check:`:
- Every settlement that upstream flagged as a city in a resource-poor spot is served by a route (SCHEMA rule 4 — no rich city in a void).
- Modes match terrain (no road over a mountain crest; sea legs only along coasts) — SCHEMA rule 8.
- Traded goods actually exist in resources.v1 (source produces it, destination needs it).
- Hubs sit at real crossings/transfers.

## Step 6 — Write and hand off
Write `worldstate/trade.v1.md` (YAML + `## Trade network` prose). Leave `days:` empty or rough — run `/travel-calculator` to fill precise travel times. Append to `LOG.md`.
