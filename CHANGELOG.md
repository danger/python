## Master

* No changes.

### 0.2.0

**BREAKING** — Toolchain modernization and runtime baseline bump. The Danger DSL, the
danger-js invocation contract, and the model JSON shapes are unchanged; the 100%
test-coverage gate is preserved.

* **BREAKING:** Dropped support for Python 3.7–3.12. `danger-python` now requires **Python 3.13+** (developed and tested on 3.14).
* **BREAKING:** Migrated the runtime from **pydantic v1 to pydantic v2** (implementation only — model JSON input/output is byte-compatible).
* **BREAKING:** Migrated the CLI from **click 7 to click 8**.
* Replaced **Poetry** with **uv** for environment, dependency, and lockfile management: PEP 621 `[project]` metadata, committed `uv.lock`, and the `uv_build` backend.
* Replaced **black + isort + flake8 + pylint** with **Ruff** for linting and formatting.
* Replaced **mypy** with **Pyrefly** for type checking.
* Consolidated all tool configuration into `pyproject.toml`; removed `setup.cfg`.
* Replaced **Travis CI** with **GitHub Actions** (`ci.yml`, Python 3.13/3.14 matrix); updated the `Dockerfile` to `python:3.14-slim` + Node 20 + uv.

### 0.1.0

* Initial release of the plugin. - [@turekj]

[@turekj]: https://github.com/turekj
