# AI Integration (in progress)

AI "for those who already know how to write code."

This doc starts with Claude in what appears to be the most commonly used IDE: VS Code.

## The fine print

- **Chat** (claude.ai in the browser, or the desktop app) has a free plan.
- **Claude Code** (the VS Code extension, terminal, or desktop app) needs a **paid plan**
  (Pro, Max, Ultra, Team, or Enterprise) **or** a Claude Console account (pay per use with API credits).
  The free plan doesn't include it.
- On a paid plan, chat and Claude Code share the same usage limits. No API key needed.

First hit is free. The second one is a subscription. Choose wisely.

## Using Claude with VS Code

### Step 0: Get an account

Sign up at https://claude.ai. For Claude Code, pick a paid plan: https://claude.com/pricing

Desktop apps for macOS, Windows, and Linux (beta): https://claude.com/download.
The desktop app does chat *and* has a Code tab for Claude Code sessions, same account.

### Step 1: Install the extension

Requires VS Code 1.94 or later.

In VS Code: `Cmd+Shift+X` → search "Claude Code" → install it.

### Step 2: Sign in

On first use, the extension opens your browser to sign in. Use your claude.ai account
(paid plan) or your Claude Console account.

---

## What to use Claude Code for

Claude Code can read your whole codebase, so use it for work that needs multi-file context:

- Generating tests for existing code
- Refactoring across files
- Type hints and docstrings at scale

For quick, single-file questions (explain this function, review this snippet), plain chat
in the browser or desktop app is usually enough.

## References

- Use Claude Code in VS Code: https://code.claude.com/docs/en/vs-code
- Claude Code with Pro, Max, or Ultra: https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan
- Install Claude Desktop: https://support.claude.com/en/articles/10065433-install-claude-desktop
