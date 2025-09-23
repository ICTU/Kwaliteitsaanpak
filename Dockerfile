FROM python:3.13-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.8.21 /uv /uvx /bin/

WORKDIR /work

ADD pyproject.toml /work/pyproject.toml
ADD uv.lock /work/uv.lock
RUN uv sync --locked
