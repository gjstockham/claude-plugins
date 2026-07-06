# UWP reference — code meanings for prose grounding

Format: `Starport Size Atmo Hydro Pop Gov Law - TL`, e.g. `A788899-C`.
Digits are extended hex (0-9, A=10, B=11 ... ). Edition-agnostic core meanings below; the generator script already applies these — use this file to write accurate prose, not to re-derive facts.

## Starport
| | |
|---|---|
| A | Excellent: refined fuel, full shipyard (starships), usually a highport |
| B | Good: refined fuel, spacecraft yards, annual maintenance |
| C | Routine: unrefined fuel, major repairs |
| D | Poor: unrefined fuel, limited repairs |
| E | Frontier: marked landing area only |
| X | No port |

## Size (digit × 1600 km diameter)
0 = asteroid/planetoid (<800 km, microgravity) · 5 ≈ Mars · 8 ≈ Earth · A = 16,000 km, 1.4g.

## Atmosphere
0 none · 1 trace · 2-3 very thin (2 tainted) · 4-5 thin (4 tainted) · 6 standard · 7 standard tainted · 8-9 dense (9 tainted) · A exotic · B corrosive · C insidious · D dense high · E thin low · F unusual.
Tainted = filter mask; exotic = air supply; corrosive/insidious = sealed suit.

## Hydrographics
Digit × 10% surface water (or other liquid for exotic atmospheres). 0 = desert world, A = water world.

## Population
10^digit people. The multiplier comes from the PBG first digit when supplied, otherwise the seeded roll. 0 = uninhabited.

## Government
0 none · 1 company/corporation · 2 participating democracy · 3 self-perpetuating oligarchy · 4 representative democracy · 5 feudal technocracy · 6 captive government/colony · 7 balkanization · 8 civil service bureaucracy · 9 impersonal bureaucracy · A charismatic dictator · B non-charismatic leader · C charismatic oligarchy · D religious dictatorship · E religious autocracy · F totalitarian oligarchy.

## Law level (what gets you arrested)
0 nothing · 1 WMD/battle dress · 2 energy weapons · 3 military weapons · 4 light assault weapons · 5 concealable firearms · 6 all firearms bar shotguns · 7 shotguns too · 8 blades and stunners · 9 any weapon outside home · A+ escalating control of movement, speech and technology.

## Tech level
0 stone age · 1-3 pre-industrial · 4-6 industrial · 7-9 pre-stellar · A-B early stellar · C-E average stellar · F+ high stellar.

## Common extensions (canon when provided, never invented)
- **Bases**: N naval · S scout · D depot · W way station · M military · B naval+scout, etc. (edition-dependent — take the user's letters at face value).
- **Travel zone**: A amber (caution) · R red (interdicted). No letter = green; do not state a zone unless given.
- **PBG**: population multiplier / planetoid belts / gas giants. Only the P digit concerns the mainworld; **never** describe belts or gas giants from B and G — out of scope.
- **Allegiance**: polity code (Im, Zh, So, Cs...). Colours politics and the port, not the dice.
- **{Ix} (Ex) [Cx]**: T5 importance, economic, cultural extensions. Quote if provided; use qualitatively (e.g. high importance = busy lanes).
- **Stellar data**: record verbatim if given but never elaborate on it — mainworld only.

## Core trade codes (computed by the script)
Ag agricultural · As asteroid · Ba barren · De desert · Fl fluid oceans · Ga garden · Hi high pop · Ht high tech · Ic ice-capped · In industrial · Lo low pop · Lt low tech · Na non-agricultural · Ni non-industrial · Po poor · Ri rich · Va vacuum · Wa water world.
Other provided codes pass through as canon: Cp/Cs/Cx capitals · Da/Pz danger/puzzle zones · Fo forbidden · Mr military rule · Pe penal · Pi pre-industrial · Pr pre-rich · Re reserve · Sa satellite · Tz twilight zone, etc.
