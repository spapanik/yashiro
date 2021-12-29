=====
Usage
=====

``yashiro``, once installed offers a single command, ``yashiro``, that parses the templated based on a JSON file. ``yashiro`` follows the GNU recommendations for command line interfaces, and offers:

* ``-h`` or ``--help`` to print help, and
* ``-V`` or ``--version`` to print the version

You can use yashiro to parse a template.

.. code:: console

    usage: yashiro [-h] [-j JSON] [-t TEMPLATE] [-V]

    optional arguments:
        -h, --help             Show this help message and exit
        -j/--json JSON         The path to the json file
        -t/--template TEMPLATE The path to the template
        -V/--version           Print the version and exit
