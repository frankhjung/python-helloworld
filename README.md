# python-example

Example Python 3 project demonstrating:

1. code formatting
1. code linting
1. command line parser
1. functions vs classes
1. unit tests
1. virtual environments

## Documentation

Module documentation is available online on:

* [GitLab Pages > python-example](https://themarlogroup.gitlab.io/training/students/fjung/python-example)

You can also download from GitHub at:

* [Pipeline Builds > frankhjung.python-example](https://dev.azure.com/frankhjung/python/_build?definitionId=9)

## Pipelines

* Azure/GitHub [![Build Status](https://dev.azure.com/frankhjung/python/_apis/build/status/frankhjung.python-example?branchName=master)](https://dev.azure.com/frankhjung/python/_build/latest?definitionId=9&branchName=master)

* [GitLab Pipelines](https://gitlab.com/theMarloGroup/training/students/fjung/python-example/pipelines)

## Quick Start

The following applies to Linux where the base installation contains both Python
2 and 3.

### Virtual Environment

Start the virtual environment, `venv` with:

```bash
pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

To end virtual environment session:

```bash
deactivate
```

### Dependent Packages

Install and list packages:

```bash
pip3 install -r requirements.txt
pip3 list
```

### Format Code

To format code to the [Google Python Code
Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) run the
[YAPF](https://github.com/google/yapf) utility:

```bash
yapf --style google -i main.py helloworld/helloworld.py
```

Where:

  - using Google style 
  - in place changes

### Lint Code

[Lint](https://www.pylint.org/) source:

```bash
pylint3 main.py helloworld/helloworld.py
```

Run application with:

```bash
python3 -m main -v
```

### Test application.

Using standard Python [unit tests]():

```bash
python3 -m unittest discover -s tests
python3 -m unittest tests/helloworld_tests.py
python3 -m unittest -h
```

**Example**

```text
$ python3 -m unittest tests/helloworld_tests.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Tools Used

These tools require Python 3.

* [pylint](https://www.pylint.org/) - checks source files
* [venv](https://docs.python.org/library/venv.html) - manage this projects environment
* [yapf](https://github.com/google/yapf) - format source files

**TODO**

* add virtualenv `activate` & `deactivate` to [Makefile](./Makefile)
* [pyflakes](https://pypi.org/project/pyflakes/) - checks source files for errors

## Future Work

* Package project using [Python Wheels](https://pythonwheels.com/)

## References

* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
* [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)
* [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
* [Unit Testing](https://docs.python.org/library/unittest.html), see also [pytest](https://docs.pytest.org/)

## LICENSE

See [LICENSE](./LICENSE)
