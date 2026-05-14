---
description: Generate HIGH-LEVEL (Smoke/Sanity) test cases from an audited requirement document. Use this for quick validation on hotfixes, new builds, or CI/CD gates.
---

# /design-testcases-hl — High-Level Test Case Generation Workflow

## Purpose

Generate a **compact, representative** set of test cases (5–15 per UC) for Smoke/Sanity testing. Covers only Happy Paths + Critical Errors. Runs under the `qa-engineer` agent using the `tc-design` skill in **high-level** mode.

---

## When to Use

| ✅ Use HL When | ❌ Do NOT Use HL When |
| :--- | :--- |
| Hotfix validation | Pre-release full regression |
| Quick build verification | First-time feature QA |
| CI/CD pipeline gate test | Compliance/Audit testing |
| Time-critical smoke test | Edge case exploration needed |

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

## Step 3A — Generate High-Level Test Cases

1. Activate the `qa-engineer` agent.
2. Read the `qc-tc-design` skill from `skills/qc-tc-design/SKILL.md`. Set mode to **`high-level`**.
3. Locate the audited requirement file. **Always fetch the file with the highest version number**.
4. **Execute Simplified Drafting:** Create a draft at `testcases/[UC-ID]/[UC-ID]_testcases-hl_draft.md`.
   - **SKIP** Feature Decomposition Tree, Edge Case Brainstorming, and RBT Matrix.
   - **FOCUS ON:**
     - 1 Happy Path per sub-function (Create, Read, Update, Delete).
     - 1 Critical Error per sub-function (e.g., required field empty, duplicate key).
     - 1 RBAC case (Admin access OK + Unauthorized role blocked).
   - **Standards still apply:** Action Keywords (`[Navigate]`, `[Input]`, `[Click]`, `[Select]`, `[Verify]`), Atomic Steps, State-based ER.
   - **Max case count:** Do NOT exceed 15 test cases per UC.
5. **Quick Traceability Check:** Map each generated TC to at least one AC/BR. Flag any Critical AC not covered.
6. **Excel Output:** Write a Python script to populate `skills/tc-design/templates/Testcase_template.xlsx`.
   - Map to **GUI** and **FUNCTION** sheets starting from row 2.
   - Use ID format: `TC_[UC-ID]_GUI/FUNC_[sequence]_v1.0`.
7. **Version Check & Save:** Check `testcases/[UC-ID]/` for existing `testcases-hl` versions. Increment if needed. Save to:
   ```
   testcases/[UC-ID]/[UC-ID]_[feature-name]_testcases-hl_[YYYYMMDD]_v[N].xlsx
   ```
8. **Cleanup & Report:** Delete the temporary `_draft.md` file. Provide Output Summary:
   ```
   ## ✅ High-Level Test Design Complete

   | Artifact | File | Count |
   |---|---|---|
   | Test Cases (HL) | [filename].xlsx | X cases (Y GUI / Z FUNC) |

   ### Coverage: Happy Path + Critical Error only
   ### ⚠️ Uncovered ACs (deferred to Detail-Level):
   - [List any ACs not covered due to HL scope]
   ```
