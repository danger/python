FROM python:3.14-slim

LABEL maintainer="Jakub Turek <jkbturek@gmail.com>"

# danger-python shells out to danger-js, so the image needs Node. Install
# Node 20 via NodeSource. python:*-slim ships without curl / gnupg /
# ca-certificates, which the NodeSource setup script requires.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        gnupg \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install uv (dependency / environment manager) from its official image.
COPY --from=ghcr.io/astral-sh/uv:0.11 /uv /uvx /bin/

WORKDIR /usr/src/danger-python
COPY . .

# Install the package and its runtime dependencies from the committed lockfile
# into an in-project virtualenv (no dev tools), then put that venv on PATH so
# the `danger-python` console script the entrypoint calls is resolvable. Use
# the base image's Python 3.14 rather than downloading a second interpreter.
ENV UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON_PREFERENCE=only-system
RUN uv sync --frozen --no-dev --no-editable
ENV PATH="/usr/src/danger-python/.venv/bin:${PATH}"

ENTRYPOINT ["npx", "--package", "danger", "danger-python", "ci"]
