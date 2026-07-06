---
name: oracle
description: "Answer solo-RPG oracle questions for a fantasy world — yes/no oracle, random events, NPC reactions, and \"what happens next\" for solo tabletop play. Use when the user is playing solo and asks the oracle a question, wants a yes/no ruling, an NPC reaction, a random event, or asks \"roll the oracle\", \"does X happen\", \"is the guard suspicious\", \"what happens next\", \"ask the fates\" — triggers include \"oracle\", \"yes/no oracle\", \"does the\", \"is the\", \"roll for\", \"NPC reaction\", \"random event\", \"chaos factor\", \"solo play\". Reads the whole worldstate (especially politics.v1, pantheon.v1, situations) and creates/updates worldstate/solo.v1.md (chaos factor, threads, NPCs) and appends the Q&A to LOG.md. Answers are Mythic-style with yes/no-and/but modified by the Chaos Factor, and stay consistent with established world facts. Do NOT use to write region rumour tables (that is /rumour-table) or to advance faction clocks over time (that is /faction-turn)."
---

# /oracle — the solo-play oracle

Live campaign state:
!`grep -E 'chaos_factor|threads:|- \{id: thr|status:' worldstate/solo.v1.md 2>/dev/null || echo "(no solo.v1 yet — will initialize)"`
Current situations & factions (for grounded answers):
!`grep -E '- \{id: sit|title:|involves:|- id: fac|name:|status:|tier:' worldstate/politics.v1.md 2>/dev/null | head -50`
Recent play:
!`tail -8 worldstate/LOG.md 2>/dev/null`

You run a Mythic-style oracle grounded in the established world. Tables and procedures: `references/oracle-tables.md`. Contract: `worldstate/SCHEMA.md` (`solo.v1`).

## Step 0 — Initialize solo.v1 if absent
If `worldstate/solo.v1.md` does not exist, create it: `chaos_factor: 5`, seed `threads:` from politics.v1 `situations` (one open thread per situation), seed `npcs:` from faction `face` leaders with `disposition:` = their faction `status`. Preserve any existing `rumour_tables:` written by /rumour-table — never clobber that section.

## Step 1 — Read the question and pick the tool
- **Yes/No question** → yes/no oracle (Step 2).
- **"What happens?" / scene disruption** → random event (Step 3).
- **Meeting someone / how do they react** → reaction roll (Step 4).

## Step 2 — Yes/No oracle
Judge likelihood (certain→impossible), cross with the current `chaos_factor` per the odds table in the reference, and roll d100. Return one of: **No and, No, No but, Yes but, Yes, Yes and**. If the d100 roll is doubles (11, 22, …) AND the tens digit ≤ the Chaos Factor, trigger a **random event** (Step 3) as well. Interpret the result IN WORLD, citing the relevant faction/situation/god it touches. Then adjust the Chaos Factor: +1 if the scene went chaotically/against the player, −1 if controlled/in their favour (clamp 1–9).

## Step 3 — Random event
Roll event focus (NPC action / thread advance / new thread / faction move / omen / setback) + two meaning words, then interpret using REAL world elements — a named faction, an NPC face, an active situation, a god's omen (use the world's moon(s) from calendar.v1 for portents). Never invent an entity that contradicts the world state; prefer escalating an existing situation.

## Step 4 — NPC reaction
Roll reaction (hostile→helpful) modified by the NPC's `disposition` and faction `status`, then describe how this specific NPC (their faction goals, their favour/fight) responds. Update the NPC's `disposition` if the interaction shifts it.

## Step 5 — Update state & log (mandatory)
- Update `chaos_factor`, `threads` (open/closed/new), and `npcs` in solo.v1. Preserve the rumour section.
- Append to `LOG.md`: `[<in-world date>] /oracle — Q: "..." → A: ... (CF now N)`.
- **Consistency check:** the answer references only existing ids and does not contradict climate/realms/politics/pantheon; echo the specific world facts the answer honored (1–2 lines) into the log entry. If a result would contradict canon, re-interpret it so it fits.
