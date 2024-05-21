# Installation

## Officially Supported Method: Using pipx

We recommend using [pipx] for the installation of `yashiro` as it provides
an isolated environment for the package, preventing any dependency conflicts.

To install `yashiro` using pipx, run the following command in your terminal:

```console
$ pipx install yashiro
```

## Alternative Method: Using pip

As an alternative, you can use [pip] to install `yashiro`.
However, this method does not provide an isolated environment for the package,
which may lead to dependency conflicts or leave your system in an inconsistent state.
Therefore, this method is not recommended or supported.

To install `yashiro` using pip, run the following command in your terminal:

```console
$ pip install --user yashiro
```

## Python Version Requirement

Please note that `yashiro` requires Python 3.11 or higher. Please ensure
that your system is using the correct Python version. If not,
consider using a tool like [pyenv] to create a shell with the required Python version.

[pip]: https://pip.pypa.io/en/stable/
[pipx]: https://pypa.github.io/pipx/
[pyenv]: https://github.com/pyenv/pyenv
