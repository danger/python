[![PyPI](https://img.shields.io/pypi/v/danger-python)](https://pypi.org/project/danger-python/)
![Python versions](https://img.shields.io/badge/python-3.13%20%7C%203.14-blue)
[![CI](https://github.com/giancarlosisasi/danger-python/actions/workflows/ci.yml/badge.svg)](https://github.com/giancarlosisasi/danger-python/actions/workflows/ci.yml)

# python

Write your Dangerfiles in Python.

### Requirements

:warning: `danger-python` is currently work in progress. Breaking changes may occur.

Running `danger-python` requires:

* Python 3.13+ (developed and tested under Python 3.14)
* danger-js 9.2 (tested under danger-js 9.2.10)

### Installation

In order to test the script please run the following commands:

```sh
# install danger-js
npm install -g danger
# install danger-python
pip install danger-python
# run danger-python
danger-python pr https://github.com/microsoft/TypeScript/pull/34806
```

### dangerfile.py

You can choose between shorter untyped version of `dangerfile.py`:

```python
title = danger.github.pr.title
markdown(title)
```

Or more verbose typed version:

```python
from danger_python import Danger, markdown

danger = Danger()
title = danger.github.pr.title
markdown(title)
```

### Using as GitHub Action

1. Create a `dangerfile.py` in the root directory of your repository.
2. Add a following workflow:

```yaml
name: Danger
on: [pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - uses: danger/python@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Using as a CI step

If you already run your own pipeline, add `danger-python` as a step after your test suite
instead of using the prebuilt action above. This works on any CI provider — the example
below uses GitHub Actions:

```yaml
name: CI
on: [pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: "3.14"
    - uses: actions/setup-node@v4
      with:
        node-version: "20"
    # ... install dependencies and run your test suite here ...
    - run: npm install -g danger
    - run: pip install danger-python
    - run: danger-python ci -v
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Development

To develop the `danger-python`, clone the repository and run the following commands:

```sh
# install danger-js
npm install -g danger
# install uv (https://docs.astral.sh/uv/getting-started/installation/)
# create the virtual environment and install all dependencies from uv.lock
uv sync
# run the full local gate: format, lint, type-check, tests (enforces 100% coverage)
uv run ruff format --check
uv run ruff check
uv run pyrefly check
uv run pytest
```

To regenerate the input JSONSchema, put the latest version in `scripts/input_schema.json` and run the following commands:

```sh
cd scripts
uv run python generate_scheme.py
```

This should update the `danger_python/models.py` file.

:warning: Please, be careful with the generation script since the `master` branch contains the hand edits to the schema. They are all covered by the test suite, though.

### Building plugins

To build a plugin, add a `danger-python` as a dependency and subclass the `DangerPlugin` class:

```python
from danger_python.plugins import DangerPlugin

class ExamplePlugin(DangerPlugin):
    def hello_world(self):
        count = len(self.danger.git.modified_files)
        self.message(f"ExamplePlugin says hello to {count} modified files")
```

Importing the package in a `dangerfile.py` will import all the instance methods to the module-level globals:

```python
import example_plugin 

# calls hello_world method from the plugin class
example_plugin.hello_world()
```
