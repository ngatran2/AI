---
name: qc-uc-review
description: Reviews a use case (UC) document to determine whether it is ready for test design. Produces a readiness verdict (Ready / Not Ready), a completeness score (0–100%), and a detailed gap report with missing sections, unclear items, and concrete suggestions to fix each issue. Use this skill whenever a user say `review uc`, `review requirement`.
---
# Requirements Readiness Review Skill

## Purpose

Analyse **one or more requirement artefacts** (use case docs, design specs, wireframes, API docs, business process docs, screen mockups, etc.) **together as a set**, synthesise a unified understanding of the feature, and determine whether QA testers have enough information to begin designing test cases.

## Operation Modes
This skill operates in two distinct modes depending on the context:
- **Mode 1: Create Mode (Initial Audit)**: Generates the very first readiness review (`v1`) from raw requirements.
- **Mode 2: Update Mode (Re-Audit)**: Generates subsequent readiness reviews (`v[N+1]`) by incorporating the BA's answers from the Question Backlog.

---

## Mode 1: Create Mode (Initial Audit)

The Create Mode has three phases:

1. **Ingest & Understand** — read all provided artefacts, understand the feature
2. **Audit** — score completeness across all required knowledge areas
3. **Report** — deliver a structured readiness report with verdict, score, gaps, and suggestions

## Supported Artefact Types

Accept any combination of:

| Type                        | Examples                                           |
| --------------------------- | -------------------------------------------------- |
| Requirements / Use Case doc | UC spec, feature brief, BRD, user story            |
| UI Design / Wireframe       | Figma export, mockup image, screen flow PDF        |
| API Specification           | REST API doc, Swagger/OpenAPI, integration spec    |
| Business Process doc        | Workflow diagram, BPMN, process description        |
| Design document             | Technical design, system design, architecture note |
| Other supporting docs       | Data dictionary, error code list, email templates  |

All file formats are supported: plain text, Markdown, PDF, Word (.docx), images (PNG/JPG).

## Phase 1 — Ingest & Understand

### Step 1: Read all artefacts

Read all the common files in the folder `requirements\Common` first.
Read each provided file or pasted content fully before scoring anything.

**Input-type routing:**

| Input type           | Action                                                                                                                                                                                                                                             |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| File path provided   | Read the file using the appropriate tool: Read for `.md`/`.txt`/`docs`; `Skill("pdf", args="<path>")` for `.pdf`; `Skill("document-extraction", args="<path>")` for `.docx`; Read (images are rendered inline) for `.png`/`.jpg` |
| Image file provided  | Use the Read tool — it renders images inline; describe all visible UI elements, labels, states, and flows in detail                                                                                                                               |
| Pasted text provided | Treat as a document; parse directly from the prompt                                                                                                                                                                                                |
> **PDF handling:** Invoke the `pdf` skill via the `Skill` tool to extract text and tables first. Example: `Skill("pdf", args="C:\\path\\to\\file.pdf")`. Do NOT use the Read tool directly on PDF files.

### Step 2: Synthesise a Feature Understanding
After fully comprehending all provided documents and analyzing the design images (including any screen mockups embedded within the specification documents), proceed to synthesize the requirement content according to the following 5 sections:
**1. UI Object Inventory & Mapping (Layout & Forms Analysis)**
Extract and catalog all user interface components based on the Design Mockup/Website and map them correspondingly to the Functional Specification document.
  - **Layout Analysis (Khung giao diện):** Xác định rõ các vùng Header, Footer, Sidebar, và Nội dung chính (Main Content).
  - **Data Display Structure:** Identify the list of data columns, define the pagination limit, default sorting, and Empty state.
  - **Form & Inputs Collection (Trường nhập liệu):** Thu thập toàn bộ `input`, `select`, `textarea`. BẮT BUỘC ghi nhận các HTML attribute gốc như `type` (text, email, password, number), `required`, `maxlength`, `minlength`, `pattern`.
  - **Navigation & Action Components:** Xác định chức năng của từng nút tương tác (Save, Submit, Cancel, Delete, Edit).

