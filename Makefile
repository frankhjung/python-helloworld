# Manage project
#
# You can run unittests using ...
# - python -m test.testemployees -v
# - python -m unittest discover -v

.DEFAULT_GOAL := help

.PHONY: check clean help run test

COMMA	:= ,
EMPTY	:=
SPACE	:= $(EMPTY) $(EMPTY)

SRCS	:= main.py helloworld/helloworld.py tests/testhelloworld.py

all: 	check run test version

help:
	@echo
	@echo "Default goal: ${.DEFAULT_GOAL}"
	@echo "  all:  	     check run test version"
	@echo "  check:      validate code and distribution config"
	@echo "  run:        run against test data"
	@echo "  test:       run unit test"
	@echo "  clean:      delete all generated files"
	@echo
	@echo "Virtual Environment"
	@echo
	@echo "activate with:"
	@echo
	@echo "  pip3 install virtualenv"
	@echo "  python -m virtualenv venv"
	@echo "  source venv/bin/activate"
	@echo
	@echo "deactivate with:"
	@echo
	@echo "  deactivate"
	@echo

check:
	# format code
	yapf --style google -i $(SRCS)
	# check with pylint
	pylint3 $(SRCS)

run:
	python3 -m main -v

test:
	python3 -m unittest discover -s tests

clean:
	# clean build distribution
	$(RM) -rf helloworld/__pycache__
	$(RM) -rf tests/__pycache__
	$(RM) -rf __pycache__
	$(RM) -v **/*.pyc **/*.pyo **/*.py,cover
	$(RM) -v *.pyc *.pyo *.py,cover

version:
	python3 -m main --version

