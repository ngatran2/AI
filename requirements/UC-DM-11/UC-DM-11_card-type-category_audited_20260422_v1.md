# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

> **How to use this template**
>This template defines the minimum information QA testers need to begin test case design.
>Fill out all sections completely before handing off to QA. Do not leave any field blank — if a section truly does not apply, write N/A and explain why.
>
> **Completion status conventions:**
> - ✅ **Complete** = section is fully populated and no longer ambiguous
> - ⚡ **Partial** = contains content but requires further clarification
> - ⚠️ **Missing** = absent — BLOCKER, cannot start test design

---

## Feature Brief

Tính năng Quản lý danh mục loại thẻ (Card Type Category Management - UC-DM-11) cho phép người dùng xem, thêm mới, sửa và xóa mềm các loại thẻ theo từng hãng bay. Hệ thống yêu cầu mã thẻ (Card ID) phải là duy nhất trong cùng một hãng bay, tự động in hoa và chỉ chứa chữ/số. Việc xóa một loại thẻ bị chặn nếu đã có dữ liệu thẻ tương ứng (BR-11.5).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `57.7 / 100` | ❌ NOT READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC-DM-11 | Card Type Category Management | v1.0 | Draft |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| N/A | N/A | 2026-04-22 | 2026-04-22 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép quản trị viên cấu hình và quản lý các loại thẻ áp dụng cho từng hãng bay trong hệ thống JOYS.

### 1.2 In Scope
- UC-LT-11.1: Xem danh mục loại thẻ
- UC-LT-11.2: Thêm loại thẻ
- UC-LT-11.3: Xem chi tiết loại thẻ
- UC-LT-11.4: Sửa loại thẻ
- UC-LT-11.5: Xóa loại thẻ (Soft delete)

### 1.3 Out of Scope
None specified.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| *(Unknown)* | Primary | Hệ thống có đề cập đến quyền "Add" (Thêm mới), nhưng chưa chỉ định rõ danh sách Role cụ thể nào có quyền này (VD: Admin, View). |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
⚠️ **Missing**: Không có mô tả về trạng thái người dùng trước khi vào luồng (VD: Đăng nhập thành công, có quyền truy cập module).

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Thêm/Sửa loại thẻ | Dữ liệu được lưu, hiển thị trên bảng danh sách. |
| Xóa loại thẻ | Bản ghi bị xóa mềm (Soft delete), không còn xuất hiện trong list active. |

---

## 4. UI Object Inventory & Mapping

| Category | Component Name | Description & Constraints |
|----------|----------------|---------------------------|
| **Data Display Structure** | Bảng danh sách | Cột: No., Card ID, Card Type, Airline. Các hành động: View, Edit, Delete. |
| **Control System** | Search Bar | Textbox. Tìm kiếm theo Card Type Name hoặc Card ID. |
| **Control System** | Airline Filter | Combobox. Default: Hãng bay đầu tiên. |
| **Navigation & Actions** | Add New Button | Chỉ hiển thị nếu có quyền "Add". |
| **Input** | Card ID | Textbox, max 30 chars, allow A-Z/0-9/Space, auto uppercase, mandatory, unique per airline. |
| **Input** | Card Type | Textbox, max 255 chars (hoặc 100 chars - xem mục Câu hỏi), mandatory. |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Popup: Xem chi tiết | Read-only | Click 'Close' | Đóng popup, quay lại danh sách. |
| Popup: Sửa | Input fields | Card ID & Airline bị Disable (Read-only). | Nút Update lưu thay đổi và hiện Toast success. Nút Delete gọi hàm xóa. Nút Close đóng popup. |
| Nút Delete | Confirmation | Click 'Xóa' | Hiện popup confirm: "Bạn có chắc chắn muốn xóa loại thẻ này không?". Nếu có dữ liệu liên quan (BR-11.5) -> Chặn xóa. |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function Name: Thêm mới (Add Card Type)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Nhấn 'Thêm mới' | Mở popup thêm mới (UI-11.2-a) | | |
| 2 | User | Nhập thông tin hợp lệ & Lưu | Lưu thành công vào DB, ghi Audit Log | Nhập mã thẻ trùng với mã đã xóa mềm -> Chấp nhận (BR-11.4) | Nhập mã thẻ bị trùng với mã đang active -> Báo lỗi. Để trống trường bắt buộc -> Báo lỗi. |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Airline | Yes | Lựa chọn từ combobox | N/A | *(Chưa định nghĩa text báo lỗi)* |
| Card ID | Yes | Tiếng Anh, số, dấu cách (Auto uppercase). Unique. | Max 30 | *(Chưa định nghĩa text báo lỗi trùng lặp)* |
| Card Type | Yes | Unicode | Max 255 | *(Chưa định nghĩa text báo lỗi)* |

**C. UI/UX Feedback**
* **Toast Messages:** ⚠️ Missing (Chưa định nghĩa nguyên văn text báo thành công hay thất bại).

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Xóa loại thẻ | Soft delete, không hiển thị trong màn hình danh sách | Dữ liệu thẻ hiện tại đang gán với Card Type này có bị ảnh hưởng không? (BR-11.5 chặn xóa nếu có, vậy nên nếu xóa được tức là không có rủi ro). |

---

## 8. Acceptance Criteria

⚠️ **Missing**: Không có bất kỳ Acceptance Criteria nào theo format Given/When/Then cho các luồng CRUD.

---

## 9. Non-functional Requirements

