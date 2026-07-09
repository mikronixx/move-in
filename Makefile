.PHONY: all

all:
	@echo "Please specify either 'make install-tools' or 'make install-all'."

install-tools:
	python -m pip cache purge
	python -m pip install --upgrade pip
	pip install -r requirements-tools.txt
	pre-commit install

install-all:
	python -m pip cache purge
	python -m pip install --upgrade pip
	pip install -r requirements-all.txt
	pre-commit install
