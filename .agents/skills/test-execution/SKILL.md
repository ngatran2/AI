---
name: test-execution
description: Executes test cases (manual or automated) against a target environment, generates execution reports with pass/fail results, and captures failure evidence. Trigger this skill whenever the user says "execute test cases", "run tests", or "chạy test".
---
# Skill: Enterprise Test Execution (Dispatcher)

**WARNING: THIS IS A MODULAR SKILL.** 
Kiến thức của bạn đã được chia nhỏ theo chuẩn Domain-Driven Design (Core, Automation, Governance, Integration) để tối ưu hóa context window.
Bạn **KHÔNG THỂ** bắt đầu chạy test nếu chưa đọc các module.

## Layered Skill Loading Protocol (Giao thức Nạp Kiến thức)

BẠN BẮT BUỘC PHẢI sử dụng công cụ `view_file` để đọc nội dung các file module nằm trong thư mục `.agents/skills/test-execution/` trước khi thực hiện task. Tùy thuộc vào yêu cầu của User và Risk Level khai báo ở Step 4 (Primary Workflow), hãy nạp module theo các bước sau:

### BƯỚC 1: ORCHESTRATION (Luôn phải đọc đầu tiên)
- Đọc file: `.agents/skills/test-execution/core/execution-core.md` (Chứa chiến lược điều phối và Risk-based Validation Depth).
- Đọc file: `.agents/skills/test-execution/core/readiness-audit.md` (Chấm điểm ERA, gatekeeper trước khi chạy).

### BƯỚC 2: AUTOMATION ENGINE (Đọc nếu task yêu cầu thao tác UI/Playwright)
- Đọc file: `.agents/skills/test-execution/automation/playwright-standard.md` (Luật viết POM, Deterministic Locators, State Inheritance).
- Đọc file: `.agents/skills/test-execution/automation/stability-engine.md` (Bí kíp chống Flaky test, dọn rác bộ nhớ, tiết kiệm RAM).

### BƯỚC 3: DATA GOVERNANCE (Đọc nếu chạy High/Critical Risk có verify DB)
- Đọc file: `.agents/skills/test-execution/governance/db-governance.md` (Triết lý thao tác Database, cấm SQL injection, check Integrity). 
- *Lưu ý:* Nếu User chỉ yêu cầu test UI/API-only (Low/Medium risk) -> BỎ QUA file này.

### BƯỚC 4: AUDIT & REPORTING (Đọc khi cần đánh giá kết quả & xuất báo cáo)
- Đọc file: `.agents/skills/test-execution/governance/rca-and-quality.md` (Phân loại RCA, đánh giá Leakage L1-L4 và kích hoạt cổng bảo vệ Quality Gate).
- Đọc file: `.agents/skills/test-execution/governance/reporting-format.md` (Quy chuẩn in kết quả vào Excel, bắt buộc có Execution Metadata).

### BƯỚC 5: JIRA INTEGRATION (Đọc nếu User có task liên quan đến Bug/Jira)
- Đọc file: `.agents/skills/test-execution/integration/jira-hook.md`.

> **Note:** Bạn phải tuân thủ nghiêm ngặt các quy tắc bất biến (Global Invariants) nằm ở `.agents/rules/qa_global_invariants.md` và hệ thống thuật ngữ nằm ở `.agents/rules/qa_shared_terms.md`.
