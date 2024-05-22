import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from yashiro.__version__ import __version__

sys.tracebacklimit = 0


def parse_args() -> Namespace:
    parser = ArgumentParser(
        prog="yashiro",
        description="A utility to manage testing and migrating a database",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Print the version and exit",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        dest="verbosity",
        help="increase the level of verbosity",
    )

    parser.add_argument(
        "-m",
        "--mappings",
        type=Path,
        help="The path to the file that contains the mappings",
    )
    parser.add_argument(
        "-s", "--strict", action="store_true", help="Disallow missing arguments"
    )
    parser.add_argument(
        "-t", "--template", required=True, type=Path, help="The path to the template"
    )

    args = parser.parse_args()
    if args.verbosity > 0:
        sys.tracebacklimit = 1000

    return args
