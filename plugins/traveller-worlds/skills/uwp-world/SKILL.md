---
name: uwp-world
description: Generate a consistent, detailed Traveller mainworld dossier from a UWP (Universal World Profile). The same hex + name + UWP always produces the same world. Use when the user provides a UWP string (e.g. "A788899-C", "0310 Regina A788899-C N Ri Cp A 703 Im") or asks to "generate a world from a UWP", "detail this Traveller world", "expand this world profile", "what is this planet like" with a UWP, or mentions "UWP", "universal world profile", "world profile", "mainworld", "sector file line". Works with any Traveller edition; extensions (bases, travel zone, PBG, allegiance, {Ix} (Ex) [Cx], stellar data) are used when present and ignored when absent. Creates traveller/worlds/<world>.md dossiers; an existing dossier is canon and is NEVER regenerated or re-rolled. Do NOT use for fantasy worldbuilding or for generating star systems, moons, or anything beyond the mainworld itself.
---

# /uwp-world — deterministic mainworld dossiers from a UWP

Existing worlds (canon — never re-roll these):
!`ls traveller/worlds/ 2>/dev/null || echo "(no worlds generated yet)"`

You expand a Traveller UWP into a detailed, internally consistent mainworld dossier. All randomness comes from `scripts/uwp_world.py`, which seeds every roll from a hash of hex + name + UWP — **you never invent dice results yourself**. Your job is parsing intent, running the script, and writing prose that is 100% grounded in the script's facts. UWP code meanings for prose grounding: `references/uwp-codes.md`.

## Step 1 — Extract the world line and check canon

Take the world line exactly as the user gave it (hex, name, UWP, and any extensions — pass the whole line through). Build the file slug: `<hex>-<name>` lowercased (e.g. `0310-regina`), or just `<name>`, or the bare UWP if unnamed.

**Check `traveller/worlds/` for an existing dossier for this world (match on slug, or on the seed inside the file).** If one exists, it is canon:

- Answer questions, expand sections, or write the requested depth **from the existing file**.
- Never re-run generation in a way that contradicts it. If the user explicitly asks to re-roll, warn that this replaces established canon and require confirmation.

## Step 2 — Run the generator

```
python3 scripts/uwp_world.py "<world line exactly as given>"
```

(Path is relative to this skill's directory.) The JSON output is the complete fact set. Key properties:

- `identity.seed` — same inputs always give this seed; quote it in the dossier.
- The seed uses **only hex + name + UWP**. Extensions never change the rolls, so a world detailed early stays identical when fuller survey data is supplied later.
- `provided_extensions` — canon supplied by the user (best-effort parse; note `parse_notes`). Only mention travel zones, bases, allegiance etc. **if provided** — never invent them.
- `derived` — pure lookup from the UWP digits (no dice). Includes computed trade codes; if `trade_code_mismatches_vs_provided` is non-empty, note the discrepancy in the dossier rather than silently picking one.
- `physical` / `society` / `colour` / `names` — the seeded rolls. Treat every value as established fact.
- `anomalies` — tensions in the UWP (e.g. billions on a vacuum rock) with a seeded explanation. These are the world's best story material: build the prose around them.

## Step 3 — Write the dossier

Ask the user for depth only if unclear from context; default **full**.

- **quick** — half a page: one paragraph of overview, the anomalies, one hook. No file needs saving unless asked (but offer).
- **full** — save to `traveller/worlds/<slug>.md` (create directories as needed) with this structure:

```markdown
# <Name> (<hex>) — <UWP>
seed: <identity.seed>   generated: <date>

## At a glance
<UWP breakdown table: each digit, its meaning, from `derived`>
<provided extensions, if any, stated as canon>

## The world
<physical: climate, geography, day/year, gravity — prose from `physical`>

## Society
<settlement pattern, government character, law character, factions, culture quirks>

## The port
<starport scene, grounded in class + law + zone if provided>

## Anomalies & tensions
<each anomaly: the tension and its canonical explanation, written as world lore>

## Places & people
<notable locations; use `names.settlements` and `names.people` for proper nouns>

## Hooks
<the three patron hooks, plus the one weird thing woven in>

## Facts block
<the full JSON output, verbatim, in a ```json fence — this is the audit trail>
```

**Prose rules:**

- Ground every sentence in the facts JSON or the UWP digits. Elaborate and connect; never contradict, never add new rolls.
- Use the generated names as given (light spelling smoothing is fine — once written to the dossier, the written form is canon).
- **Mainworld only.** Never mention stars, moons, gas giants, belts, or other system bodies — other tools may generate those separately. `physical` values (day length, climate) stand alone without stellar justification.
- Interpret facts *together*: a "temperate" climate on a thin-atmosphere world is temperate for people in filter masks; law 9 colours the starport scene; TL caps what factions can plausibly do.
- Write in a dry, Traveller-library-data-meets-field-report voice. Anomalies are features, not errors.

## Step 4 — Log

Append one line to `traveller/worlds/LOG.md`: date, slug, UWP, seed, depth. If the dossier replaced canon (explicit re-roll), say so in the log line.
