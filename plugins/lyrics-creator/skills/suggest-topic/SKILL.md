---
name: suggest-topic
description: >
  Suggests a random songwriting topic from a curated list of creative prompts.
  Use this whenever a user wants a song topic, asks for inspiration, doesn't know
  what to write about, or wants to get started with songwriting. Invoke proactively
  any time the user seems stuck for a subject — don't wait for them to explicitly
  ask for a "prompt" or "suggestion".
argument-hint: ""
user-invocable: true
allowed-tools: Bash
context: fork
---

The user wants a random songwriting topic.

## Step 1 — Pick a random topic

Run the following command using the Bash tool:

```
python3 "${CLAUDE_SKILL_DIR}/scripts/pick-topic.py" "${CLAUDE_SKILL_DIR}/topics.txt"
```

The script prints one randomly selected topic to stdout. If it exits with an error,
stop and report: "Could not read the topics file. Please check the plugin installation."

## Step 2 — Present the topic

Output in exactly this format:

---
**Songwriting prompt:** [topic text]

**One possible angle:** [A single sentence suggesting an unexpected or non-obvious
take on this topic — not the most obvious interpretation. Something that would
surprise the user slightly but feel true once they hear it.]

---

To write a song on this topic: `/write-lyrics [topic text]`
Run `/suggest-topic` again for a different prompt.
