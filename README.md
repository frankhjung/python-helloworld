# python-helloworld

Example Python 3 project demonstrating:

1. code formatting
1. code linting
1. command line parser
1. functions vs classes
1. logging
1. unit tests
1. virtual environments

## Documentation

Module documentation is available online on:

* [GitLab Pages > python-helloworld](https://themarlogroup.gitlab.io/training/students/fjung/python-helloworld)

You can also download from GitHub at:

* [Pipeline Builds > frankhjung.python-helloworld](https://dev.azure.com/frankhjung/python/_build?definitionId=9)

## Pipelines

* Azure/GitHub [![Build Status](https://dev.azure.com/frankhjung/python/_apis/build/status/frankhjung.python-helloworld?branchName=master)](https://dev.azure.com/frankhjung/python/_build/latest?definitionId=9&branchName=master)

* [GitLab Pipelines](https://gitlab.com/theMarloGroup/training/students/fjung/python-helloworld/pipelines)

## Quick Start

The following applies to Linux where the base installation contains both Python 2 & 3.

### Virtual Environment

To initialise the virtual environment, `venv`:

```bash
pip3 install virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip3 install -Ur requirements.txt
```

To start the virtual environment:

```bash
source venv/bin/activate
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
pip3 freeze
```

### Format Code

To format code to the [Google Python Code
Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) run
[ruff](https://docs.astral.sh/ruff/) utility:

```bash
ruff format
```

### Lint Code

Lint source using [ruff](https://docs.astral.sh/ruff/):

```bash
ruff check --output-format grouped --fix
```

Run application with:

```bash
python3 -m helloworld -h
```

### Test application

Testing using PyTest:

```bash
pytest -v tests/*.py
```

Or with a unit test and coverage reports:

```bash
# coverage
pytest --verbose --cov --cov-config=.coveragerc --cov-report=html
# test report
pytest --html=public/reports/pytest_report.html --self-contained-html
```

Where the unit tests are in `cover/pytest_report.html`, and later moved to
`target/docs/_static/pytest_report.html`.

The coverage report is in `cover/index.html`, which is later moved to
`target/docs/_static/index.html`.

Both reports are linked from [unittests.rst](./docs/unittests.rst).

#### Example

```text
$ pytest -v
============================================================================= test session starts =============================================================================
platform linux -- Python 3.13.1, pytest-7.4.4, pluggy-1.5.0 -- /home/frank/dev/python/helloworld/.venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.13.1', 'Platform': 'Linux-6.12.11-amd64-x86_64-with-glibc2.40', 'Packages': {'pytest': '7.4.4', 'pluggy': '1.5.0'}, 'Plugins': {'mock': '3.14.0', 'metadata': '3.1.1', 'html': '3.2.0', 'cov': '4.1.0'}, 'JAVA_HOME': '/usr/lib/jvm/java-21-openjdk-amd64'}
rootdir: /home/frank/dev/python/helloworld
plugins: mock-3.14.0, metadata-3.1.1, html-3.2.0, cov-4.1.0
collected 12 items

helloworld/tests/test_helloworld.py::test_empty PASSED                                                                                                                  [  8%]
helloworld/tests/test_helloworld.py::test_message PASSED                                                                                                                [ 16%]
helloworld/tests/test_helloworld.py::test_get_periods PASSED                                                                                                            [ 25%]
helloworld/tests/test_helloworld.py::test_logging PASSED                                                                                                                [ 33%]
public/docs/_downloads/76e658de181154512846773edbd78801/test_helloworld.py::test_empty PASSED                                                                           [ 41%]
public/docs/_downloads/76e658de181154512846773edbd78801/test_helloworld.py::test_message PASSED                                                                         [ 50%]
public/docs/_downloads/76e658de181154512846773edbd78801/test_helloworld.py::test_get_periods PASSED                                                                     [ 58%]
public/docs/_downloads/76e658de181154512846773edbd78801/test_helloworld.py::test_logging PASSED                                                                         [ 66%]
public/docs/_static/test_helloworld.py::test_empty PASSED                                                                                                               [ 75%]
public/docs/_static/test_helloworld.py::test_message PASSED                                                                                                             [ 83%]
public/docs/_static/test_helloworld.py::test_get_periods PASSED                                                                                                         [ 91%]
public/docs/_static/test_helloworld.py::test_logging PASSED                                                                                                             [100%]

============================================================================= 12 passed in 0.07s ==============================================================================
```

## Update Packages

Use `pip list --outdated` to show updates to packages.

To update outdated packages, use:

```bash
pip3 list -o | cut -f1 -d' ' | tr " " "\n" | awk '{if(NR>=3)print}' | cut -d' ' -f1 | xargs -n1 pip3 install -U
```

## Tools Used

These tools require Python 3.

* [GNU Make](https://www.gnu.org/software/make/) - build automation
* [pytest](https://docs.pytest.org/) - unit tests
* [ruff](https://docs.astral.sh/ruff/) - Python tooling
* [sort-requirements](https://pypi.org/project/sort-requirements/) - sort requirements.txt
* [venv](https://docs.python.org/library/venv.html) - manage this projects environment

## References

* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
* [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)
* [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
* [PyTest](https://docs.pytest.org/)
* [Sphinx](http://www.sphinx-doc.org/en/master/)

## LICENSE

See [LICENSE](./LICENSE)
