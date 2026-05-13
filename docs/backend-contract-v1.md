# FactoryFlow Copilot — Backend Contract V1

## Purpose
The backend provides custom incident-triage and action-planning logic that will later be called by the FactoryFlow Orchestrator in Copilot Studio.

## Why a backend is needed
Copilot Studio handles user interaction, orchestration, and knowledge-grounded answers.
The Python backend will handle structured logic, incident categorization, and next-step generation.

## First backend capability
Incident Triage API


## Endpoint 1
POST /incident/triage

## Purpose
Accept an incident description and return a structured triage result.

## Example input
{
  "incident_text": "Controller reported abnormal temperature and increasing torque before shutdown.",
  "machine_type": "industrial_controller",
  "severity_hint": "medium"
}

## Example output
{
  "issue_category": "possible thermal or load-related anomaly",
  "possible_failure_modes": [
    "heat dissipation issue",
    "overstrain condition",
    "unexpected operational stress"
  ],
  "confidence": "medium",
  "recommended_next_step": "Review controller diagnostics guidance and inspect for overheating-related conditions before restarting.",
  "needs_manual_lookup": true
}
``