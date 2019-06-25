#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example Python 3 project.
"""

import argparse
import logging
import os.path
import sys
from helloworld.helloworld import greet


def main(argv):

    """ Run Hello World example program. """

    __version__ = '0.1.0'

    parser = argparse.ArgumentParser(
        prog=os.path.basename(argv[0]),
        usage='%(prog)s [options]',
        description='a Python 3 example',
        epilog='© 2019 Frank H Jung mailto:frank.jung@marlo.com.au')
    parser.add_argument(
        '-v',
        '--verbose',
        help='verbose output',
        action='count')
    parser.add_argument(
        '--version',
        action='version',
        version=__version__)

    # process command line arguments
    args = parser.parse_args()
    prog = parser.prog
    verbose = args.verbose

    # show command parameters
    logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)
    logger = logging.getLogger(__name__)
    if verbose:
        logger.setLevel(logging.DEBUG)

    # show workings
    logger.debug('Program name (prog): %s', prog)
    logger.debug('Flag (verbose): %s', verbose)
    logger.debug('Version (version): %s', __version__)

    # run static greeting
    logger.info(greet())

    return 0


#
# MAIN
#
if __name__ == '__main__':
    RC = main(sys.argv)
    sys.exit(RC)

#EOF
