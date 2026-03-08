---
name: lyric-recipe
description: >
  Searches the web for the lyrics of a specified song and produces an abstract
  "lyric recipe" — a generalised stylistic formula describing how the song is
  written without naming the song, artist, or quoting actual lyrics. Useful for
  writers who want to emulate a style. Use this when a user asks for a style
  guide, a writing recipe, or wants to write a song in the style of another.
argument-hint: "[song title] by [artist]"
user-invocable: true
allowed-tools: Agent
context: fork
---

The user wants a lyric recipe — an abstract stylistic formula — derived from a song's lyrics. The song is: $ARGUMENTS

## Step 1 — Validate input

If $ARGUMENTS does not clearly contain both a song title and an artist name, stop and ask:
"Could you provide both the song title and the artist? For example: `/lyric-recipe Running Up That Hill by Kate Bush`"

## Step 2 — Retrieve lyrics

Use the Agent tool to invoke the "lyrics-search" agent with the following prompt:
"Find the complete lyrics for $ARGUMENTS."

If the agent responds with a message beginning with `LYRICS_NOT_FOUND:`, stop and report to the user:
"Sorry, I could not find lyrics for '$ARGUMENTS'. [reason from agent]. Please check the song title and artist name and try again."

## Step 3 — Produce the lyric recipe

Using the retrieved lyrics, produce an abstract "lyric recipe".

IMPORTANT CONSTRAINTS:
- Do NOT mention the song title anywhere in the output.
- Do NOT mention the artist or songwriter name anywhere in the output.
- Do NOT quote any actual lyrics verbatim.
- Do NOT reference the year, album, or any identifying release details.
- The recipe must be usable as a standalone creative brief — someone who has never heard the song should be able to follow it.

Format the recipe using Markdown. Use the following sections:

### The Premise
One sentence describing the abstract emotional or narrative territory of the song (e.g. "A declaration of defiance from someone who has been underestimated") — without tying it to any real person, event, or song.

### Structure Blueprint
A structural template showing the song's architecture:
- Number of verses, choruses, bridges, outros
- Approximate line count per section
- Any structural patterns worth noting (e.g. "the final chorus drops a line compared to earlier iterations")

### Rhyme and Rhythm Pattern
- Rhyme scheme using letter notation, per section
- Metre or syllabic feel (e.g. "lines run long and breathless, resisting neat stress patterns")
- Any deliberate rhythmic tension or syncopation in the writing

### Tonal Recipe
Describe the narrator's voice and register — e.g. intimate vs. declaratory, conversational vs. poetic, bitter vs. celebratory. Note any tonal shifts between sections.

### Devices to Deploy
List 4–7 specific literary or rhetorical devices used, described abstractly. For example: "Use anaphora at the start of each verse line to build momentum" or "Employ a single extended metaphor that runs through all verses but is dropped in the chorus."

### Imagery Palette
Describe the categories of imagery used (e.g. "domestic and mundane objects", "natural phenomena", "urban decay") without citing specific images from the lyrics.

### Emotional Arc
Map the emotional journey: how does the narrator's emotional state or the song's energy shift from opening to close?

### The Recipe in One Paragraph
Synthesise all of the above into a single prose paragraph a songwriter could read as a creative brief before writing.
