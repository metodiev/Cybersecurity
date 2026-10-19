PYTHON ?= python3.14
VENV ?= .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
MKDOCS := $(VENV)/bin/mkdocs
PYMARKDOWN := $(VENV)/bin/pymarkdown
MD_FILES := $(shell find . -name '*.md' -not -path './.venv/*' -not -path './site/*' -not -type l | sort)

.PHONY: help venv install serve build lint links manifest mermaid mermaid-strict check clean

help:
	@printf '%s\n' \
	  'make install        Create .venv and install pinned documentation dependencies' \
	  'make serve          Serve the site at http://127.0.0.1:8000' \
	  'make build          Build the site into site/ with --strict' \
	  'make lint           Lint Markdown with .pymarkdown.json' \
	  'make links          Check local links, anchors, and MkDocs nav targets' \
	  'make manifest       Validate the curriculum manifest against its JSON Schema' \
	  'make mermaid        Render Mermaid blocks if mmdc is available' \
	  'make mermaid-strict Render Mermaid blocks and fail if mmdc is unavailable' \
	  'make check          Run manifest, links, lint, and strict build' \
	  'make clean          Remove site/'

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-docs.txt

serve: install
	$(MKDOCS) serve -a 127.0.0.1:8000

build: install
	$(MKDOCS) build --strict

lint: install
	$(PYMARKDOWN) --config .pymarkdown.json --strict-config scan $(MD_FILES)

links: install
	$(PY) scripts/check_links.py

manifest: install
	$(PY) scripts/validate_manifest.py

mermaid: install
	$(PY) scripts/check_mermaid.py --render

mermaid-strict: install
	$(PY) scripts/check_mermaid.py --render --require-render

check: manifest links lint build

clean:
	rm -rf site
