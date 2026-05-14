# Performance Test Plan Template

**Dự án:** [Tên dự án]
**Mô đun:** [UC-ID] - [Tên chức năng]
**Kịch bản chính:** [Ví dụ: 100 Users truy cập đồng thời]

---

## 1. Mục tiêu (Objective)
Đánh giá khả năng chịu tải, tính ổn định và xác định điểm nghẽn (bottlenecks) của hệ thống [Tên chức năng] khi có nhiều người dùng thao tác cùng lúc.

## 2. Phạm vi kiểm thử (Scope)
- **Các API/Endpoint cần test:**
  - `POST /api/v1/...`
  - `GET /api/v1/...`
- **Các thành phần nằm ngoài phạm vi (Out of scope):**
  - Giao diện Frontend (Rendering).
  - Các hệ thống của bên thứ 3 (Thanh toán, Email Server) sẽ được mock.

## 3. Các kịch bản hiệu năng (Test Scenarios)

| ID | Loại Test | Mô tả Kịch bản | Số VUs (Concurrent Users) | Ramp-up (Tăng tải) | Thời gian duy trì (Duration) |
|---|---|---|---|---|---|
| **PT-01** | **Load Testing** | Kiểm tra sức chịu đựng ổn định với lượng tải dự kiến. | 100 | 30s | 5 phút |
| **PT-02** | **Spike Testing** | Kiểm tra khả năng sốc tải khi lượng người dùng tăng đột ngột. | 100 | 1s | 1 lần (Single iteration) |
| **PT-03** | **Stress Testing** | Đẩy tải vượt ngưỡng dự kiến để tìm giới hạn bẻ gãy (Breakpoint). | 300 - 500 | 60s | 10 phút |

## 4. Chỉ số kỳ vọng (Acceptance Criteria / KPIs)
Để một kịch bản được đánh giá là **PASS**, hệ thống phải thỏa mãn:
- **Tỷ lệ lỗi (Error Rate):** `< 1%` (Không có lỗi HTTP 500, 502, 504).
- **Thời gian phản hồi (Response Time):**
  - P90 (90% lượng request) hoàn thành dưới **2000ms**.
  - P99 hoàn thành dưới **5000ms**.
- **Thông lượng (Throughput):** Duy trì ổn định ở mức `X requests/sec`.

## 5. Dữ liệu & Thiết lập (Test Data & Setup)
### 5.1. Công cụ sử dụng
- **Tool giả lập tải:** JMeter / k6
- **Tool giám sát Server:** Grafana / Prometheus (RAM, CPU, I/O)

### 5.2. Chuẩn bị Dữ liệu (Test Data)
- **File Data:** `[tên_file].csv` chứa thông tin các user.
- **Tài khoản:** [Số lượng] tài khoản đã được kích hoạt trên môi trường Test/Staging.
- **Authentication/Bypass:** [Cơ chế bypass OTP/Captcha nếu có].

## 6. Quy trình thực thi API (Execution Steps)
*(Mô tả luồng các API sẽ chạy tuần tự trong JMeter/k6)*
1. **Request 1:** `POST /login` -> Trích xuất Token.
2. **Request 2:** `GET /data` kèm Token ở Header.
3. **Assertions:** Xác nhận HTTP Code trả về 200 OK.

## 7. Rủi ro & Cảnh báo (Risks & Monitoring)
- **Database Locks/Deadlocks:** Do [Lý do, VD: có nhiều câu lệnh UPDATE chạy cùng lúc].
- **Rate Limiting/WAF:** Tường lửa Nginx có thể chặn tải. Cần Whitelist IP của máy chạy Load Test.
- **Memory Leak:** Giám sát RAM backend sau khi dứt tải xem có hạ nhiệt độ không.
