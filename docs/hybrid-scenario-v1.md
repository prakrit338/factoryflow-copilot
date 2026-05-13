# FactoryFlow Copilot — Hybrid Scenario V1

## User question
This controller showed overheating and abnormal torque before shutdown. What issue might this be, and what should I check in the Siemens manual?

## Expected system behavior
1. Copilot Studio identifies that the question needs both:
   - incident classification
   - manual-grounded guidance

2. Python backend returns a structured triage result:
   - issue_category
   - possible_failure_modes
   - confidence
   - recommended_next_step
   - needs_manual_lookup

3. Copilot Studio uses the Siemens S7-1200 manual as the document-grounding source.

4. Final response should:
   - mention the likely issue category from the backend
   - stay cautious
   - point the user back to the uploaded Siemens S7-1200 System Manual
   - avoid inventing unsupported manual details

## Goal
Demonstrate the difference between:
- document-grounded answering
- structured backend triage
- hybrid orchestration