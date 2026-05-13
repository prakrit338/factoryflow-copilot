# FactoryFlow Copilot — Synthetic Incident Schema V1

## Purpose
Define the structure of synthetic incident tickets that simulate private enterprise maintenance records.

## Fields
- incident_id
- timestamp
- machine_type
- short_summary
- full_description
- observed_symptoms
- suspected_issue_category
- severity
- recommended_next_step
- related_manual
- escalation_required

## Example
- incident_id: INC-0001
- timestamp: 2026-05-08T08:00:00
- machine_type: industrial_controller
- short_summary: Controller shutdown after rising temperature
- full_description: During normal operation, controller temperature increased and torque readings became abnormal before shutdown.
- observed_symptoms: overheating, abnormal torque, shutdown
- suspected_issue_category: thermal/load anomaly
- severity: medium
- recommended_next_step: inspect diagnostics and review safe restart procedure
- related_manual: Siemens S7-1200 System Manual
- escalation_required: yes