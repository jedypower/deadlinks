# deadlinks

[![Travis (.org)](https://img.shields.io/travis/butuzov/deadlinks/develop)](https://travis-ci.org/butuzov/deadlinks)
[![codecov](https://codecov.io/gh/butuzov/deadlinks/branch/develop/graph/badge.svg)](https://codecov.io/gh/butuzov/deadlinks)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cff8901ed5974425a61dff833f8f81b8/develop/)](https://codacy.com/manual/butuzov/deadlinks)

## Description

`deadlinks` is a simple cli tool to check your website for deadlinks.

### Features

-   Retries in the case of `502`, `503` and `504`
-   Concurrent and recursive checks
-   External links checks

## Usage

```bash
# run 10 instances of crawler against https://gobyexample.com.ua
# with the additional check for the external links (except ones that
# match play.golang.org)
deadlinks https://gobyexample.com.ua -n 10 -e -d play.golang.org

# get more help with
deadlinks --help
```

## Installing

### From Source

```bash
# installation into virtual environment
python3 -m venv .venv
source .venv/bin/activate
pip install  git+https://github.com/butuzov/deadlinks.git@develop
```

## Alternatives

These are a lot of alternative ways to check your website for dead links errors, you can check a [open software](https://github.com/topics/link-checker) or check other options:

| Platform           | Title                      | Link                                                                |
|--------------------|----------------------------|---------------------------------------------------------------------|
| `mac`, `ui`        | Integrity                  | <https://peacockmedia.software/mac/integrity/free.html>             |
| `win`, `ui`        | Xenu's Link Sleuth         | <http://home.snafu.de/tilman/xenulink.html>                         |
| `web`              | Online Broken Link Checker | <https://www.brokenlinkcheck.com/>                                  |
| `web`              | Free Broken Link Tool      | <https://www.deadlinkchecker.com/website-dead-link-checker.asp>     |
| `win`, `ui`        | InterroBot                 | <https://interro.bot/>                                              |
| `go`, `cli`        | muffet                     | <https://github.com/raviqqe/muffet>                                 |
| `cli`, `ui`, `web` | linkchecker                | <https://wummel.github.io/linkchecker>                              |