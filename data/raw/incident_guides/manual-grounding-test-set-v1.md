# FactoryFlow Copilot — Manual Grounding Test Set V1

## Goal
Test whether the agent answers grounded questions using the uploaded Siemens manual.

## Test Questions

1. What kind of document are you using to answer my questions?
2. I am troubleshooting an industrial controller issue. Which manual should I consult first?
3. Can you help me find information related to diagnostics in the Siemens S7-1200 manual?
4. What should I check before taking a safety-critical maintenance action?
5. If I am unsure about a controller-related issue, how should I proceed?
6. Does the documentation suggest a cautious approach when the answer is uncertain?
7. Can you point me toward the most relevant technical source for PLC troubleshooting?
8. What kind of guidance can this manual help with?
9. Should I rely on undocumented assumptions for maintenance actions?
10. If the manual does not clearly support an answer, what should you tell me?

## What a good answer should look like
- grounded in the uploaded Siemens manual
- cautious when uncertain
- no invented machine states or values
- professional tone
- suggests checking official documentation or consulting a qualified engineer when needed