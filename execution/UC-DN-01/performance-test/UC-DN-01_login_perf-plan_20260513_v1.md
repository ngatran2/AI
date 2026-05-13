# Performance Test Plan

**Dự án:** LAMS (JOYS-V3)
**Mô đun:** UC-DN-01 - Login 2FA
**Kịch bản chính:** 4 Users truy cập đồng thời, Ramp-up 1p, Duration 3p.

---

## 1. Mục tiêu (Objective)
Đánh giá khả năng chịu tải và tính ổn định của tính năng Đăng nhập (Login) kết hợp xác thực 2FA khi có nhiều tài khoản truy cập đồng thời, đảm bảo hệ thống không bị nghẽn tại bước xử lý Token hoặc sinh OTP.

## 2. Phạm vi kiểm thử (Scope)
- **Các API/Endpoint cần test:**
  - `POST https://lams-api.sotatek.works/api/v1/auth/login` (Xác thực User/Pass)
  - `POST https://lams-api.sotatek.works/api/v1/auth/verify-otp` (Xác thực 2FA OTP)
- **Các thành phần nằm ngoài phạm vi (Out of scope):**
  - Giao diện Frontend.
  - Tốc độ gửi Email/SMS OTP (vì OTP được sinh nội bộ qua Secret Key).

## 3. Các kịch bản hiệu năng (Test Scenarios)

| ID | Loại Test | Mô tả Kịch bản | Số VUs (Concurrent Users) | Ramp-up (Tăng tải) | Thời gian duy trì (Duration) |
|---|---|---|---|---|---|
| **PT-DN01-01** | **Load Testing** | Kiểm tra tải ổn định theo yêu cầu người dùng. | 4 | 60s | 3 phút |
| **PT-DN01-02** | **Stress Testing** | Đề xuất: Kiểm tra giới hạn bẻ gãy (Breakpoint). | 20 - 50 | 2 phút | 5 phút |

## 4. Chỉ số kỳ vọng (Acceptance Criteria / KPIs)
Để một kịch bản được đánh giá là **PASS**, hệ thống phải thỏa mãn:
- **Tỷ lệ lỗi (Error Rate):** `< 10%` (Theo yêu cầu người dùng).
- **Thời gian phản hồi (Response Time):**
  - P95 hoàn thành dưới **5000ms** (Theo yêu cầu người dùng).
- **Thông lượng (Throughput):** Duy trì ổn định, không có hiện tượng tụt giảm đột ngột (Drop) khi tải tăng.

## 5. Dữ liệu & Thiết lập (Test Data & Setup)
### 5.1. Công cụ sử dụng
- **Tool giả lập tải:** JMeter
- **Thư viện bổ trợ:** `pyotp` (để mô phỏng sinh mã OTP trong script).

### 5.2. Chuẩn bị Dữ liệu (Test Data)
- **File Data:** `accounts.csv` chứa thông tin `email`, `password`, `secret_key`.
- **Tài khoản:** 4 tài khoản Admin đã được kích hoạt trên môi trường Staging.
- **2FA:** Sử dụng cơ chế sinh mã OTP thời gian thực từ Secret Key để bypass việc nhập mã thủ công.

## 6. Quy trình thực thi API (Execution Steps)
1. **Request 1:** `POST /api/v1/auth/login`
   - Input: email, password từ CSV.
   - Output: Trích xuất `transaction_id` hoặc trạng thái chờ OTP.
2. **Groovy Script:** Sinh mã OTP 6 số từ `secret_key` bằng thuật toán TOTP.
3. **Request 2:** `POST /api/v1/auth/verify-otp`
   - Input: otp_code + session info.
   - Output: Trích xuất `access_token`.
4. **Assertions:** Xác nhận HTTP Code trả về 201 Created và có chứa `access_token`.

## 7. Rủi ro & Cảnh báo (Risks & Monitoring)
- **Rate Limiting:** Server có thể chặn IP nếu gửi quá nhiều request login trong thời gian ngắn (cần check WAF).
- **OTP Synchronization:** Thời gian trên máy chạy JMeter phải đồng bộ với Server để mã OTP sinh ra có hiệu lực (sai lệch < 30s).
- **Data Dependency:** Các tài khoản test không được bị khóa (Locked) trong quá trình chạy.
