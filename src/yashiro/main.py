import argparse
import json
import os

import jinja2

from yashiro import __version__


class Parser:
    def __init__(self, template_path, json_path):
        with open(template_path) as file:
            self.template = jinja2.Template(file.read())
        self.json = dict(os.environ)
        if json_path is not None:
            with open(json_path) as file:
                self.json.update(json.load(file))

    def __call__(self):
        return self.template.render(self.json)


def parse_args():
    parser = argparse.ArgumentParser(
        prog="yashiro",
        description="A cli wrapper for jinja templates",
    )
    parser.add_argument(
        "-V",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="Print the version and exit",
    )
    parser.add_argument("-j", "--json", help="The path to the json file")
    parser.add_argument(
        "-t", "--template", required=True, help="The path to the template"
    )

    return parser.parse_args()


def get_output():
    args = parse_args()
    parser = Parser(args.template, args.json)
    return parser()


def write_output():
    print(get_output())
