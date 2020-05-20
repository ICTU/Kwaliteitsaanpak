#!/bin/sh

set -e

black --quiet --line-length 118 src
mypy --no-error-summary src
pylint src
NAMES_TO_IGNORE=''
vulture --min-confidence 0 --ignore-names $NAMES_TO_IGNORE src/ .vulture_white_list.py
