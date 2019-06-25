# python-example

Example Python 3 project.

## Quick Start

The following applies to Linux where the base installation contains both Python
2 and 3.

Start the virtual environment, `venv` with:

```bash
python3 -m virtualenv venv
source venv/bin/activate
```

List installed packages:

```bash
pip list
```

[Lint](https://www.pylint.org/) source:

``bash
pylint3 main.py **/*.py
```


Run application with

```bash
python3 main.py
```


## Tools Used

These tools require Python 3.

* [tox](https://tox.readthedocs.io/en/latest/) - testing framework
* [venv](https://docs.python.org/3/library/venv.html) - manage this projects environment
* [pylint](https://www.pylint.org/) - checks source files
* [pyflakes](https://pypi.org/project/pyflakes/) - checks source files for errors

## References

* [Python 3 Tutorial](https://docs.python.org/3/tutorial/)
* [Virtual Environment Tutorial](https://realpython.com/python-virtual-environments-a-primer/)
* [Python Code Style](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

## LICENSE

See [LICENSE](./LICENSE)
