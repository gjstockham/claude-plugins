# Trade & travel reference

Premodern trade routing and travel speeds. Sources: Worldbuilding Workshop trade guides; medieval travel figures (Margaret Wade Labarge; Peter Spufford).

## Routing logic
- Goods flow from surplus (low price) to scarcity (high price); the gap funds transport and profit (Ricardo comparative advantage).
- Route along the CHEAPEST path, not the shortest: water beats land by far; valleys and plains beat mountains and forest. Water transport is roughly an order of magnitude cheaper per tonne-km than land.
- Bulky/cheap goods (grain, timber, stone) move only short distances or by water. High-value/low-bulk goods (spices, silk, gems, metals) justify long overland caravans.
- Hubs form where routes cross or change mode (river mouth ports, desert-edge caravanserais, mountain-pass towns). These become the wealthy, cosmopolitan centers.
- Security enables trade: a policed route (Pax Mongolica → Silk Road boom) carries far more than a bandit-ridden one. Flag unsafe legs as `hazards`.
- Routes carry ideas, religions, and disease alongside goods — note this for downstream religion/history hooks.

## Travel speeds (medieval, for the `days:` fields)

| Mode | Speed | Notes |
|------|-------|-------|
| Ordinary carrier / traveller on foot or with a laden horse | **30–40 km/day** | daylight only; typical pace with light merchandise |
| Messenger (light, night travel, remounts) | **~90 km/day** (55–60 miles/day) | fastest; requisitions fresh horses |
| Heavy freight / ox-cart | **<30 km/day** (often 15–25) | bulk goods, poor roads |
| Convoy (men + pack horses) | ~50 km/day | Spufford: Dijon–Paris, 6 days, ~50 km/day |
| River barge (downstream) | 40–50 km/day | faster down, slow up |
| Coastal sailing ship | 100–150 km/day fair winds | wind-dependent, seasonal |

Rules of thumb for `days:` = distance_km / speed, rounded up:
- `carrier` uses 35 km/day.
- `messenger` uses 90 km/day.
- `freight` uses 25 km/day.
Add delays for passes, river crossings, monsoon closure, and unsafe legs. Sea and river legs use the water figures instead where relevant; note the mode in the leg.

## Seasonality
Monsoon and winter close routes: mountain passes snow shut, deserts become impassable in high summer, sailing seasons open and close. Tie closures to the calendar and climate.v1 seasons.
