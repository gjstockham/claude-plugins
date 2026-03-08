---
name: analyze-lyrics
description: >
  Searches the web for the lyrics of a specified song and produces a deep literary
  analysis: themes, structure, rhyme scheme, literary devices, imagery, mood, and
  cultural or historical context. Use this when a user asks to analyze song lyrics
  or wants to understand what a song means or how it is constructed.
argument-hint: "[song title] by [artist]"
user-invocable: true
allowed-tools: Agent
context: fork
---

The user wants a deep analysis of a song's lyrics. The song is: $ARGUMENTS

## Step 1 — Validate input

If $ARGUMENTS does not clearly contain both a song title and an artist name, stop and ask:
"Could you provide both the song title and the artist? For example: `/analyze-lyrics Bohemian Rhapsody by Queen`"

## Step 2 — Retrieve lyrics

Use the Agent tool to invoke the "lyrics-search" agent with the following prompt:
"Find the complete lyrics for $ARGUMENTS."

If the agent responds with a message beginning with `LYRICS_NOT_FOUND:`, stop and report to the user:
"Sorry, I could not find lyrics for '$ARGUMENTS'. [reason from agent]. Please check the song title and artist name and try again."

## Step 3 — Analyse the lyrics

Using the lyrics returned by the agent, produce a structured analysis with the following sections. Use Markdown headings.

### Overview
A one-paragraph summary of the song's subject matter and emotional register.

### Themes
Identify 2–5 major themes. For each theme, briefly explain how it manifests in the lyrics, citing specific lines (quoted exactly from the retrieved lyrics) as evidence.

### Structure
Describe the song's compositional structure (e.g. verse-chorus-bridge, AABA, through-composed). Note any structural variations or surprises.

### Rhyme Scheme
Map the rhyme scheme using letter notation (ABAB, AABB, etc.) for at least one representative verse and the chorus. Note any slant rhymes, internal rhymes, or deliberate breaks in the scheme.

### Literary Devices
Identify and explain instances of: metaphor, simile, personification, alliteration, assonance, anaphora, or any other notable devices. Quote the relevant line for each.

### Imagery and Sensory Language
Describe the dominant imagery (visual, auditory, tactile, etc.) and explain what emotional or thematic work it does.

### Mood and Tone
Characterise the emotional mood and the narrator's tone. Note any shifts in mood across the song.

### Cultural and Historical Context
Where relevant, place the song in its cultural, historical, or biographical context. Note any references, allusions, or events the song responds to.

### Conclusion
A brief closing paragraph synthesising the above into an overall interpretation of the song's significance or craft.
