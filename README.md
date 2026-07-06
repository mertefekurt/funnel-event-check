<img src="assets/readme-cover.svg" alt="Funnel Event Check cover" width="100%" />

# Funnel Event Check

Audit product funnel events for ordering, ownership, and conversion gaps.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `funnel-event-check` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `unknown-owner` | high | event owner missing |
| `missing-next-event` | medium | next funnel event missing |
| `undefined-order` | low | event order missing |

## Command line

```bash
python -m pip install -e ".[dev]"
funnel-event-check examples/sample.txt
funnel-event-check examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
event signup_started owner unknown next_event missing order undefined
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
