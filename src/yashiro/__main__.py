from yashiro.command.yashiro import Command
from yashiro.lib.cli import parse_args


def main() -> None:
    args = parse_args()
    command = Command(args.template, args.mapping, strict=args.strict)
    command.write()
