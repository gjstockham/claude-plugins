# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

This is a public Claude plugin marketplace (`gjstockham-plugins`) containing skills, agents, and commands for Claude Code and CoWork. Users install it via:

```
/plugin marketplace add gjstockham/claude-plugins
/plugin install <plugin-name>@gjstockham-plugins
```

## Repository Structure

```
.claude-plugin/
  marketplace.json        # Marketplace catalog — register every plugin here
plugins/
  <plugin-name>/
    .claude-plugin/
      plugin.json         # Plugin manifest (optional but recommended)
    skills/
      <skill-name>/
        SKILL.md          # Skill definition with YAML frontmatter
    agents/
      <agent-name>.md     # Agent system prompt with YAML frontmatter
    hooks/
      hooks.json          # Hook event configuration
    README.md
```

## Adding a New Plugin

1. Create `plugins/<plugin-name>/` with its components.
2. Add an entry to `.claude-plugin/marketplace.json` under `"plugins"`:

```json
{
  "name": "my-plugin",
  "source": "./plugins/my-plugin",
  "description": "What this plugin does",
  "version": "1.0.0",
  "author": { "name": "Geoff Stockham", "email": "geoff@stormid.com" },
  "license": "MIT",
  "keywords": ["tag1", "tag2"],
  "category": "productivity"
}
```

3. Update the Plugins table in `README.md`.

## Plugin Component Formats

### Skills (`skills/<name>/SKILL.md`)

```yaml
---
name: my-skill           # kebab-case, becomes /my-skill; defaults to directory name
description: >           # Used by Claude to decide when to auto-invoke
  What this skill does and when to use it.
argument-hint: "[arg]"   # Shown in autocomplete
user-invocable: true     # false = Claude-only, hidden from / menu
allowed-tools: Read, Grep, Glob
# context: fork          # Uncomment to run in isolated subagent
---

Skill instructions. Use $ARGUMENTS for passed args.
Use ${CLAUDE_SKILL_DIR} for paths to supporting files.
```

### Agents (`agents/<name>.md`)

```markdown
---
name: my-agent
description: When Claude should invoke this agent and what it specialises in.
---

Detailed system prompt for the agent.
```

### Hooks (`hooks/hooks.json`)

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/scripts/my-script.sh" }
        ]
      }
    ]
  }
}
```

Always use `${CLAUDE_PLUGIN_ROOT}` (not relative paths) in hooks and MCP configs — plugins are installed to a cache directory.

### Plugin Manifest (`.claude-plugin/plugin.json`)

Only `name` is required. If omitted entirely, Claude Code auto-discovers components from default locations.

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Short description",
  "skills": "./skills/",
  "agents": "./agents/",
  "hooks": "./hooks/hooks.json"
}
```

## Version Bumping

When modifying any files inside `plugins/<plugin-name>/`, bump the plugin's `version` field in `.claude-plugin/marketplace.json` using semver:

- **Patch** (`1.0.0` → `1.0.1`): fixes, wording tweaks, consistency changes
- **Minor** (`1.0.0` → `1.1.0`): new skills, agents, commands, or hooks added
- **Major** (`1.0.0` → `2.0.0`): breaking changes (renamed/removed skills or commands)

Do this as part of the same commit as the changes. Never commit plugin changes without a version bump.

## Claude Code vs CoWork

Both use the same file format. The marketplace is public GitHub, which Claude Code CLI supports directly. CoWork only supports private GitHub or ZIP upload — keep that in mind if building CoWork-specific plugins.

## Line Endings

All text files use LF (enforced via `.gitattributes`).
