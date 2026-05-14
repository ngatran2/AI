---
name: test-execution
description: Executes test cases (manual or automated) against a target environment, generates execution reports with pass/fail results, and captures failure evidence. Trigger this skill whenever the user says "execute test cases", "run tests", or "chạy test".
---
# Skill: Unified Test Execution (Master Standard)

This document represents the absolute technical and operational source of truth for the Test Executor (Quality Control Agent).

## 1. Execution Readiness Audit (ERA)

- **Objective:** Before execution, the Agent acting as a pre-execution gatekeeper MUST audit the test suite to ensure it is executable and accurate.
- **Scoring Rubric (Total: 100 points):**
    - **Prerequisites (25 pts):** Are all URLs, roles, and initial data clearly defined?
    - **Account Alignment (25 pts):** Do the roles in the test case match `project-config.md` 1:1?
    - **Step Clarity (30 pts):** Are steps atomic, logical, and have clear expected results?
    - **Data Precision (20 pts):** Is the test data specific and valid?
- **Verdict Thresholds:**
    - **90-100:** ✅ **READY** (Proceed).
    - **70-89:** ⚠️ **CONDITIONALLY READY** (Proceed, but list gaps).
    - **< 70:** ❌ **NOT READY** (STOP and request revision).
- **Output Format (Mandatory):**
### Execution Readiness Verdict
| Metric | Score | Notes |
| :--- | :--- | :--- |
| Prerequisites | X/25 | ... |
| Account Alignment | X/25 | ... |
| Step Clarity | X/30 | ... |
| Data Precision | X/20 | ... |
| **Overall Score** | **XX / 100** | **[VERDICT]** |

## 2. Persona & Mindset (Senior QC)

- **Role:** Senior Test Execution Manager.
- **Mindset:** "Shift-left" (pre-execution verification), "Risk-based" (immediate blocking of dependent flows), and "Self-healing" (auto-recovery from locator failures).
- **Dynamic Data Strategy (Linked Data Rule):** 
    - **Priority:** Always attempt to use the ID (e.g., `PCM001`) created in previous linked steps.
    - **Self-Healing:** If the target ID does not exist (due to a previous failure), Agent **MUST** scan the current list on UI to suggest/select an alternative valid record and continue testing instead of blocking the entire flow.

## 3. Technical POM & Automation Standards (Playwright)

- **POM Architecture:** All interactions via `scripts/automation/pages/`.
    - **Constructor:** Define all locators as properties.
    - **Assertion Boundary:** Assertions (assert/expect) CHỈ được đặt trong Test classes/files. KHÔNG đặt assertions bên trong Page classes — Page classes chỉ chứa locators và interaction methods.
    - **Web-first Locators & Accessibility Tree ("Snapshot" principle):** Phải ưu tiên bắt phần tử qua ngữ nghĩa Accessibility Tree (Role/Text/ID) bằng `getByRole`, `getByLabel`. KHÔNG dính líu giao diện thị giác cứng nhắc. Khẳng định Automation test "sống dai" là nhờ bắt trúng Ngữ Nghĩa chứ không phải ảnh pixel. Tốc độ và sự mạnh mẽ đến từ Playwright Web-first Assertions.
    - **DOM Recon First:** Bắt buộc mở trình duyệt lấy bản chất DOM thật (Snapshot) thay vì đoán selector từ requirement. Không được vi phạm Strict Mode.
    - **Strict Mode Resolution:** Always prioritize `.get_by_role()` or `.first` to prevent locator collisions. **Tuy nhiên (Lesson 9 - UI Multi-layer Mismatch)**: Với các bộ lọc hoặc thẻ UI nhỏ lẻ (như "Đặt lại bộ lọc"), TRÁNH hardcode `.get_by_role('button')` vì Frontend thường code bằng thẻ `<span>` hoặc `<a>`. Bắt buộc dùng `page.locator("text=Đặt lại bộ lọc")` ở phạm vi component cha.
    - **Locator Blacklist (NGHIÊM CẤM):** Tuyệt đối không sử dụng:
        - CSS class name động / hash tạm thời (e.g., `css-1n2xyz-btn`)
        - Chuỗi `nth-child`, `nth-of-type` khi có lựa chọn semantic tốt hơn
        - ID tự sinh bởi framework (auto-generated IDs)
        - XPath tuyệt đối dựa trên vị trí (e.g., `//div[3]/div[2]/form/button`)
    - **Self-Healing Logic (Triết lý Tự Phục Hồi):** Khi xảy ra Element Not Found, Agent tự động kích hoạt quy trình chẩn đoán nội bộ: Phân tích log lỗi chập chờn -> Mường tượng DOM (Snapshot) hiện tại -> Tự động rà quét và chẩn đoán thay thế Locator bị chết, đồng thời sinh kịch bản "Fallback" dự phòng miễn nhiễm thay đổi Frontend.
