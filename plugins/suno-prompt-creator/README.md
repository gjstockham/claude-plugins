# suno-prompt-creator

Converts song lyrics into a pair of Suno AI music prompts: a formatted lyric
block with structural meta tags, and a crafted style prompt — plus a recommended
parameter table for Suno's Advanced Options.

## Install

```
/plugin install suno-prompt-creator@gjstockham-plugins
```

## Skills

### `/create-suno-prompt`

Walks through a short Q&A about genre, mood, vocals, instruments, and energy,
then produces:

1. **Lyric block** — your lyrics reformatted with Suno meta tags (`[Verse 1]`,
   `[Chorus]`, `[Bridge]`, etc.). For Suno v5, inline dynamic tags are added at
   key structural moments (`[Solo: 12s guitar swell]`, `[Break: bass drop]`).

2. **Style prompt** — a crafted style descriptor for the Suno style field,
   anchoring key mood/genre terms at both start and end, with specific
   instrument and vocal descriptors.

3. **Recommended parameters** — a table of suggested Vocal Gender, Weirdness %,
   Style Influence %, and Exclude Styles for Suno's Advanced Options panel.

Output is saved to `suno-prompt.md`.

## Works great with

- **lyrics-creator** — run `/write-lyrics` first, then `/create-suno-prompt`
  picks up `lyrics-draft.md` automatically.
- **lyrics-analyzer** — analyse an existing song's style with `/lyric-recipe`,
  then write your own lyrics and convert with `/create-suno-prompt`.

## Suno versions supported

Prompts are tailored for **Suno v5** by default (inline dynamic tags, narrative
style sentences, repeated anchor cues). Specify v4/v4.5 in the Q&A and the skill
switches to structural-tags-only lyric formatting.
