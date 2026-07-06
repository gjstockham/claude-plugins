# Oracle tables reference

Solo-play oracle procedures. Sources: Mythic GM Emulator 2e (Fate Chart / Chaos Factor / yes-and-but), One Page Solo Engine, Ironsworn. Roll d100 unless noted.

## Chaos Factor (1–9)
Tracks how in- or out-of-control the story is. Starts at 5. After each scene: +1 if the scene was chaotic / went against the player; −1 if controlled / in their favour. Clamp 1–9. Higher chaos = "yes" more likely and random events more frequent.

## Yes/No oracle (Fate-Chart style)
1. Rate the question's **likelihood**, then read the target for the current Chaos Factor. Roll d100 ≤ target = Yes.

| Likelihood | CF1 | CF3 | CF5 | CF7 | CF9 |
|-----------|----|----|----|----|----|
| Certain | 45 | 70 | 85 | 95 | 99 |
| Likely | 30 | 55 | 75 | 90 | 97 |
| 50/50 | 15 | 35 | 50 | 65 | 85 |
| Unlikely | 5 | 15 | 25 | 45 | 70 |
| Impossible| 1 | 5 | 15 | 30 | 55 |

2. **And/But modifiers:** roll within 1/5 of the low end → "…and" (stronger); within 1/5 of the high end → "…but" (complication). So results scale: **No and · No · No but · Yes but · Yes · Yes and.**
3. **Random event trigger:** if the d100 roll is doubles (11, 22, …, 99) AND the tens digit ≤ Chaos Factor, a random event also fires.

### Simple d6 fallback (no d100)
1 No, and · 2 No · 3 No, but · 4 Yes, but · 5 Yes · 6 Yes, and. Shift up/down 1 step for Likely/Unlikely.

## Random event (roll d100 focus, or d10)
| d10 | Focus |
|----|-------|
| 1–2 | An NPC acts (use a real faction face) |
| 3 | A current thread advances |
| 4 | A new thread opens |
| 5–6 | A faction makes a move (tie to a live situation) |
| 7 | An omen / divine sign (use a god + the world's moon(s) from calendar.v1) |
| 8 | A setback for the player |
| 9 | A boon / lucky break |
| 10 | Something ambiguous — interpret loosely |

Then draw **two meaning words** (action + subject) and interpret against real world elements. Meaning-word seeds: *seize, betray, reveal, delay, demand, protect, flee, bargain, threaten, mourn, gather, corrupt* × *silver, oath, water, caravan, heir, border, faith, debt, kin, route, secret, grain.* Always resolve toward an EXISTING faction/situation/NPC before inventing anything new.

## NPC reaction roll (2d6 + disposition)
| Total | Reaction |
|------|----------|
| ≤3 | Hostile — acts against the player |
| 4–6 | Wary / unfriendly |
| 7–8 | Neutral — non-committal |
| 9–11 | Favourable — will help with a price |
| ≥12 | Helpful — genuinely on-side |
Modifier: add the NPC's `disposition` (−3..+3) and the faction `status`. Interpret through the NPC's goal, favour, and fight.

## Scene setup (optional, Mythic-style)
Frame the expected scene, then roll d10 vs Chaos Factor: ≤CF and odd = "altered scene" (twist it); ≤CF and even = "interrupt scene" (random event instead). Above CF = scene proceeds as expected.

## Grounding rule
Every oracle output must be interpreted using the actual world state — named factions, situations, gods, regions, the calendar's moon(s) — and must never contradict established climate/realms/politics. When in doubt, escalate a live situation rather than introduce a new element.
