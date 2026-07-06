---
name: worldbuild-init
description: "Initialize a new TTRPG world bible. Use when the user wants to start a new world, new setting, or new worldbuilding project — triggers include \"start a new world\", \"new campaign setting\", \"begin worldbuilding\", \"set up my world\", \"create a world bible\", \"init the worldstate\". Interviews the user for premise, tech level, tone, focus elements, planetary parameters, and a map description, then creates worldstate/world.v1.md and LOG.md per worldstate/SCHEMA.md. Do NOT use for editing an existing world's climate, resources, peoples, history, realms, politics, trade, religion, or solo play — those have their own skills."
---

# /worldbuild-init — create the world bible

Current state of the bible:
!`ls worldstate/ 2>/dev/null || echo "(no worldstate/ yet)"`
!`head -30 worldstate/world.v1.md 2>/dev/null`

You are creating the foundation file every other worldbuilding skill depends on. The contract is `worldstate/SCHEMA.md` — read its `world.v1` block schema and universal conventions before writing anything.

## Step 1 — Guard

If `worldstate/world.v1.md` already exists, STOP and ask the user to confirm they want to replace the existing world (show them its `name:` and `premise:`). Never overwrite silently. Downstream files (climate.v1.md etc.), if present, become stale on re-init — warn the user to regenerate them in pipeline order.

## Step 2 — Interview

Ask the user, in one batch (accept "you decide" for any item and propose something fitting):

1. **Premise** — the world in 1–3 sentences.
2. **Tech level** — e.g. bronze-age, classical, late-medieval, renaissance.
3. **Tone** — e.g. grim low-magic intrigue, hopeful sword-and-sorcery.
4. **Focus elements** (Sanderson's rule): exactly **one physical** element and **up to two cultural** elements this world explores deeply. If the user offers more, push back — depth over breadth — and park extras in `open_questions`.
5. **Planet**: axial tilt (default 23.5°), rotation (default prograde), sea level (default normal). Offer Earth-like defaults; note tilt drives seasons and rotation direction mirrors the prevailing-wind bands.
6. **Calendar anchor**: era label (e.g. "AE") and current in-world year.
7. **Map description** — the critical input. Follow `references/map-description-guide.md`. Required: overall scale, latitude range, each landmass, each mountain range with orientation, coastlines and major seas/gulfs, big rivers if known. If the user has a map image, transcribe it into this structured text and read it back for confirmation — the text, not the image, becomes canon.

## Step 3 — Draft world.v1

Fill the `world.v1` YAML block exactly as specified in `worldstate/SCHEMA.md` (same field names, no additions). Header: `written_by: /worldbuild-init`, `depends_on: []`, today's date. Follow the YAML block with prose sections: `## Premise` (expanded), `## The Map` (readable geography tour), `## Open Questions`.

## Step 4 — Consistency check (mandatory — do not skip)

Before writing the file, verify and then echo the results into the header's `consistency_check:` list (≥3 entries):

- Map description contains a latitude range, at least one mountain range with orientation, and explicit coastlines (SCHEMA global rules 1–2 depend on these downstream).
- `focus.physical` is single; `focus.cultural` has ≤2 entries.
- Tone and tech level do not contradict the premise or each other.
- Planet parameters are stated (defaults count) — climate cannot run without tilt and rotation.

If any check fails, resolve it with the user before writing.

## Step 5 — Write and hand off

1. Write `worldstate/world.v1.md`.
2. Create (or append to) `worldstate/LOG.md`: `[<date>] /worldbuild-init — world "<name>" created`.
3. Tell the user the next pipeline step is `/climate-from-map`, and that the region registry it creates will become the master key for everything else.
