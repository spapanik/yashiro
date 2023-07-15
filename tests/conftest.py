from __future__ import annotations

from collections.abc import Callable
from pathlib import Path

import pytest


@pytest.fixture()
def data_path() -> Callable[[str], Path]:
    def _data_path(path: str) -> Path:
        return Path(__file__).parent.joinpath("data").joinpath(path)

    return _data_path
