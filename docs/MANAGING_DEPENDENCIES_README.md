# Managing Dependencies

How module versions are pinned: some with plain `==` pins, some hash-locked.
Why the difference, and how Dependabot keeps them current.

## Prerequisite reading

- [Shift-left security](./SHIFT_LEFT_SECURITY_README.md): the big picture; dependency management is one piece of it
- [Python venv](./PYTHON_VENV_README.md): every install below assumes an active venv
- [Pre-commit](./PRE_COMMIT_README.md): pip-audit runs as a pre-commit hook; run it by hand with `pre-commit run pip-audit --all-files`

## Basic Guidance

**Hash what GitHub Action(CI) installs. Plain pins for local tooling.**

CI runs unattended on a fresh machine for every PR, so every package it installs
(including dependencies of dependencies) is locked to an exact version and sha256 hash.
Local installs on your own machine use plain `==` pins: less ceremony, lower risk.

## Files where versions are managed

| Input (you edit) | Lock (generated) | Installed by |
|---|---|---|
| `requirements-pre-commit.in` | `requirements-pre-commit.txt` | CI: `pre-commit.yaml`, `links.yaml` |
| `useful_python/http_requests/requirements.in` | `useful_python/http_requests/requirements.txt` | CI: `python-tests.yaml` |
| `requirements-tools.txt` | (plain pins) | `make install-tools` |
| `requirements-all.txt` | (plain pins) | `make install-all` |
| `useful_python/aws/requirements.txt` | (plain pins) | nothing yet; gets a lock when `aws` joins CI |

Locally, `make install-pre-commit` installs from the `.in`, not the lock.

## Known Issues

If any file in a single `pip install` has hashes, pip requires hashes for **every**
package in that install. Mixing a lock with a plain file fails.

So: never `-r` a lock file from a plain one, and never pass both to one `pip install`.
pip-audit has the same limit, which is why it runs as three separate hooks
(plain files, `http_requests` lock, pre-commit lock).

## Changing a version

For a locked pair: edit the `.in`, then recompile under Python 3.13:

```bash
pip-compile --generate-hashes --strip-extras \
  --output-file=requirements-pre-commit.txt requirements-pre-commit.in

# for http_requests:
cd useful_python/http_requests
pip-compile --generate-hashes --strip-extras \
  --output-file=requirements.txt requirements.in

```

Never edit a lock by hand. For plain files, just edit the pin.

## Pinning versions twice on purpose

Some packages appear in more than one file:

- `pytest`, `requests_mock`, `mypy`: in `requirements-tools.txt` and `http_requests/requirements.in`
- `boto3`: in `requirements-all.txt` and `aws/requirements.txt`

Each folder in `useful_python/` carries its own requirements so it can be copied and
used on its own. Dependabot groups pip bumps across directories, so the copies
normally move together. If they drift, match them.

## Dependabot

`.github/dependabot.yml`, weekly, with a **7-day cooldown**: no PR until a release is
a week old, so a bad release that gets pulled never reaches us.

| Ecosystem | Watches |
|---|---|
| `pip` | `/`, `/useful_python/http_requests`, `/useful_python/aws` |
| `github-actions` | action SHAs in `.github/workflows/`, with their `# vX.Y.Z` comments |
| `pre-commit` | hook `rev`s in `.pre-commit-config.yaml` |

For a locked pair, Dependabot bumps the `.in` and regenerates the `.txt`, hashes
included, in one PR. Check the first one it opens to confirm both files changed.

## Looking ahead (before the cooldown)

Look early, install late. None of these change anything:

```bash
pip list --outdated                            # what's behind in your venv
pip-compile --upgrade --dry-run --generate-hashes --strip-extras \
  --output-file=requirements-pre-commit.txt requirements-pre-commit.in
```

For tools you care about, use **Watch → Custom → Releases** on their GitHub page.
