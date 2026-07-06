# Worldbuilding Skills — a chainable suite for solo TTRPG worldbuilding

A set of 17 composable Claude skills that build a coherent fantasy world one causal layer at a time — map → climate → resources → peoples → history → realms → politics → trade → religion/culture → solo-play tools. Each skill reads the previous skills' output from a shared "world bible" (`worldstate/`) and writes its own, so the world stays internally consistent: the deserts explain the trade routes, the trade routes explain the wars, and the myths explain the deserts.

## How it works

Everything lives in one folder of Markdown files, `worldstate/`, the machine-readable "world bible." Every skill:

1. Reads the upstream file(s) it depends on (auto-loaded into context when the skill runs).
2. Generates its layer, applying real-world rules (climate science, premodern economics, faction mechanics).
3. Runs a **consistency check** against everything already established, and echoes the specific facts it honored.
4. Writes one `worldstate/*.v1.md` file and logs a line to `worldstate/LOG.md`.

The contract that keeps them all speaking the same language is `worldstate/SCHEMA.md` — the single source of truth for field names and the ten global consistency rules. Read it if you want to understand or extend the system.

## Requirements

This is a Claude plugin (for Cowork, Claude Code and Claude Desktop). Install the `.plugin` file and the skills are available in any session; each world lives in whatever folder you point Claude at, where the skills create and maintain its `worldstate/` files. Skills are invoked by typing `/skill-name`, and Claude will also trigger the right one automatically when you describe what you want.

## Getting started

Build the world in dependency order. Run each step, review the file it writes, then move on. You can stop at any layer — a world with just climate and realms is perfectly usable.

> **Lost? Run `/worldbuild-status`** at any time. It's a read-only guide that shows a phase checklist, tells you the next skill to run and why, and warns if anything is missing or out of date. It never changes your world — it just orients you.

**Phase 0 — Foundation**
- `/worldbuild-init` — interviews you for premise, tech level, tone, focus elements, planet params, and a map description; creates the empty bible.

**Phase 1 — Climate** (everything depends on this)
- `/climate-from-map` — turns your map into regions with biomes, winds, seasons. Establishes the region registry every later skill references.

**Phase 2 — The causal chain** (run in this order)
- `/resource-map` → what each region produces and needs
- `/populate` → who lives where, and why
- `/history-and-migration` → the past that explains the present
- `/realms-and-borders` → kingdoms, borders, capitals, cities
- `/political-intrigue` → factions, rivalries, live situations
- `/trade-routes` then `/travel-calculator` → trade network + journey times

**Phase 3 — Cultural layer** (any order)
- `/pantheon` · `/calendar` · `/mythology` · `/naming`

**Phase 4 — Solo play** (once the world exists)
- `/oracle` — yes/no oracle, random events, NPC reactions (Mythic-style, grounded in your world)
- `/rumour-table` — setting-consistent gossip for any town, every rumour traceable to a real hook
- `/faction-turn` — advance the world between sessions; ticks faction clocks and cascades the fallout

## Tips

- **Trust the order.** Each skill refuses to run if a file it needs is missing and tells you which skill to run first.
- **Review as you go.** Every file has a human-readable prose section under the YAML block — read it and edit freely; the skills parse only the YAML.
- **Editing by hand is fine.** If you change a fact, later skills will honor it. If you change something big (e.g. re-run climate), regenerate the downstream files in order.
- **Playing solo:** ask `/oracle` questions in natural language ("is the guard suspicious?"), pull `/rumour-table` for wherever the party is, and run `/faction-turn` between sessions to keep the world moving on its own.
- **`worldstate/LOG.md`** is your campaign journal — oracle answers, faction turns, and pipeline steps all land there.

## What's in this folder

```
README.md                     ← this file
worldbuilding-skills.md       ← the design report / methodology behind the suite
.claude/skills/               ← the 17 skills (each a folder with SKILL.md, some with references/)
worldstate/
  SCHEMA.md                   ← the contract: field names + 10 consistency rules
  *.v1.md                     ← the world bible (one file per layer)
  LOG.md                      ← append-only campaign & pipeline log
```

## The sample world (Vessa)

`worldstate/` currently contains a complete worked example — **Vessa**, a continent of caravan cities strung across a rain-shadow desert, generated end-to-end as a build test. Use it to see what good output looks like. When you're ready to build your own, run `/worldbuild-init` (it will ask before overwriting) and regenerate each layer in order, or delete the `*.v1.md` files first for a clean slate. Keep `SCHEMA.md` and `LOG.md`.
