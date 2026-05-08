# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

## Feature Brief

Tính năng cho phép người dùng đăng nhập vào hệ thống LAMS thông qua hai phương thức: tài khoản hệ thống (LAMS) hoặc tài khoản Tổng công ty (LDAP). Sau khi xác thực thông tin đăng nhập thành công, hệ thống tiếp tục kiểm tra trạng thái kích hoạt 2FA. Nếu 2FA đã kích hoạt, người dùng bắt buộc phải nhập mã OTP 6 số (UC-2FA-05) để xác thực trước khi truy cập vào hệ thống.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `90.9 / 100` | ❌ **NOT READY** (Do thiếu Acceptance Criteria - Critical Area) |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC-DN-01, UC-2FA-05 | Đăng nhập & Xác thực 2 lớp | v1.0 | In Review |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| N/A | N/A | 2026-04-21 | 2026-04-21 |

---

## 1. Objective & Scope

### 1.1 Objective
Bảo mật quyền truy cập vào hệ thống LAMS thông qua cơ chế xác thực thông tin (LDAP/LAMS) và bảo mật 2 lớp (2FA).

### 1.2 In Scope
- Đăng nhập bằng tài khoản LDAP
- Đăng nhập bằng tài khoản LAMS
- Xác thực mã OTP 2FA khi đăng nhập

### 1.3 Out of Scope
- Quản lý tài khoản LDAP (Nằm ngoài hệ thống)

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Người dùng | Primary | Thực hiện đăng nhập và xác thực OTP để vào hệ thống. |
| Quản trị viên | System | Có thể reset 2FA của người dùng trong quá trình đăng nhập. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Màn hình Đăng nhập: Người dùng đang ở UI-01-a.
- Màn hình Xác thực 2FA: Người dùng đã xác thực User/Pass thành công và cơ chế 2FA đã được kích hoạt.

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Đăng nhập hợp lệ nhưng chưa kích hoạt 2FA | Điều hướng sang luồng kích hoạt 2FA (UC-2FA-04). |
| Xác thực 2FA thành công | Điều hướng đến chức năng đầu tiên theo phân quyền. |

---

## 4. UI Object Inventory & Mapping (Layout & Forms Analysis)

| Category | Component Name | Description & Constraints |
|----------|----------------|---------------------------|
| **Data Display Structure** | Form đăng nhập (UI-01-a) | Không có Grid/Table. Giao diện form cơ bản. |
| **Control System** | Lựa chọn đăng nhập | Radio box. Mặc định: Tài khoản LDAP. |
| **Form & Inputs Collection** | Tên đăng nhập | Text field, `type="email"`, `required=true`. Placeholder: "Email đăng nhập". |
| **Form & Inputs Collection** | Mật khẩu | Text field, `type="password"`, `required=true`. Có icon ẩn/hiện mật khẩu. |
| **Form & Inputs Collection** | Mã xác thực (UI-05) | Input field, `type="number"`, `maxlength=6`, `required=true`. |
| **Navigation & Actions** | Nút Đăng nhập | Button. Trigger luồng xác thực LDAP/LAMS. |
| **Navigation & Actions** | Nút Xác nhận (UI-05) | Button. Trigger luồng xác thực OTP. |
| **Navigation & Actions** | Nút Trở về (UI-05) | Button. Quay lại màn hình đăng nhập UI-01-a. |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| Radio Lựa chọn | Enabled | Click | Chuyển đổi giữa luồng xác thực LDAP và LAMS. |
| Tên đăng nhập | Enabled | Focus / Blur | Bôi đỏ khung input và báo lỗi "Vui lòng nhập địa chỉ email hợp lệ" nếu sai định dạng. |
| Icon Ẩn/Hiện Pass | Enabled | Click | Đổi type của input Mật khẩu giữa `text` và `password`. |
| Nút Đăng nhập | Enabled | Click | Báo lỗi inline nếu bỏ trống. Gọi API xác thực nếu hợp lệ. |
| Nút Xác nhận OTP | Enabled | Click | Báo lỗi inline nếu bỏ trống hoặc < 6 ký tự. Gọi API verify OTP. |

---

## 6. System Decomposition & Functional Logic

### 6.1 Sub-module 1: Đăng nhập (UC-DN-01)

**A. Workflows & Dependencies**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Người dùng | Nhập Email + Pass và Click Đăng nhập | Hệ thống gửi request sang LDAP (nếu chọn LDAP) hoặc Backend LAMS (nếu chọn LAMS). | LDAP thành công nhưng User không tồn tại ở LAMS -> Toast lỗi "Tài khoản chưa được khởi tạo...". | Lỗi 500 hoặc Timeout -> Toast lỗi "Không thể kết nối..." / "Hệ thống đang bận...". |
| 2 | Hệ thống | Kiểm tra trạng thái 2FA | Trạng thái Đã kích hoạt -> Chuyển sang màn UI-05. | Chưa kích hoạt -> Chuyển sang UI-04-a (Thiết lập 2FA). | Tài khoản bị khóa -> Báo lỗi "Tài khoản bị khóa...". |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Tên đăng nhập | Yes | Định dạng Email | N/A | "Vui lòng nhập địa chỉ email hợp lệ" |
| Mật khẩu | Yes | Định dạng Password | N/A | N/A |

