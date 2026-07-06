# traveller-worlds

Turn a Traveller UWP into a consistent, detailed mainworld dossier.

## How it works

Three layers:

1. **Derived facts** — pure lookup from the UWP digits (atmosphere type, trade codes, law meaning). No randomness.
2. **Seeded rolls** — climate, geography, government character, factions, culture, locations, hooks. A Python script seeds every roll from `hash(hex | name | UWP)`, with an independent sub-seed per category, so the same world always rolls the same details and adding new tables later never reshuffles old ones.
3. **Prose** — the AI writes the dossier grounded strictly in layers 1-2. Written once to `traveller/worlds/<world>.md`; thereafter the file is canon and is never re-rolled.

Extensions (bases, travel zone, PBG, allegiance, {Ix} (Ex) [Cx], stellar data) are used as canon when present and ignored when absent. They do **not** affect the seed, so supplying fuller survey data later never changes an established world.

**Mainworld only** — no stars, moons, belts or gas giants are ever generated or implied, so this composes cleanly with any system-generation method you use.

## Usage

Give Claude anything from a bare UWP to a full sector line:

- `Generate a world from A788899-C`
- `Detail 0310 Regina A788899-C N Ri Cp A 703 Im`
- `Quick version of 2712 Ashfall D550357-5`

Dossiers land in `traveller/worlds/` in your working folder, with the full facts JSON embedded as an audit trail.

## Determinism caveat

The dice are truly deterministic; the prose is not (it's written by the model). Reproducibility of prose comes from persistence: once a dossier exists, it is read, not regenerated. An explicit re-roll requires confirmation and is noted in `traveller/worlds/LOG.md`.