- **Dynamic Elements (JS injection):** Use `page.evaluate()` to identify elements in tables/lists by text content to prevent index-shift errors.
- **Synchronization Guards:**
    - Wait for `.chakra-skeleton` to be `hidden`.
    - Wait 2s after Search/Filter before assertion.
    - **Chakra UI Spinner Polling (Lesson 2):** Use `await page.wait_for_selector('.chakra-spinner', state='visible', timeout=2000)` instantly after submit actions to handle quick popovers. Use `force=True` on deep icons.
    - **Success Branching & Navigation Detection (Lesson 12 Harden):** 
        1. **URL Departure Sync:** Loop check for URL departure from `/login` for max resilience. 
        2. **Direct-First Navigation:** To move to a sub-module, attempt to click the sub-menu item directly with a short timeout FIRST. Only toggle parents if the direct click fails.
        3. **RBAC Recovery:** Wrap role execution blocks in try-except to preserve session states and reporting integrity even if one role's sync fails.
    - **Verification:** Check for `Toast Message`, `URL Change`, OR specific `Page Title` (e.g. "Nhập mã xác thực" for 2FA screens) in parallel to confirm action success.
    - **Poll for Fleetings:** For loading indicators or dynamic UI states, use short-timeout `wait_for_selector` (polling) instead of static sleeps.
- **2FA/OTP Automation:** 
    - Generate via `pyotp.TOTP(secret_key).now()`.
    - **Guard:** Clear input, type, and verify value on UI. Retry **once** if value is empty.
    - **Error:** If it fails, log "OTP Authentication Failed for Role [Name]".
- **Context Reuse (Session Sharing) cho các Test cases (Lesson 8):**
    - **Save State:** Tại test case đầu tiên của một Role, script BẮT BUỘC gọi `await context.storage_state(path=f"state_{role}.json")` sau khi login thành công.
    - **Load State:** Ở các test case tiếp tục cùng Role, dùng `browser.new_context(storage_state=f"state_{role}.json")` để nhảy thẳng vào hệ thống, bỏ qua hoàn toàn bước nhập User/Pass/2FA.
    - **Lesson 8.1 (Navigation Boot):** After `storage_state` restore, browser opens `about:blank`. MUST call `await page.goto(BASE_URL)` + `wait_for_load_state('networkidle')` before any locator interaction.
    - **Lesson 8.2 (One Context Per Role Block — Hiệu năng tối đa):** 
    - **Nguyên tắc:** KHÔNG tạo `new_context()` hay `new_page()` cho mỗi test case.
    - **Thực thi:** Tạo MỘT context duy nhất cho toàn bộ nhóm cases cùng Role/Module. Giữ nguyên Page đó để chạy tuần tự từ FUNC_01 đến FUNC_n. 
    - **Lợi ích:** Tránh việc trình duyệt tắt/mở liên tục gây lag máy và lỗi "bật nhiều Chrome". Chỉ đóng context khi chuyển sang Role khác hoặc Module hoàn toàn khác.
