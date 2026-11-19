.PHONY: all install-tools install-all test clean

PIP := python -m pip
PIP_INSTALL := $(PIP) install --only-binary :all:

all:
	@echo "Please specify either 'make install-tools' or 'make install-all'."

install-tools:
	$(PIP_INSTALL) --upgrade pip
	$(PIP_INSTALL) -r requirements-tools.txt
	pre-commit install

install-all: install-tools
	$(PIP_INSTALL) -r requirements-all.txt

test:
	pre-commit run --all-files --show-diff-on-failure

clean:
	pre-commit clean
	find . -type d \( -name __pycache__ -o -name .ruff_cache -o -name .pytest_cache \) -prune -exec rm -rf {} +
