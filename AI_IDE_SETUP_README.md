## AI Integration (in progress)

AI "for those who already know how to write code"

This Document will start with using Claude with what appears to be the most commonly used IDE: VS Code

## The Fine Print

 IMPORTANT: claude.ai is free for most tasks. Claude Code in VS Code burns API tokens.

 First hit is free. Choose wisely.

## Using Claude with VS Code

### Step 0 — Get a claude.ai account

Sign up at https://claude.ai. A free account works. A paid subscription gets you more.

A native desktop app is available for macOS and Linux at https://claude.ai/download.
The desktop app is functionally identical to the browser — same account, same subscription.

### Step 1 — Install the Claude Code extension

In VS Code: `Command+Shift+X` → search "Claude Code" → install `anthropic.claude-code`

### Step 2 — Authenticate

On first use, VS Code will open your browser and ask you to authorize the extension against your Anthropic account. Follow the prompts.

To use Claude Code beyond the free tier, you will need to add API credits at https://console.anthropic.com. Minimum is $5.

---

## What to use Claude Code for

Claude Code can read your entire codebase — use it for tasks that require multi-file context:

- Generating tests for existing code
- Refactoring across files
- Type hints and docstrings at scale

For single-file tasks (docstrings, quick questions, code review): use either the desktop application or claude.ai in the browser. It is not going to burn tokens.
