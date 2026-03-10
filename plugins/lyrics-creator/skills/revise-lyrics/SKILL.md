---
name: revise-lyrics
description: >
  Revises song lyrics using the critique in lyrics-review.md, preserving what works
  and improving what does not. Reads lyrics-draft.md and lyrics-review.md from the
  current directory, archives the old draft, and writes a new one. Use this whenever
  the user wants to improve, change, or iterate on existing lyrics — especially after
  a /review-lyrics pass. Also invoke it when the user says things like "make the
  chorus shorter" or "change the ending" with a draft already in context.
argument-hint: "[optional: specific additional instruction, e.g. 'make chorus shorter']"
user-invocable: true
allowed-tools: Read, Write
context: fork
---

## Step 1 — Load the draft

Read `lyrics-draft.md` from the current working directory.
If not found, stop: "No draft found. Run `/write-lyrics [topic]` to create one first."

## Step 2 — Load the review

Read `lyrics-review.md` from the current working directory.
If not found, stop: "No review found. Run `/review-lyrics` to generate a critique first."

## Step 3 — Plan the revision

Before changing anything, identify:

1. **What to preserve:** Every line, image, or section the review identified as
   working. A revision that fixes the bad parts by breaking the good ones isn't
   progress.

2. **What to fix:** The one most important change identified by the reviewer. If the
   user passed specific instructions ("$ARGUMENTS"), treat those as the primary
   directive and let the reviewer's recommendations inform the rest. Focused revision
   beats wholesale rewrite — the song already has a shape; work with it.

3. **What clichés to remove:** Any lines flagged in the reviewer's cliché audit.

## Step 4 — Revise the lyrics

Apply the planned changes, keeping the same craft standards the original writer
aimed for: concrete sensory detail per section, a chorus that earns its structural
difference from the verses, and an ending that shifts something rather than restating.

Read the revised draft back through and check it against the same patterns to avoid
as the original writer used — lazy defaults can creep back in during a revision:

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

**Banned metaphor defaults:**
- Fire = passion or anger
- Storm = emotional turmoil
- Chains / cage = constraint or bad relationship
- Journey / road = life or personal growth
- Light = hope (unless subverted)
- Darkness = depression or grief (unless subverted)

When you find one of these patterns, the goal isn't just to remove it — it's to find
what the song is actually trying to say at that moment and say that instead.

## Step 5 — Update the craft notes

Update the craft notes block to record what changed in this revision and why.
Keep the original craft decisions for reference; add a "Revision notes" subsection:

---
**Revision notes**
- Changes made: [list the specific changes]
- Preserved from previous draft: [what was kept and why]
- Additional instruction applied: [what $ARGUMENTS asked for, if anything]

## Step 6 — Archive and save

Generate a timestamp string in the format `YYYYMMDD-HHMMSS` (use the current date/time
as best you know it — precision is not critical, uniqueness is).

Write the old draft content (read in Step 1) to `lyrics-draft-[timestamp].md`.
This is the archive. Do not modify the archived content.

Write the new revised draft (lyrics + updated craft notes) to `lyrics-draft.md`,
overwriting the previous version.

Print the new draft in full, then add:

---
*Previous draft archived to `lyrics-draft-[timestamp].md`. New draft saved to
`lyrics-draft.md`. Run `/review-lyrics` to review the revised version.*
