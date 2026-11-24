# move-in

A **Platform/SRE move-in kit**: dotfiles, reusable Python helpers, and a
shift-left CI setup you can lift into other repos.

## Why?

I reuse this stuff constantly. Putting it in one repo saves me time. Maybe it helps someone else too.

It's also deliberately massive overkill, with more to come as needed, so I never have to figure this out again.

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
- **aws**:  helpers for AWS sessions and pagination, with tests (moto) and type hints
- **http_requests**: HTTP helpers with timeouts, tests, and type hints
- **requests_legacy**: old versions kept for reference (excluded from checks)

### CI (`.github/`, `.pre-commit-config.yaml`)
- Same checks locally (pre-commit) and in CI (GitHub Actions); CI is the gate
- Every action pinned to a commit SHA; least-privilege tokens; no persisted credentials
- CI installs from hash-locked requirements; plain pins locally
- Lint, format, type-check, and test per package, in a matrix
- Secret scanning on commit and across full git history; dependency audits; workflow security checks (zizmor)
- Dependabot for pip, Actions, and hooks, with a 7-day cooldown
- SonarQube Cloud quality gate on new code; signed commits enforced on `main`
- Details: [Shift-left security](./docs/SHIFT_LEFT_SECURITY_README.md).

## Docs

In [docs](./docs) you will find the following:

- [Python venv](./docs/PYTHON_VENV_README.md): set up your environment
- [Pre-commit](./docs/PRE_COMMIT_README.md): Basics of pre-commit.
- [Shift-left](./docs/SHIFT_LEFT_SECURITY_README.md): local setup, pre-commits, GitHub Actions for CI, and how the checks fit together
- [Managing Dependencies](./docs/MANAGING_DEPENDENCIES_README.md): pins, hashed locks, and how GitHub Dependabot keeps them current
- [AI IDE integration](./docs/AI_IDE_SETUP_README.md): AI integration with VS Code

## Roadmap
- Bearer token and retry support for the HTTP helpers
- Expand boto3 session/pagination into a reusable module
