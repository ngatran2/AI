## ✅ Detail-Level Test Design Complete

| Artifact | File | Count |
|---|---|---|
| Test Cases (DET) | UC-DN-01-2FA-05_login_testcases-det_20260509_v1.xlsx | 22 cases (3 GUI / 19 FUNC) |
| RTM Report | UC-DN-01-2FA-05_login_testcases-det_20260509_v1_rtm.md | AC coverage: 100% |

### Requirement Traceability Matrix
| AC ID / Rule | Acceptance Criteria | Linked Test Cases | Status |
|---|---|---|---|
| AC-01 | Đăng nhập LAMS thành công | TC_UCDN01_FUNC_07, TC_UCDN01_FUNC_06 | Covered |
| AC-02 | Xác thực OTP thành công | TC_UC2FA05_FUNC_07 | Covered |
| CMR-03 | Trim khoảng trắng | TC_UCDN01_FUNC_04 | Covered |
| CMR-07 | Required field | TC_UCDN01_FUNC_02 | Covered |
| CMR-12 | Loading State | TC_UCDN01_FUNC_08, TC_UC2FA05_FUNC_08, TC_UCDN01_FUNC_09 | Covered |
| REQ-DN-03 | Đăng nhập tài khoản khóa / Lỗi hệ thống | TC_UCDN01_FUNC_05, TC_UCDN01_FUNC_09 | Covered |
| REQ-DN-02 | Form Validation | TC_UCDN01_FUNC_02, TC_UCDN01_FUNC_03 | Covered |
| REQ-2FA-02 | Form Validation OTP (BVA/Format) | TC_UC2FA05_FUNC_02, TC_UC2FA05_FUNC_03 | Covered |
| REQ-2FA-03 | Lỗi OTP, Timeout, Reset 2FA | TC_UC2FA05_FUNC_04, TC_UC2FA05_FUNC_05, TC_UC2FA05_FUNC_06 | Covered |
| UI-01-a / UI-05 | Screen Initialization | TC_UCDN01_GUI_01, TC_UC2FA05_GUI_01 | Covered |
| REQ-SECURITY | SQL Injection / XSS | TC_UCDN01_FUNC_10 | Covered |
| REQ-LOGIC | Sai Mật khẩu | TC_UCDN01_FUNC_11 | Covered |

### Self-Review Results
| # | Weakness Found | Action Taken |
|---|---|---|
| 1 | Thiếu test data injection (XSS/SQLi) | Thêm `TC_UCDN01_FUNC_10` cho Security Injection để thử SQLi vào Email. |
| 2 | Chưa rõ hành vi kiểm tra Validation sai password (AC không đề cập rõ). | Thêm `TC_UCDN01_FUNC_11` để mô tả chi tiết trường hợp nhập sai Mật khẩu. |
| 3 | AC-01/02 đã bao phủ, nhưng thiếu kịch bản Đăng nhập thành công mà chưa setup 2FA. | Thêm `TC_UCDN01_FUNC_06` xử lý Happy Path chuyển hướng sang màn kích hoạt 2FA. |

### Notes
- LDAP Đã loại bỏ khỏi Scope nên không có TC nào liên quan.
- Trường hợp quên mật khẩu (UC-DN-02) nằm ngoài phạm vi UC này nên không thiết kế TC.
- Performance / Load Testing không nằm trong Scope của bộ test này.
