# Supply Chain Agent

An AI agent that tracks purchase orders and inventory, built with the Claude API.

## Setup

```
python -m venv .venv
pip install -e ".[dev]"
cp .env.example .env   # then add your API key
```

## Run

- Smoke test: `python scripts/hello_claude.py`
- Tests: `pytest`
