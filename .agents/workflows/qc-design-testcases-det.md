---
description: Generate DETAIL-LEVEL (Full Regression) test cases from an audited requirement document (and optional test scenarios). Use this for comprehensive pre-release QA.
---

# /design-testcases-det — Detail-Level Test Case Generation Workflow

## Purpose

Generate an **exhaustive, step-by-step** set of test cases (30–80+ per UC) covering all 6 Phases, Edge Cases, BVA, RBAC, Decision Tables, and Data Integrity checks. Runs under the `qa-engineer` agent using the `tc-design` skill in **detail-level** mode.

---

## When to Use

| ✅ Use DET When | ❌ Do NOT Use DET When |
| :--- | :--- |
| Pre-release full regression | Quick hotfix validation |
| First-time feature QA | CI/CD pipeline gate (too slow) |
| Compliance/Audit testing | Time-critical smoke test |
| Acceptance testing | Only verifying basic flows |

---

## Pre-flight Check

Before starting, confirm the input type:

### Case A: UI/Function Requirement (Standard)
- [ ] An audited requirement file exists at `requirements/[UC-ID]/[UC-ID]_*_audited_*_v[N].md`
- [ ] The readiness verdict from `uc-review` is **READY** or **CONDITIONALLY READY**
- If the audited file does not exist → STOP. Report: *"Audited requirement not found for [UC-ID]. Please run /review-uc first."*
- If verdict is NOT READY → STOP. Do NOT generate test cases.

### Case B: API Requirement (Swagger/OpenAPI)
- [ ] User provided a Swagger/OpenAPI URL or JSON/YAML file.
- **Action:** If API input is detected, AUTOMATICALLY redirect to `/qc-api-test-gen` workflow.

---

## Step 3B — Generate Detail-Level Test Cases

1. Activate the `qa-engineer` agent.
2. Read the `qc-tc-design` skill from `skills/qc-tc-design/SKILL.md`. Set mode to **`detail-level`**.
3. **MANDATORY:** Read all Common Rule files from `d:\AI\JOYS-V2\requirements\COMMON\` to ensure global behaviors (CMR) are applied.
4. Locate the audited requirement file and the scenarios file (if any). **Always fetch the file with the highest version number**.
5. **Execute Phase 1 (Detailed Drafting):** Create a draft at `testcases/[UC-ID]/[UC-ID]_testcases-det_draft.md`.
   - **ALL sub-steps MANDATORY:**
     - Sub-step A: Feature Decomposition (Text Mindmap)
     - Sub-step B: Risk-Based Assessment (RBT Matrix)
     - Sub-step C: Edge Case Brainstorming
   - **ALL 6 Phases MANDATORY:**
     - Phase 1: Screen Initialization (Static States)
     - Phase 2: Item Interactions (Component States)
     - Phase 3: Core Functional Testing (Logic Analysis) — incl. BVA, Decision Tables, Data Type Integrity
     - Phase 4: Functional Integration
     - Phase 5: UI-Level Non-Functional Testing
     - Phase 6: GUI & Visual Compliance
   - **STRICT V3 STANDARDS:**
     - Use Action Keywords: `[Navigate]`, `[Input]`, `[Click]`, `[Select]`, `[Verify]`.
     - Use Atomic Steps: One action per line.
     - Use State-based ER: `[UI]`, `[API]`, `[DB]`.
     - Explicit Data: No inference, use `{{ }}` for dynamic data.
   - Expand scenarios using specific test data and split atomic tests. Do NOT write Python or Excel scripts here.
6. **Execute Phase 2 & 3 (Self-Review & Traceability Matrix):**
   - Run the Self-Criticism Loop (identify ≥3 weaknesses and fix them).
   - Build the full Requirement Traceability Matrix (Forward + Backward).
   - Ensure 100% AC coverage before proceeding.
7. **Execute Phase 4 (Excel Output):** Write a Python script to populate `skills/tc-design/templates/Testcase_template.xlsx`.
   - Map to **GUI**, **FUNCTION**, or **API** sheets starting from row 2.
   - Use ID format: `TC_[UC-ID]_GUI/FUNC/API_[sequence]_v1.0`.
8. **Version Check & Save:** Check `testcases/[UC-ID]/` for existing `testcases-det` versions. Increment if needed. Save to:
   ```
   testcases/[UC-ID]/[UC-ID]_[feature-name]_testcases-det_[YYYYMMDD]_v[N].xlsx
   ```
9. **Cleanup & Report:** Delete the temporary `_draft.md` file. Provide Output Summary:
   ```
   ## ✅ Detail-Level Test Design Complete

   | Artifact | File | Count |
   |---|---|---|
   | Test Cases (DET) | [filename].xlsx | X cases (Y GUI / Z FUNC) |
   | RTM Report | [filename]_rtm.md | AC coverage: 100% |

   ### Requirement Traceability Matrix
   | AC ID | Acceptance Criteria | Linked Test Cases | Status |
   |---|---|---|---|
   | AC-01 | ... | TC_UC001_GUI_01, TC_UC001_GUI_02 | Covered |

   ### Self-Review Results
   | # | Weakness Found | Action Taken |
   |---|---|---|
   | 1 | ... | ... |
   ```
