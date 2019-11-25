from unittest import mock

from yashiro import main


class TestMain:
    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_version(mocked_args_parser):
        args = mocked_args_parser()
        args.version = True
        assert main.get_output().startswith("Yashiro ")

    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = data_path("test.json")
        expected = "Three cards:\n1. None\n1. 42\n1. "
        assert main.get_output() == expected