- **Lesson 11 — Purpose-Based Group Execution & State Inheritance (BẮT BUỘC):**
    - **Nguyên tắc Serial:** Tuyệt đối KHÔNG chạy song song (Parallel). Sử dụng `workers: 1` để đảm bảo chỉ có 1 session duy nhất tại một thời điểm.
    - **Mục tiêu:** Chạy tuần tự các case trong cùng nhóm (Tìm kiếm, Lọc, CRUD) trên cùng một trang hiện hành.
    - **State Inheritance (Kế thừa trạng thái):** Các sub-cases trong cùng GROUP **không gọi lại `goto(BASE_URL)` hay Refresh page**.
        - Ví dụ: FUNC_03 thực hiện lọc Mã = 'A'. FUNC_04 sẽ bắt đầu ngay trên kết quả đó để lọc tiếp Tên = 'B' (kiểm tra tìm kiếm kết hợp AND).
        - Chỉ reset/navigate lại khi cần xóa sạch dữ liệu để thực hiện một luồng nghiệp vụ mới hoàn toàn.
    - **GROUP Templates:**
        - `GROUP_LIST`: Load danh sách + phân trang
        - `GROUP_SEARCH`: Tìm kiếm đơn, kết hợp, rỗng, UI controls (cộng dồn filter)
        - `GROUP_RBAC`: Kiểm tra quyền (mỗi Role cần context riêng)
    - **POM Constraint:** `navigate_to_module()` BẮT BUỘC gọi `page.wait_for_selector("text=[Sidebar Label]", state="visible", timeout=20000)` trước khi click, tránh timeout sau session restore.

## 4. Mandatory Action Constraints

- **Navigation Guard:** Navigate ONLY via UI. Verify final URL.
- **Input Verification (Verify-after-Type):** Get value after typing. If empty, retry **exactly once** to save tokens and time. 
- **Evidence Integrity (Lean Storage Rule):** 
    - **Failure Evidence (MANDATORY):** Chỉ chụp ảnh màn hình khi test case có kết quả `FAIL`, `ERROR` hoặc khi gặp trang trắng (timeout 5s).
    - **Success Evidence:** Tuyệt đối KHÔNG chụp ảnh cho các case `PASS` để tiết kiệm bộ nhớ.
- **Pass Criteria:** A test case is "Passed" ONLY if: (1) all inputs are visible on UI and (2) Actual Result matches Expected Result 100%.
- **File Source Protection:** Tuyệt đối KHÔNG tự động xóa file source (test case, config, script gốc) khi chưa xác nhận với User. Kiểm tra cấu trúc thư mục hiện có trước khi tạo file mới — tránh duplicate.
- **Traceable Data Format:** Mọi dữ liệu unique sinh ra bởi automation (email, username, ID) PHẢI theo format traceable:
    ```
    [prefix]_[testName]_[timestamp]_[random]
    Ví dụ: auto_createCustomer_20260402_A3F2@test.com
    ```
    Mục đích: Nhìn vào DB biết ngay test nào tạo ra record này.

## 5. Reporting & Excel Standards

- **Primary Output (MANDATORY):** Copy the original Test Case file to the result file using the standard naming convention:
  ```
  execution/[UC-ID]/reports/res_[UC-ID]_[feature-name]_testcases_res_[YYYYMMDD]_v[N].xlsx
  ```
- **Execution Folder Structure:**
  - `execution/[UC-ID]/scripts/` : Chứa file script tự động (Playwright, MCP).
  - `execution/[UC-ID]/logs/` : Log chi tiết hệ thống khi chạy test.
  - `report/Image/{Module}/{TestFileName}/` : Screenshot minh chứng (giữ nguyên để tập trung quản lý media).
- **Version Check:** ALWAYS check the `execution/[UC-ID]/` directory first. If previous result versions exist, increment the version (e.g., `v1` becomes `v2`). Never overwrite existing files.
- **Result Columns (MANDATORY):** Populate the following columns starting from Column H:
  - **Column H [Status]:** Giá trị `PASS`, `FAIL`, `BLOCKED`, hoặc `SKIPPED`.
  - **Column I [Actual Result]:** Mô tả thực tế những gì diễn ra trên hệ thống.
  - **Column J [Note]:** Ghi chú thêm, kết quả query DB, hoặc Trace ID.
