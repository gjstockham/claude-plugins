---
name: travel-calculator
description: "Calculate travel times and distances between places in a fantasy world for different modes (foot, horse, cart, ship, messenger). Use when the user asks how long a journey takes, how far apart places are, travel time, \"how many days from X to Y\", \"how long to get there\", \"march time\", \"how fast can a messenger reach\" — triggers include \"travel time\", \"how long to travel\", \"how many days\", \"distance between\", \"how far is\", \"messenger speed\", \"fill travel days\". Reads worldstate/trade.v1.md and worldstate/world.v1.md (for map scale) and fills the days: {carrier, messenger, freight} fields on trade legs, or answers a one-off journey query using medieval travel speeds. Do NOT use for designing the routes themselves (that is /trade-routes) or for resources/politics."
---

# /travel-calculator — journey times by mode

Inputs:
!`grep -E 'id:|from:|to:|mode:|distance_km:|days:' worldstate/trade.v1.md 2>/dev/null | head -80 || echo "no trade.v1 yet — can still answer a one-off query"`
!`grep -E 'scale' worldstate/world.v1.md 2>/dev/null`

You convert distances to days by mode. Speed table: `references` in the trade-routes skill (`../trade-routes/references/trade-and-travel.md`) — or use the built-in rates below. This skill is a calculator: it can (A) fill the `days:` fields across trade.v1, or (B) answer a single "how long from X to Y" question.

## Rates (medieval)
- `carrier` (foot/laden horse, daylight): **35 km/day**
- `messenger` (light, remounts, night travel): **90 km/day**
- `freight` (ox-cart/bulk): **25 km/day**
- river barge downstream ~45 km/day; coastal ship ~120 km/day fair winds (use for sea/river legs).
Formula: days = ceil(distance_km / rate). Add delays for passes, crossings, monsoon/winter closure, and unsafe legs.

## Mode A — fill trade.v1
1. Guard: if trade.v1 is missing, tell the user to run `/trade-routes` first (or switch to Mode B for a hypothetical).
2. For each leg, read `distance_km` and `mode`; compute `days: {carrier, messenger, freight}`. For sea/river legs, also note the water speed in the leg `notes`/hazards since carrier/messenger/freight assume land.
3. Round up; add a note for any leg with a pass, crossing, or seasonal closure.
4. **Consistency check (mandatory):** every leg with a `distance_km` has all three `days` filled and consistent with its `mode` (a sea leg shouldn't show a plausible ox-cart time); echo ≥3 checks into a short note appended to trade.v1's `consistency_check` header (add entries, don't remove existing). Append to `LOG.md`.

## Mode B — one-off query
If the user just asks "how long from A to B?", estimate the distance (from trade.v1 legs if the pair is on a route, else from world.v1 `map.scale` and region adjacency), then give days for each requested mode with the formula shown. State assumptions (route, terrain, season). No file writes needed unless asked.
