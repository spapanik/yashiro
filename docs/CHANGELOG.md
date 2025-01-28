# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

### Changed

-   Changed template to be a positional instead of an optional cli arg

### Removed

-   Dropped python 3.7 support
-   Dropped python 3.8 support
-   Dropped python 3.9 support
-   Dropped python 3.10 support

## [0.9.0] - 2022-03-10

### Changed

-   Change toml parser to tomli
-   Use dj_settings to parse the mappings file
-   Replaced -j/\--json and -o/\--toml flags with a single -m/\--mapping
    one
-   Require a yashiro section in the config

## [0.8.0] - 2022-01-10

### Removed

-   Removed changelog from the published wheel

## [0.7.0] - 2022-01-05

### Added

-   Added python310 support

### Removed

-   Dropped python36 support

## [0.6.0] - 2021-05-17

### Removed

-   Drop support for python 3.6.0 and 3.6.1

### Changed

-   Updated jinja2 version

## [0.5.0] - 2021-03-22

### Added

-   Added an option to allow variables in toml files

## [0.4.0] - 2021-03-01

### Added

-   Added an option to disallow undefined variables in templates

## [0.3.0] - 2019-12-24

### Added

-   Env vars are now the default values of the template variables

## [0.2.0] - 2019-11-25

### Changed

-   The output of the parser is printed to the stdout

## [0.1.0] - 2019-11-22

### Added

-   Added a template parser

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
[Unreleased]: https://github.com/spapanik/yashiro/compare/v0.9.0...main
[0.9.0]: https://github.com/spapanik/yashiro/compare/v0.8.0...v0.9.0
[0.8.0]: https://github.com/spapanik/yashiro/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/spapanik/yashiro/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/spapanik/yashiro/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/spapanik/yashiro/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/spapanik/yashiro/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/spapanik/yashiro/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/spapanik/yashiro/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/spapanik/yashiro/releases/tag/v0.1.0
