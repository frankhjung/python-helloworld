#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Simple tests for application.
"""

from datetime import date

from helloworld.helloworld import get_periods, greet


def test_empty():
    """Empty greeting - should give "Hello World"."""
    assert greet() == "Hello World"


def test_message():
    """Echo message."""
    assert greet("foo") == "foo"


def test_get_periods():
    """Reporting periods."""
    jan_2019_truth = {
        1: date.fromisoformat("2019-01-01"),
        2: date.fromisoformat("2019-01-08"),
        3: date.fromisoformat("2019-01-15"),
        4: date.fromisoformat("2019-01-22"),
        5: date.fromisoformat("2019-01-29"),
    }
    jan_2019_test = get_periods("2019-01-01", "2019-01-31")
    assert jan_2019_truth == jan_2019_test