**C. UI/UX Feedback**
* **Loading States:** Chưa được định nghĩa rõ trong UI-01-a (Cần làm rõ).
* **Toast Messages:** 
  - Lỗi mạng/500: "Không thể kết nối hệ thống xác thực. Vui lòng thử lại sau."
  - Lỗi Timeout: "Hệ thống đang bận. Vui lòng thử lại sau."
  - Lỗi LDAP/LAMS: "Tài khoản chưa được khởi tạo trên hệ thống LAMS..."
* **Inline Errors:** "Sai Tên đăng nhập hoặc Mật khẩu.", "Tài khoản bị khóa, vui lòng liên hệ với quản trị viên."

### 6.2 Sub-module 2: Xác thực 2 lớp (UC-2FA-05)

**A. Workflows & Dependencies**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Người dùng | Nhập OTP và Click Xác nhận | Hệ thống điều hướng đến chức năng đầu tiên theo phân quyền. | Token hết hạn -> Toast lỗi "Phiên xác thực đã hết hạn..." -> Quay về Đăng nhập. | Admin reset 2FA giữa chừng (403 REQUIRED_2FA) -> Toast lỗi "Xác thực thất bại..." -> Quay về Đăng nhập. |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Mã xác thực | Yes | Chỉ chứa số | Max 6 ký tự | "Mã xác thực không hợp lệ. Vui lòng thử lại" / "Vui lòng nhập mã xác thực" / "Mã xác thực không đúng..." |

**C. UI/UX Feedback**
* **Toast Messages:** "Phiên xác thực đã hết hạn. Vui lòng thử lại.", "Xác thực thất bại. Vui lòng thử lại."

---

## 7. Functional Integration Analysis (Ma trận & Tích hợp)

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Quản trị viên Reset 2FA (UC-2FA-07) | Trạng thái 2FA của User bị chuyển thành "Chưa kích hoạt" ngay lập tức. | Xác minh nếu User đang ở màn UI-05 và bấm Xác nhận, hệ thống phải bắt được lỗi 403 REQUIRED_2FA và đẩy ra màn đăng nhập. |
| Đăng nhập LDAP thành công | Chuyển luồng xác thực tiếp theo (LAMS Check). | Phải map được email LDAP với email có trong CSDL LAMS. |

---

## 8. Acceptance Criteria

⚠️ **MISSING:** Tài liệu không có bất kỳ dòng nào định nghĩa Acceptance Criteria (Given/When/Then).

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
| Q1 | High | N/A (Missing) | Thiếu hoàn toàn phần Acceptance Criteria (AC). | Không có tiêu chí nghiệm thu (Pass/Fail) rõ ràng cho QA thiết kế test cases. | Open |
| Q2 | Medium | UC-DN-01 (Basic Flow) | Chưa định nghĩa hành vi Loading State khi click nút "Đăng nhập". Nút có bị disable không? | Tránh việc user click nhiều lần (Spam request) gây lỗi hệ thống. | Open |
| Q3 | Medium | UI-01-a (Lựa chọn đăng nhập) | Khi user chuyển đổi giữa "Tài khoản LDAP" và "Tài khoản LAMS", form input (Email/Pass) có bị reset (xóa trắng) không? | Cần xác định UI Behavior cho việc reset form. | Open |

### 10.2 Dependencies
- Phụ thuộc hệ thống LDAP của Tổng công ty Vietnam Airlines.
- Phụ thuộc UC-2FA-04 (Kích hoạt 2FA) và UC-MK-02 (Reset mật khẩu).

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1.0 | 2026-04-21 | antigravity | Initial Audit dựa trên tài liệu yêu cầu LAMS. |

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
| 9 | Acceptance Criteria | 10 | 0 | ❌ |
| 10 | Non-functional Requirements | 5 | 5 | ⚡ |
| **Total** | | **110** | **100/110 → 90.9/100** | **❌ NOT READY** (Due to Auto-fail on #9) |

---
## 🟢 What's Good
Tài liệu được viết rất chi tiết ở phần Basic/Alternative/Exception flow. Các mã lỗi, nội dung Error Message, và Validation Rule của từng trường input (định dạng, độ dài) được định nghĩa rất cụ thể. Luồng Exception xử lý đứt kết nối LDAP và Timeout cũng đã được lường trước khá tốt.

## 🧪 Testability Outlook
**What CAN be tested now:**
- UI Validation (Maxlength, Required, Type Email).
- Luồng Happy path đăng nhập LDAP và LAMS.
- Luồng kiểm tra 2FA OTP.

**What CANNOT be tested yet (blocked by gaps):**
- Không có AC nên không thể chốt tiêu chuẩn nghiệm thu cuối cùng.
- Thiếu định nghĩa về Loading State/Spam click.

**Suggested test focus areas:**
- Negative Testing (BVA) cho mã OTP 6 ký tự.
- Test tích hợp (Integration): Giả lập Admin reset 2FA khi User đang nhập OTP (Mã lỗi 403 REQUIRED_2FA).
- Exception Testing: Giả lập LDAP timeout.

### 📌 Summary & Recommendation
Tài liệu nhìn chung có chất lượng phân tích luồng và validation rất tuyệt vời (Raw Score > 90/100). Tuy nhiên, **do thiếu hoàn toàn phần Acceptance Criteria (AC) - một hạng mục Bắt buộc (Critical)**, tài liệu này tạm thời bị đánh giá là **❌ NOT READY**. Khuyến nghị BA bổ sung AC và làm rõ thêm về form reset UI Behavior (Q3) trước khi QA tiến hành sinh Test Scenarios.
