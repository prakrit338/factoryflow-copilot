# FactoryFlow Copilot — API Flow V1

## Purpose
Explain how Copilot Studio will later communicate with the Python backend.

## Core idea
Copilot Studio handles the user conversation and orchestrates capabilities.
Python backend handles structured custom logic.
An API is the bridge between them.

## Example flow
1. User asks an incident-related question.
2. Copilot Studio decides whether a backend tool is needed.
3. Copilot Studio sends a request to the Python API.
4. Python returns a structured JSON response.
5. Copilot Studio combines the backend result with knowledge-based answers if needed.
6. Final answer is shown to the user.

## Three paths
- Knowledge-only path
- Tool/API-only path
- Hybrid path

## Current status
- Knowledge layer is being prepared in Copilot Studio
- Backend contract has been designed
- API connection will be implemented later