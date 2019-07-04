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
pip3 install -r requirements.txt
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

Testing using PyTest:

```bash
pytest -v tests/test*.py
```

**Example**

```text
(venv) $ pytest -v tests/test*.py
============================================================================= test session starts ==============================================================================
platform linux -- Python 3.7.3, pytest-5.0.0, py-1.8.0, pluggy-0.12.0 -- /usr/bin/python3
cachedir: .pytest_cache
metadata: {'Python': '3.7.3', 'Platform': 'Linux-4.19.0-5-amd64-x86_64-with-debian-10.0', 'Packages': {'pytest': '5.0.0', 'py': '1.8.0', 'pluggy': '0.12.0'}, 'Plugins': {'metadata': '1.8.0', 'cov': '2.7.1', 'html': '1.21.1'}, 'JAVA_HOME': '/usr/lib/jvm/default-java'}
rootdir: /home/frank/dev/python/helloworld
plugins: metadata-1.8.0, cov-2.7.1, html-1.21.1
collected 2 items                                                                                                                                                              

tests/testhelloworld.py::test_empty PASSED                                                                                                                               [ 50%]
tests/testhelloworld.py::test_message PASSED                                                                                                                             [100%]

=========================================================================== 2 passed in 0.02 seconds ===========================================================================
(venv)
```

## Tools Used

These tools require Python 3.

* [pylint](https://www.pylint.org/) - checks source files
* [pytest](https://docs.pytest.org/) - unit tests
* [venv](https://docs.python.org/library/venv.html) - manage this projects environment
* [yapf](https://github.com/google/yapf) - format source files

## References

* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
* [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)
* [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
* [PyTest](https://docs.pytest.org/)

## LICENSE

See [LICENSE](./LICENSE)
