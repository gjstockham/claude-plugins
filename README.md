# claude-plugins

An eclectic mix of skills, agents and commands for Claude Code and CoWork.

## Install

```
/plugin marketplace add gjstockham/claude-plugins
```

Then install individual plugins:

```
/plugin install <plugin-name>@gjstockham-plugins
```

## Plugins

| Plugin | Description |
|--------|-------------|
| [lyrics-analyzer](./plugins/lyrics-analyzer/) | Analyse song lyrics for themes and literary craft, or extract an abstract style recipe to guide songwriting. |
| [lyrics-creator](./plugins/lyrics-creator/) | Write original song lyrics with anti-cliché constraints, review with structured critique, and iterate through a create-review-revise cycle. |
| [suno-prompt-creator](./plugins/suno-prompt-creator/) | Turn song lyrics into Suno AI music prompts — formatted lyric block with meta tags, crafted style prompt, and recommended advanced parameters. |
| [watercolor-guide](./plugins/watercolor-guide/) | Analyse any image and receive a step-by-step watercolor painting guide — composition, tonal plan, palette, and every technique in the order they are applied. |

## Structure

Each plugin lives in `plugins/<plugin-name>/` and may contain:

- `skills/` — slash-command skills (user or Claude invocable)
- `agents/` — subagent definitions
- `hooks/` — hook configurations
- `.claude-plugin/plugin.json` — plugin manifest

Works in both Claude Code CLI and Claude CoWork.
