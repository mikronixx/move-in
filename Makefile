install:
	python -m pip install --upgrade pip
	pip install -r requirements-tools.txt
	pre-commit install
