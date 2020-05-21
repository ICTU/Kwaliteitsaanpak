#!/bin/sh

set -e

black --quiet --line-length 118 src tests
mypy --no-error-summary src tests
pylint src tests
NAMES_TO_IGNORE=''
vulture --min-confidence 0 --ignore-names $NAMES_TO_IGNORE src tests .vulture_white_list.py
