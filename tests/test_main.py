import os
from unittest import mock

from yashiro import main


class TestMain:
    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = data_path("test.json")
        expected = "Three cards:\n1. None\n1. 42\n1. "
        assert main.get_output() == expected

    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser_with_env_vars(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = None
        os.environ.clear()
        os.environ["that"] = "3.14159"
        os.environ["other"] = "Hello, world!"
        expected = "Three cards:\n1. \n1. 3.14159\n1. Hello, world!"
        assert main.get_output() == expected

    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser_with_env_vars_and_json(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = data_path("test.json")
        os.environ.clear()
        os.environ["that"] = "3.14159"
        os.environ["other"] = "Hello, world!"
        expected = "Three cards:\n1. None\n1. 42\n1. Hello, world!"
        assert main.get_output() == expected
