# FactoryFlow Copilot — Version 1 Case Study

## 1. Problem
Industrial troubleshooting information is often split across:
- technical manuals
- troubleshooting knowledge
- informal incident descriptions

Users need both:
- a likely issue classification
- document-grounded guidance

## 2. Solution
FactoryFlow Copilot is a hybrid Microsoft AI agent that combines:
- Copilot Studio knowledge grounding using the Siemens S7-1200 manual
- a custom FastAPI backend for incident triage
- a REST API tool inside Copilot Studio for structured classification

## 3. Architecture
### User-facing layer
- Copilot Studio agent: FactoryFlow Orchestrator

### Knowledge layer
- Siemens S7-1200 System Manual uploaded to Copilot Studio

### Logic layer
- FastAPI backend with `/incident/triage`

### Integration layer
- REST API tool imported into Copilot Studio from an OpenAPI v2 specification

## 4. Backend capabilities
The backend returns:
- issue_category
- possible_failure_modes
- confidence
- recommended_next_step
- needs_manual_lookup
- matched_keywords
- escalation_required
- triage_summary

## 5. Hybrid behavior demonstrated
### Example 1
Thermal issue:
- overheating + torque
- tool classification + manual-grounded caution

### Example 2
Mechanical issue:
- vibration + noise
- tool classification + manual-grounded installation/specification checks

## 6. What worked well
- missing tool inputs were requested automatically
- backend tool influenced the final answer
- manual grounding remained present
- answer format became structured and more professional

## 7. Current limitations
- some manual-grounded sections may still sound broader than ideal
- tool/knowledge orchestration could be further tuned
- local dev tunnel / development connection flow is not a production deployment setup

## 8. Why this project matters
This project demonstrates:
- Microsoft Copilot Studio tool orchestration
- document-grounded enterprise AI behavior
- Python/FastAPI backend integration
- structured agent design for real workflow use cases