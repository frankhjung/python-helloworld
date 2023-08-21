#!/usr/bin/env make

.PHONY: all check clean doc dist help run tags test version

.DEFAULT_GOAL := default

CTAGS	:= $(shell which ctags)
PIP	:= $(shell which pip3)
PYTHON	:= $(shell which python3)
SRCS	:= $(filter-out docs/conf.py setup.py, $(wildcard *.py **/*.py))

default: check test

all:	check test run doc dist

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:   check cover run test doc dist"
	@echo "  check: check style and lint code"
	@echo "  run:   run against test data"
	@echo "  test:  run unit tests"
	@echo "  doc:   create documentation including test coverage and results"
	@echo "  clean: delete all generated files"
	@echo
	@echo "Activate virtual environment (.venv) with:"
	@echo
	@echo "pip3 install virtualenv; python3 -m virtualenv .venv; source .venv/bin/activate; pip3 install -Ur requirements.txt"
	@echo
	@echo "Start virtual environment (.venv) with:"
	@echo
	@echo "source .venv/bin/activate"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "deactivate"
	@echo

check:
ifdef CTAGS
	# ctags for vim
	ctags --recurse -o tags $(SRCS)
endif
	# sort imports
	isort $(SRCS)
	# format code to googles style
	black --quiet $(SRCS)
	# sort requirements
	sort-requirements requirements.txt
	# check with flake8
	flake8 $(SRCS)
	# check with pylint
	pylint $(SRCS)

test:
	pytest -v --html=cover/unittests.html --cov=helloworld --cov-report=html:cover tests/*.py

doc:	test
	# create sphinx documentation
	(cd $(PWD)/docs; make html)

dist:
	# create source package and build distribution
	$(PYTHON) setup.py clean
	$(PYTHON) setup.py sdist --dist-dir=target/dist
	$(PYTHON) setup.py build --build-base=target/build
	cp -pr target/docs public
	cp -p target/dist/*.tar.gz public

run: version
	$(PYTHON) -m helloworld -h
	$(PYTHON) -m helloworld -l INFO

version:
	$(PYTHON) -m helloworld --version

clean:
	# clean build distribution
	$(PYTHON) setup.py clean
	# clean generated documents
	(cd docs; make clean)
	# clean generated artefacts
	-$(RM) -rf __pycache__ **/__pycache__
	-$(RM) -rf .coverage
	-$(RM) -rf .pytest_cache
	-$(RM) -rf cover
	-$(RM) -rf public
	-$(RM) -rf target
	-$(RM) -v *.pyc *.pyo *.py,cover
	-$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
