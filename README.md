# python

Write your Dangerfiles in Python.

### Requirements

Running `danger-python` requires:

* Python 3.7 (tested under Python 3.7.5)
* danger-js 9.2 (tested under danger-js 9.2.10)

### Installation

:warning: The script is currently work in progress. Installation requires:

* Poetry 1.0.2

In order to test the script please run the following commands:

```sh
# install danger
npm install -g danger
# install poetry
pip install poetry
# install project dependencies
poetry install --no-dev
# activate virtual environment
poetry shell
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

### Development

To develop the code, clone the repository and run the following commands:

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

### TODOs

- [x] Parse complete Danger DSL
- [x] Plugin infrastructure
- [ ] Release the initial version of the package

