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
__version__ = "2023.08.21"

parser = argparse.ArgumentParser(
    prog=os.path.basename(sys.argv[0]),
    usage="%(prog)s [options]",
    description="a Python 3 example",
    epilog="© 2019-2023 Frank H Jung mailto:frank.jung@marlo.com.au",
)
parser.add_argument(
    "-l",
    "--log",
    dest="logLevel",
    choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    help="Set the logging level",
    default="WARNING",
)
parser.add_argument("--version", action="version", version=__version__)

# process command line arguments
args = parser.parse_args()

# show command parameters
logging.basicConfig(
    format="%(asctime)s %(message)s", level=getattr(logging, args.logLevel)
)
logger = logging.getLogger()  # use root logger

# show workings
logger.debug("Program name (PROG): %s", parser.prog)
logger.warning("Log level (LOG): %s", getattr(logging, args.logLevel))
logger.debug("Version (VERSION): %s", __version__)

# run static greeting
logger.info(greet())
logger.warning(get_periods("2019-01-01", "2019-01-31"))
