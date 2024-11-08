#!/bin/sh

set -e

uvx ruff check
uvx ruff format --check
uvx mypy --python-executable=.venv/bin/python src tests
NAMES_TO_IGNORE=''
uvx vulture --min-confidence 0 --ignore-names $NAMES_TO_IGNORE src tests .vulture_white_list.py
uvx md-dead-link-check .
