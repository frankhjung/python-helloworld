.. _references:

References
==========

Here are links to the tools and articles I read to prepare this project:

* `Black code formatter using Google style <https://pypi.org/project/black/>`_
* `Code linter <https://www.pylint.org/>`_
* `Code test coverage measurement <https://coverage.readthedocs.io/>`_
* `Distutils <https://docs.python.org/distutils/introduction.html>`_
* `Flake8 code linter <https://pypi.org/project/flake8/>`_
* `GNU Make <https://www.gnu.org/software/make/>`_
* `PyDoc <https://docs.python.org/library/pydoc.html>`_
* `pylint code linter <https://pypi.org/project/pylint/>`_
* `PyTest <https://docs.pytest.org>`_
* `Python documentation <https://docs.python.org/>`_
* `Sphinx <https://www.sphinx-doc.org/en/master/>`_

PyDoc
-----

PyDoc can be generated for each module using::

   pydoc [module]

For example::

   pydoc example.__main__

I've included the PyDoc output for all :ref:`classes` and the
:ref:`example_main` module. You can generate HTML output using PyDoc. To
run the web interface call::

   pydoc -p 8888

.. EOF
