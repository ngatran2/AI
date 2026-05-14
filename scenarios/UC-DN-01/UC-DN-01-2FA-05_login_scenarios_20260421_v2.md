# Test Scenarios (v2)
**Project: LAMS (VNA)**
**Use Cases: UC-DN-01 (Đăng nhập) & UC-2FA-05 (Xác thực 2FA)**

---

> [!IMPORTANT]
> **MANDATORY RULES APPLIED:**
> - CMR-03: Tự động Trim khoảng trắng đầu/cuối cho Email.
> - CMR-12: Nút bấm chuyển sang Loading/Disabled khi gọi API xác thực.
> - CMR-04: Thông báo lỗi/thành công qua Toast ở góc dưới bên trái (5s).

---

## 1. Traceability Matrix & Gap Analysis

| Req-ID | Module / Feature | Covered by Scenarios | Status |
|--------|------------------|----------------------|--------|
| REQ-DN-01 | Đăng nhập Happy Path | TS_DN01_001 | Covered |
| REQ-DN-02 | Form Validation | TS_DN01_002, 003, 004, 005 | Covered |
| REQ-DN-03 | Exception Handling | TS_DN01_006, 007 | Covered |
| REQ-2FA-01 | 2FA Happy Path | TS_2FA05_001 | Covered |
| REQ-2FA-02 | 2FA Validation (BVA) | TS_2FA05_002, 003, 004 | Covered |
| REQ-2FA-03 | 2FA Exception | TS_2FA05_005, 006 | Covered |
| CMR-03 | Trim Space Rule | TS_DN01_005 | Covered |
| CMR-12 | Loading State Rule | TS_DN01_008, TS_2FA05_007 | Covered |

---

## 2. Detailed Scenarios

### UC-DN-01 — Đăng nhập LAMS

### Scenario ID: TS_DN01_001
**Scenario Title:** Đăng nhập thành công với tài khoản LAMS hợp lệ
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-01
**Test Type:** Functional
**Description:** Nhập email và mật khẩu đúng, hệ thống điều hướng đến màn hình nhập mã xác thực OTP (UI-05).
**Test Focus:** Happy path

### Scenario ID: TS_DN01_002
**Scenario Title:** Đăng nhập với tài khoản chưa kích hoạt 2FA
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-03
**Test Type:** Functional
**Description:** Nhập thông tin đúng nhưng user chưa setup 2FA, hệ thống điều hướng sang luồng kích hoạt 2FA (UC-2FA-04).
**Test Focus:** Alternative flow

### Scenario ID: TS_DN01_003
**Scenario Title:** Validation - Email sai định dạng
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-02
**Test Type:** UI/Validation
**Description:** Nhập email thiếu "@" hoặc domain, kiểm tra lỗi bôi đỏ và thông báo "Vui lòng nhập địa chỉ email hợp lệ".
**Test Focus:** Error/Exception

### Scenario ID: TS_DN01_004
**Scenario Title:** Validation - Bỏ trống trường bắt buộc
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-02
**Test Type:** UI/Validation
**Description:** Để trống Email hoặc Mật khẩu, bấm Đăng nhập, kiểm tra thông báo lỗi "{Field} là trường bắt buộc".
**Test Focus:** Error/Exception

### Scenario ID: TS_DN01_005
**Scenario Title:** CMR-03 - Tự động Trim khoảng trắng Email
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** CMR-03
**Test Type:** Data Integrity
**Description:** Nhập "  admin@lams.com  " (có space đầu/cuối), hệ thống tự động trim và đăng nhập thành công.
**Test Focus:** Boundary

### Scenario ID: TS_DN01_006
**Scenario Title:** Đăng nhập bằng tài khoản đang bị khóa
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-03
**Test Type:** Security
**Description:** Nhập account có trạng thái `isActive = false`, kiểm tra thông báo "Tài khoản bị khóa...".
**Test Focus:** Error/Exception

