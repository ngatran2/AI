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

Tính năng Quản lý danh mục loại thẻ (Card Type Category Management - UC-DM-11) cho phép người dùng xem, thêm mới, xem chi tiết, sửa và xóa các loại thẻ hội viên của từng hãng bay trong hệ thống. Các nghiệp vụ bao gồm: quy tắc mã thẻ duy nhất trên mỗi hãng bay, quy định xóa mềm (không thể xóa/sửa nếu đang được sử dụng trong scanning session hoặc cấu hình phòng chờ), và bắt buộc xác thực trạng thái tài khoản khi gọi API để phòng chống tranh chấp khi session còn hoạt động nhưng user bị vô hiệu hóa.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `80.8 / 100` | ❌ NOT READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC-DM-11 | Card Type Category Management | v2 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| N/A | N/A | 2026-04-23 | 2026-04-23 |

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép quản lý cấu hình các loại thẻ hội viên áp dụng cho từng hãng bay trong hệ thống, làm dữ liệu nền tảng cho các nghiệp vụ scan thẻ và cấu hình điều kiện phòng chờ.

### 1.2 In Scope
- UC-LT-11.1: Xem danh mục loại thẻ
- UC-LT-11.2: Thêm loại thẻ
- UC-LT-11.3: Xem chi tiết loại thẻ
- UC-LT-11.4: Sửa loại thẻ
- UC-LT-11.5: Xóa loại thẻ

### 1.3 Out of Scope
None specified.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| *(Unknown User Role)* | Primary | Tài liệu có đề cập đến các quyền Xem, Thêm, Sửa, Xóa Danh mục nhưng chưa mô tả cụ thể Role nào sẽ nắm giữ các quyền này (Admin, User view, etc.). |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng đăng nhập hệ thống thành công.
- Người dùng có quyền truy cập chức năng tương ứng (Xem/Thêm/Sửa/Xóa).

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Thêm mới / Sửa | Lưu thông tin vào CSDL, hiển thị Toast success, update danh mục sử dụng trên toàn hệ thống, log audit (Title, Time, Actor, Content). |
| Xóa | Xóa khỏi danh mục quản lý, không được chọn ở cấu hình mới, dữ liệu lịch sử giữ nguyên phục vụ tra cứu. Người dùng có thể tạo lại mã trùng với thẻ đã xóa. Log audit lưu vết xóa. |

---

## 4. UI Object Inventory & Mapping

| Category | Component Name | Description & Constraints |
|----------|----------------|---------------------------|
| **Data Display Structure** | Danh mục loại thẻ (Table) | Cột: Mã thẻ, Loại thẻ, Hãng bay. Action: Xem, Sửa, Xóa. Sort mặc định theo ngày tạo giảm dần. Màn trống (CMR-08) nếu ko có DL. |
| **Control System** | Search Popup | Nhập từ khóa tìm kiếm, enter để tìm kiếm (CMR-09). |
| **Control System** | Hãng bay (Dropdown) | Chọn hãng bay (CMR-02). |
| **Navigation & Actions** | Buttons (Table) | Thêm mới (nếu có quyền thêm), Xem (nếu có quyền xem, ko có quyền sửa), Sửa, Xóa. |
| **Other Components** | Popup Thêm / Sửa / Chi tiết / Xóa | Form input thông tin Mã thẻ, Loại thẻ, dropdown Hãng bay, nút Xác nhận / Cập nhập / Đóng. |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Mã thẻ (Input) | Add: Editable. Edit/View: Read-only. | Max 30 chars, allow A-Z/0-9/Space. Auto uppercase. | Báo lỗi inline nếu trống hoặc trùng ID trong cùng hãng. |
| Loại thẻ (Input) | Add/Edit: Editable. View: Read-only. | Max 100 chars. | Báo lỗi inline nếu để trống. |
| Cập nhập / Xác nhận | Enabled (Add/Delete). Disabled if no change (Edit). | Click to Submit | Kiểm tra validation, gọi API, hiện Success/Error Toast, đóng Popup. Nếu token hết hạn logout user. |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function Name: Thêm mới (Add Card Type)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Nhấn 'Thêm mới' trên List | Hệ thống mở màn UI-11.2-a (Popup) | | |
| 2 | User | Nhập đủ thông tin, nhấn Thêm mới | Check validation hợp lệ, thêm DB, đóng popup, hiển thị Success Toast: "Thêm mới [mã thẻ - loại thẻ] thành công." | Người dùng nhấn Đóng -> Về màn danh sách. Nhấn khi Token hết hạn -> Báo lỗi & Logout. | Dữ liệu không hợp lệ (Bỏ trống, quá dài, trùng lặp) -> Hiển thị Inline error. |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Mã thẻ | Yes | Chữ (EN), số, space. Auto uppercase. Unique theo Hãng bay. | Max 30 | "Mã thẻ đã tồn tại trong hãng bay này." (Nếu trùng) |
| Loại thẻ | Yes | Text | Max 100 | N/A (Mặc định theo CMR) |
| Hãng bay | Yes | Dropdown list | N/A | N/A (Mặc định theo CMR) |

