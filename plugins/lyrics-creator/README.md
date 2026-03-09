# lyrics-creator

Write original song lyrics with anti-cliché constraints and structured critique.

## Install

```
/plugin install lyrics-creator@gjstockham-plugins
```

## Skills

### `/suggest-topic`

Suggests a random songwriting prompt from a curated list.

```
/suggest-topic
/suggest-topic melancholy
/suggest-topic humour
```

Optionally pass a mood or genre keyword to filter the list. Run multiple times for
different suggestions.

---

### `/write-lyrics [topic or brief]`

Writes a complete song draft from a topic, theme, or detailed brief. Applies
deliberate craft choices and a strict anti-cliché ruleset before writing.

Saves the draft to `lyrics-draft.md` in the current working directory.

```
/write-lyrics The last train home on a Sunday night
/write-lyrics a song about watching someone you love forget things
/write-lyrics upbeat country song about a small victory at work
```

---

### `/review-lyrics`

Provides a structured craft critique of the current draft in `lyrics-draft.md`.
Covers what works, what does not, a cliché audit, structural assessment, and
one concrete actionable recommendation.

Saves the review to `lyrics-review.md`.

```
/review-lyrics
/review-lyrics [paste lyrics directly for a one-off review]
```

---

### `/revise-lyrics [optional notes]`

Revises the draft using the review in `lyrics-review.md`. Preserves what works,
improves what does not. Archives the previous draft as `lyrics-draft-[timestamp].md`
before overwriting.

```
/revise-lyrics
/revise-lyrics make the bridge shorter and cut the final verse
/revise-lyrics change to second-person throughout
```

---

## Typical workflow

```
/suggest-topic                          # get a prompt
/write-lyrics [the suggested topic]     # write first draft → lyrics-draft.md
/review-lyrics                          # structured critique → lyrics-review.md
/revise-lyrics                          # apply the critique → new lyrics-draft.md
/review-lyrics                          # review again
/revise-lyrics make the chorus punchier # further targeted revision
```

## Adding topics

The topic list lives at `plugins/lyrics-creator/skills/suggest-topic/topics.txt`.
One topic per line. Add your ~500 prompts to this file — no special formatting needed.
