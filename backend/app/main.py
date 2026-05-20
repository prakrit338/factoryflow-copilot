from fastapi import FastAPI
from app.models import (
    IncidentTriageRequest,
    IncidentTriageResponse,
    JiraCreateIssueRequest,
    JiraCreateIssueResponse
)



app = FastAPI(
    title="FactoryFlow Learning Backend",
    description="Backend API for incident triage and future action planning.",
    version="0.1.0"
)
def get_confidence_from_keywords(keywords):
    if len(keywords) >= 2:
        return "high"
    elif len(keywords) == 1:
        return "medium"
    else:
        return "low"


def should_escalate(severity_hint, issue_category, confidence):
    if severity_hint in ["high", "critical"]:
        return True
    elif issue_category == "possible thermal/load anomaly" and confidence == "high":
        return True
    else:
        return False
    
def build_triage_summary(issue_category, confidence, matched_keywords, escalation_required):
    if matched_keywords:
        keyword_text = ", ".join(matched_keywords)
    else:
        keyword_text = "No strong keyword matches found"

    if escalation_required:
        escalation_text = "Escalation recommended."
    else:
        escalation_text = "Escalation not required."

    return f"{issue_category.capitalize()} detected with {confidence} confidence. Matched keywords: {keyword_text}. {escalation_text}"

from fastapi import Request

@app.middleware("http")
async def log_request_body(request: Request, call_next):
    body = await request.body()
    print("RAW REQUEST BODY:", body.decode("utf-8"))
    response = await call_next(request)
    return response



@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/incident/triage", response_model=IncidentTriageResponse)
def triage_incident(request: IncidentTriageRequest):
    incident_text_lower = request.incident_text.lower()
    severity_hint_lower = request.severity_hint.lower()

    thermal_keywords = []

    if "overheat" in incident_text_lower:
        thermal_keywords.append("overheat")

    if "temperature" in incident_text_lower:
        thermal_keywords.append("temperature")

    if "torque" in incident_text_lower:
        thermal_keywords.append("torque")

    thermal_confidence = get_confidence_from_keywords(thermal_keywords)

    mechanical_keywords = []

    if "vibration" in incident_text_lower:
        mechanical_keywords.append("vibration")

    if "noise" in incident_text_lower:
        mechanical_keywords.append("noise")

    if "shaking" in incident_text_lower:
        mechanical_keywords.append("shaking")

    mechanical_confidence = get_confidence_from_keywords(mechanical_keywords)

    thermal_escalation = should_escalate(
        severity_hint_lower,
        "possible thermal/load anomaly",
        thermal_confidence
    )

    mechanical_escalation = should_escalate(
        severity_hint_lower,
        "possible mechanical anomaly",
        mechanical_confidence
    )

    fallback_escalation = should_escalate(
        severity_hint_lower,
        "general industrial anomaly",
        "low"
    )

    if thermal_keywords:
        return IncidentTriageResponse(
            issue_category="possible thermal/load anomaly",
            possible_failure_modes=[
                "heat dissipation issue",
                "overstrain condition"
            ],
            confidence=thermal_confidence,
            recommended_next_step="Review diagnostics guidance and inspect for overheating-related conditions before restart.",
            needs_manual_lookup=True,
            matched_keywords=thermal_keywords,
            escalation_required=thermal_escalation,
            triage_summary=build_triage_summary(
                "possible thermal/load anomaly",
                thermal_confidence,
                thermal_keywords,
                thermal_escalation
            )
        )

    elif mechanical_keywords:
        return IncidentTriageResponse(
            issue_category="possible mechanical anomaly",
            possible_failure_modes=[
                "mechanical imbalance",
                "component wear",
                "alignment issue"
            ],
            confidence=mechanical_confidence,
            recommended_next_step="Inspect mechanical components, review maintenance history, and check the relevant troubleshooting guidance.",
            needs_manual_lookup=True,
            matched_keywords=mechanical_keywords,
            escalation_required=mechanical_escalation,
            triage_summary=build_triage_summary(
                "possible mechanical anomaly",
                mechanical_confidence,
                mechanical_keywords,
                mechanical_escalation
            )
        )

    else:
        return IncidentTriageResponse(
            issue_category="general industrial anomaly",
            possible_failure_modes=[
                "undetermined operational issue"
            ],
            confidence="low",
            recommended_next_step="Gather more symptoms, review diagnostics, and consult the relevant technical manual.",
            needs_manual_lookup=True,
            matched_keywords=[],
            escalation_required=fallback_escalation,
            triage_summary=build_triage_summary(
                "general industrial anomaly",
                "low",
                [],
                fallback_escalation
            )
        )

@app.post("/jira/create-issue", response_model = JiraCreateIssueResponse)

@app.post("/jira/create-issue", response_model=JiraCreateIssueResponse)
def create_jira_issue(request: JiraCreateIssueRequest):
    issue_key = "FACT-101"
    issue_url = f"https://example.atlassian.net/browse/{issue_key}"

    jira_summary = build_jira_summary(request.issue_category, request.machine_type)
    jira_priority = get_jira_priority_from_severity(request.severity_hint)

    message = (
        f"Jira issue created successfully. "
        f"Summary: {jira_summary}. "
        f"Priority: {jira_priority}."
    )

    return JiraCreateIssueResponse(
        success=True,
        jira_issue_key=issue_key,
        jira_issue_url=issue_url,
        message=message
    )

def get_jira_priority_from_severity(severity_hint):
    severity = severity_hint.lower()

    if severity in ["high", "critical"]:
        return "High"
    else:
        return "Medium"
def build_jira_summary(issue_category, machine_type):
    return f"{issue_category.capitalize()} detected in {machine_type}"