**C. UI/UX Feedback**
* **Loading States:** Mặc định theo hệ thống.
* **Toast Messages:** 
  - Success: "Thêm mới [mã thẻ - loại thẻ] thành công."
  - Error Token: "Thêm mới thẻ thất bại - Vui lòng thử lại sau."

### 6.2 Function Name: Sửa / Xóa (Edit / Delete Card Type)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | User | Nhấn 'Sửa' / 'Xóa' | Mở popup tương ứng UI-11.3-a / UI-11.5-a. | User nhấn Đóng -> Hủy bỏ thao tác. | Đang được dùng trong scanning session -> Không cho thao tác, hiện Toast Error. |
| 2 | User | Xác nhận thao tác | Cập nhật DB. Hiển thị Success Toast. | Xóa thành công -> Giữ nguyên lịch sử ở module report. | Token hết hạn -> "Xóa / Cập nhập thẻ thất bại - Vui lòng thử lại sau" và logout. |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Thẻ (Runtime) | N/A | Không được phép sửa/xóa nếu đang trong scanning session. | N/A | "Không thể xóa/cập nhập khi loại thẻ đang được sử dụng." |

**C. UI/UX Feedback**
* **Toast Messages:** 
  - Success: "Cập nhập/Xóa [mã thẻ - loại thẻ] thành công."
  - Error Rule: "Không thể cập nhập/xóa khi loại thẻ đang được sử dụng."
  - Error Token: "Cập nhập/Xóa thẻ thất bại - Vui lòng thử lại sau."

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Xóa loại thẻ | Không được chọn ở cấu hình mới hoặc thao tác scan thẻ. | Lịch sử scan và master data tra cứu cũ giữ nguyên. Mã thẻ xóa xong có thể tái sử dụng cho thẻ mới (BR-11.7, BR-11.8). |
| Sửa loại thẻ | Các thay đổi được đồng bộ hóa tức thì trên danh mục toàn hệ thống. | Thay đổi hiển thị ngay tại module cấu hình điều kiện và master data đang tham chiếu (BR-11.5). |

---

## 8. Acceptance Criteria

⚠️ **Missing**: Tài liệu hoàn toàn không liệt kê danh sách Acceptance Criteria (Given/When/Then) làm cơ sở đo lường kết quả test.

---

## 9. Non-functional Requirements

⚠️ **Missing**: Không có các chỉ số đo lường hiệu năng, thời gian phản hồi, bảo mật bổ sung (nếu có).

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
| # | Question / Issue | Context | Owner | Status |
|---|-----------------|---------|-------|--------|
| Q1 | Thiếu Acceptance Criteria (AC) | Cần có để QA viết testcase (AC dạng Given/When/Then). | BA | Open |
| Q2 | Thiếu Ma trận Phân quyền cụ thể (RBAC Matrix) | Đề cập "quyền xem, quyền sửa" nhưng không định nghĩa cụ thể Role nào (vd: Admin, View, Edit, User) có những quyền nào để test Security. | BA | Open |
| Q3 | Non-functional requirements | Thời gian tìm kiếm / phản hồi của các api crud là bao lâu? (Nếu có) | BA | Open |

