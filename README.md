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
[black](https://pypi.org/project/black/) utility:

```bash
black --line-length=79 --quiet helloworld/*.py tests/*.py
```

### Lint Code

[Lint](https://www.pylint.org/) source:

```bash
pylint helloworld/*helloworld*.py tests/*.py
```

Run application with:

```bash
python3 -m helloworld -v
```

### Test application

Testing using PyTest:

```bash
pytest -v tests/*.py
```

Or with a unit test and coverage reports:

```bash
pytest -v --html=cover/unittests.html --cov=helloworld --cov-report=html:cover tests/*.py
```

Where the unit tests are in `cover/unittests.html`, and later moved to
`target/docs/_static/unittests.html`.

The coverage report is in `cover/index.html`, which is later moved to
`target/docs/_static/index.html`.

Both reports are linked from [unittests.rst](./docs/unittests.rst).

#### Example

```text
(venv) $ pytest -v tests/*.py
============================================================================= test session starts =============================================================================
platform linux -- Python 3.11.2, pytest-7.3.1, pluggy-1.0.0 -- /home/frank/dev/python/helloworld/venv/bin/python
cachedir: .pytest_cache
metadata: {'Python': '3.11.2', 'Platform': 'Linux-6.1.0-7-amd64-x86_64-with-glibc2.36', 'Packages': {'pytest': '7.3.1', 'py': '1.11.0', 'pluggy': '1.0.0'}, 'Plugins': {'metadata': '1.11.0', 'html': '3.1.1', 'cov': '4.0.0'}, 'JAVA_HOME': '/usr/lib/jvm/java-17-openjdk-amd64/'}
rootdir: /home/frank/dev/python/helloworld
plugins: metadata-1.11.0, html-3.1.1, cov-4.0.0
collected 6 items

tests/testhelloworld.py::test_empty PASSED                                                                                                                              [ 16%]
tests/testhelloworld.py::test_message PASSED                                                                                                                            [ 33%]
tests/testhelloworld.py::test_get_periods PASSED                                                                                                                        [ 50%]
tests/testhelloworld.py::test_empty PASSED                                                                                                                              [ 50%]
tests/testhelloworld.py::test_message PASSED                                                                                                                            [ 50%]
tests/testhelloworld.py::test_get_periods PASSED                                                                                                                        [ 50%]

============================================================================== 6 passed in 0.02s ==============================================================================
```

## Tools Used

These tools require Python 3.

* [pylint](https://www.pylint.org/) - checks source files
* [pytest](https://docs.pytest.org/) - unit tests
* [venv](https://docs.python.org/library/venv.html) - manage this projects environment
* [flake8](https://pypi.org/project/flake8/) - source code checker
* [black](https://pypi.org/project/black/) - format source files
* [isort](https://pypi.org/project/isort/) - sort imports
* [sort-requirements](https://pypi.org/project/sort-requirements/) - sort requirements.txt

## References

* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
* [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)
* [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
* [PyTest](https://docs.pytest.org/)
* [Sphinx](http://www.sphinx-doc.org/en/master/)

## LICENSE

See [LICENSE](./LICENSE)
