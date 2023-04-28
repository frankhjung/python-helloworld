#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" A simple Python example project. """

import argparse
import logging
import os.path
import sys

from helloworld.helloworld import get_periods, greet

#
# MAIN
#
__version__ = "2023.04.28"

parser = argparse.ArgumentParser(
    prog=os.path.basename(sys.argv[0]),
    usage="%(prog)s [options]",
    description="a Python 3 example",
    epilog="© 2019,2021 Frank H Jung mailto:frank.jung@marlo.com.au",
)
parser.add_argument("-v", "--verbose", help="verbose output", action="count")
parser.add_argument("--version", action="version", version=__version__)

# process command line arguments
args = parser.parse_args()
prog = parser.prog
verbose = args.verbose

# show command parameters
logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
logger = logging.getLogger()  # use root logger
if verbose:
    logger.setLevel(logging.DEBUG)

# show workings
logger.debug("Program name (PROG): %s", prog)
logger.debug("Flag (VERBOSE): %s", verbose)
logger.debug("Version (version): %s", __version__)

# run static greeting
logger.info(greet())
logger.info(get_periods("2019-01-01", "2019-01-31"))
