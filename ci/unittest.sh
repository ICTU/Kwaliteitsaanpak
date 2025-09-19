#!/bin/sh

export PYTHONPATH=src:$PYTHONPATH
.venv/bin/coverage run --omit=*venv/* --branch -m unittest --quiet
.venv/bin/coverage xml -o build/unittest-coverage.xml
.venv/bin/coverage html --directory build/unittest-coverage
.venv/bin/coverage report --fail-under=97 --skip-covered
