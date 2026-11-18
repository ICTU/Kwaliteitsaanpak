# Show the available recipes
default:
    @just --list

# Install the dependencies
install:
    npm install --ignore-scripts
    uv sync

# Generate documents, e.g. `just make DocumentDefinitions/wijzigingsgeschiedenis.json`; without arguments, generate all documents
make *document_definitions="DocumentDefinitions/*.json":
    uv run src/convert.py {{ document_definitions }}

# Run the unit tests
test:
    PYTHONPATH=src .venv/bin/coverage run -m unittest --quiet
    .venv/bin/coverage xml -o build/unittest-coverage.xml
    .venv/bin/coverage html --directory build/unittest-coverage
    .venv/bin/coverage report

# Run the quality checks; the markdown link check needs generated documents in the build folder
check:
    uvx ruff check src tests
    uvx ruff format --check
    uvx mypy --python-executable=.venv/bin/python src tests
    uvx vulture --min-confidence 0 src tests .vulture_white_list.py
    node_modules/markdown-link-check/markdown-link-check --quiet build --config markdown-link-check.json

# Remove generated files and caches
clean:
    rm -rf build docs/wip/* .coverage .mypy_cache .ruff_cache
