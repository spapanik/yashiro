from __future__ import annotations

import argparse
import os
from pathlib import Path

import jinja2
from dj_settings import ConfigParser

from yashiro.__version__ import __version__


class Parser:
    __slots__ = ["template", "mapping"]

    def __init__(self, args: argparse.Namespace):
        raw_template = args.template.read_text()
        undefined = jinja2.StrictUndefined if args.strict else jinja2.Undefined
        self.template = jinja2.Template(raw_template, undefined=undefined)
        self.mapping = dict(os.environ)
        mappings_file = args.mappings
        if mappings_file is not None:
            data = ConfigParser([Path(mappings_file)]).data
            self.mapping |= data.get("yashiro", {})

    def __call__(self) -> str:
        return self.template.render(self.mapping)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
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

    return parser.parse_args()


def get_output() -> str:
    args = parse_args()
    parser = Parser(args)
    return parser()


def write_output() -> None:
    print(get_output())
