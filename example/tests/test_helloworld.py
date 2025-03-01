#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple tests for application.
"""

import logging

from example.helloworld import greet


def test_empty():
    """Empty greeting - should give "Hello World"."""
    assert greet() == "Hello World"


def test_message():
    """Echo message."""
    assert greet("foo") == "foo"


def test_logging():
    """Check root logger."""
    logger = logging.getLogger()  # use root logger
    assert logger.level == logging.WARNING
