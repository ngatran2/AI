---
description: Generate test scenarios from an audited requirement document
---

# /design-scenarios — Test Scenario Generation Workflow

## Purpose

Trigger the test scenario design pipeline for a given UC. Takes an audited requirement file as input and produces high-level test scenarios (`.md`). Runs under the `qa-engineer` agent using the `scenario-design` skill.

---

## Pre-flight Check

Before starting, confirm:

- [ ] An audited requirement file exists at `requirements/[UC-ID]/[UC-ID]_*_audited_*_v[N].md`
- [ ] The readiness verdict from `uc-review` is **READY** or **CONDITIONALLY READY**
- [ ] If CONDITIONALLY READY: user has explicitly approved proceeding despite open warnings

If the audited file does not exist → STOP. Report: *"Audited requirement not found for [UC-ID].
Please run /review-uc first."*

---

## Step 2 — Generate Test Scenarios

1. Activate the `qa-engineer` agent.
2. Read the `qc-scenario-design` skill from `skills/qc-scenario-design/SKILL.md`.
3. **MANDATORY:** Read all Common Rule files from `d:\AI\JOYS-V2\requirements\COMMON\` to ensure global UI/System behaviors are incorporated into scenarios.
4. Read the audited requirement file:
   ```
   requirements/[UC-ID]/[UC-ID]_[feature-name]_audited_[YYYYMMDD].md
   ```
4. Build a full understanding of: UC IDs, main flows, alternative flows, error flows,
   business rules, acceptance criteria, actors, pre/postconditions, UI states, API behaviour.
5. Generate test scenarios covering **all** applicable coverage areas:
   - Happy path (main flow)
   - Each named alternative flow
   - Each error/exception flow
   - Each business rule / validation
   - Boundary value cases (min/max/format)
   - Role/permission variations
   - UI state transitions (if applicable)
   - API contract verification (if applicable)
   - Acceptance criteria verification
6. Save the scenarios file to:
   ```
   scenarios/[UC-ID]/[UC-ID]_[feature-name]_scenarios_[YYYYMMDD].md
   ```
7. Present the scenario file to the user.