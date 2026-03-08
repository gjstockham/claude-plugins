# lyrics-analyzer

Analyse song lyrics or generate abstract style recipes for any song.

## Skills

### `/analyze-lyrics [song] by [artist]`

Retrieves the lyrics for a song and produces a structured literary analysis covering themes, structure, rhyme scheme, literary devices, imagery, mood, and cultural context.

**Example:**
```
/analyze-lyrics Hurt by Nine Inch Nails
```

### `/lyric-recipe [song] by [artist]`

Retrieves the lyrics for a song and produces an abstract "lyric recipe" — a generalised stylistic formula you could use to write a song in the same style, without naming the song or artist or quoting its lyrics.

**Example:**
```
/lyric-recipe Running Up That Hill by Kate Bush
```

## Agent

### `lyrics-search`

Internal agent used by both skills to search the web for and retrieve song lyrics. Not user-invocable directly.

## Notes

- Both skills require a song title and artist name. Use the form `[title] by [artist]`.
- If lyrics cannot be found (obscure songs, regional releases, very new releases), the skill will say so clearly.
- Lyrics are retrieved live from the web each time — the plugin does not cache.