⚠️ **Missing**: Không có định nghĩa về hiệu năng, tốc độ, hay trình duyệt.

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
| # | Question / Issue | Context | Owner | Status |
|---|-----------------|---------|-------|--------|
| Q1 | Thiếu AC (Acceptance Criteria) và Pre-conditions | Cần có để QA viết testcase. | BA | Open |
| Q2 | Mâu thuẫn độ dài trường `Card Type` | Trong UC 11.2 ghi max 255 chars, nhưng trong UC 11.4 ghi là sửa max 100 chars. Độ dài thực tế là bao nhiêu? | BA | Open |
| Q3 | Thiếu Audit Log cho Edit và Delete | Đã định nghĩa log cho Create, nhưng thiếu cấu trúc log cho Update và Delete. | BA | Open |
| Q4 | Thiếu nguyên văn thông báo lỗi / Toast | Chưa có chuỗi string chính xác cho các lỗi như: Trùng ID, Bỏ trống trường bắt buộc, Thêm/Sửa thành công. | BA | Open |
| Q5 | Ma trận phân quyền (RBAC Matrix) ở đâu? | Nhắc đến quyền "Add", nhưng thiếu danh sách cụ thể Role nào được quyền gì. | BA | Open |
| Q6 | Thông báo khi bị chặn xóa (BR-11.5) là gì? | "Không được phép xóa loại thẻ nếu đã có dữ liệu thẻ tương ứng...". Vậy câu Toast thông báo cho user chính xác là gì? | BA | Open |

### 10.2 Dependencies
N/A

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-04-22 | requirement-reviewer | Initial audit of extracted UC-DM-11 requirements. |

---

*UC Readiness Template v3.0 — For QA Test Design*

---

### 📊 Audit Summary

| #               | Knowledge Area                 | Max Pts       | Score | Status                     |
| --------------- | ------------------------------ | ------------- | ----- | -------------------------- |
| 1               | Feature Identity               | 5             | 5/5   | ✅                         |
| 2               | Objective & Scope              | 5             | 5/5   | ✅                         |
| 3               | Actors & User Roles            | 10            | 5/10  | ⚡                         |
| 4               | Preconditions & Postconditions | 10            | 0/10  | ⚠️ BLOCKER                 |
| 5               | UI Object Inventory & Mapping  | 15            | 15/15 | ✅                         |
| 6               | Object Attributes & Behavior Definition| 20            | 10/20 | ⚡                         |
| 7               | Functional Logic & Workflow Decomposition| 20            | 20/20 | ✅                         |
| 8               | Functional Integration Analysis    | 10            | 5/10  | ⚡                         |
| 9               | Acceptance Criteria    | 10            | 0/10  | ⚠️ BLOCKER                 |
| 10              | Non-functional Requirements    | 5             | 0/5   | ⚠️                         |
| 11              | Audit Log & Traceability       | 10            | 5/10  | ⚡                         |
| 12              | Security & Concurrency         | 10            | 5/10  | ⚡                         |
| **Total**       |                                | **130**       |       | **75/130 → 57.7/100**       |

### 📋 Unified Gap & Question Report
| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | N/A (Missing) | Yêu cầu cung cấp Pre-conditions và Acceptance Criteria (AC). | QA không có tiêu chí xác định trạng thái ban đầu và định nghĩa "Pass" cho từng luồng. | Open |
| Q2 | Medium | "Textbox, maximum 255 Unicode characters." vs "Editable. Maximum 100 characters" | Trường `Card Type` có max-length là bao nhiêu (100 hay 255)? | Gây lỗi thiết kế Boundary Test Data. | Open |
| Q3 | Medium | "Audit Log: Title: Create New Card Type... Content: [User Name] created..." | Cần bổ sung format Audit Log cho hành động Sửa (Update) và Xóa (Delete). | Yêu cầu truy vết theo chuẩn Giai đoạn 2 chưa đầy đủ. | Open |
| Q4 | Medium | N/A (Missing) | Cung cấp nguyên văn 100% Text thông báo lỗi (Trùng mã, Bỏ trống, Cấm xóa do BR-11.5) và thông báo thành công. | Thiếu dữ liệu Verbatim cho automation test. | Open |
| Q5 | Medium | "Displayed only if the user has the 'Add' permission." | Cần bổ sung Ma trận phân quyền (RBAC Matrix) rõ ràng cho các Roles (Admin, View, Edit, v.v.). | Thiếu thông tin để sinh test case phần Security/Roles. | Open |

### 🟢 What's Good
Các quy tắc nghiệp vụ (Business Rules) từ BR-11.3 đến BR-11.6 được định nghĩa rất rõ ràng, chi tiết, xử lý triệt để logic "soft delete" và "cấp lại mã trùng". Khung danh sách màn hình và các trường UI được liệt kê tường minh.

### 🧪 Testability Outlook

**What CAN be tested now:**
- Validation định dạng trường (Card ID chỉ chữ số viết hoa).
- Luồng chặn theo Business Rules cơ bản.

**What CANNOT be tested yet (blocked by gaps):**
- Test case phân quyền (do thiếu RBAC Matrix).
- Automation test assertions (do thiếu thông báo Toast nguyên văn).
- Test Audit Log (thiếu định dạng cho Update/Delete).

### 📌 Summary & Recommendation
Tài liệu hiện tại có phần Business Rules tốt nhưng lại thiếu hoàn toàn các thông số quan trọng cho QA: Acceptance Criteria, Preconditions, RBAC Matrix và nguyên văn Toast Messages (Verbatim). Đánh giá: **❌ NOT READY**. Yêu cầu BA bổ sung thông tin qua các Ticket (Q1-Q5) trước khi QA tiến hành viết kịch bản test.
