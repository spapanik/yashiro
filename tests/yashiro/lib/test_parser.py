import os
from pathlib import Path
from unittest import mock

import pytest

from yashiro.lib.cli import parse_args


@pytest.mark.parametrize(
    ("verbose", "expected_verbosity"),
    [("-v", 1), ("-vv", 2), ("-vvvvv", 5)],
)
def test_yashiro_verbose(verbose: str, expected_verbosity: int) -> None:
    with mock.patch("sys.argv", ["yashiro", os.devnull, verbose]):
        args = parse_args()

    assert args.verbosity == expected_verbosity


def test_yashiro_strict() -> None:
    with mock.patch("sys.argv", ["yashiro", os.devnull, "--strict"]):
        args = parse_args()
    assert args.strict is True


def test_yashiro_mapping() -> None:
    with mock.patch(
        "sys.argv", ["yashiro", os.devnull, "--mapping", "./path/to/mapping"]
    ):
        args = parse_args()
    assert args.mapping == Path("./path/to/mapping")
