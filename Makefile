.PHONY: all install-tools install-all

PIP := python -m pip
PIP_INSTALL := $(PIP) install --only-binary :all:

all:
	@echo "Please specify either 'make install-tools' or 'make install-all'."

install-tools:
	$(PIP_INSTALL) --upgrade pip
	$(PIP_INSTALL) -r requirements-tools.txt
	pre-commit install

install-all:
	$(PIP_INSTALL) --upgrade pip
	$(PIP_INSTALL) -r requirements-all.txt
	pre-commit install
