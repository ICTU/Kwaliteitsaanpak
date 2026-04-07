#!/bin/sh

set -e

uvx ruff check src tests
uvx ruff format --check
uvx mypy --python-executable=.venv/bin/python src tests
uvx vulture --min-confidence 0 src tests .vulture_white_list.py
node_modules/markdown-link-check/markdown-link-check --quiet build --config markdown-link-check.json
