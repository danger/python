[![PyPI](https://img.shields.io/pypi/v/danger-python)](https://pypi.org/project/danger-python/)
![Python versions](https://img.shields.io/pypi/pyversions/danger-python)
[![Build Status](https://travis-ci.org/danger/python.svg?branch=master)](https://travis-ci.org/danger/python)

# python

Write your Dangerfiles in Python.

### Requirements

:warning: `danger-python` is currently work in progress. Breaking changes may occur.

Running `danger-python` requires:

* Python 3.7 (tested under Python 3.7.5)
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
    - uses: actions/checkout@v2
    - uses: danger/python@master
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Using as a CI step (Travis)

1. Create a `dangerfile.py` in the root directory of your repository.
2. Set up the CI to execute the `danger-python` script after the test suite.

Example `.travis.yml` configuration:

```yaml
language: python
python:
    - "3.7"
cache:
    yarn: true
    pip: true
    directories:
        - node_modules
install:
    - pip install poetry
    - poetry install
script:
    - poetry run pytest
after_script:
    - nvm install 10.16.0
    - nvm use 10.16.0
    - yarn global add danger
    - pip install danger-python
    - danger-python ci -v
```

### Development

To develop the `danger-python`, clone the repository and run the following commands:

```sh
# install danger
npm install -g danger
# install poetry
pip install poetry
# install project dependencies
poetry install
# activate virtual environment
poetry shell
# run tests
pytest
```

To regenerate the input JSONSchema, put the latest version in `scripts/input_schema.json` and run the following commands:

```sh
cd scripts
python generate_scheme.py
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
