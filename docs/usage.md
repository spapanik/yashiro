# Usage

`yashiro`, once installed offers a single command, `yashiro`, that
parses the templated based on a JSON file. `yashiro` follows the GNU
recommendations for command line interfaces, and offers:

-   `-h` or `--help` to print help, and
-   `-V` or `--version` to print the version

You can use yashiro to parse a template.

```console
usage: yashiro [-h] [-V] [-m MAPPING] [-s] -t TEMPLATE

optional arguments:
    -h, --help             Show this help message and exit
    -m/--mappings MAPPINGS The path to the file that contains the mappings
    -t/--template TEMPLATE The path to the template
    -V/--version           Print the version and exit
```
