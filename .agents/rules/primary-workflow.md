---
trigger: always_on
---

## Primary Pipeline — Strict Sequential Execution

Upon receiving a job request, the AI **MUST** analyze which of the following steps the job belongs to. Once identified, the AI **MUST** act as the `Agent Assigned`, automatically activating the `Primary Skill`, and only use `Supplementary Skills` if truly stuck.

**Sequential enforcement rules:**
- A step MUST NOT begin if the previous step's output file does not exist in its designated output folder
- Agents MUST NOT self-trigger the next step — each step is only started when explicitly invoked
- Agents MUST NOT prompt the user to move to the next step — the user controls pipeline progression
- If a step's required input is missing, STOP and report the missing dependency to the user
- Each agent MUST own distinct files. Overlapping edits are a critical violation — MUST STOP and report immediately.

### Step 0: Requirement Extract
- **Goal:** Extract requirement if the user provide the requirement URL instead of local file
- **Agent Assigned:** `docs-reader`
- **Primary Skill:** `document-extraction`
- **Input:** Requirement URL (e.g. Confluence, Wiki)
- **Output:** `requirements/[UC-ID]/[UC-ID]_[feature-name]_[type]_[date-or-version].md`
- **Important:** If the user provide requirement file instead of an URL, skip this step.

### Step 1: Requirement Audit
- **Goal:** Review and identify inconsistencies/contradictions/missing information in the document.
- **Agent Assigned:** `requirement-reviewer`
- **Primary Skill:** `qc-uc-review`
- **Supplementary Skills (Optional):**
  - `pdf` — activated when the source document is a PDF file, to extract full text/tables before review
  - `qc-ask-ba` - activated after auditing and need the BA to confirm/provide more information.
- **Input:** `requirements/[UC-ID]/[UC-ID]_[feature-name]_[type]_[date-or-version].md` — any format: PDF, DOCX, TXT, MD, XLSX, JSON, etc.
- **Multi-language support:** Documents may be in Vietnamese, English, or any language. Agents MUST read and process content accurately without translation, distortion, or reinterpretation. Preserve all original text, terminology, and formatting exactly as provided.
- **PDF handling:** If the source is a `.pdf` file, invoke the `pdf` skill via the `Skill` tool first to extract its text and tables into readable text. Do NOT attempt to read PDF directly with the `view_file`/`Read` tool.
- **Output:** `requirements/[UC-ID]/[UC-ID]_[feature-name]_audited_[YYYYMMDD]_v[N].md`

### Step 2: Scenario design (Optional)
- **Goal:** Design test scenarios (Happy path, Edge case).
- **Agent Assigned:** `qa-engineer`
- **Primary Skill:** `qc-scenario-design`
- **Supplementary Skills (Optional):** `brainstorming`, `planning`.
- **Input:** `requirements/[UC-ID]/[UC-ID]_[feature-name]_audited_[YYYYMMDD].md`
- **Output:** `scenarios/[UC-ID]/[UC-ID]_[feature-name]_scenarios_[YYYYMMDD].md`

### Step 3A: Test Case Design — High-Level (HL)
- **Goal:** Generate a compact set of representative test cases covering only Happy Paths + Critical Errors. Used for Smoke/Sanity testing on hotfixes or new builds.
- **Agent Assigned:** `qa-engineer`
- **Primary Skill:** `qc-tc-design` (mode: `high-level`)
- **Input:** `requirements/[UC-ID]/[UC-ID]_[feature-name]_audited_[YYYYMMDD].md`
- **Optional Input:** `scenarios/[UC-ID]/[UC-ID]_[feature-name]_scenarios_[YYYYMMDD].md`
- **Output:** `testcases/[UC-ID]/[UC-ID]_[feature-name]_testcases-hl_[YYYYMMDD]_v[N].xlsx`
- **Typical case count:** 5–15 cases per UC.
- **When to use:** Quick validation, regression-lite, CI/CD pipeline gate.

### Step 3B: Test Case Design — Detail-Level (DET)
- **Goal:** Write exhaustive, step-by-step test cases covering all Phases (1–6), Edge Cases, BVA, RBAC, Decision Tables, and Data Integrity checks. Used for full Regression Testing before release.
- **Agent Assigned:** `qa-engineer`
- **Primary Skill:** `qc-tc-design` (mode: `detail-level`)
- **Supplementary Skills (Optional):** `research` (search for sample test schemas).
- **Input:** `requirements/[UC-ID]/[UC-ID]_[feature-name]_audited_[YYYYMMDD].md`
- **Optional Input:** `scenarios/[UC-ID]/[UC-ID]_[feature-name]_scenarios_[YYYYMMDD].md`
- **Output:** `testcases/[UC-ID]/[UC-ID]_[feature-name]_testcases-det_[YYYYMMDD]_v[N].xlsx`
- **Typical case count:** 30–80+ cases per UC.
- **When to use:** Full regression, pre-release QA, acceptance testing.