- **Formatting & Write Rules (Lesson 1 & 13):** 
    - Font: Black (`000000`), Size: `11`.
    - **Force View:** Set `row_dimensions[row].hidden = False` and `row_dimensions[row].height = 30-40` to prevent invisible data.
    - Status Coloring: Pass (Green), Fail (Red), Other (Gray).
    - **Header Guard (Lesson 13):** Script BẮT BUỘC kiểm tra và điền tiêu đề `[Status]`, `[Actual Result]`, `[Note]` nếu thiếu.
    - **ID Sanitization (Lesson 13):** Luôn gọi `.strip()` cho TC ID đọc từ Excel để tránh lỗi so khớp do khoảng trắng dư thừa.
    - **Master Cell Rule:** If writing to a merged cell region, always locate and write to the Top-Left Master Cell to avoid errors.
- **Bug Report (12-Columns):** 
    - **Mapping:** Bug ID (A), Environment (B), Data test (C), TC ID (D), Bug title (E), Precondition (F), Steps (G), Actual result (H), Expected result (I), Evidence (J), Severity (K), Priority (L).
- **Context:** Every failure must include the Environment and specific Test Data used.

## 6. Mô hình Khám Bệnh Flaky Test

Bản năng đánh giá của QA Agent (đồng thời là bộ Cẩm nang chẩn đoán bệnh training cho test team):
Bắt buộc phân lập lỗi chập chờn (Flaky) thành 4 bệnh nền cơ bản, qua đó `flaky_test_analyzer` sẽ ra quyết định:
1. **Trễ Timing (Timing Delay):** Do animation, spinner của Chakra UI chưa tắt. -> Thuốc: Dùng Web-first Assertions (`expect().toBeVisible()`), Short-polling thay vì sleep tĩnh.
2. **Xung đột Data chạy song song (Parallel Data Conflict):** Test case chạy đè Data của test khác -> Thuốc: Data Lifecycle cách ly (Tạo mới -> Dọn dẹp).
3. **Locator không ổn định (Unstable Locator):** Element bị lồng ghép thêm thẻ <div>/<span> từ Frontend -> Thuốc: Cơ chế "Snapshot" (Accessibility Tree) và Fallback Scripts.
4. **Môi trường (Environment Issues):** Network rớt mạng, Backend quá tải -> Thuốc: Cơ chế API retry, Wait loading state.

## 7. MCP-Enhanced Capabilities (OPTIONAL)

> Các tính năng dưới đây CHỈ khả dụng khi MCP Server được cấu hình trong `project-config.md` (Section 10). Nếu MCP chưa được thiết lập, Agent BẮT BUỘC bỏ qua section này và thực thi bằng phương thức UI-only truyền thống.

### 7.1 Dynamic Data Fetching (Layer 2 — Data Integrity Verification)
Khi MCP Database Server khả dụng, Agent có thể thực hiện xác minh dữ liệu ở tầng DB — thay vì chỉ kiểm tra trên UI.

**Workflow:**
1. **Pre-condition Check:** Trước khi thực thi TC, Agent sử dụng MCP DB để chạy `SELECT` query xác nhận trạng thái dữ liệu hiện tại (e.g., `SELECT status FROM records WHERE id = '123'`).
2. **Post-action Verification:** Sau khi thực hiện hành động trên UI (Create/Edit/Delete), Agent query DB lần nữa để so sánh:
   - Dữ liệu trên UI có khớp với dữ liệu trong DB không?
   - Trạng thái đã chuyển đổi đúng chưa (e.g., `Draft` → `Active`)?
   - Total count có đúng không?
3. **Ghi kết quả:** Nếu UI và DB khớp → `PASS (UI+DB verified)`. Nếu lệch → `FAIL` kèm chi tiết `UI shows X, DB shows Y`.

**Ràng buộc:**
- CHỈ thực hiện `SELECT` queries. Tuyệt đối KHÔNG chạy `INSERT`, `UPDATE`, `DELETE` trên DB thông qua MCP.
- Query results MUST được ghi vào cột Note trong Excel report để làm bằng chứng.

### 7.2 Automated Log Extraction (Enhanced Failure Diagnostics)
Khi test case FAIL, thay vì chỉ có screenshot, Agent có thể thu thập thêm dữ liệu chẩn đoán:

