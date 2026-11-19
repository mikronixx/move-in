# Python Virtual Environments for Mac

## Why

It is a very bad idea to use the version of Python installed with macOS. Reasons include:

- Apple ships an older Python version tied to the OS — you do not control it
- System Python is used by macOS internals — installing packages into it can break things
- Package versions installed system-wide conflict across projects
- Upgrades are outside your control and can break your tooling silently

The fix: manage your own Python, isolated per project.

---

## Option 1: venv (simple, no version management)

Works fine if you only need one Python version.

```bash
# Create a virtual environment
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Deactivate when done
deactivate
```

Install dependencies once activated:

```bash
pip install -r requirements.txt
pip install -r requirements-tools.txt
```

---

## Option 2: pyenv + venv (recommended)

Use pyenv when you need multiple Python versions across projects.

### Install pyenv

```bash
brew install pyenv

#or

curl -fsSL https://pyenv.run | bash #recommended by the maintainer

```

Add to your shell (`~/.zshrc`):

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Reload:

```bash
source ~/.zshrc
```

### Install a Python version

```bash
pyenv install 3.13.7
pyenv global 3.13.7
pyenv virtualenv 3.13.7 ineedpython #alternative install , and add the following aliases to your shell rc file

alias ineedpython="pyenv activate ineedpython"
alias idontneedpython="pyenv deactivate ineedpython"
alias pnuke="pyenv virtualenv-delete  ineedpython && pyenv virtualenv 3.13.7 ineedpython"

# Activate,  if you are adverse to aliases
pyenv activate ineedpython

# Or set it locally per project
pyenv local ineedpython
```

### Create a named virtualenv

```bash
python -m venv ~/.venvs/myproject
source ~/.venvs/myproject/bin/activate
```

---

## Workflow (with this repo)

```bash
git clone git@github.com:mikronixx/move-in.git <your_branch_name>
cd <your_branch_name>

# Create and activate venv first
python3 -m venv .venv
source .venv/bin/activate

# Install deps and pre-commit hooks
make install

git checkout -b <your_branch_name>
```

---

## Tips

- Never commit `.venv/` — it is already in `.gitignore`
- Always activate your venv before running `pip install`
- When in doubt: `which python` should show your venv path, not `/usr/bin/python`

## References

https://docs.python.org/3/library/venv.html

https://github.com/pyenv/pyenv

https://cheat.readthedocs.io/en/latest/python/pyenv.html
