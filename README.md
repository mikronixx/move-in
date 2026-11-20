# move-in

A **Platform/SRE move-in kit**: dotfiles, reusable Python helpers, and a
shift-left CI setup you can lift into other repos.

## Why?

I reuse this stuff constantly. Putting it in one repo saves me time. Maybe it helps someone else too.

## Quick start

Create and activate a virtual environment first (see [Python venv](./docs/PYTHON_VENV_README.md)).

Clone into a directory named after your intended branch. This keeps your working tree and branch name in sync.

```bash
git clone git@github.com:mikronixx/move-in.git <branch-name>
cd <branch-name>
git checkout -b <branch-name>

make install-tools   # pre-commit + linters/scanners, installs the git hook
# or
make install-all     # tools + AWS/Ansible extras

make test            # run every check against the whole repo
```

Other targets: `make install-pre-commit` (just the hook), `make clean`.

## What's inside

### [`dotfiles`](./dotfiles)
- zsh config with sample aliases and pyenv setup you can toggle on/off
- sample git, vim, and bash profiles
- **Note:** nothing is installed automatically. Shells are personal, so use what fits.

### [`useful_python`](./useful_python)
- **aws**: helpers for AWS sessions and pagination
- **http_requests**: HTTP helpers with timeouts, tests, and type hints
- **requests_legacy**: old versions kept for reference (excluded from checks)

### CI (`.github/`, `.pre-commit-config.yaml`)
Every commit and PR runs linting, type checks, tests, secret scanning,
dependency audits, and workflow security checks. Locally via pre-commit,
and again in GitHub Actions. Dependabot keeps everything current, and
SonarQube Cloud adds a quality gate on new code.
Details: [Shift-left security](./docs/SHIFT_LEFT_SECURITY_README.md).

## Docs
- [Shift-left security](./docs/SHIFT_LEFT_SECURITY_README.md): how the checks fit together
- [Pre-commit](./docs/PRE_COMMIT_README.md): installing the git hook everywhere
- [Python venv](./docs/PYTHON_VENV_README.md): venv and pyenv setup on a Mac
- [AI IDE setup](./docs/AI_IDE_SETUP_README.md): Claude Code in VS Code

## Roadmap
- Tests for `aws` (with moto), then add it to CI
- Bearer token and retry support for the HTTP helpers
- Expand boto3 session/pagination into a reusable module
