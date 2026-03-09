---
name: review-lyrics
description: >
  Provides a structured craft critique of song lyrics. Reads lyrics-draft.md from
  the current directory, or reviews lyrics passed directly as an argument. Use this
  whenever there are lyrics to evaluate — after /write-lyrics, after /revise-lyrics,
  or any time a user asks for feedback, critique, or "what do you think?" about
  lyrics. Don't be shy about invoking this: honest craft feedback is the point.
argument-hint: "[optional: paste lyrics here, or leave blank to review lyrics-draft.md]"
user-invocable: true
allowed-tools: Read, Write
context: fork
---

## Step 1 — Source the lyrics

If $ARGUMENTS is non-empty and looks like song lyrics (more than 20 words, contains
line breaks or section labels), treat $ARGUMENTS as the lyrics to review.

Otherwise, read `lyrics-draft.md` from the current working directory.
If the file does not exist and $ARGUMENTS is empty, stop and respond:
"No lyrics found. Run `/write-lyrics` to create a draft, or paste lyrics directly:
`/review-lyrics [paste lyrics here]`"

## Step 2 — Extract craft notes (if present)

If the source contains a "Craft notes" block (written by `/write-lyrics`), extract
it separately. Note the stated intentions — the review should assess whether they
were achieved, not just whether the lyrics are good in the abstract.

## Step 3 — Produce the critique

Write a structured critique under these headings. Be specific throughout: quote lines,
name the exact mechanism of success or failure, avoid vague encouragement.

### What works

Identify 2–4 specific lines, images, or structural choices that succeed. For each:
- Quote the line or name the structural choice exactly
- Explain why it works at the level of craft, not sentiment (not "this line is moving"
  but "this line works because the verb choice does X" or "this image is specific
  enough to feel true but universal enough to transfer")

### What doesn't work

Identify 2–4 specific lines or choices that fail or underperform. For each:
- Quote the line exactly
- Name the failure mechanism: too abstract, clichéd, rhythm breaks down, wrong
  register for the song's voice, does not earn its place, borrowed from another song
- Do not soften this. A bad line is a bad line.

### Cliché audit

Scan for any of the following and flag them by line:
- Phrases from the standard banned list: "fade away", "fire in my soul", "broken
  dreams", "in the darkness", "rise from the ashes", "heart of [noun]", "storm"
  as emotional metaphor, "chains" or "cage" as constraint metaphor, "journey" or
  "road" as life metaphor, "light" as hope without subversion
- Rhyme anchors that feel lazy: heart/apart, eyes/skies, fire/desire, pain/rain
- Any chorus that only restates the title or the verse's emotional summary
- Any ending that resolves too easily into hope or resolution

If none found, state that clearly: "No significant clichés detected."

### Structural assessment

- Does the song's architecture serve its content?
- Is the chorus doing something the verses cannot do, or is it just the verses louder?
- Does the ending land? Does it shift anything, or does it peter out?
- Is there a section that should be cut, shortened, or moved?

### If craft notes were present

State whether the writer's stated intentions were achieved:
- Did the chosen structure serve the brief?
- Was the central conceit deployed effectively throughout, or did it get lost?
- Did the unexpected word choices land?

### The one most important change

Name one specific, actionable change that would most improve this song.
Not a list. One thing. Be precise about which line, section, or structural move
to change, and what to change it to or in which direction.

## Step 4 — Save and present

Write the critique to `lyrics-review.md` in the current working directory.
Print it to stdout, then add:

---
*Review saved to `lyrics-review.md`. Run `/revise-lyrics` to apply changes
(optionally add specific instructions: `/revise-lyrics [your notes]`), or
paste a revised version and run `/review-lyrics` again.*
