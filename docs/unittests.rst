.. _unittests:

Unit Tests
==========

Unit Test Results
-----------------

To run the unit tests using :download:`testhelloworld <../tests/testhelloworld.py>`::

   >>> pytest -v tests/test*.py

To generate a HTML report use::

   >>> pytest -v tests/test*.py --html=target/report.html

See `Unit Tests <_static/report.html>`_ report.

Unit Test Coverage
------------------

To generate a report on test coverage::

   >>> pytest -v --cov=helloworld tests/test*.py
   >>> coverage html -d cover helloworld/helloworld.py

See `Test Coverage <_static/index.html>`_ report.

.. EOF
