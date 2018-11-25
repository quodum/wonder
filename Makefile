all: install

install:
	pip install -r requirements.txt

install_dev:
	pip install -r requirements-dev.txt

lint:
	flake8 wonderpy