**Workflow:**
1. **On Failure:** Khi TC có kết quả `FAIL` hoặc `ERROR`, Agent tự động:
   - Gọi MCP để đọc system logs (application logs, error logs) trong khoảng thời gian thực thi TC.
   - Trích xuất `Trace ID`, `Error Stack`, hoặc `HTTP Status Code` liên quan.
2. **Enrich Bug Report:** Thông tin log được thêm vào cột Evidence (J) trong Bug Report 12-Columns, cùng với screenshot path.
3. **Storage:** Log files (nếu export) được lưu tại `report/Logs/{Module}/{TC-ID}_[Timestamp].log`.

**Ràng buộc:**
- CHỈ đọc logs. Không xóa hoặc ghi đè log files.
- Nếu MCP Log Server không khả dụng, Agent chỉ sử dụng screenshot truyền thống (Section 4).

## 8. Quy Trình Làm Việc & Code Cleanup

### 8.1 Quy Trình Làm Việc (Workflow)
- **Recon (Điều tra):** Luôn inspect giao diện thực tế hoặc DOM/HTML/XML trước khi viết automation. Tuyệt đối KHÔNG ĐOÁN locator.
- **Implementation:** Giữ vững mô hình **Page Object Model (POM)**. Phân tách rõ Page objects, Test execution và Utils/Test data.
- **Execution & Self-fix:** Chạy test ngay sau khi code xong. Nếu test FAIL → tự đọc log → phân tích root cause → sửa code → chạy lại → đến khi PASS ổn định. Chỉ hỏi User khi gặp business rule mâu thuẫn.

### 8.2 Code Cleanup (Bắt buộc trước khi hoàn thành)
- [ ] Xoá toàn bộ `print()`, `console.log()`, debug log tạm thời.
- [ ] Xoá locator không còn sử dụng.
- [ ] Không để lại commented-out code.
- [ ] Không có `waitForTimeout` / `Thread.sleep` hardcoded.
- [ ] Không có test data hardcoded (email, username, ID phải random/traceable).
- [ ] Không có logic trùng lặp — tạo helper methods cho các hành động lặp đi lặp lại.

### 8.4 Naming Convention (Automation Files)

| Thành phần | Quy tắc | Ví dụ |
|---|---|---|
| Page class | PascalCase + hậu tố `Page` | `LoginPage.ts`, `CartPage.ts` |
| Test file | kebab-case + `.spec.ts` | `login.spec.ts`, `cart.spec.ts` |
| Test block | `test('mô tả hành vi')` | `test('đăng nhập thành công')` |
| Locator biến | lowerCamelCase hoặc readonly | `readonly loginButton` |
| Utils | PascalCase hoặc kebab-case | `DataGenerator.ts`, `data-generator.ts` |

### 8.3 Báo Cáo Kết Quả (BẮT BUỘC sau khi hoàn thành execute)
Agent BẮT BUỘC in ra báo cáo tổng kết chi tiết cho User theo cấu trúc chuẩn sau đây trước khi kết thúc task:

1.  **Tóm tắt kết quả (Summary):** Tổng số lượng test PASS / FAIL / SKIP.
2.  **Chi tiết Coverage:** Giải trình lý do cụ thể cho mọi case **SKIPPED** hoặc **BLOCKED**.
3.  **Phân tích RCA (Root Cause Analysis):** BẮT BUỘC phân loại mọi lỗi FAIL/ERROR theo nhóm **R1-R4** (chi tiết tại Section 11.1).
4.  **Mật độ lỗi & Độ ổn định (Stability):** Báo cáo chỉ số **Defect Density (DD%)** và xếp hạng màu **Green/Yellow/Red** (chi tiết tại Section 11.2).
5.  **Hiệu quả & Độ tin cậy (Efficiency):** Báo cáo chỉ số **Reliability Score** dựa trên Triple-Link (chi tiết tại Section 11.3).
6.  **Antigravity Quality Gate (V3):** In bảng tổng kết mở rộng theo định dạng tại Section 10.4.
7.  **Đề xuất hành động (Recommendations):** Đưa ra các bước tiếp theo cụ thể dựa trên kết quả RCA (ví dụ: "Cần fix gấp Validation", "Cần cập nhật lại Requirement", hoặc "Chạy lại bộ test sau khi ổn định môi trường").

