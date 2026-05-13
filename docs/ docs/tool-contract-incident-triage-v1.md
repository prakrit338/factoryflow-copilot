# Tool Contract — Incident Triage Analyzer (V1)

## Tool name
Incident Triage Analyzer

## Tool purpose
Classify industrial incidents based on described symptoms and return a structured triage result.

## When to use
Use this tool when the user describes an industrial incident, anomaly, failure, or abnormal behavior and asks what kind of issue it might be.

Do not use this tool for documentation-only questions.

## Input schemaxxx
- incident_text: string
- machine_type: string
- severity_hint: string

## Output schema
- issue_category: string
- possible_failure_modes: list of strings
- confidence: string
- recommended_next_step: string
- needs_manual_lookup: boolean

## Backend mapping
POST /incident/triage