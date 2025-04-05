#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Simple Python example including logging and unit tests."""

import argparse
import logging
import os.path
from sys import argv
from example.periods import format_periods, get_periods
from example.helloworld import greet
from example.mylogging import setup_logging


__version__ = "2025.03.01"


def parse_args() -> argparse.Namespace:
    """Parse command line arguments. :no-index:"""

    parser = argparse.ArgumentParser(
        prog=os.path.basename(argv[0]),
        usage="%(prog)s [options]",
        description="a simple hello world project",
        epilog="© 2019-2025 Frank H Jung mailto:frankhjung@linux.com",
    )
    parser.add_argument(
        "-l",
        "--log",
        dest="logLevel",
        choices=list(logging.getLevelNamesMapping()),
        help="Set the logging level",
        default="INFO",
    )
    parser.add_argument(
        "-g",
        "--greet",
        action="store_true",
        help="Greet the user",
    )
    parser.add_argument(
        "-p",
        "--periods",
        action="store_true",
        help="Get weekly periods",
    )
    parser.add_argument("--version", action="version", version=__version__)
    return parser.parse_args()


def main():
    """Main function. :no-index:"""

    # process command line arguments
    args = parse_args()

    # configure logging
    logger = setup_logging(args.logLevel)

    logger.debug("Log level (LOG): %s", args.logLevel)
    logger.debug("Version (VERSION): %s", __version__)

    # run greet example
    if args.greet:
        reply = greet()
        logger.info("Greeting: %s", reply)

    # run get_periods example
    if args.periods:
        periods = get_periods("2025-03-01", "2025-03-31")
        logger.info("Periods:\n%s", format_periods(periods))


if __name__ == "__main__":  # pragma: no cover
    main()
