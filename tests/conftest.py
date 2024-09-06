from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Callable


@pytest.fixture
def data_path() -> Callable[[str], Path]:
    def _data_path(path: str) -> Path:
        return Path(__file__).parent.joinpath("data").joinpath(path)

    return _data_path
