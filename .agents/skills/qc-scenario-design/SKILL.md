---
name: scenario-design
description: Designs test scenarios from a finalized, reviewed UC (Use Case) requirement document. Trigger this skill whenever the user says "design test scenarios", "build test scenarios", or provides a uc-review output and asks to proceed with testing. Also trigger when the user mentions their requirement is ready and they want to move to QA/test design, even if they don't say "test scenario" explicitly.
---
# Test Scenario Design Skill

## Purpose

Transform a finalized UC requirement (ideally reviewed and approved by `uc-review`) into ready-to-use QA artifacts: **`test_scenarios.md`** — Test scenarios grouped by UC, covering all test types

This skill covers the following test types for **web applications and APIs**:

- Functional Testing
- Integration Testing
- UI Testing
- Functional/End-to-End (E2E) Testing
- Acceptance Testing

## Anti-Hallucination Guardrails (STRICT)

1. **No Guessing:** If the UC document does NOT specify a detail (e.g., exact error message text, field length limit, specific color code), Agent MUST NOT fabricate it. Instead, mark it as `[TBD - Not specified in UC]` in the scenario description. NEVER invent data that is not in the source document.
2. **Cross-reference Mandatory:** Every Test Scenario MUST be traceable back to a specific section in the UC document via the `Req-ID` field. If a scenario is inferred (not directly stated), flag it with `[INFERRED]` in the description.

## Output Files

| Artifact       | Output Path                                                            |
| -------------- | ---------------------------------------------------------------------- |
| Test Scenarios | `scenarios/[UC-ID]/[UC-ID]_[feature-name]_scenarios_[YYYYMMDD].md`   |


## Input

The user will provide one or more of the following (same artefact types as `uc-review`):

- **MANDATORY:** Read all files in `d:\AI\JOYS-V2\requirements\COMMON\` folder first to understand global rules (CMR).
- UC requirement document (Markdown, PDF, Word, plain text)
- The `uc-review` readiness report (the output from the `uc-readiness-review` skill)
- Supporting artefacts: wireframes, API specs, design docs

**Before generating anything**, read all provided documents fully and build a clear understanding of:

- All UC IDs and their names (e.g., `UC-001`, `UC_LOGIN`)
- All functions/features described within each UC
- The main flow, alternative flows, error flows
- All business rules and validations
- Acceptance criteria
- Actors/roles
- Pre and postconditions
- API endpoints and behaviors (if applicable)
- UI states and field behaviors (if applicable)

If the UC ID or function names are not clearly stated in the document, infer them from the
feature name and note your inference clearly. For example: *"UC ID inferred as UC-001 from
document title 'User Login Feature'."*

### MANDATORY Test Design Techniques Application

**CRITICAL RULE:** To guarantee comprehensive coverage and discover edge cases, you MUST forcefully expand requirements using these specific Test Design Techniques during scenario generation:

1. **Equivalence Partitioning (EP) Validation:** 
   - Never bundle valid or invalid inputs into a single scenario if they belong to different partitions.
   - Example: If allowed formats are `.png`, `.jpg`, and `.svg`, create a scenario checking ALL valid extensions independently, and separate scenarios for specific invalid extensions (`.pdf`, `.txt`).
   - Split compound rules into discrete positive/negative scenarios.

2. **Boundary Value Analysis (BVA):**
   - For ANY field with numerical, length, or sizing limits (e.g., max 255 chars, max 1MB), you MUST forcefully generate scenarios mapping exactly to the Boundary (`Limit`), and immediately outside the Boundary (`Limit + 1 unit`, `Limit - 1 unit`).
   - Example: For 255 chars limit, test 1 char, 255 chars, and 256 chars. For a 1MB limit, test 1.00MB exactly, and 1.01MB.

3. **Decision Tables / Combinatorics:**
   - Force matrix-based testing for search filters or multi-variable forms.
   - Example: Create combinations like `Filter A (Valid) + Filter B (Valid)` and `Filter A (Valid) + Filter C (Invalid)`.
   - Never test just one filter in isolation if multiple filters can logically interact on a List layout.
4. **Multi-Role Coverage (RBAC Override - Lesson 17):**
   - For ANY feature involving Create, Update, or Delete (CUD), you MUST forcefully generate scenarios for at least 5 standard roles: **Admin, View, Edit, Delete, Locked**.
   - **EXCEPTION TO "NO GUESSING":** Even if the UC document only explicitly mentions 1 or 2 roles, you MUST still generate scenarios for all 5 standard roles. Infer standard logical restrictions: Role Edit sees and uses Edit/Add (hides Delete/View); Role Delete sees and uses Delete/View (hides Add/Edit); Role Locked cannot log in or perform actions.

Failure to apply these techniques limits the scenarios to simple basic flows. Applying these bounds correctly typically scales valid CRUD feature scenarios upwards of 20-50 detailed variants.

### Traceability & Gap Analysis (MANDATORY)

To guarantee 100% requirement coverage, the Agent MUST perform a Traceability Check before finalizing scenarios:
1. **Mapping:** Map each decomposed Module/Rule to its specific Requirement ID (e.g., REQ-01, REQ-02).
2. **Gap Analysis (Cross-check):** Actively cross-check the original UC document against the generated scenario list to find any "Orphaned Requirements" (requirements with no scenarios) and immediately generate scenarios for them.
3. **5-Pillar Focus:** Ensure the High-Level Scenarios cover: Security/RBAC, UI Validation, Business Logic, Data Integrity, and Error Handling.

### Test Scenario Template

```
### Scenario ID: TS_[UC ID]_[SequenceNo]
**Scenario Title:** [Short, clear description of what is being tested]
**UC Reference:** [UC ID and UC Name]
**Req-ID:** [Requirement ID(s) this scenario traces to — e.g., UC-001-FR-003]
**Test Type:** [Functional | Integration | UI | End-to-End | Acceptance]
**Description:** [One or two sentences describing the scenario — what condition or flow is being verified]
**Test Focus:** [Happy path | Alternative flow | Error/Exception | Boundary | Permission/Role | UI State | API contract]
```

### Scenario Coverage Rules

For each UC, generate scenarios that cover **all of the following** that apply:

| Coverage Area                    | Source in UC                                        |
| -------------------------------- | --------------------------------------------------- |
| Happy path (main flow)           | Main Flow section                                   |
| Each named alternative flow      | Alternative Flows section                           |
| Each error/exception flow        | Exception & Error Flows section                     |
| Each business rule / validation  | Business Rules section                              |
| Boundary value cases             | Any field with min/max/format constraints           |
| Role/permission variations       | Actors & User Roles section                         |
| UI state transitions             | UI/UX Behaviour section (if applicable)             |
| API contract verification        | API / Integration Behaviour section (if applicable) |
| Acceptance criteria verification | Acceptance Criteria section                         |

Do not skip any coverage area just because the UC is brief. If a UC only has a main flow and
two business rules, you still generate scenarios for each. Quality over quantity — each scenario
should represent a meaningfully different test intent.

### Output File: test_scenarios.md

Structure the file like this:

```markdown
# Test Scenarios