## 9. Antigravity Quality Gate (Post-Execution Audit)

Sau khi báo cáo kết quả, Agent BẮT BUỘC tự kích hoạt cổng kiểm soát chất lượng dựa trên các tiêu chí sau:

### 9.1 Post-Execution Audit Criteria (Gold Standard)
Agent phân tích log và báo cáo dựa trên 4 trụ cột:
1.  **Execution Integrity:** Kiểm tra số lượng case chạy thực tế có khớp với file Excel (1:1). Giải trình lý do cho mọi case **Skipped**.
2.  **Failure Analysis (Rule E3):** Phân loại lỗi FAIL thành: **Environment** (E1 - lag/timeout), **Script** (E2 - locator sai), hoặc **Actual Bug** (E3 - lỗi logic phần mềm).
3.  **Deep Validation Check:** Xác nhận đã thực hiện các bước kiểm tra sâu (Check DB/API qua MCP) thay vì chỉ dừng lại ở việc check UI thành công.
4.  **Common Rule Compliance:** Đảm bảo các quy tắc chung (như Audit Log, RBAC enforcement) thực sự được kiểm tra trong quá trình chạy.

### 9.2 Cross-Check Execution (Random Verification)
Agent thực hiện chọn ngẫu nhiên 3 testcase bất kỳ (1 Pass, 1 Fail, 1 Skipped) và giải trình chi tiết logic dẫn đến kết quả đó dựa trên Log và Screenshots. Nếu không giải trình được logic nhất quán, đợt chạy bị đánh dấu là **'Unreliable'**.

## 10. Advanced Hardening Layers (Zero-Tolerance Policy)

Để đạt được độ tin cậy tuyệt đối, Agent phải tuân thủ 3 tầng phòng ngự sau:

### 10.1 Tầng đối soát Tuyệt đối (Zero-Skip Policy)
- **Logic Kiểm soát:** Trước khi chạy, Agent phải đếm tổng số dòng (TCs) trong Excel. Sau khi chạy, lấy `Passed + Failed` so sánh với `Total`. 
- **Verdict:** Nếu `Total - (Passed + Failed) > 0`, toàn bộ đợt chạy bị đánh dấu **FAILED (Incomplete)**.
- **Hash Validation:** Mọi Test Data sử dụng phải khớp 100% với file Case/Config. Nếu Agent tự ý thay đổi data (ảo giác), phải dừng thực thi ngay lập tức.

### 10.2 Tầng xác thực thực tế (Deep Evidence Collection)
Mọi kết quả PASS đều bị nghi ngờ cho đến khi có đủ 3 bằng chứng (Triple-Link):
1.  **Screenshot:** Ảnh chụp tại thời điểm tương tác cuối cùng (Click/Submit).
2.  **API Response:** Trích xuất log API (Status 200/201) từ Network/MCP.
3.  **Database Result:** Query trực tiếp qua MCP DB để xác nhận bản ghi đã tồn tại/thay đổi đúng giá trị.
- **Quality Gate:** Nếu thiếu 1 trong 3, kết quả bị hạ cấp xuống **FAIL (Insufficient Evidence)**.

### 10.3 Tầng thử thách hệ thống (Fault Injection Verification)
- **Cơ chế bẫy:** Agent phải sẵn sàng tâm thế đối đầu với các "Fake Pass" hoặc "Intended Failures" được cài cắm trong bộ test (ví dụ: 5 case sai data cố ý).
- **IQ Check:**
    - Nếu Agent báo PASS cho case được cài bẫy FAIL -> Hệ thống Assertions bị coi là "Blind" (Mù).
    - Chỉ số tin cậy chỉ đạt 100% khi Agent phát hiện chính xác các lỗi được cài cắm.

### 10.4 Quality Gate Output (V3 - Enhanced)

Cuối mỗi task execution, Agent phải in bảng tổng kết mở rộng:

