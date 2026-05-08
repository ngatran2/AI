# Test Scenarios

> [!WARNING]
> **Human Checkpoint:** User cần review danh sách High-Level Scenarios dưới đây để bổ sung các trường hợp rủi ro đặc thù (nếu có) trước khi Agent tiến hành sinh Test Cases chi tiết ở bước tiếp theo.

## 1. Traceability Matrix & Gap Analysis

| Req-ID | Module / Feature | Covered by Scenarios | Status |
|--------|------------------|----------------------|--------|
| REQ-DN-01 | Đăng nhập Happy Path (AC-01) | TS_DN01_001 | Covered |
| REQ-DN-02 | Validation Form Đăng nhập | TS_DN01_002, 003, 004 | Covered |
| REQ-DN-03 | Đăng nhập sai/lỗi (Exception) | TS_DN01_005, 006, 007 | Covered |
| REQ-DN-04 | UI State (Loading Disable) | TS_DN01_008 | Covered |
| REQ-2FA-01 | Xác thực OTP Happy Path (AC-02) | TS_2FA05_001 | Covered |
| REQ-2FA-02 | Validation Form OTP (BVA & EP) | TS_2FA05_002, 003, 005 | Covered |
| REQ-2FA-03 | OTP sai/lỗi (Exception & Integration) | TS_2FA05_004, 006, 007 | Covered |
| REQ-2FA-04 | UI State (Loading Disable) | TS_2FA05_008 | Covered |

*(100% Yêu cầu đã được bao phủ bởi kịch bản kiểm thử, không có orphaned requirements).*

## 2. Detailed Scenarios

### UC-DN-01 — Đăng nhập LAMS

### Scenario ID: TS_DN01_001
**Scenario Title:** Đăng nhập thành công với tài khoản LAMS (2FA đã kích hoạt)
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-01
**Test Type:** Functional
**Description:** Kiểm tra hệ thống điều hướng sang màn hình nhập mã xác thực (UI-05) khi nhập đúng email và password của tài khoản LAMS.
**Test Focus:** Happy path

### Scenario ID: TS_DN01_002
**Scenario Title:** Đăng nhập với trường Email bỏ trống
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-02
**Test Type:** UI
**Description:** Kiểm tra hệ thống hiển thị lỗi inline khi người dùng bỏ trống trường Email và bấm Đăng nhập.
**Test Focus:** Error/Exception

### Scenario ID: TS_DN01_003
**Scenario Title:** Đăng nhập với trường Password bỏ trống
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-02
**Test Type:** UI
**Description:** Kiểm tra hệ thống hiển thị lỗi inline khi người dùng bỏ trống trường Password và bấm Đăng nhập.
**Test Focus:** Error/Exception

### Scenario ID: TS_DN01_004
**Scenario Title:** Đăng nhập với định dạng Email không hợp lệ
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-02
**Test Type:** UI
**Description:** Kiểm tra hệ thống bôi đỏ khung input và báo lỗi "Vui lòng nhập địa chỉ email hợp lệ" khi email sai format (EP).
**Test Focus:** Boundary / Validation

### Scenario ID: TS_DN01_005
**Scenario Title:** Đăng nhập sai tên đăng nhập hoặc mật khẩu
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-03
**Test Type:** Functional
**Description:** Kiểm tra hệ thống báo lỗi "Sai Tên đăng nhập hoặc Mật khẩu." khi nhập sai thông tin.
**Test Focus:** Alternative flow

### Scenario ID: TS_DN01_006
**Scenario Title:** Đăng nhập bằng tài khoản đang bị khóa
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-03
**Test Type:** Functional
**Description:** Kiểm tra hệ thống hiển thị thông báo "Tài khoản bị khóa, vui lòng liên hệ với quản trị viên." khi tài khoản LAMS bị vô hiệu hóa.
**Test Focus:** Error/Exception

### Scenario ID: TS_DN01_007
**Scenario Title:** Đăng nhập khi Backend LAMS lỗi 500 hoặc Timeout
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-03
**Test Type:** Integration
**Description:** Kiểm tra hệ thống hiển thị Toast message "Không thể kết nối hệ thống xác thực. Vui lòng thử lại sau." (500) hoặc "Hệ thống đang bận. Vui lòng thử lại sau." (Timeout).
**Test Focus:** Error/Exception

### Scenario ID: TS_DN01_008
**Scenario Title:** Kiểm tra Loading State khi đang gửi yêu cầu đăng nhập
**UC Reference:** UC-DN-01 Đăng nhập
**Req-ID:** REQ-DN-04
**Test Type:** UI
**Description:** Kiểm tra nút Đăng nhập chuyển trạng thái Disabled trong quá trình gọi API, ngăn user spam click.
**Test Focus:** UI State

