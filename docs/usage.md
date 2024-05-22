# Usage

`yashiro`, once installed offers a single command, `yashiro`, that
parses the templated based on a JSON file. `yashiro` follows the GNU
recommendations for command line interfaces, and offers:

-   `-h` or `--help` to print help, and
-   `-V` or `--version` to print the version

You can use yashiro to parse a template.

```console
usage: yashiro [-h] [-V] [-v] [-m mapping] [-s] template

Jinja2's missing CLI interface

positional arguments:
  template              The path to the template

options:
  -h/--help             show this help message and exit
  -V/--version          print the version and exit
  -v/--verbose          increase the level of verbosity
  -m/--mapping mapping  the path to the file that contains the extra mapping
  -s/--strict           disallow missing arguments
```
