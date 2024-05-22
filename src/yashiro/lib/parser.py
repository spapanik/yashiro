import sys
from argparse import ArgumentParser, Namespace
from pathlib import Path

from yashiro.__version__ import __version__

sys.tracebacklimit = 0


def parse_args() -> Namespace:
    parser = ArgumentParser(
        prog="yashiro",
        description="Jinja2's missing CLI interface",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="print the version and exit",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        dest="verbosity",
        help="increase the level of verbosity",
    )

    parser.add_argument("template", type=Path, help="The path to the template")

    parser.add_argument(
        "-m",
        "--mapping",
        metavar="mapping",
        type=Path,
        help="the path to the file that contains the extra mapping",
    )
    parser.add_argument(
        "-s", "--strict", action="store_true", help="disallow missing arguments"
    )

    args = parser.parse_args()
    if args.verbosity > 0:
        sys.tracebacklimit = 1000

    return args
