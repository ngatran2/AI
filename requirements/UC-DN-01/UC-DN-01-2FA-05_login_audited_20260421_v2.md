# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

## Feature Brief

Tính năng cho phép người dùng đăng nhập vào hệ thống LAMS thông qua tài khoản hệ thống (LAMS). Các trường hợp Đăng nhập bằng LDAP đã được loại khỏi phạm vi (Out of Scope). Sau khi xác thực thông tin đăng nhập thành công, hệ thống tiếp tục kiểm tra trạng thái kích hoạt 2FA. Nếu 2FA đã kích hoạt, người dùng bắt buộc phải nhập mã OTP 6 số (UC-2FA-05) để xác thực trước khi truy cập vào hệ thống.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `100 / 100` | ✅ **READY** |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC-DN-01, UC-2FA-05 | Đăng nhập & Xác thực 2 lớp | v2.0 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| N/A | N/A | 2026-04-21 | 2026-04-21 |

---

## 1. Objective & Scope

### 1.1 Objective
Bảo mật quyền truy cập vào hệ thống LAMS thông qua cơ chế xác thực thông tin (LAMS) và bảo mật 2 lớp (2FA).

### 1.2 In Scope
- Đăng nhập bằng tài khoản LAMS
- Xác thực mã OTP 2FA khi đăng nhập

