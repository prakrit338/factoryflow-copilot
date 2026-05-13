# FactoryFlow Copilot — Hybrid Answer Template V1

## Purpose
Define the structure of the first hybrid response that combines backend triage and manual-grounded guidance.

## Hybrid answer structure
1. Likely issue category
2. Confidence and caution
3. Recommended next step
4. Manual-grounded guidance
5. Safe fallback if the manual does not verify the action

## Example answer
Based on the described symptoms, this appears to be a possible thermal/load anomaly.

Confidence: medium. This is an initial triage assessment based on the incident description and should be verified before action is taken.

Recommended next step: review diagnostics guidance and inspect for overheating-related conditions before restart.

From the uploaded Siemens S7-1200 System Manual, the correct document to consult first is the Siemens S7-1200 System Manual itself. Use it as the primary source for system-related troubleshooting. If the manual does not clearly verify the required action, do not assume a safe maintenance step and consult a qualified engineer.