# /execute-testcases — Test Case Execution Workflow

## Purpose

Trigger the test case execution pipeline for a given UC. Takes a test case Excel file as input, executes them against the target environment, and produces execution reports with pass/fail results. Runs under the `quality-control` agent using the `test-execution` skill.

---

## Pre-flight Check

Before starting, confirm:

- [ ] An Excel test case file exists at `testcases/[UC-ID]/`
- [ ] The automation script exists at `scripts/automation/` (if automated execution)
- [ ] **Lesson 8.1:** After restoring `storage_state`, the script MUST call `await page.goto(BASE_URL)` + `wait_for_load_state('networkidle')` before any interaction.
- [ ] **Lesson 8.2:** Do NOT create a new context per test case. Create ONE context per Role group and run all cases for that role sequentially on the same page.
- [ ] **Lesson 11 (Purpose-Based Groups):** Organize test cases into GROUPs by test purpose, NOT by role:
  - `GROUP_LIST` → data loading & pagination
  - `GROUP_SEARCH` → all search sub-cases share ONE page; FUNC_04 inherits the filter state left by FUNC_03
  - `GROUP_RBAC` → role-specific checks get a separate context
  - Each group's `setup` navigates to the module exactly **once**.
- [ ] **POM Lesson 11 & 12:** Every `navigate_to_module()` MUST call `page.wait_for_selector(".chakra-sidebar", state="visible", timeout=20000)` and attempt **Direct-First Navigation**.
- [ ] **RBAC Safe-catch (Lesson 12):** Orchestrator MUST use try-except blocks around role context groups.
- [ ] **Reporting Integrity (Lesson 13):** Script reporting function BẮT BUỘC có logic **Header Injection** và **ID Sanitization**.

If the test case file does not exist → STOP. Report: *"Test case file not found for [UC-ID]. Please run /qc-design-testcases first."*

---

## Step 0 — Execution Readiness Audit (Mandatory Gate)

1. Activate the `quality-control` agent.
2. Read the `test-execution` skill from `skills/test-execution/SKILL.md`.
3. **Evaluate Test Suite:** Audit the provided test cases against the **ERA rubric** in `SKILL.md`.
4. **Generate Verdict:** Output the Execution Readiness Verdict table.
5. **Gatekeeper Logic:**
   - If Verdict is ✅ **READY** or ⚠️ **CONDITIONALLY READY** → Continue to Step 1.
   - If Verdict is ❌ **NOT READY** → STOP, report gaps, and wait for user revision.

---

## Step 1 — Reference Initialization & Planning

### Step 1a: Reference Initialization (Mandatory)
1. **Load Config:** Read `.agents/config/project-config.md` to identify environment settings and test accounts.
2. **Load Rules:** Read `.agents/rules/qa_lessons_learned.md` for technical safeguards.
3. **Common Rules:** Read any system reference files in `report/analyze_requirements/CommonRules/` to understand module dependencies.

### Step 1b: Analyze & Plan
1. **Read Test Cases:** Open and parse the provided test suite (Excel).
2. **Selective Execution Logic:**
   - Verify if a previous execution report exists for the current module in `execution/[UC-ID]/`.
   - 💡 If a report exists, filter and target only those test cases with status **Failed**, **Blocked**, or **Not Run**.
3. **Resource Mapping:** Identify the specific accounts and data objects needed for these cases.

---

## Step 2 — Resource Readiness

1. **Environment Verification:** Confirm the target environment (Dev/QA/Staging) is reachable.
2. **Account Validation:** Ensure the required role credentials are valid.
3. **Proactive Data Preparation:** If specific records are missing for a test case (e.g., an item to delete), attempt to create them via API or UI.
4. **MCP Data Pre-check (if MCP configured):** When MCP Database Server is available (see `project-config.md` Section 10), Agent MAY query DB to verify pre-condition data exists before execution. This replaces UI-scanning for data validation.
5. **Blocker Communication:** If data cannot be created automatically, inform the user and request manual preparation before proceeding.

---

## Step 3 — Precise Execution

1. **Multi-Role Interaction:** Execute test cases using the specified roles, ensuring correct permission boundaries are tested.
2. **DOM Recon & Snapshot (Accessibility Tree):** Tuyệt đối không để script đoán mò locator. Bắt elements qua Accessibility Tree (Role/Text/ID) sử dụng quy tắc mạnh mẽ Web-first Assertions của Playwright.
3. **Navigation Guard:** Always navigate through the application (Dashboard -> Menu -> Sub-menu) to confirm UI consistency.
4. **Self-Healing & Flaky Test Model:**
   - Sử dụng quy trình Self-Healing Logic: Chạy Script -> (Trường hợp Element Not Found) -> Agent tự động phân tích log lỗi, mường tượng DOM hiện tại và tự thay thế Locator chết, đồng thời inject thêm Script Fallback dự phòng.
5. **Resilience & Validation:** Apply "Skeleton Wait" and "Search Latency" rules. Validate every input visually on the UI using Context Assertions.

---

## Step 4 — Reporting & Closure

1. **Version Check:** ALWAYS check the `execution/[UC-ID]/` directory first. If previous result versions exist, increment the version (e.g., `v1` becomes `v2`). Never overwrite existing files.
2. **Excel Report Update:** Save a versioned copy of the test case file to:
   ```
   execution/[UC-ID]/reports/res_[UC-ID]_[feature-name]_testcases_res_[YYYYMMDD]_v[N].xlsx
   ```
3. **Quality Logging:**
   - Update `GUI` and `FUNCTION` sheets with Status, Actual Result, and Bug ID.
   - For every failure, provide a detailed 12-column entry in the `Bug report` sheet.
4. **Evidence Capture:** Store all failure screenshots in `report/Image/{Module}/{TestFileName}/`.
5. **Log Extraction (if MCP configured):** On FAIL/ERROR, Agent MAY use MCP to extract system logs (Trace ID, Error Stack) and attach to Bug Report Evidence column. Logs stored at `report/Logs/{Module}/{TC-ID}_[Timestamp].log`.
6. **Output Summary:** Provide a summary with pass/fail counts, blocked items, and any re-test recommendations.
