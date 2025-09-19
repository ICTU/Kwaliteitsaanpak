FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.8.19 /uv /uvx /bin/

WORKDIR /work

ADD pyproject.toml /work/pyproject.toml
ADD uv.lock /work/uv.lock
RUN uv sync --locked
