## Pre-commit hooks

To install the Git hook automatically in every future clone or `git init`, run this once per machine:

```bash
git config --global init.templateDir ~/.git-template
pre-commit init-templatedir ~/.git-template
```

Repos without a `.pre-commit-config.yaml` are unaffected because the hook does nothing.

This doesn't change existing clones. Run `pre-commit install` once in each of those.
