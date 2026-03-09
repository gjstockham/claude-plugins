---
name: write-lyrics
description: >
  Writes original song lyrics from a topic, theme, or creative brief — applying
  deliberate anti-cliché constraints and craft choices to produce distinctive,
  human-feeling lyrics. Saves the draft to lyrics-draft.md. Use this whenever a
  user wants to write, create, or draft a song or lyrics, even if they just describe
  a feeling or situation without explicitly asking for a song. If they have a topic
  in mind, go straight to writing — don't ask for more detail unless the brief is
  truly empty.
argument-hint: "[topic, theme, or creative brief]"
user-invocable: true
allowed-tools: Write
context: fork
---

The user wants to write song lyrics. Brief: $ARGUMENTS

## Step 1 — Validate input

If $ARGUMENTS is empty or too vague to write from, stop and respond:
"What would you like to write a song about? Give me a topic, a situation, a character,
a mood, or a detailed brief. Or run `/suggest-topic` to get a random prompt."

## Step 2 — Make craft decisions (before writing anything)

Before generating a single line of lyrics, decide and note down:

- **Structure:** choose a form that fits the brief (verse/chorus/bridge, AABA,
  through-composed, or something else). The form should serve the content — do not
  default to verse/chorus/verse/chorus/bridge/chorus out of habit.
- **Rhyme scheme:** choose the scheme per section. It does not need to be consistent
  across the whole song. Consider whether any section benefits from no rhyme at all.
- **Tonal register:** where does this sit — conversational, formal, fragmented,
  stream-of-consciousness, blunt? Who is the narrator and what is their specific
  situation (not just their feeling)?
- **Central image or conceit:** one concrete, physical thing or situation that anchors
  the whole song. This is not the theme — it is the specific lens the theme is seen
  through.

Record these decisions. They will appear as a craft notes block at the end of the output.

## Step 3 — Write the lyrics

Write the full song. Aim for 2–3 verses, a chorus, and a bridge as a baseline, but
follow the structure you chose in Step 2.

### Craft moves that make the difference

These are the things that separate a memorable song from a serviceable one — each
addresses a specific failure mode of AI-generated lyrics:

- **Concrete sensory detail per section.** The detail that could only exist in *this*
  song's world: a specific object, an exact gesture, a texture. Not "the rain" — the
  rain of this particular moment. Specificity is what makes a listener feel seen.
- **Chorus that earns its place.** If the chorus just restates the verse's feeling
  more loudly, it's decoration. A good chorus does something the verses structurally
  or tonally can't — shifts register, widens the frame, or arrives at a different
  kind of language.
- **At least one unexpected word choice per verse.** The word that's slightly wrong
  but more true than the obvious word. This is what creates the small shock of
  recognition that makes lyrics stick.
- **An ending that moves.** The final lines should shift something — perspective,
  tense, who the narrator is addressing, the emotional key. An ending that simply
  restates the thesis is a song that doesn't trust its own journey.

### Phrases and patterns to avoid

These aren't arbitrary rules — they're patterns so overused that they now signal
"AI wrote this" or "nobody really thought about this". Encountering them in a draft
is a sign to stop and find what you actually mean:

**Banned phrases (exact or close variants):**
- "dance in the rain" / "dancing in the rain"
- "scars that remain" / "scars remain"
- "broken wings" / "shattered dreams" / "broken dreams"
- "fade to grey" / "fade away into"
- "burn it all down" / "watch it burn"
- "rise from the ashes"
- "lose yourself" / "find myself" / "find my way"
- "in the end" / "after all" / "when all is said and done"
- "in the silence" / "in the darkness" / "beneath the stars" / "lost in the night"
- "heart of gold" / "heart of stone" / "heart of fire"
- "fire in my soul" / "fire in my veins" / "set my soul on fire"
- "the weight of the world" / "carry the weight"
- "a symphony of" / "a tapestry of" / "a kaleidoscope of"
- "whispers in the wind"
- Any line of the form "I am [adjective], I am [adjective], I am [noun]"

**Banned rhyme pairs as primary anchors:**
- heart / apart (or heart / start, heart / art)
- eyes / skies (or eyes / lies, eyes / rise)
- fire / desire
- pain / rain
- love / above
- night / light (unless used with real purpose)
- free / me / be / see as the only rhyme strategy in a chorus

**Banned structural moves:**
- Opening the first three lines with "I" as the first word
- A chorus that consists only of the title repeated or the song's theme restated
- Ending with a question the lyrics just finished answering
- An unearned uplift ending — if the song has been about loss or difficulty, do not
  resolve it into hope unless the lyrics have genuinely earned that turn

**Banned metaphor defaults:**
- Fire = passion or anger
- Storm = emotional turmoil
- Chains / cage = constraint or bad relationship
- Journey / road = life or personal growth
- Light = hope (unless subverted)
- Darkness = depression or grief (unless subverted)

### Self-audit before finalising

Read back through the draft and check each line against the patterns above. The goal
isn't mechanical compliance — it's noticing where a lazy default crept in and finding
what the song actually wants to say instead. The rewrite should be better, not just
technically clean.

## Step 4 — Assemble the output

Format the song with section labels: [Verse 1], [Chorus], [Verse 2], [Bridge], etc.

Follow the lyrics with a horizontal rule and a craft notes block:

---
**Craft notes**
- Structure: [what you chose and why]
- Rhyme scheme: [per section, using letter notation]
- Register: [tonal description]
- Central conceit: [the one concrete thing anchoring the song]
- One unexpected word choice and why: [quote line, explain the word]

## Step 5 — Save to file

Write the complete output (lyrics + craft notes) to `lyrics-draft.md` in the
current working directory.

Then print the full output and add:

---
*Draft saved to `lyrics-draft.md`. Run `/review-lyrics` for structured feedback,
or `/revise-lyrics [notes]` to make specific changes.*