### Scenario ID: TS_DN01_007
**Scenario Title:** API Timeout / Server Error (500)
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** CMR-12/REQ-DN-03
**Test Type:** Integration
**Description:** Giả lập lỗi 500 hoặc mạng chậm > 60s, kiểm tra Toast "Hệ thống đang bận. Vui lòng thử lại sau.".
**Test Focus:** Error/Exception

### Scenario ID: TS_DN01_008
**Scenario Title:** CMR-12 - Loading State cho nút Đăng nhập
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** CMR-12
**Test Type:** UI State
**Description:** Trong khi đang gọi API xác thực, nút [Đăng nhập] phải ở trạng thái Disabled và hiển thị Spinner.
**Test Focus:** UI State

---

### UC-2FA-05 — Xác thực 2 lớp khi đăng nhập

### Scenario ID: TS_2FA05_001
**Scenario Title:** Xác thực mã OTP thành công
**UC Reference:** UC-2FA-05 Xác thực 2 lớp
**Req-ID:** REQ-2FA-01
**Test Type:** Functional
**Description:** Nhập đúng 6 số OTP từ Google Authenticator, hệ thống điều hướng vào Dashboard.
**Test Focus:** Happy path

### Scenario ID: TS_2FA05_002
**Scenario Title:** Validation - OTP không đủ 6 số (BVA)
**UC Reference:** UC-2FA-05 Xác thực 2 lớp
**Req-ID:** REQ-2FA-02
**Test Type:** UI/Boundary
**Description:** Nhập 5 số, kiểm tra hệ thống báo lỗi "Mã xác thực không hợp lệ".
**Test Focus:** Boundary

### Scenario ID: TS_2FA05_003
**Scenario Title:** Validation - OTP chứa ký tự không phải số
**UC Reference:** UC-2FA-05 Xác thực 2 lớp
**Req-ID:** REQ-2FA-02
**Test Type:** UI/Validation
**Description:** Cố gắng nhập chữ hoặc ký tự đặc biệt, kiểm tra UI chặn không cho nhập (Numeric only).
**Test Focus:** Error/Exception

### Scenario ID: TS_2FA05_004
**Scenario Title:** Xác thực mã OTP sai
**UC Reference:** UC-2FA-05 Xác thực 2 lớp
**Req-ID:** REQ-2FA-03
**Test Type:** Functional
**Description:** Nhập sai 6 số OTP, kiểm tra thông báo Toast "Mã xác thực không đúng. Vui lòng thử lại."
**Test Focus:** Alternative flow

### Scenario ID: TS_2FA05_005
**Scenario Title:** Nút [Trở về] màn hình đăng nhập
**UC Reference:** UC-2FA-05 Xác thực 2 lớp
**Req-ID:** UI-05
**Test Type:** UI/Navigation
**Description:** Bấm nút [Trở về], hệ thống quay lại màn hình Login (UI-01-a).
**Test Focus:** UI State

### Scenario ID: TS_2FA05_006
**Scenario Title:** Session Timeout khi đang ở màn OTP
**UC Reference:** UC-2FA-05 Xác thực 2 lớp
**Req-ID:** REQ-2FA-03
**Test Type:** Integration
**Description:** Token tạm hết hạn (sau 5-10p), bấm Xác nhận, Toast báo lỗi và đẩy ra màn Login.
**Test Focus:** Error/Exception

### Scenario ID: TS_2FA05_007
**Scenario Title:** CMR-12 - Loading State cho nút Xác nhận (OTP)
**UC Reference:** UC-2FA-05 Xác thực 2 lớp
**Req-ID:** CMR-12
**Test Type:** UI State
**Description:** Nút [Xác nhận] phải bị disable khi đang verify OTP với backend.
**Test Focus:** UI State

---

## ⚠️ Out-of-Scope Flags

| Scenario Area | Reason | Recommended Action |
|--------------|--------|--------------------|
| Đăng nhập LDAP | BA xác nhận loại khỏi scope. | Không thiết kế test. |
| Quên mật khẩu | Nằm ở UC khác (UC-DN-02). | Tham chiếu UC-DN-02. |

---
*Generated by qa-engineer agent.*
