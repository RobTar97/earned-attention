# Installation

## Requirements

Use Node.js and npm plus Git to install from GitHub. This guide was verified with `skills` **1.7.2** on **2026-10-13**; that npm release declares Node.js **22.20.0 or newer**. Check the [npm package metadata](https://www.npmjs.com/package/skills) for the requirements of a newer release.

The installed skill itself is a set of instructions and references. It does not require Node.js, Python, API keys, or a server to perform its writing workflow. The CLI uses Node.js for installation; maintainers use Python for repository validation.

## Inspect before installing

```bash
npx skills add RobTar97/earned-attention --list
```

This lists the discovered skill without installing it. You can also read [SKILL.md](../skills/psychological-content-strategy/SKILL.md) and its references directly.

## Project installation

Run this inside the project where you want to use the skill:

```bash
npx skills add RobTar97/earned-attention --skill psychological-content-strategy
```

The installer prompts for an agent. To select one directly:

```bash
# Codex
npx skills add RobTar97/earned-attention --skill psychological-content-strategy --agent codex

# Claude Code
npx skills add RobTar97/earned-attention --skill psychological-content-strategy --agent claude-code

# Cursor
npx skills add RobTar97/earned-attention --skill psychological-content-strategy --agent cursor
```

The CLI chooses the agent's supported skill directory. See the current [supported agents table](https://github.com/vercel-labs/skills#supported-agents) for paths and agent-specific limitations.

## Global installation

Add `--global` to make it available across projects:

```bash
npx skills add RobTar97/earned-attention --skill psychological-content-strategy --agent codex --global
```

Global installation may update an existing skill with this identifier. If you have customized a local copy, preserve your changes before installing over it.

## Windows and copy mode

The CLI normally links agent locations to a canonical skill copy. If your filesystem or workflow requires regular directories, use its copy mode:

```bash
npx skills add RobTar97/earned-attention --skill psychological-content-strategy --agent codex --copy
```

In PowerShell environments that block npm's `.ps1` wrapper, run the equivalent command with `npx.cmd`:

```powershell
npx.cmd skills add RobTar97/earned-attention --skill psychological-content-strategy --agent codex --copy
```

## Confirm, update, and remove

```bash
# Project installation
npx skills list --agent codex
npx skills update psychological-content-strategy --project
npx skills remove psychological-content-strategy --agent codex

# Global installation
npx skills list --agent codex --global
npx skills update psychological-content-strategy --global
npx skills remove psychological-content-strategy --agent codex --global
```

For unattended installation, add `--yes`. Select the intended agent and scope explicitly rather than installing to every agent.

## Reproducing the verified installer

```bash
npx skills@1.7.2 add RobTar97/earned-attention --skill psychological-content-strategy --agent codex --copy
```

This fixes the **installer** version. It still downloads the repository's current default-branch content. A [GitHub release](https://github.com/RobTar97/earned-attention/releases) records a versioned snapshot of the skill and documentation.

## Using the skill

In Codex, type a prompt such as:

```text
Use $psychological-content-strategy to audit the script below and
give a complete rewrite plus one focused experiment.
```

Other agents may accept natural-language selection or their own invocation syntax. Start a new session or refresh skill discovery if your host does not immediately expose the newly installed skill.

## Troubleshooting

| Symptom | Action |
|---|---|
| `npx` is missing | Install a supported Node.js distribution with npm; reopen the terminal |
| Unsupported Node.js version | Check `node --version` against the chosen CLI release's requirements |
| GitHub clone fails | Check Git/network access and try the full repository URL |
| No skill discovered | Run `--list`; confirm you used this repository and the exact skill identifier |
| Link creation fails | Repeat the installation with `--copy` |
| Agent cannot see the skill | Check agent and scope with `skills list`; refresh the agent's skill discovery |
| Wrong installation updated | Specify `--project` or `--global` and the exact skill identifier |

## skills.sh discovery

The [official FAQ](https://skills.sh/docs/faq) describes listing through real CLI installations with telemetry enabled. Repository publication makes the GitHub source installable; skills.sh indexing and cached page updates are handled by that service and can take time. A listed page is not an endorsement or a guarantee of results.

This repository includes [`skills.sh.json`](../skills.sh.json) to group the skill under “Content & Marketing,” following the [catalog customization documentation](https://skills.sh/docs/customize).

The CLI supports opting out through `DISABLE_TELEMETRY=1`; see [official CLI telemetry documentation](https://skills.sh/docs/cli). Opting out affects installation telemetry used for discovery, not the skill's writing workflow.
