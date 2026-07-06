# Funnel Event Check

Audit product funnel events for ordering, ownership, and conversion gaps. I keep it small because this kind of check is most useful when it can run beside the work, not after the work has already shipped.

## Project card

<img src="assets/readme-cover.svg" alt="Funnel Event Check cover" width="100%" />

| Detail | Value |
| --- | --- |
| Area | product operations |
| Command | `funnel-event-check` |
| Example | `examples/sample.txt` |

## What would make me stop a review

| Stopper | Level | Why it matters |
| --- | --- | --- |
| `unknown-owner` | high | event owner missing |
| `missing-next-event` | medium | next funnel event missing |
| `undefined-order` | low | event order missing |

## Run from a fresh clone

```bash
git clone https://github.com/mertefekurt/funnel-event-check.git
cd funnel-event-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
funnel-event-check examples/sample.txt
funnel-event-check examples/sample.txt --json
```
