from pydantic import BaseModel
from typing import List


class IncidentTriageRequest(BaseModel):
    incident_text: str
    machine_type: str
    severity_hint: str


class IncidentTriageResponse(BaseModel):
    issue_category: str
    possible_failure_modes: List[str]
    confidence: str
    recommended_next_step: str
    needs_manual_lookup: bool
    matched_keywords: List[str]
    escalation_required: bool

    triage_summary: str

class JiraCreateIssueRequest(BaseModel):
    incident_text: str
    machine_type: str
    severity_hint: str
    issue_category: str
    confidence: str
    recommended_next_step: str
    matched_keywords: List[str]
    escalation_required: bool
    triage_summary: str

class JiraCreateIssueResponse(BaseModel):
    success: bool
    jira_issue_key: str
    jira_issue_url: str
    message: str


