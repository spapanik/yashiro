import os
from unittest import mock

from yashiro import main


class TestMain:
    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser_with_toml(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = None
        args.toml = data_path("test.toml")
        args.strict = False
        os.environ.clear()
        expected = "Three cards:\n1. False\n2. 42\n3. missing"
        assert main.get_output() == expected

    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser_with_json(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = data_path("test.json")
        args.toml = None
        args.strict = False
        os.environ.clear()
        expected = "Three cards:\n1. None\n2. 42\n3. missing"
        assert main.get_output() == expected

    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser_with_env_vars(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = None
        args.toml = None
        args.strict = False
        os.environ.clear()
        os.environ["that"] = "3.14159"
        os.environ["the_other"] = "Hello, world!"
        expected = "Three cards:\n1. \n2. 3.14159\n3. Hello, world!"
        assert main.get_output() == expected

    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser_with_env_vars_and_json(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = data_path("test.json")
        args.toml = None
        args.strict = False
        os.environ.clear()
        os.environ["that"] = "3.14159"
        os.environ["the_other"] = "Hello, world!"
        expected = "Three cards:\n1. None\n2. 42\n3. missing"
        assert main.get_output() == expected

    @staticmethod
    @mock.patch("yashiro.main.parse_args")
    def test_parser_with_env_vars_and_toml(mocked_args_parser, data_path):
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.json = None
        args.toml = data_path("test.toml")
        args.strict = False
        os.environ.clear()
        os.environ["that"] = "3.14159"
        os.environ["the_other"] = "Hello, world!"
        expected = "Three cards:\n1. False\n2. 42\n3. missing"
        assert main.get_output() == expected
