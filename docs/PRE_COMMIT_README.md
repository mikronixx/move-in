# Pre-commit hooks

[pre-commit](https://pre-commit.com) runs the checks in `.pre-commit-config.yaml`
on every `git commit`: linting, formatting, secret scanning, type checks, tests.
If a check fails, the commit stops. Fix the issue (or let the hook fix it), `git add`, and commit again.

The same hooks run again in CI, so skipping them locally only delays the failure.

## Install for this repo

From the repo root, in your venv:

```bash
make install-pre-commit   # or install-tools / install-all, which include it

#or if you want to cowboy it...deeply not recommended

pip install pre-commit
pre-commit install

```

This installs pre-commit and runs `pre-commit install`, which adds the hook to `.git/hooks/`.

## Install everywhere

To install the Git hook automatically in every future clone or `git init`, run this once per machine:

```bash
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir ~/.git-template
```

Repos without a `.pre-commit-config.yaml` are unaffected because the hook does nothing.

This doesn't change existing clones. Run `pre-commit install` once in each of those.

## Everyday commands

```bash
pre-commit run                          # staged files only (what a commit does)
make test                               # every hook, every file (same as CI)
pre-commit run <hook-id> --all-files    # one hook, e.g. ruff-check or pip-audit
SKIP=<hook-id> git commit -m "..."      # skip one hook, once
make clean                              # wipe cached hook environments
```

Hooks that fix files (ruff-format, trailing-whitespace, end-of-file-fixer) change them
and fail the commit. That's normal: `git add` the fixes and commit again.

## Updating hooks

Dependabot bumps hook versions weekly. To update by hand:

```bash
pre-commit autoupdate --freeze
```

`--freeze` pins each hook to a commit SHA, with the version in a comment.

## Known issues

- **lychee:** `autoupdate` picks its moving `nightly` tag. After any autoupdate,
  check the lychee line still says `# frozen: lychee-vX.Y.Z`, or update the others
  with `--repo <url>` instead.
- **Hooks run twice:** you have a `[hook "…"]` section in `~/.gitconfig` *and* the
  git template. Use one or the other: `git config --global --remove-section hook.<name>`.
- **Hook can't find Python / `pyenv: pre-commit: command not found`:** the hook in
  `.git/hooks/` (and in `~/.git-template`) records the Python it was installed with.
  If that venv or version is gone, re-run `pre-commit init-templatedir ~/.git-template`
  and `pre-commit install --overwrite` in each repo.
- **pytest and mypy hooks fail with import errors:** they use your active venv, so
  activate it first. They're skipped in CI's pre-commit job and run in the tests workflow instead.
- **First run is slow:** each hook builds its own environment once, then it's cached.