> [!WARNING]
> **Human Checkpoint:** User cần review danh sách High-Level Scenarios dưới đây để bổ sung các trường hợp rủi ro đặc thù (nếu có) trước khi Agent tiến hành sinh Test Cases chi tiết ở bước tiếp theo.

## 1. Traceability Matrix & Gap Analysis

| Req-ID | Module / Feature | Covered by Scenarios | Status |
|--------|------------------|----------------------|--------|
| REQ-01 | [Module Name]    | TS_UC01_001, 002     | Covered|

*(List all requirements to prove 100% coverage)*

## 2. Detailed Scenarios

### [UC ID] — [UC Name]

### Scenario ID: TS_[UC ID]_001
**Scenario Title:** ...
**UC Reference:** ...
**Req-ID:** ...
**Test Type:** ...
**Description:** ...
**Test Focus:** ...

### Scenario ID: TS_[UC ID]_002
...

---

## [Next UC ID] — [Next UC Name]

...
```

---

## Output Summary

After generating both files, provide a brief summary:

```
## ✅ Test Design Complete

| Artifact | File | Count |
|---|---|---|
| Test Scenarios | scenarios/[UC-ID]/[UC-ID]_[feature-name]_scenarios_[YYYYMMDD].md | X scenarios across Y UCs |

### Coverage breakdown by test type:
- Functional: X test scenarios
- Integration: X test scenarios
- UI: X test scenarios
- End-to-End: X test scenarios
- Acceptance: X test scenarios

### Notes:
- Any inferred UC IDs or function names
- Any gaps found in the requirements that limited test case generation
- Suggestions for areas to revisit (if applicable)
```

---

## Quality Checks Before Finalizing

**Self-Criticism Loop (MANDATORY):**
Sau khi hoàn thành bộ Scenarios, Agent PHẢI tự đánh giá bằng cách trả lời 3 câu hỏi:
1. Có luồng Negative/Exception nào trong UC mà chưa có Scenario tương ứng không?
2. Có Acceptance Criteria nào chưa được bao phủ bởi bất kỳ Scenario nào không?
3. Có Scenario nào mô tả quá chung chung, vi phạm quy tắc "No Guessing" không?

Agent PHẢI bổ sung hoặc sửa các Scenarios để khắc phục trước khi tiến hành Quality Checks bên dưới.

**Checklist:**
Before writing the final output, verify:

- [ ] Every UC in the requirement has at least one scenario
- [ ] All critical knowledge areas from `uc-review` have corresponding test coverage
  (main flow, alternative flows, error flows, business rules, acceptance criteria)
- [ ] Every test case has a unique ID
- [ ] All test data uses realistic values (not abstract placeholders)
- [ ] Pre-conditions are specific enough that a tester can set up the test independently
- [ ] Expected results are observable and verifiable (not vague like "works correctly")
- [ ] API test cases describe the request and expected response clearly
- [ ] E2E test cases trace the full journey from start to finish

---

## Important Notes

- **Scope**: This skill covers functional, integration, UI, E2E, and acceptance testing only.
- System testing and non-functional testing (performance, security, load) are handled by separate skills.
- **Version**: All new test cases start at `v1.0`. If updating existing test cases,
  the user will specify the new version.
- **Traceability**: Every test case must be traceable back to a UC via its ID. Never generate
  a test case without a clear UC reference.

## Out-of-Scope Handling

When a scenario is identified as performance, security (beyond functional auth checks), or load testing:

1. Do NOT generate test cases for it
2. Add an entry to the `## ⚠️ Out-of-Scope Flags` section at the end of the scenarios file:

```markdown
## ⚠️ Out-of-Scope Flags

| Scenario Area | Reason | Recommended Action |
|--------------|--------|--------------------|
| [Description] | [NFR: PERFORMANCE / SECURITY / LOAD] | Defer to performance/security testing specialist |
```
