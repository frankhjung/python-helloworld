#!/usr/bin/env python
# coding: utf-8
"""
Example Python 3 use of function rather than class.
"""

from datetime import date, timedelta
from typing import Dict


def greet(greeting: str = "Hello World") -> str:
    """Provide a static method for a greeting.

    Default greeting is 'Hello World'.
    """
    return greeting


def get_periods(from_date: str, to_date: str) -> Dict[int, date]:
    """
    Get reporting week periods between dates.

    Returns dictionary of week and week start date.
    """

    start = date.fromisoformat(from_date)
    end = date.fromisoformat(to_date)

    # build list by weekly increments from start date until end date
    weeks: Dict[int, date] = {}
    one_week = timedelta(days=7)
    while start < end:
        week = start.isocalendar()[1]
        weeks.update({week: start})
        start += one_week

    return weeks