> **Important:** Step 3A and Step 3B are **independent paths**. The user chooses ONE per invocation. They do NOT depend on each other (HL does NOT require DET to exist, and vice versa). Both require Step 1 output.

### Step 4: Execute Test Cases (Manual/Automation)
- **Goal:** Act as a tester to execute test cases via browser or manual operations.
- **Agent Assigned:** `quality-control`
- **Primary Skill:** `test-execution`
- **Supplementary Skills (Optional):** `mcp-management` (for taking screenshots, UI operations).
- **Input:** `testcases/[UC-ID]/[UC-ID]_[feature-name]_testcases-{hl|det}_[YYYYMMDD]_v[N].xlsx`
- **Output:** `execution/[UC-ID]/reports/res_[UC-ID]_[feature-name]_testcases-{hl|det}_res_[YYYYMMDD]_v[N].xlsx`
- **Note:** Execution accepts EITHER HL or DET test case files. The execution report inherits the same level suffix.

---

## Agent & Skill Overview

| Agent                  | Role                              | Primary Skill      |
| :--------------------- | :-------------------------------- | :----------------- |
| `docs-reader         ` | Extract requirement from Confluence, Wiki      | `document-extraction`        |
| `requirement-reviewer` | Audit requirement documents       | `uc-review`        |
| `qa-engineer`          | Design scenarios & test cases     | `scenario-design`, `tc-design (hl \| det)` |
| `quality-control`      | Execute test cases & reporting    | `test-execution`   |

| Skill           | Purpose                                                | Used In          |
| :-------------- | :----------------------------------------------------- | :--------------- |
| `document-extraction`| Extract requirement                              | Step 0 (URL only)|
| `qc-uc-review`  | Readiness audit (completeness, clarity, consistency)   | Step 1           |
| `pdf`           | Extract text/tables from PDF files                     | Step 1 (PDF only)|
| `qc-scenario-design`| Scenario design                                   | Step 2       |
| `qc-tc-design (hl)` | High-level test case design (Smoke/Sanity)        | Step 3A     |
| `qc-tc-design (det)`| Detail-level test case design (Full Regression)   | Step 3B     |
| `qc-ask-ba`     | Transfer open questions from audit report to BA backlog | Step 1 (post-audit) |
| `test-execution` | Execute test cases, generate reports, capture evidence | Step 4      |

## Pipeline Diagram

```
docs-reader ← user provides requirement link (skip this step if the provided requirement is a local file)
     │
     ▼
requirements/    ← user provides requirement document (any format)
         │
         ▼  [if PDF] ──── pdf skill
         │                │
         │                ▼
         └──── requirement-reviewer ──→ requirements/[UC-ID]/
                                            │
                                            ▼  [Gateway: NOT READY → STOP]
                                            │
                                            ▼  qa-engineer ──→ scenarios/[UC-ID]/ (Optional)
                                            │                           │
                                            └───────────────────────────┤
                                                                        │
                                                              ┌─────────┴─────────┐
                                                              │                   │
                                                     [Step 3A: HL]       [Step 3B: DET]
                                                              │                   │
                                                    testcases-hl/       testcases-det/
                                                              │                   │
                                                              └─────────┬─────────┘
                                                                        │
                                                                        ▼  [Gateway: NOT READY → STOP]
                                                                        │
                                                               quality-control ──→ execution/[UC-ID]/
```

---

## Re-run & Recovery Protocol

The following rules apply whenever a step output is rejected or needs to be revised.

### Rule 1 — Never overwrite outputs
If an output (any file matching `*_v[N].*`) needs to be revised, the agent MUST
create a new version (`vN+1`) and leave the original intact.

### Rule 2 — Amendment Protocol (Step 1 re-run)
If the user provides an amended requirement document after the audit:
1. The `requirement-reviewer` MUST re-run the full `uc-review` skill on the amended document.
2. Output MUST be saved as a new dated file (not overwrite the previous `_audited_*.md`).
3. The agent MUST explicitly note what changed vs the previous audit in the Executive Summary.

### Rule 3 — Partial completion
If a step is interrupted mid-execution:
1. Do NOT save a partial output file.
2. Re-run the step from the beginning when resumed.
3. Report to user which step was interrupted and what input is needed to resume.

### Rule 4 — Input rejection
If the user explicitly rejects an output (e.g., "this audit is wrong"):
1. Ask the user to specify which section(s) are incorrect.
2. Do NOT self-revise without explicit user guidance.
3. Once corrections are received, produce a new versioned file.

### Rule 6 — Master Dashboard Update Frequency
The `PROJECT_MASTER_DASHBOARD` MUST be updated at the end of each significant work day or after a major milestone (e.g., completing an execution cycle for a UC). 
- It MUST NOT be updated for every single minor task to avoid version clutter.
- The latest version ALWAYS serves as the single source of truth for project health and progress.
- Updates MUST be saved as a new versioned file (e.g., `v7` → `v8`).