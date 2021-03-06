import pathlib

import pytest


@pytest.fixture()
def data_path():
    def _data_path(path):
        return pathlib.Path(__file__).parent.joinpath("data").joinpath(path).as_posix()

    return _data_path
