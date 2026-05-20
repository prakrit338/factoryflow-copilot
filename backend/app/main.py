
import os
import base64
import requests
from dotenv import load_dotenv
load_dotenv()
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
@app.post("/jira/create-issue", response_model=JiraCreateIssueResponse)
def create_jira_issue(request: JiraCreateIssueRequest):
    jira_base_url = os.getenv("JIRA_BASE_URL")
    jira_email = os.getenv("JIRA_EMAIL")
    jira_api_token = os.getenv("JIRA_API_TOKEN")
    jira_project_key = os.getenv("JIRA_PROJECT_KEY")

    if not all([jira_base_url, jira_email, jira_api_token, jira_project_key]):
        return JiraCreateIssueResponse(
            success=False,
            jira_issue_key="",
            jira_issue_url="",
            message="Jira configuration is missing. Please set the Jira environment variables."
        )

    jira_summary = build_jira_summary(request.issue_category, request.machine_type)
    jira_priority = get_jira_priority_from_severity(request.severity_hint)
    jira_description = build_jira_description_adf(request, jira_priority)

    auth_string = f"{jira_email}:{jira_api_token}"
    auth_encoded = base64.b64encode(auth_string.encode("utf-8")).decode("utf-8")

    headers = {
        "Authorization": f"Basic {auth_encoded}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "fields": {
            "project": {
                "key": jira_project_key
            },
            "summary": jira_summary,
            "issuetype": {
                "name": "Task"
            },
            "description": jira_description
        }
    }

    jira_url = f"{jira_base_url}/rest/api/3/issue"

    try:
        response = requests.post(jira_url, headers=headers, json=payload)
        response_data = response.json()

        if response.status_code in [200, 201]:
            issue_key = response_data.get("key", "")
            issue_url = f"{jira_base_url}/browse/{issue_key}"

            return JiraCreateIssueResponse(
                success=True,
                jira_issue_key=issue_key,
                jira_issue_url=issue_url,
                message=f"Jira issue created successfully. Summary: {jira_summary}. Priority: {jira_priority}."
            )
        else:
            return JiraCreateIssueResponse(
                success=False,
                jira_issue_key="",
                jira_issue_url="",
                message=f"Jira issue creation failed. Status: {response.status_code}. Response: {response.text}"
            )

    except Exception as e:
        return JiraCreateIssueResponse(
            success=False,
            jira_issue_key="",
            jira_issue_url="",
            message=f"Error while creating Jira issue: {str(e)}"
        )

def get_jira_priority_from_severity(severity_hint):
    severity = severity_hint.lower()

    if severity in ["high", "critical"]:
        return "High"
    else:
        return "Medium"
def build_jira_summary(issue_category, machine_type):
    return f"{issue_category.capitalize()} detected in {machine_type}"
def build_jira_description_adf(request: JiraCreateIssueRequest, jira_priority: str):
    description_text = (
        f"Incident text: {request.incident_text}\n\n"
        f"Machine type: {request.machine_type}\n"
        f"Severity hint: {request.severity_hint}\n"
        f"Issue category: {request.issue_category}\n"
        f"Confidence: {request.confidence}\n"
        f"Matched keywords: {', '.join(request.matched_keywords)}\n"
        f"Escalation required: {request.escalation_required}\n"
        f"Recommended next step: {request.recommended_next_step}\n"
        f"Triage summary: {request.triage_summary}\n"
        f"FactoryFlow priority interpretation: {jira_priority}"
    )

    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "text": description_text
                    }
                ]
            }
        ]
    }