**2. Object Attributes & Behavior Definition**
Determine the state and response of each UI object based on specific system conditions.
  - **System States:** Define the default state of the object (Enabled, Disabled, Hidden, Read-only).
  - **Interaction Matrix:** Specify possible actions (Click, Hover) and responses.
  - **UI/UX Feedback (Cảnh báo/Thông báo):** BẮT BUỘC ghi nhận chính xác **nguyên văn 100%** (Verbatim) tất cả Alerts, Toasts, và Validation Messages. Tuyệt đối không được tóm tắt. Nếu có dữ liệu động (Ví dụ: [Mã - Tên]), phải giữ nguyên định dạng ngoặc vuông `[]` để phục vụ Automation Assertion.

**3. System Decomposition & Functional Logic (Phân rã hệ thống & Nghiệp vụ)**
BẮT BUỘC phân rã tính năng phức tạp thành các Module/Sub-module nhỏ trước khi phân tích chi tiết, nhằm tránh việc AI chỉ tập trung vào case chính mà bỏ quên tiểu tiết (VD: 1 danh mục quản lý phải được phân rã rõ thành Flow Xem, Flow Thêm, Flow Sửa, Flow Xóa).
  - **Decomposition (Phân rã):** Liệt kê danh sách các Sub-modules (phân rã theo UI hoặc theo Luồng) và mô tả ngắn gọn chức năng của chúng.
  - **Workflows & Dependencies (Sự phụ thuộc):** Trích xuất rõ luồng công việc và chỉ ra Dependencies giữa các Module (VD: Nút Submit chỉ enable khi đã tích chọn Checkbox).
  - **Main Flow & Alternative Flows:** Happy paths và alternative paths cho TỪNG Sub-module đã phân rã.
  - **Exception & Error Flows:** Scenarios involving system errors or invalid data. BẮT BUỘC phân tích kỹ các điều kiện chặn (Blockers) cho hành động Xóa (Delete) bằng cách tìm kiếm các từ khóa: `session`, `sử dụng`, `liên kết`, `ràng buộc` trong toàn bộ tài liệu.
  - **Business Rules & Validations:** Format constraints, value ranges, and mandatory fields.

**4. Functional Integration Analysis (Ma trận & Tích hợp)**
Analyze and evaluate the linkages and influences between the cataloged functions.
  - **RBAC Matrix (Phân quyền):** Trích xuất ma trận phân quyền rõ ràng cho từng Role (VD: Admin thấy tất cả button, Role View chỉ thấy button View).
  - **Integration Flow (Luồng liên kết màn hình):** Xác định ảnh hưởng của màn hình này đến màn hình khác. BẮT BUỘC kiểm tra: Nếu dữ liệu được thêm mới ở màn A, dữ liệu đó phải xuất hiện trong các Dropdown liên quan ở màn B. Nếu thực thể B xuất hiện trong thông báo lỗi của màn A, phải truy vết mối quan hệ tích hợp giữa chúng.
  - **Data Consistency:** Verify data synchronization across all related UI components.

**5. Traceability, Security & Concurrency Analysis (Bảo mật & Truy vết)**
Xác định các ràng buộc phi chức năng nhưng cực kỳ quan trọng đối với hệ thống quản lý thông tin.
  - **Audit Log Requirements:** BẮT BUỘC kiểm tra xem tài liệu có quy định lưu vết không (Ai tạo, ai sửa, thời gian nào, giá trị cũ/mới). Nếu không có, phải đặt câu hỏi cho BA.
  - **Data Isolation (Bảo mật tầng dữ liệu):** Role A có được xem dữ liệu của Role B không? Có cơ chế "Data masking" (ẩn bớt thông tin nhạy cảm) không?
  - **Concurrency Control (Tranh chấp):** Điều gì xảy ra khi 2 người cùng nhấn "Lưu" trên 1 bản ghi? Hệ thống dùng cơ chế khóa (Locking) hay báo lỗi?

