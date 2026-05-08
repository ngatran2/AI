# /performance-testing — Performance Test Workflow

## Purpose
Trigger the Performance Testing pipeline to analyze a requirement, generate a comprehensive Performance Test Plan, and optionally provide scripts (JMeter/k6) and Test Data (CSV) for the execution. 

---

## Pre-flight Check

Before starting, confirm:
- [ ] User has provided the target module/UC or an audited requirement file.
- [ ] The scenario/load constraint is known (e.g., 100 concurrent users).

If missing, politely ask the user for the missing parameters.

---

## Step 1 — Analyze and Generate Performance Test Plan

1. Activate the `qa-engineer` (or `performance-tester`) agent.
2. Read the `performance-testing` skill from `skills/performance-testing/SKILL.md`.
3. If an audited requirement file exists for the module, read it to extract:
   - APIs to be tested.
   - Dynamic data constraints (Tokens, OTP, UUIDs).
   - Integration boundaries.
4. Using the template at `skills/performance-testing/template/perf_test_plan_template.md`, generate a complete Performance Test Plan.
5. Save the output plan to:
   ```
   execution/report/[UC-ID]_[feature]_perf-plan_[YYYYMMDD]_v[N].md
   ```

---

## Step 2 — Generate Test Data and Scripts (If required)

1. If the user asks for JMeter or k6 scripts/data, generate the required CSV files.
   - Save the CSV files to `execution/[UC-ID]/scripts/`.
2. Provide script snippets (e.g., Groovy PreProcessors for JMeter, JSON extractors) directly in the chat to help the user configure their tool.
3. For `k6`, generate the full `script.js` file and save it to `execution/[UC-ID]/scripts/`.

---

## Output

| Artifact | Path |
|----------|------|
| Test Plan | `execution/report/[UC-ID]_[feature]_perf-plan_[YYYYMMDD]_v[N].md` |
| Test Data (Optional) | `execution/[UC-ID]/scripts/[feature]_test_data.csv` |
| Script (Optional) | `execution/[UC-ID]/scripts/perf_script.[js/jmx]` |
