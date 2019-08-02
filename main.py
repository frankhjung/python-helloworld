#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Example Python 3 project. """

import argparse
import logging
import os.path
import sys
from helloworld.helloworld import greet, get_periods

#
# MAIN
#
if __name__ == '__main__':

    __version__ = '0.1.0'

    PARSER = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        usage='%(prog)s [options]',
        description='a Python 3 example',
        epilog='© 2019 Frank H Jung mailto:frank.jung@marlo.com.au')
    PARSER.add_argument('-v',
                        '--verbose',
                        help='verbose output',
                        action='count')
    PARSER.add_argument('--version', action='version', version=__version__)

    # process command line arguments
    ARGS = PARSER.parse_args()
    PROG = PARSER.prog
    VERBOSE = ARGS.verbose

    # show command parameters
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    LOGGER = logging.getLogger(__name__)
    if VERBOSE:
        LOGGER.setLevel(logging.DEBUG)

    # show workings
    LOGGER.debug('Program name (PROG): %s', PROG)
    LOGGER.debug('Flag (VERBOSE): %s', VERBOSE)
    LOGGER.debug('Version (version): %s', __version__)

    # run static greeting
    LOGGER.info(greet())

    REPORT_PERIODS = get_periods('2019-01-01', '2019-01-31')
    print("reporting periods")
    for (week, date) in REPORT_PERIODS.items():
        print(week, " : ", date)

    sys.exit(0)
