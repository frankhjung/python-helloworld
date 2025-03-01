#!/usr/bin/env python
# coding: utf-8
"""
Example Python 3 use of function rather than class.
"""

import logging

logger = logging.getLogger()


def greet(greeting: str = "Hello World") -> str:
    """Provide a static method for a greeting.

    Default greeting is 'Hello World'.
    """

    logger.debug("in greet ...")
    return greeting
