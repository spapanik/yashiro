from __future__ import annotations

import os
from pathlib import Path

import jinja2
from dj_settings import ConfigParser


class Command:
    __slots__ = ("template", "mapping")

    def __init__(self, template: Path, mapping: Path | None, *, strict: bool) -> None:
        raw_template = template.read_text()
        undefined = jinja2.StrictUndefined if strict else jinja2.Undefined
        self.template = jinja2.Template(raw_template, undefined=undefined)
        self.mapping = dict(os.environ)
        if mapping is not None:
            data = ConfigParser([Path(mapping)]).data
            self.mapping |= data.get("yashiro", {})

    def render(self) -> str:
        return self.template.render(self.mapping)

    def write(self) -> None:
        print(self.render())
