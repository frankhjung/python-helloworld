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


def get_date(from_date, to_date):
    """
    Get reporting periods between dates.
    """

    start = date.fromisoformat(from_date)
    end = date.fromisoformat(to_date)
    one_week = timedelta(days=7)

    # need to find Monday of the first week
    report_periods = []
    while start < end:
        print("period starting:", start)
        week = start.isocalendar()[1]
        report_periods.append(week)
        start += one_week

    return report_periods
