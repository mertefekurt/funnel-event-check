# funnel-event-check

> Audit product funnel events for ordering, ownership, and conversion gaps.

## Operator guide Overview

Audit product funnel events for ordering, ownership, and conversion gaps. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts funnel event map. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
funnel-event-check examples/sample.txt
funnel-event-check examples/sample.txt --json --fail-on medium
python -m funnel_event_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `unknown-owner` | high | event owner missing |
| `missing-next-event` | medium | next funnel event missing |
| `undefined-order` | low | event order missing |

## Validation Notes

```bash
ruff check .
pytest
python -m funnel_event_check --help
```

Example risky input:

```text
event signup_started owner unknown next_event missing order undefined
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
