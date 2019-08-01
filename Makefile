#!/usr/bin/env make

.DEFAULT_GOAL := help

.PHONY: check clean dist doc help run test version

SHELL	:= /bin/sh
COMMA	:= ,
EMPTY	:=
SPACE	:= $(EMPTY) $(EMPTY)
PYTHON	:= ./venv/bin/python

SRCS	:= main.py helloworld/helloworld.py tests/testhelloworld.py

all:	check test run doc dist

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:   check cover run test doc dist"
	@echo "  check: check style and lint code"
	@echo "  run:   run against test data"
	@echo "  test:  run unit tests"
	@echo "  dist:  create a distrbution archive"
	@echo "  doc:   create documentation including test converage and results"
	@echo "  clean: delete all generated files"
	@echo
	@echo "This is a Python 3 project."
	@echo
	@echo "Initialise virtual environment (venv) with:"
	@echo
	@echo "pip3 install virtualenv; python3 -m virtualenv venv; source venv/bin/activate; pip3 install -r requirements.txt"
	@echo
	@echo "Start virtual environment (venv) with:"
	@echo
	@echo "source venv/bin/activate"
	@echo
	@echo "Deactivate with:"
	@echo
	@echo "deactivate"
	@echo

check:
	# format code to googles style
	yapf --style google --parallel -i $(SRCS) setup.py
	# check with pylint
	pylint $(SRCS)
	# check distutils
	$(PYTHON) setup.py check

test:
	pytest -v --html=cover/report.html --cov=helloworld --cov-report=html:cover tests/test*.py

doc:	test
	# create sphinx documentation
	(cd $(PWD)/docs; make html)

dist:
	# create source package and build distribution
	$(PYTHON) setup.py clean
	$(PYTHON) setup.py sdist --dist-dir=target/dist
	$(PYTHON) setup.py build --build-base=target/build
	cp -pr target/docs/html public
	cp -p target/dist/*.tar.gz public

run:
	$(PYTHON) -m main -v
	$(PYTHON) -m main -h
	$(PYTHON) -m main --version

version:
	$(PYTHON) -m main --version

clean:
	# clean build distribution
	$(PYTHON) setup.py clean
	# clean generated documents
	(cd docs; make clean)
	$(RM) -rf cover
	$(RM) -rf .coverage
	$(RM) -rf __pycache__ helloworld/__pycache__ tests/__pycache__
	$(RM) -rf public
	$(RM) -rf python_*.egg-info/
	$(RM) -rf target
	$(RM) -v MANIFEST
	$(RM) -v *.pyc *.pyo *.py,cover
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover

