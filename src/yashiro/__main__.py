from yashiro.command.yashiro import Command
from yashiro.lib.parser import parse_args


def main() -> None:
    args = parse_args()
    command = Command(args.template, args.mapping, strict=args.strict)
    command.write()
