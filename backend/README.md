# FactoryFlow Copilot

FactoryFlow Copilot is a hybrid Microsoft AI agent prototype for industrial troubleshooting.

It combines:
- **Microsoft Copilot Studio** for orchestration and document-grounded responses
- a **FastAPI backend** for structured incident triage
- a **REST API tool** integrated into the agent
- a **Siemens S7-1200 manual knowledge source** for document-grounded guidance

## Problem

Industrial troubleshooting often requires both:
1. a likely issue classification based on observed symptoms
2. grounded guidance from technical documentation

In many environments, these two capabilities are fragmented across different tools and documents.

## Solution

FactoryFlow Copilot is a hybrid agent that combines:
- backend-based incident classification
- manual-grounded troubleshooting guidance
- structured response orchestration inside Microsoft Copilot Studio

## Version 1 Capabilities

### Backend triage
The FastAPI backend classifies incident descriptions into categories such as:
- thermal/load anomaly
- mechanical anomaly
- general industrial anomaly

It returns:
- issue category
- possible failure modes
- confidence
- recommended next step
- matched keywords
- escalation signal
- triage summary

### Copilot Studio agent
The Copilot Studio agent:
- uses the Siemens S7-1200 System Manual as a knowledge source
- calls the backend as a REST API tool
- asks for missing required tool inputs
- combines tool output with manual-grounded responses

### Hybrid behavior
FactoryFlow Copilot can answer questions such as:

> “This controller showed overheating and abnormal torque before shutdown. What kind of issue does this resemble, and what should I check in the Siemens S7-1200 manual before attempting a restart?”

## Architecture

```text
User
  ↓
FactoryFlow Orchestrator (Copilot Studio)
  ├── Siemens S7-1200 manual knowledge source
  └── Incident Triage REST API tool
         ↓
      FastAPI backend
         ↓
   structured triage response