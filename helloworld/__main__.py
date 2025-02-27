#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple Python example project."""

# TODO
# - move logging setup to own module
# - add logging setup unit tests
# - move periods formatting to own module
# - add periods formatting unit tests

import argparse
import logging
from logging.config import dictConfig
import os.path
import json
from sys import argv
from datetime import date
from helloworld.helloworld import get_periods, greet


__version__ = "2025.02.07"


def setup_logging(log_level: str) -> logging.Logger:
    """Configure logging with the specified level.

    Args:
        log_level: String representation of logging level (e.g., "INFO", "DEBUG")

    Returns:
        Configured logger instance
    """
    # Load config from JSON file
    try:
        with open("logging_config.json", "r", encoding="UTF-8") as f:
            config = json.load(f)
        # do not use level in config file, get from command line
        config["handlers"]["console"]["level"] = log_level
        dictConfig(config)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        # Fallback to default config if file not found or invalid
        logging.basicConfig(
            format="%(asctime)s %(levelname)s %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%SZ",
        )
        logging.warning("Failed to load logging config from file {e}", e)
    # set logger to not propagate to root logger and set default level
    logger = logging.getLogger()
    logger.propagate = False
    logger.setLevel(getattr(logging, log_level))
    return logger


def format_periods(periods: dict[int, date]):
    """Format periods dictionary into a readable string."""
    if not periods:
        return "No periods found"
    # pretty format the periods
    formatted = "Weekly periods:\n"
    for week_num, start_date in sorted(periods.items()):
        formatted += f"  Week {week_num}: {start_date.strftime('%Y-%m-%d')}\n"
    return formatted.rstrip()


def main():
    """Main function."""
    # SETUP

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
    parser.add_argument("--version", action="version", version=__version__)

    # process command line arguments
    args = parser.parse_args()

    # configure logging
    logger = setup_logging(args.logLevel)

    # show workings
    logger.debug("Program name (PROG): %s", parser.prog)
    logger.debug("Log level (LOG): %s", args.logLevel)
    # noqa: E501
    logger.debug("Version (VERSION): %s", __version__)

    # MAIN

    # run greet example
    reply = greet()
    logger.info("Greeting: %s", reply)

    # run get_periods example
    periods = get_periods("2019-01-01", "2019-01-31")
    logger.info("Periods:\n%s", format_periods(periods))


if __name__ == "__main__":
    main()
