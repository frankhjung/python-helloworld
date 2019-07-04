#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple tests for application.
"""

from helloworld.helloworld import greet


def test_empty():
    """ Empty greeting - should give "Hello World". """
    assert greet() == 'Hello World'


def test_message():
    """ Echo message. """
    assert greet('foo') == 'foo'
