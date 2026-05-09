# Performance Test Plan: UC-DM-11 Card Category Management
**Dự án:** JOYS-V3 LAMS
**Module:** Quản lý danh mục loại thẻ (UC-DM-11)
**Ngày tạo:** 2026-05-09
**Phiên bản:** v2 (Updated for JMeter)

---

## 1. Mục tiêu kiểm thử (Objectives)
Đánh giá độ ổn định và hiệu năng của hệ thống khi xử lý các thao tác quản lý danh mục thẻ hội viên dưới áp lực tải thực tế bằng công cụ Apache JMeter.
- Xác định Response Time của các API Danh mục.
- Kiểm tra khả năng xử lý concurrency (100 threads).
- Đảm bảo cơ chế trích xuất Dynamic Token (JSON Extractor) hoạt động ổn định.

## 2. Phạm vi kiểm thử (Scope)
Tập trung vào các API Endpoints chịu tải chính:
1. **Auth:** `POST /api/v1/auth/login` (Lấy Token).
2. **Read:** `GET /api/v1/card-categories` (Phân trang 20 records).
3. **Write:** `POST /api/v1/card-categories` (Thêm mới thẻ hội viên).

## 3. Cấu hình tải (Load Profile - SMOKE TEST)
| Thông số | Giá trị | Ghi chú |
| :--- | :--- | :--- |
| **Tool** | **Apache JMeter 5.5+** | Công cụ kiểm thử |
| **Thread Group** | 15 Threads | Kiểm tra tính đúng đắn của script |
| **Ramp-up Period** | 30 seconds | Tăng dần mỗi 2 giây |
| **Loop Count** | 5 Loops | Chạy nhanh để verify logic |
| **Think Time** | Constant Timer | 2000ms |

## 4. Cấu hình Script JMeter (JMX Highlights)
- **JSON Extractor:** Trích xuất `$.token` từ login response để nạp vào Header Manager.
- **CSV Data Set Config:** Nạp dữ liệu `airline_id`, `card_type` từ file CSV để randomize dữ liệu test.
- **Random Code:** Sử dụng hàm `${__time(YMDHMS,)}` để tạo `Mã thẻ` duy nhất, tránh lỗi trùng lặp dữ liệu (BR-11.3).

## 5. Tiêu chí đánh giá (Thresholds / KPIs)
| Metric | Ngưỡng đạt (SLA) | Priority |
| :--- | :--- | :--- |
| **Response Time (P95)** | < 2000 ms | CRITICAL |
| **Error Rate** | < 1% | CRITICAL |
| **Successful Auth** | 100% | CRITICAL |

---

## 6. Hướng dẫn thực thi (Execution Guide)

### Chạy bằng Giao diện (GUI Mode - Dành cho Debug)
1. Mở JMeter.
2. Chọn **File -> Open** trỏ tới file `UC-DM-11_card-category_load-test_v1.jmx`.
3. Nhấn **Start** (nút xanh) và xem kết quả tại **View Results Tree**.

### Chạy bằng Dòng lệnh (CLI Mode - Khuyên dùng)
Để kết quả chính xác và không tốn tài nguyên RAM:
```bash
jmeter -n -t UC-DM-11_card-category_load-test_v1.jmx -l results.jtl -e -o ./report-folder
```
- `-n`: Non-GUI mode.
- `-t`: Đường dẫn file kịch bản.
- `-l`: File lưu log kết quả.
- `-e -o`: Tự động xuất báo cáo HTML Dashboard.

---
**Antigravity QA System** - *Performance Engineering Unit*
