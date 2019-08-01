#!/usr/bin/env python
# coding: utf-8
"""
Example Python 3 use of function rather than class.
"""

from datetime import date, timedelta


def greet(greeting="Hello World"):
    """ Provide a static method for a greeting.

    Default greeting is 'Hello World'.
    """
    return greeting


def get_periods(from_date, to_date):
    """
    Get reporting week periods between dates.

    Returns dictionary of week and week start date.
    """

    start = date.fromisoformat(from_date)
    end = date.fromisoformat(to_date)

    # need to find Monday of the first week
    weeks = {}
    one_week = timedelta(days=7)
    while start < end:
        week = start.isocalendar()[1]
        weeks.update({week: start})
        start += one_week

    return weeks