---

### UC-2FA-05 — Xác thực 2 lớp khi đăng nhập

### Scenario ID: TS_2FA05_001
**Scenario Title:** Xác thực mã OTP thành công
**UC Reference:** UC-2FA-05 Xác thực 2 lớp khi đăng nhập
**Req-ID:** REQ-2FA-01
**Test Type:** Functional
**Description:** Kiểm tra hệ thống điều hướng vào màn Hệ thống/Quản lý người dùng sau khi nhập mã OTP 6 số hợp lệ.
**Test Focus:** Happy path

### Scenario ID: TS_2FA05_002
**Scenario Title:** Xác nhận OTP với trường mã xác thực bỏ trống
**UC Reference:** UC-2FA-05 Xác thực 2 lớp khi đăng nhập
**Req-ID:** REQ-2FA-02
**Test Type:** UI
**Description:** Kiểm tra hệ thống báo lỗi "Vui lòng nhập mã xác thực" khi bấm Xác nhận mà không nhập OTP.
**Test Focus:** Error/Exception

### Scenario ID: TS_2FA05_003
**Scenario Title:** Xác nhận OTP với độ dài mã dưới 6 ký tự (BVA)
**UC Reference:** UC-2FA-05 Xác thực 2 lớp khi đăng nhập
**Req-ID:** REQ-2FA-02
**Test Type:** UI
**Description:** Nhập 5 ký tự số (Limit - 1) và kiểm tra lỗi "Mã xác thực không hợp lệ. Vui lòng thử lại".
**Test Focus:** Boundary

### Scenario ID: TS_2FA05_004
**Scenario Title:** Xác nhận OTP với mã xác thực sai (đủ 6 số)
**UC Reference:** UC-2FA-05 Xác thực 2 lớp khi đăng nhập
**Req-ID:** REQ-2FA-03
**Test Type:** Functional
**Description:** Nhập đủ 6 số nhưng sai OTP so với Google Authenticator, kiểm tra thông báo "Mã xác thực không đúng. Vui lòng thử lại."
**Test Focus:** Alternative flow

### Scenario ID: TS_2FA05_005
**Scenario Title:** Xác nhận OTP chỉ cho phép nhập ký tự số
**UC Reference:** UC-2FA-05 Xác thực 2 lớp khi đăng nhập
**Req-ID:** REQ-2FA-02
**Test Type:** UI
**Description:** Cố gắng nhập ký tự chữ (a-z) hoặc ký tự đặc biệt (!@#) vào trường OTP để đảm bảo UI chặn nhập (Numeric only).
**Test Focus:** Boundary / UI State

### Scenario ID: TS_2FA05_006
**Scenario Title:** Hết hạn Token (Timeout) khi đang ở màn OTP
**UC Reference:** UC-2FA-05 Xác thực 2 lớp khi đăng nhập
**Req-ID:** REQ-2FA-03
**Test Type:** Integration
**Description:** Chờ hết thời gian hiệu lực của pre-authorize token, bấm Xác nhận, kiểm tra Toast lỗi "Phiên xác thực đã hết hạn..." và hệ thống đẩy ra màn Đăng nhập.
**Test Focus:** Error/Exception

### Scenario ID: TS_2FA05_007
**Scenario Title:** Admin Reset 2FA trong lúc User đang nhập OTP (Lỗi 403 REQUIRED_2FA)
**UC Reference:** UC-2FA-05 Xác thực 2 lớp khi đăng nhập
**Req-ID:** REQ-2FA-03
**Test Type:** Integration / Cross-function
**Description:** Giả lập Admin thiết lập lại 2FA (UC-2FA-07), User bấm Xác nhận OTP, kiểm tra hệ thống bắt lỗi 403, báo Toast "Xác thực thất bại..." và đẩy ra màn Đăng nhập.
**Test Focus:** Alternative flow

### Scenario ID: TS_2FA05_008
**Scenario Title:** Kiểm tra Loading State khi đang gửi yêu cầu xác thực OTP
**UC Reference:** UC-2FA-05 Xác thực 2 lớp khi đăng nhập
**Req-ID:** REQ-2FA-04
**Test Type:** UI
**Description:** Kiểm tra nút Xác nhận chuyển trạng thái Disabled trong quá trình gọi API verify OTP.
**Test Focus:** UI State

---

## ⚠️ Out-of-Scope Flags

| Scenario Area | Reason | Recommended Action |
|--------------|--------|--------------------|
| Đăng nhập bằng LDAP | BA đã xác nhận loại bỏ LDAP khỏi scope test. | Bỏ qua toàn bộ luồng LDAP. |