**6. Acceptance Criteria (AC) Synthesis**
Establish the final set of measurement and evaluation standards regarding the completeness of the requirement.
  - Establishing Acceptance Criteria (AC): Categorize and detail the acceptance criteria for each group: Interface (UI), Function, and Integration.

## Phase 2 — Audit

### Knowledge Areas Checklist

Score the **combined artefact set** against these knowledge areas.
A tester needs all of these to design complete test cases.

Mark each as:

- ✅ **Clear** — explicitly stated and unambiguous (full marks)
- ⚠️ **Partial** — present but vague, incomplete, or only inferred (half marks)
- ❌ **Missing** — absent from all provided artefacts (zero marks)

| #   | Knowledge Area                        | Max Pts | Critical? | What to look for                                                                                                                                                                                                                               |
| --- | ------------------------------------- | ------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Feature Identity (title, ID, context) | 5       | Yes       | Is it clear what this feature is and where it fits in the system?                                                                                                                                                                              |
| 2   | Objective & Scope                     | 5      | Yes       | Why does this feature exist? What is in/out of scope?                                                                                                                                                                                          |
| 3   | Actors & User Roles                   | 10      | Yes       | Who triggers the feature? What roles/permissions are involved?                                                                                                                                                                                 |
| 4   | Preconditions & Postconditions        | 10      | Yes       | What must be true before? What is the system state after success?                                                                                                                                                                              |
| 5   | UI Object Inventory & Mapping         | 15      | Yes       | List all user interface components based on the Design Mockup and map them correspondingly to the Functional Specification  document.|
| 6   | Object Attributes & Behavior Definition| 20      | Yes       | Determine the state and response of each UI object based on specific system conditions|
| 7   | Functional Logic & Workflow Decomposition| 20      | Yes       | Analyze in detail the business processes of each function available on the feature screen. Duplicate the block below for each major sub-function (e.g., View List, Create Record).|
| 8   | Functional Integration Analysis       | 10      | Yes       | Analyze and evaluate the linkages and influences between the cataloged functions, acting as an integration check between functions.|
| 9   | Acceptance Criteria                   | 10      | Yes       | Measurable, verifiable pass/fail statements|
| 10   | Non-functional Requirements           | 5       | No        | Performance, compatibility, accessibility                                                                                                                                                                                                      |
| 11   | Audit Log & Traceability              | 10      | Yes       | Is there a requirement to track who created/modified data and when? (Audit trail)                                                                                                                                                              |
| 12   | Security & Concurrency                | 10      | Yes       | Data-level permissions, encryption, and handling of simultaneous data access/edits.                                                                                                                                                            |

**Total: 130 points → Normalise to 100 for the final score.**

**Normalization formula:** `Final Score = round((Raw Score / 130) × 100, 1)`

> Example: Raw score 88 / 110 → Final Score = round((88 / 110) × 100, 1) = **80.0 / 100**
> Example: Raw score 95 / 110 → Final Score = round((95 / 110) × 100, 1) = **86.4 / 100**

**Auto-fail rule:** If any Critical knowledge area scores 0, verdict = NOT READY
regardless of total score.

> **Critical areas** (rows marked "Yes"): Areas #1–#9. If ANY of these score 0, the verdict is automatically NOT READY regardless of total score.
> **Non-critical areas** (rows marked "No"): Areas #10–#12. Scoring 0 here reduces the total but does not trigger auto-fail.

### Cross-Artefact Conflict Check

After scoring, check for **conflicts between artefacts**:

- Does the UC doc describe a flow that contradicts the wireframe?
- Does the API spec define fields not mentioned in requirements?
- Are there UI elements in the design with no corresponding business rule?
- Are labels/field names inconsistent across documents?

List all conflicts found — they are automatic Warnings.

### Blocked Artefact Protocol

If a referenced artefact (wireframe, API spec, supporting doc) is **unavailable or inaccessible**:

