# python



### Fixtures

Generating a fixture: 

```sh
# install danger
npm install -g danger
# generate a JSON fixture of what danger-js will pass to the python
danger pr https://github.com/microsoft/TypeScript/pull/34806 --json > fixtures/typescript-34806.json
```

Then to work on the process

```sh
# Using a fixture
cat fixtures/typescript-34806.json | python danger_runner.py

# Using Danger


```
