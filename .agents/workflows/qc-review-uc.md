---
description: Run full requirement review pipeline — Step 0 (extract from URL) + Step 1 (audit requirement)
---

# /qc-review-uc — Requirement Review Workflow

## Purpose

Trigger the full requirement readiness review pipeline. Handles both URL-based and
local-file-based requirements. Ends with a readiness verdict. Does NOT proceed to test design.

---

## Pre-flight Check

Before starting, confirm:

- [ ] User has provided either a **URL** (Confluence, Jira, Wiki) OR a **local file path**
- [ ] The file format is one of: `.md`, `.pdf`, `.docx`, `.txt` (any format accepted)
- [ ] The UC-CAT-ID is known or can be inferred from the document title

If any of the above is missing, STOP and ask the user before proceeding.

---

## Step 0 — Extract Requirement (URL only)

> Skip this step if the user provided a local file path.

1. Activate the `docs-reader` agent.
2. Read the `document-extraction` skill from `skills/document-extraction/SKILL.md`.
3. Navigate to the provided URL and extract the full content into Markdown. **(Mandate - Lesson 16):** For Google Docs URLs, you MUST use `browser_subagent` to perform a select-all/copy-paste to prevent hidden table data loss. Do not rely solely on standard URL reading.
4. Handle errors per the Error Handling Protocol in the skill (dead links, auth required, etc.).
5. Save extracted content to:
   ```
   requirements/[UC-CAT-ID]/[UC-CAT-ID]_[feature-name]_extracted_[YYYYMMDD]_v[N].md
   ```
6. Report extraction summary to user (section count, any `[UNCLEAR]`/`[MISSING]` markers).
7. Use the extracted file as input for Step 1.

---

## Step 1 — Audit Requirement

1. Activate the `requirement-reviewer` agent. 
2. Read the `qc-uc-review` skill from `skills/qc-uc-review/SKILL.md`.
3. Determine input file:
   - If came from Step 0 → use the `_extracted_*.md` file saved above
   - If user provided a local file → use that file directly
   - If the file is `.pdf` → invoke the `pdf` skill first to extract text, then proceed
4. Run the full 3-phase audit (Ingest → Audit → Report) as defined in the `qc-uc-review` skill.
5. Open the template: `skills/qc-uc-review/template/UC_readiness_review_template_v3.md`
6. Fill all 10 template sections (Sections 0–9) plus supplementary sections (Feature Brief, Audit Summary, Unified Gap & Question Report, What's Good, Testability Outlook, Summary).
7. Save the completed audit report to:
   ```
   requirements/[UC-CAT-ID]/[UC-CAT-ID]_[feature-name]_audited_[YYYYMMDD]_v[N].md
   ```
8. Return the readiness verdict to the user:
   - ✅ **READY** (score 90–100)
   - ⚠️ **CONDITIONALLY READY** (score 70–89)
   - ❌ **NOT READY** (score 0–69 or any critical area scoring 0)

---

## Step 2 — Re-Audit (BA Feedback Iteration)

> Execute this step ONLY when the user provides a Question Backlog file containing BA answers.

1. Activate the `requirement-reviewer` agent.
2. Read the `qc-uc-review` skill.
3. Run the **Mode 2: Update Mode** as defined in the `qc-uc-review` skill.
4. The agent will read the BA's answers and generate the `_audited_v[N+1].md` file.

## Step 3 — Post-Audit Routing

Following the completion of the re-audit and the generation of `_audited_v[N+1].md`:

- **Path A (New Questions Generated):**  
  If the re-audit uncovered new gaps or questions based on the BA's answers, the agent MUST call the `qc-ask-ba` skill to write these new items into the `question-backlog.md`.
  **Action:** STOP the workflow and prompt the user to wait for the BA to answer the newly generated questions.

- **Path B (Ready & No New Questions):**  
  If the re-audit resolves all critical issues, establishes a score > 90 (READY), and 0 new questions are generated:  
  **Action:** Notify the user that the audit is complete with READY status (score > 90, 0 open questions). The user may now invoke `/qc-design-testcases` to begin test case generation.

---

## Output

| Artifact | Path |
|----------|------|
| Extracted requirement (if URL) | `requirements/[UC-CAT-ID]/[UC-CAT-ID]_[feature-name]_extracted_[YYYYMMDD]_v[Highest+1].md` |
| Audit report | `requirements/[UC-CAT-ID]/[UC-CAT-ID]_[feature-name]_audited_[YYYYMMDD]_v[N].md` |
| Question backlog | `requirements/[UC-CAT-ID]/[UC-CAT-ID]_question-backlog.md` |