### 10.2 Dependencies
- Phụ thuộc CMR-02, CMR-03, CMR-07, CMR-08, CMR-09.

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v2 | 2026-04-23 | requirement-reviewer | Re-audit full extracted Google Doc content. Resolved Verbatim Toasts, Validations, and Audit Log structure. |

---

*UC Readiness Template v3.0 — For QA Test Design*

---

### 📊 Audit Summary

| #               | Knowledge Area                 | Max Pts       | Score | Status                     |
| --------------- | ------------------------------ | ------------- | ----- | -------------------------- |
| 1               | Feature Identity               | 5             | 5/5   | ✅                         |
| 2               | Objective & Scope              | 5             | 5/5   | ✅                         |
| 3               | Actors & User Roles            | 10            | 5/10  | ⚡                         |
| 4               | Preconditions & Postconditions | 10            | 10/10 | ✅                         |
| 5               | UI Object Inventory & Mapping  | 15            | 15/15 | ✅                         |
| 6               | Object Attributes & Behavior Definition| 20            | 20/20 | ✅                         |
| 7               | Functional Logic & Workflow Decomposition| 20            | 20/20 | ✅                         |
| 8               | Functional Integration Analysis    | 10            | 10/10 | ✅                         |
| 9               | Acceptance Criteria    | 10            | 0/10  | ⚠️ BLOCKER                 |
| 10              | Non-functional Requirements    | 5             | 0/5   | ⚠️                         |
| 11              | Audit Log & Traceability       | 10            | 10/10 | ✅                         |
| 12              | Security & Concurrency         | 10            | 5/10  | ⚡                         |
| **Total**       |                                | **130**       |       | **105/130 → 80.8/100**     |

### 📋 Unified Gap & Question Report
| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | N/A (Missing) | Yêu cầu cung cấp Acceptance Criteria (AC). | QA không có định nghĩa chuẩn xác (Given/When/Then) để xác định Pass/Fail của hệ thống. | Open |
| Q2 | Medium | "Người dùng có quyền truy cập..." | Cần có Ma trận phân quyền (RBAC Matrix) rõ ràng, role nào được Xem/Sửa/Thêm/Xóa. | Thiết lập tài khoản giả lập và chạy test Security/Role. | Open |

### 🟢 What's Good
Tài liệu được viết vô cùng chi tiết và toàn diện ở phần Logic Nghiệp vụ (Business Rules). 100% các validation, Text thông báo lỗi (Error Message), thông báo thành công (Success Message) và logic Audit Log được cung cấp nguyên văn (verbatim), giúp cực kỳ dễ dàng cho việc xây dựng kịch bản Automation UI Testing. Các logic ngoại lệ như xử lý khi token hết hạn, chặn thao tác khi thẻ đang trong scanning session cũng được xử lý rất sắc bén.

### 🧪 Testability Outlook

**What CAN be tested now:**
- Toàn bộ flow CRUD (Thêm, Xem, Sửa, Xóa).
- UI assertions (Hiển thị form, ẩn/hiện nút bấm, validation rule chữ in hoa/độ dài).
- Toast messages & Inline error messages nguyên văn.
- Logic Data Integration (Thẻ bị xóa có thể tái tạo mã trùng, không thể sửa khi đang ở session scan).
- Audit Log (Title, Content, Author, Date).

**What CANNOT be tested yet (blocked by gaps):**
- System Acceptance Criteria (Thiếu AC).
- Security & Role-Based Access Control (Thiếu RBAC Matrix).

### 📌 Summary & Recommendation
Tài liệu đạt chất lượng rất cao về nghiệp vụ kỹ thuật, xử lý triệt để validation và verbatim cho UI/Automation. Tuy nhiên, do thiếu hoàn toàn bảng Acceptance Criteria (một tiêu chí Critical mang tính bắt buộc), điểm tổng kết chỉ đạt 80.8/100 và rơi vào trạng thái **❌ NOT READY**. Yêu cầu BA bổ sung AC và làm rõ ma trận Role/Permission để mở khóa giai đoạn Test Design.