| Criterion | Verdict | Reliability Score | Note |
| :--- | :--- | :--- | :--- |
| **Zero-Skip** | [PASS/FAIL] | XX% | Count: Total vs (P+F) |
| **Deep Evidence** | [PASS/FAIL] | XX% | UI+API+DB Checked |
| **Fault Injection** | [OK/BLIND] | XX% | Found X/Y Intended Fails |
| **Final Result** | **[TRUSTED / RE-RUN]** | **OVERALL SCORE** | |

## 11. Advanced Post-Execution Analysis (RCA & Efficiency)

Sau khi có kết quả thực thi, Agent thực hiện phân tích sâu để đánh giá chất lượng sản phẩm và bộ test.

### 11.1 Root Cause Analysis (RCA) - Phân loại lỗi
Mọi kết quả `FAIL/ERROR` phải được gán nhãn RCA:
- **[R1] Actual Bug:** Lỗi logic phần mềm so với Requirement. -> *Hành động: Log Bug.*
- **[R2] Requirement Gap:** Tài liệu thiếu/sai/không cập nhật kịp code. -> *Hành động: Review BA.*
- **[R3] Environment/Infra:** Server lag, Timeout, Network, Auth expired. -> *Hành động: Check Infra.*
- **[R4] Script Flaw:** Locator hỏng, logic automation chưa tối ưu. -> *Hành động: Fix Script.*

### 11.2 Defect Density & Module Stability
- **Mật độ lỗi (DD):** `(Số lượng Bug R1 + R2) / Tổng số Test Case * 100%`.
- **Phân loại ổn định:**
    - **Green (Stable):** DD < 5% - Module đủ điều kiện release.
    - **Yellow (At Risk):** DD 5% - 15% - Cần regression test thêm.
    - **Red (Unstable):** DD > 15% - Module nát, cần code review lại toàn bộ.

### 11.3 Efficiency & Leakage Metric
- **Detection Efficiency:** `(Số Bug tìm thấy bằng Automation) / (Tổng số Bug phát hiện sau đó)`.
- **Độ tin cậy (Reliability):** Dựa trên Triple-Link (UI+API+DB). Nếu pass UI mà DB không đổi data → **Leakage detected** (Logic ngầm sai).

## 12. Jira Status Transition Hook (Automated Monitoring)

Quy định này áp dụng cho việc theo dõi tự động các thay đổi trạng thái của Bug trên Jira để kích hoạt quy trình Re-test kịp thời.

### 12.1 Điều kiện kích hoạt (The Hook)
Agent thực hiện quét Jira định kỳ hoặc theo yêu cầu dựa trên các điều kiện:
1.  **Chuyển trạng thái:** Khi một Ticket chuyển từ `In Progress` hoặc `Fixed` sang **`Ready for Test`** (hoặc trạng thái tương đương tùy dự án).
2.  **Lịch trình (Cron):** Mặc định quét vào **9:00 AM hàng ngày** để tổng hợp danh sách các bug đã sẵn sàng để kiểm thử lại.

### 12.2 Logic xử lý (The Action)
Khi phát hiện có sự thay đổi hoặc có bug mới ở trạng thái `Ready for Test`, Agent thực hiện:
1.  **Quét JQL:** Sử dụng câu lệnh `project = [Key] AND issuetype = Bug AND status = "Ready for Test"`.
2.  **So sánh Snapshot:** Đối chiếu với bản báo cáo Bug gần nhất để xác định danh sách "Newly Ready for Test".
3.  **Khởi tạo thông báo:**
    - **Tạo file báo cáo:** Lưu tại `report/daily-bug-notification_YYYYMMDD.md`.
    - **Nội dung:** Liệt kê ID, Tiêu đề, Link Jira và ghi chú Re-test (nếu có).
4.  **Thông báo người dùng:** Gửi tóm tắt danh sách bug mới này trực tiếp cho User.

### 12.3 Cấu hình trong Project Config
Agent phải đọc các tham số sau từ `project_config.json` (Section `jira.hooks`):
- `target_status`: Danh sách trạng thái cần theo dõi (mặc định: `Ready for Test`).
- `scan_schedule`: Thời gian quét tự động.
- `notification_channel`: `file` (mặc định) hoặc `email`.
