#!/usr/bin/env python
# coding: utf-8
"""
Example Python 3 use of function rather than class.
"""

import logging
from datetime import date, timedelta

logger = logging.getLogger()


def greet(greeting: str = "Hello World") -> str:
    """Provide a static method for a greeting.

    Default greeting is 'Hello World'.
    """

    logger.debug("in greet ...")
    return greeting


def get_periods(from_date: str, to_date: str) -> dict[int, date]:
    """
    Get reporting week periods between dates.

    Returns dictionary of week and week start date.
    """

    logger.debug("in get_periods ...")
    start = date.fromisoformat(from_date)
    end = date.fromisoformat(to_date)

    # build list by weekly increments from start date until end date
    weeks: dict[int, date] = {}
    one_week = timedelta(days=7)
    while start < end:
        week = start.isocalendar()[1]
        weeks.update({week: start})
        start += one_week

    return weeks
