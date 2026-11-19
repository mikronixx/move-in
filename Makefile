.PHONY: all install-pre-commit install-tools install-all test clean

PIP := python -m pip
PIP_INSTALL := $(PIP) install --only-binary :all:

all:
	@echo "Please specify either 'make test, make clean, make install-pre-commit, make install-tools' or 'make install-all'."

install-pre-commit:
	$(PIP_INSTALL) --upgrade pip
	$(PIP_INSTALL) -r requirements-pre-commit.in
	pre-commit install

install-tools: install-pre-commit
	$(PIP_INSTALL) -r requirements-tools.txt


install-all: install-tools
	$(PIP_INSTALL) -r requirements-all.txt

test:
	pre-commit run --all-files --show-diff-on-failure

clean: install-pre-commit
	pre-commit clean
	find . -type d \( -name __pycache__ -o -name .ruff_cache -o -name .pytest_cache \) -prune -exec rm -rf {} +