- Mark the dependent knowledge area(s) as `[BLOCKED: artefact name not accessible]`
- Score those areas as 0
- Since blocked artefacts almost always affect Critical knowledge areas (#1–#9), surface each blocked area as a 🔴 **Blocker** in the report under the "Blockers" section
- Do NOT infer or assume content from unavailable artefacts


## Phase 3 — Report

> **Template reference:** .agents\skills\qc-uc-review\template\UC_readiness_review_template_v3.md
>
> The report is based on the **UC Readiness Review Template** (`.md`). Open the template file, fill every section based on what was found (or not found) in the provided artefacts, then save the completed `.md` as the report output.
>
> **Status markers used throughout:**
> - ✅ **Complete** — explicitly stated and unambiguous
> - ⚡ **Partial** — present but vague, incomplete, or only inferred (half marks)
> - ⚠️ **Missing** — absent from all provided artefacts (zero marks)
> - *(inferred)* — the reviewer inferred information rather than finding it explicitly; these are candidates for confirmation before test design begins

### 📊 Audit Summary

> **Note:** Knowledge area numbers map to template sections as follows:
> #1 → Section 0 · #2 → Section 1 · #3 → Section 2 · #4 → Section 3 · #5 → Section 4 · #6 → Section 5 · #7 → Section 6 · #8 → Section 7 · #9 → Section 8 · #10 → Section 9 

| #               | Knowledge Area                 | Max Pts       | Score | Status                     |
| --------------- | ------------------------------ | ------------- | ----- | -------------------------- |
| 1               | Feature Identity               | 5             | X/5   | ✅/⚡/⚠️                 |
| 2               | Objective & Scope              | 5             | X/5   | ✅/⚡/⚠️                 |
| 3               | Actors & User Roles            | 10            | X/10  | ✅/⚡/⚠️                 |
| 4               | Preconditions & Postconditions | 10            | X/10  | ✅/⚡/⚠️                 |
| 5               | UI Object Inventory & Mapping  | 15            | X/15  | ✅/⚡/⚠️                 |
| 6               | Object Attributes & Behavior Definition| 20            | X/20  | ✅/⚡/⚠️                 |
| 7               | Functional Logic & Workflow Decomposition| 20            | X/20  | ✅/⚡/⚠️                 |
| 8               | Functional Integration Analysis    | 10            | X/10  | ✅/⚡/⚠️                 |
| 9               | Acceptance Criteria    | 10            | X/10  | ✅/⚡/⚠️                 |
| 10              | Non-functional Requirements    | 5             | X/5   | ✅/⚡/⚠️                 |
| **Total**       |                                | **110**       |       | **XX/110 → XX/100**       |

### 📋 Unified Gap & Question Report
Synthesize all gaps, missing info, warnings, conflicts, and open questions from all analyzed sections into a single comprehensive table for the BA to review. Ensure there is no duplicated content.
| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| *(e.g., Q1)* | *(High / Medium / Low)* | *(Exact excerpt from requirement. Skip if Missing)* | *(Main content to clarify or fix)* | *(Why this is an issue, impact on testability)* | *(Open)* |
- **ID**: ID of the question (e.g., Q1, Q2)
- **Priority**: 
- **High**: Blockers (critical knowledge areas scoring 0, missing critical info).
- **Medium**: Warnings, Cross-artefact conflicts, Partial/Vague details.
- **Low**: Suggestions for improvement, minor open questions.
- **Ref**: Exact excerpt from the requirement that led to this question. If the issue is something completely missing, write "N/A (Missing)".
- **Question**: Clearly state what needs to be answered, provided, or corrected by the BA. Make sure to include the description of the issue as currently found.
- **Why It Matters**: Explain the specific reason for raising this question (e.g., impact on test design, potential bugs, data inconsistency).
- **Status**: Default to "Open".

### 🟢 What's Good

Briefly acknowledge what is well-documented. Give the author credit for what is ✅ Complete.


### 🧪 Testability Outlook

**What CAN be tested now:**

- [Test areas with enough information to start]

**What CANNOT be tested yet (blocked by gaps):**

- [Test areas blocked by ⚠️ Missing or ⚡ Partial sections]

**Suggested test focus areas** *(once gaps are resolved)*:

- Happy path: [based on Section 5. Object Attributes & Behavior Definition
- Alternative scenarios: [based on Section 5. Object Attributes & Behavior Definition]
- Boundary & validation tests: [based on Section 5. Object Attributes & Behavior Definition]
- Error & exception scenarios: [based on Section 5. Object Attributes & Behavior Definition]
- UI-specific checks: [based on Section 5. Object Attributes & Behavior Definition, if design/wireframe was provided]

### 📌 Summary & Recommendation

One paragraph: overall state of the artefact set, key actions required, and a clear recommendation — hold until fixed / fix specific items and proceed / proceed now.

---

## Readiness Thresholds

| Score   | Verdict                           | Meaning                                                              |
| ------- | --------------------------------- | -------------------------------------------------------------------- |
| 90–100 | ✅**READY**                 | QA can begin test design immediately                                 |
| 70–89  | ⚠️**CONDITIONALLY READY** | QA can start on clear areas; flagged items must be fixed in parallel |
| 0–69   | ❌**NOT READY**             | Too many gaps; do not begin test design                              |

**Auto-fail:** Any Critical knowledge area scoring 0 → ❌ NOT READY regardless of total.


## Common Gap Patterns

| Gap Pattern                                  | Impact on Test Design                         |
| -------------------------------------------- | --------------------------------------------- |
| No preconditions stated                      | Tester can't set up test data correctly       |
| Vague actor ("the user")                     | Can't determine which role/permission to test |
| Missing field validation rules               | Can't write boundary value or negative tests  |
| No error messages specified                  | Can't verify error handling behaviour         |
| Acceptance criteria use "should" / "can"     | Not verifiable; can't define pass/fail        |
| Error UI state not described                 | Can't verify UI error behaviour               |
| API error codes not listed                   | Can't verify API error handling               |
| Design shows fields not in requirements      | Ambiguous scope and validation rules          |
| Flows reference other features without links | Can't trace test dependencies                 |


## Output Contract

- **Output path:** `requirements/[UC-ID]/[UC-ID]_[feature-name]_audited_[YYYYMMDD]_v[N].md`
- **Important:** Check the output directory for existing versions. If `v[N].md` exists, increment the version to `v[N+1].md`. Never overwrite existing files.

---

## Mode 2: Update Mode (Re-Audit with BA Answers)

**Trigger:** Execute this mode when the user provides an answered Question Backlog or requests to re-audit an existing Use Case using BA answers (e.g., "update the audited file for UC-VOB-001 based on BA answers").

### Phase 1 — Ingest Current State & Answers
1. Locate the highest version of the audited file at `requirements/[UC-ID]/*_audited_*_v[N].md`.
2. Locate and read the `requirements/[UC-ID]/[UC-ID]_question-backlog.md` file - `Answered Questions` section and `Deferred Questions` section.

### Phase 2 — Apply Answers & Resolve Gaps
1. Analyze the BA's answers in the backlog.
2. Incorporate the clarified business rules, logic, and UI behavior into the 5 synthesis sections (Object Attributes, Workflows, etc.) of the previous audited file.

### Phase 3 — Backlog Maintenance & Re-Audit
1. Recalculate the Readiness Score based on the newly introduced information. Determine the new Readiness verdict (Ready / Conditionally Ready / Not Ready).
2. **Handle Existing Questions:** For any questions where the BA provided a satisfactory answer, update the `[UC-CAT-ID]_question-backlog.md` file to change the status of that question from `Open` to `Resolved`. Move these rows to the "Answered Questions" section table.
3. **Handle New Questions:** If the re-audit reveals *new* conflicts or missing information arising from the BA's answers, immediately call the `qc-ask-ba` skill to append these new questions to the "Open Questions" table of the backlog file.

### Phase 4 — Generate Audited v[N+1]
1. Update the "Unified Gap & Question Report" inside the audited document to reflect the resolved and new questions.
2. Add a "Changelog" at the bottom of the audited document summarizing what rules/answers were integrated.
3. Save the combined updated content as a new file, incrementing the version: `v[N+1].md`. (Never overwrite the `v[N]` version).
