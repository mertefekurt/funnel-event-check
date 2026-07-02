"""Public API for funnel-event-check."""

from funnel_event_check.core import audit_records, read_records
from funnel_event_check.models import AuditReport, Finding, Rule

__all__ = ["AuditReport", "Finding", "Rule", "audit_records", "read_records"]
__version__ = "0.1.0"
