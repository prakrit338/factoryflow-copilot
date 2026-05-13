# FactoryFlow Copilot — Hybrid Evaluation V1

## Goal
Evaluate whether the agent can combine:
1. backend incident triage
2. Siemens manual-grounded guidance

## Test Case 1 — Hybrid thermal question
Prompt:
This controller showed overheating and abnormal torque before shutdown. What kind of issue does this resemble, and what should I check in the Siemens S7-1200 manual before attempting a restart?

Expected qualities:
- identifies possible thermal/load anomaly
- gives a reasonable next step
- uses the Siemens manual as a source
- stays cautious if the manual does not explicitly verify detailed thermal procedures

## Evaluation notes
- Tool invocation observed: yes
- Manual grounding observed: yes
- Overconfidence risk: medium
- Overall result: good first hybrid response