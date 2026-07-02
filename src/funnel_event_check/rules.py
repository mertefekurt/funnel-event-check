from __future__ import annotations

from funnel_event_check.models import Rule

PROJECT_NAME = 'funnel-event-check'
SUMMARY = 'Audit product funnel events for ordering, ownership, and conversion gaps.'
SAMPLE_RISK = 'event signup_started owner unknown next_event missing order undefined'
SAMPLE_CLEAN = 'event signup_started owner growth next_event signup_completed order 1'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='unknown-owner',
        severity='high',
        pattern='owner\\s+(unknown|none|missing)',
        message='event owner missing',
        recommendation='assign analytics owner',
    ),
    Rule(
        code='missing-next-event',
        severity='medium',
        pattern='next_event\\s+(missing|none|unknown)',
        message='next funnel event missing',
        recommendation='define funnel transition',
    ),
    Rule(
        code='undefined-order',
        severity='low',
        pattern='order\\s+(undefined|missing|none)',
        message='event order missing',
        recommendation='number funnel stages',
    ),
)
