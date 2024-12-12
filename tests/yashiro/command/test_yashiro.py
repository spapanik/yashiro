from __future__ import annotations

import os
from typing import TYPE_CHECKING
from unittest import mock

from yashiro.command.yashiro import Command

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path


class TestCommand:
    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_toml(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = data_path("test.toml")
        args.strict = False
        os.environ.clear()
        expected = "Three cards:\n1. False\n2. 42\n3. missing"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected

    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_json(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = data_path("test.json")
        args.strict = False
        os.environ.clear()
        expected = "Three cards:\n1. None\n2. 42\n3. missing"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected

    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_yaml(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = data_path("test.yml")
        args.strict = False
        os.environ.clear()
        expected = "Three cards:\n1. False\n2. 42\n3. missing"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected

    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_ini(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = data_path("test.ini")
        args.strict = False
        os.environ.clear()
        expected = "Three cards:\n1. False\n2. 42\n3. missing"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected

    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_env_vars(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = None
        args.strict = False
        os.environ.clear()
        os.environ["THAT"] = "3.14159"
        os.environ["THE_OTHER"] = "Hello, world!"
        expected = "Three cards:\n1. \n2. 3.14159\n3. Hello, world!"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected

    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_env_vars_and_json(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = data_path("test.json")
        args.strict = False
        os.environ.clear()
        os.environ["THAT"] = "3.14159"
        os.environ["THE_OTHER"] = "Hello, world!"
        expected = "Three cards:\n1. None\n2. 42\n3. missing"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected

    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_env_vars_and_toml(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = data_path("test.toml")
        args.strict = False
        os.environ.clear()
        os.environ["THAT"] = "3.14159"
        os.environ["THE_OTHER"] = "Hello, world!"
        expected = "Three cards:\n1. False\n2. 42\n3. missing"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected

    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_env_vars_and_yaml(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = data_path("test.yml")
        args.strict = False
        os.environ.clear()
        os.environ["THAT"] = "3.14159"
        os.environ["THE_OTHER"] = "Hello, world!"
        expected = "Three cards:\n1. False\n2. 42\n3. missing"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected

    @staticmethod
    @mock.patch("yashiro.lib.parser.parse_args")
    def test_parser_with_env_vars_and_ini(
        mocked_args_parser: mock.MagicMock, data_path: Callable[[str], Path]
    ) -> None:
        args = mocked_args_parser()
        args.template = data_path("test.template")
        args.mappings = data_path("test.ini")
        args.strict = False
        os.environ.clear()
        os.environ["THAT"] = "3.14159"
        os.environ["THE_OTHER"] = "Hello, world!"
        expected = "Three cards:\n1. False\n2. 42\n3. missing"
        command = Command(args.template, args.mappings, strict=args.strict)
        assert command.render() == expected


def test_command_write(
    capsys: mock.MagicMock, data_path: Callable[[str], Path]
) -> None:
    template = data_path("test.template")
    mappings = data_path("test.toml")
    command = Command(template, mappings, strict=False)
    command.write()
    captured = capsys.readouterr()
    assert captured.out == "Three cards:\n1. False\n2. 42\n3. missing\n"
    assert captured.err == ""
