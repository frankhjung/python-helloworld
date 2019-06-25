#!/usr/bin/env python
# coding: utf-8

"""
Provide a greeting.
"""


class HelloWorld():

    """ Provide the universal greeting. """

    __version__ = '0.1.0'

    @staticmethod
    def greet(greeting="Hello World"):
        """ Provide a greeting
        Default greeting is 'Hello World'.
        """
        return greeting
