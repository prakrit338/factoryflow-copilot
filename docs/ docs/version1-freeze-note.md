# FactoryFlow Copilot — Version 1 Freeze Note

FactoryFlow Copilot V1 is the first working hybrid prototype of the system.

This version demonstrates:
- a Copilot Studio agent using the Siemens S7-1200 manual as a knowledge source
- a FastAPI backend for structured incident triage
- a REST API tool integrated into Copilot Studio
- hybrid responses that combine backend triage and manual-grounded guidance

## Scope of Version 1
- thermal anomaly path
- mechanical anomaly path
- fallback anomaly path
- dynamic confidence
- dynamic escalation
- triage summary output
- tool-based incident classification
- manual-grounded response support

## Known limitations
- some manual-grounded answer sections may still be broader than ideal
- backend logic is currently rule-based and prototype-oriented
- local testing uses a dev-tunnel style setup rather than production deployment

## Purpose of freezing V1
This freeze preserves the first end-to-end working version before future refinements and Version 2 improvements.