### 1.3 Out of Scope
- Quản lý tài khoản LDAP (Nằm ngoài hệ thống)
- Đăng nhập bằng tài khoản LDAP (Đã loại bỏ khỏi phạm vi thiết kế test theo xác nhận của BA)

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Người dùng | Primary | Thực hiện đăng nhập và xác thực OTP để vào hệ thống. |
| Quản trị viên | System | Có thể reset 2FA của người dùng trong quá trình đăng nhập. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Màn hình Đăng nhập: Người dùng đang ở UI-01-a (https://lams-fe.sotatek.works/login?redirect=%2Fsystem%2Fusers).
- Màn hình Xác thực 2FA: Người dùng đã xác thực User/Pass thành công và cơ chế 2FA đã được kích hoạt.

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Đăng nhập hợp lệ nhưng chưa kích hoạt 2FA | Điều hướng sang luồng kích hoạt 2FA (UC-2FA-04). |
| Xác thực 2FA thành công | Điều hướng đến chức năng màn Hệ thống/Quản lý người dùng (https://lams-fe.sotatek.works/system/users). |

---

## 4. UI Object Inventory & Mapping (Layout & Forms Analysis)

| Category | Component Name | Description & Constraints |
|----------|----------------|---------------------------|
| **Data Display Structure** | Form đăng nhập (UI-01-a) | Không có Grid/Table. Giao diện form cơ bản. |
| **Control System** | Lựa chọn đăng nhập | Radio box. Chỉ test option: Tài khoản LAMS. |
| **Form & Inputs Collection** | Tên đăng nhập | Text field, `type="email"`, `required=true`. Placeholder: "Email đăng nhập". |
| **Form & Inputs Collection** | Mật khẩu | Text field, `type="password"`, `required=true`. Có icon ẩn/hiện mật khẩu. |
| **Form & Inputs Collection** | Mã xác thực (UI-05) | Input field, `type="number"`, `maxlength=6`, `required=true`. |
| **Navigation & Actions** | Nút Đăng nhập | Button. Trigger luồng xác thực LAMS. Bị disable khi loading. |
| **Navigation & Actions** | Nút Xác nhận (UI-05) | Button. Trigger luồng xác thực OTP. Bị disable khi loading. |
| **Navigation & Actions** | Nút Trở về (UI-05) | Button. Quay lại màn hình đăng nhập UI-01-a. |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Radio Lựa chọn | Enabled | Click | Bỏ qua test LDAP. Chỉ test chọn LAMS. |
| Tên đăng nhập | Enabled | Focus / Blur | Bôi đỏ khung input và báo lỗi "Vui lòng nhập địa chỉ email hợp lệ" nếu sai định dạng. |
| Icon Ẩn/Hiện Pass | Enabled | Click | Đổi type của input Mật khẩu giữa `text` và `password`. |
| Nút Đăng nhập | Enabled / Disabled | Click | Báo lỗi inline nếu bỏ trống. Gọi API xác thực nếu hợp lệ. Bị disable trong quá trình gọi API (Loading State). |
| Nút Xác nhận OTP | Enabled / Disabled | Click | Báo lỗi inline nếu bỏ trống hoặc < 6 ký tự. Gọi API verify OTP. Bị disable trong quá trình gọi API (Loading State). |

---

## 6. System Decomposition & Functional Logic

### 6.1 Sub-module 1: Đăng nhập (UC-DN-01)

**A. Workflows & Dependencies**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Người dùng | Nhập Email + Pass và Click Đăng nhập | Hệ thống gửi request sang Backend LAMS. | LDAP flows bị bỏ qua theo scope mới. | Lỗi 500 hoặc Timeout -> Toast lỗi "Không thể kết nối..." / "Hệ thống đang bận...". |
| 2 | Hệ thống | Kiểm tra trạng thái 2FA | Trạng thái Đã kích hoạt -> Chuyển sang màn UI-05. | Chưa kích hoạt -> Chuyển sang UI-04-a (Thiết lập 2FA). | Tài khoản bị khóa -> Báo lỗi "Tài khoản bị khóa...". |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Tên đăng nhập | Yes | Định dạng Email | N/A | "Vui lòng nhập địa chỉ email hợp lệ" |
| Mật khẩu | Yes | Định dạng Password | N/A | N/A |

**C. UI/UX Feedback**
* **Loading States:** Nút "Đăng nhập" bị disable trong quá trình gọi API.
* **Toast Messages:** 
  - Lỗi mạng/500: "Không thể kết nối hệ thống xác thực. Vui lòng thử lại sau."
  - Lỗi Timeout: "Hệ thống đang bận. Vui lòng thử lại sau."
* **Inline Errors:** "Sai Tên đăng nhập hoặc Mật khẩu.", "Tài khoản bị khóa, vui lòng liên hệ với quản trị viên."

### 6.2 Sub-module 2: Xác thực 2 lớp (UC-2FA-05)

**A. Workflows & Dependencies**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Người dùng | Nhập OTP và Click Xác nhận | Hệ thống điều hướng đến chức năng quản lý người dùng. | Token hết hạn -> Toast lỗi "Phiên xác thực đã hết hạn..." -> Quay về Đăng nhập. | Admin reset 2FA giữa chừng (403 REQUIRED_2FA) -> Toast lỗi "Xác thực thất bại..." -> Quay về Đăng nhập. |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Mã xác thực | Yes | Chỉ chứa số | Max 6 ký tự | "Mã xác thực không hợp lệ. Vui lòng thử lại" / "Vui lòng nhập mã xác thực" / "Mã xác thực không đúng..." |

**C. UI/UX Feedback**
* **Loading States:** Nút "Xác nhận" bị disable trong quá trình gọi API.
* **Toast Messages:** "Phiên xác thực đã hết hạn. Vui lòng thử lại.", "Xác thực thất bại. Vui lòng thử lại."

---

## 7. Functional Integration Analysis (Ma trận & Tích hợp)

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Quản trị viên Reset 2FA (UC-2FA-07) | Trạng thái 2FA của User bị chuyển thành "Chưa kích hoạt" ngay lập tức. | Xác minh nếu User đang ở màn UI-05 và bấm Xác nhận, hệ thống phải bắt được lỗi 403 REQUIRED_2FA và đẩy ra màn đăng nhập. |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given *(precondition)* | When *(user action)* | Then *(expected result)* |
|------|----------|------------------------|----------------------|--------------------------|
| AC-01 | Đăng nhập LAMS thành công | Ở màn đăng nhập (https://lams-fe.sotatek.works/login?redirect=%2Fsystem%2Fusers) | Nhập thông tin email, password đúng và Nhấn nút đăng nhập | Direct to màn nhập mã xác thực |
| AC-02 | Xác thực OTP thành công | Ở màn nhập mã xác thực | Nhập đúng mã otp tương ứng với email | Direct to màn Hệ thống/Quản lý người dùng (https://lams-fe.sotatek.works/system/users) |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Timeout Handling | Yêu cầu xác thực bị timeout phải hiển thị toast message rõ ràng. | UC-DN-01 Exception Flow |

---

## 10. Open Questions & Dependencies

### 10.1 Unified Gap & Question Report (Gửi BA)
| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q1 | High | N/A (Missing) | Thiếu hoàn toàn phần Acceptance Criteria (AC). | Không có tiêu chí nghiệm thu (Pass/Fail) rõ ràng cho QA thiết kế test cases. | **Resolved** |
| Q2 | Medium | UC-DN-01 (Basic Flow) | Chưa định nghĩa hành vi Loading State khi click nút "Đăng nhập". Nút có bị disable không? | Tránh việc user click nhiều lần (Spam request) gây lỗi hệ thống. | **Resolved** |
| Q3 | Medium | UI-01-a (Lựa chọn đăng nhập) | Khi user chuyển đổi giữa "Tài khoản LDAP" và "Tài khoản LAMS", form input (Email/Pass) có bị reset (xóa trắng) không? | Cần xác định UI Behavior cho việc reset form. | **Resolved** (LDAP bị loại khỏi Scope) |

### 10.2 Dependencies
- Phụ thuộc UC-2FA-04 (Kích hoạt 2FA) và UC-MK-02 (Reset mật khẩu).
- Không còn phụ thuộc LDAP.

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-04-21 | antigravity | Initial Audit dựa trên tài liệu yêu cầu LAMS. |
| v2.0 | 2026-04-21 | antigravity | Re-Audit tích hợp BA Answers: Bổ sung ACs, Loading States, và loại bỏ luồng xác thực LDAP khỏi scope. |

---

## 📊 Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|----------------|---------|-------|--------|
| 1 | Feature Identity | 5 | 5 | ✅ |
| 2 | Objective & Scope | 5 | 5 | ✅ |
| 3 | Actors & User Roles | 10 | 10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10 | ✅ |
| 10 | Non-functional Requirements | 5 | 5 | ✅ |
| **Total** | | **110** | **110/110 → 100/100** | ✅ **READY** |

---
## 🟢 What's Good
Tất cả các vướng mắc (Gaps) đã được BA giải quyết triệt để. Quyết định loại bỏ LDAP ra khỏi scope giúp làm gọn test suite và giảm độ phức tạp cho Automation. Bổ sung Loading State giúp kiểm tra triệt để lỗi Spam Click.

## 🧪 Testability Outlook
**What CAN be tested now:**
- UI Validation (Maxlength, Required, Type Email).
- Luồng Happy path đăng nhập LAMS.
- Luồng kiểm tra 2FA OTP.
- UI State: Nút Đăng nhập/Xác nhận bị disabled khi loading.

**What CANNOT be tested yet (blocked by gaps):**
- N/A (Không còn blocker).

**Suggested test focus areas:**
- Negative Testing (BVA) cho mã OTP 6 ký tự.
- Test tích hợp (Integration): Giả lập Admin reset 2FA khi User đang nhập OTP (Mã lỗi 403 REQUIRED_2FA).

### 📌 Summary & Recommendation
Tài liệu hiện tại đã hoàn chỉnh 100% (Ready). Tất cả các câu hỏi đã được giải quyết (Resolved) và Scope được thu hẹp tập trung vào LAMS. Đội QA có thể tiến hành sinh Test Scenarios và Test Cases.
