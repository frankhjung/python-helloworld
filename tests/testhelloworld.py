#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple tests for application.
"""

import unittest
from helloworld.helloworld import greet


class TestHelloWorld(unittest.TestCase):
    """ Unit Tests for Hello World. """

    def test_empty(self):
        """ Empty greeting - should give "Hello World". """
        self.assertEqual(greet(), 'Hello World')

    def test_message(self):
        """ Echo message. """
        self.assertEqual(greet('foo'), 'foo')


if __name__ == '__main__':
    unittest.main()
