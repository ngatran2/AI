---
trigger: manual
---

##Common
- SKIP all other knowledge, histories that not stored in this project.
- If there is any ambiguity in the user's prompt, DO NOT attempt to guess; HAVE TO ask the user for clarification to obtain complete information.

## Language & Communication
- Communication language: Vietnamese is the default language for all exchanges, reports, and explanations.
- All outputs MUST be written in **English**.
- All skill/workflow/agent.md files MUST be written in English.
- All labels/messages MUST be kept in their original language (e.g., Korean, Vietnamese) and annotated with the English translation in parentheses.

## File & Naming Standards

- All output files MUST follow the naming convention defined in `rules/naming-convention.md`.
- NEVER overwrite a file. Create a new version instead (`v1`, `v2`, etc.).
- All files MUST include a header with: document title, date created, author/agent name, and version.

## Output Quality Standards

- Every output MUST be **evidence-based** — cite sources, reference specific sections of requirements.
- NEVER fabricate data, make up statistics, or assume requirements that are not documented.
- When uncertain, MUST explicitly state the uncertainty and ask the user for clarification.
- **Quality Gate Mandate:** All test executions (Automation/Manual) MUST pass the "Antigravity Quality Gate" audit as defined in the `test-execution` skill. No execution report is considered valid without a Reliability Score >= 95%.

## Agent Boundaries

- Each agent MUST focus **strictly** on its own responsibilities.
- An agent must NEVER perform tasks assigned to another agent's role.
- When an agent needs input from another agent, it MUST reference the appropriate output file in `requirements/` or `testcases/` — NEVER redo the work.

## Workflow Compliance

- All agents operating in the primary pipeline MUST adhere to rules/primary-workflow.md.

## Error Handling

- If an agent encounters an error or ambiguity, it MUST stop and report to the user.
- Do not make assumptions to "fill gaps" in requirements or documents.
- The Agent MUST log all issues, conflicts, or missing information in the output report.

## Security & Privacy
- Data Security: NEVER share sensitive data (PII, passwords, proprietary code) with public models.
- NEVER store production passwords or sensitive credentials in any output file.