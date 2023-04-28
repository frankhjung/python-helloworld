.. _unittests:

Unit Tests
==========

Unit tests are performed using `PyTest <references.html>`_.

Code coverage is reported by `Coverage <https://coverage.readthedocs.io/>`_.

Both reports are collated during when Sphinx documentation is built.

Unit Test Results
-----------------

To run the unit tests::

   pytest -v tests/test*.py

To generate a HTML report with coverage run::

   pytest -v --html=cover/unittests.html tests/*.py

**Report** `Unit Tests <_static/unittests.html>`_

Unit Test Coverage
------------------

To generate a report on test coverage::

   pytest -v --cov=helloworld --cov-report=html:cover tests/*.py

**Report** `Test Coverage <_static/index.html>`_

.. EOF
