from unittest import mock

from yashiro.__main__ import main


@mock.patch(
    "yashiro.__main__.parse_args",
    new=mock.MagicMock(
        return_value=mock.MagicMock(
            template="/path/to/template", mapping="/path/to/mapping", strict=True
        )
    ),
)
@mock.patch("yashiro.__main__.Command")
def test_clone(mock_command: mock.MagicMock) -> None:
    main()
    assert mock_command.call_count == 1
    calls = [mock.call("/path/to/template", "/path/to/mapping", strict=True)]
    assert mock_command.call_args_list == calls
