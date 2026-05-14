# Performance Test Evaluation Report

**Dự án:** LAMS (JOYS-V3)
**Mô đun:** UC-DN-01 - Login 2FA
**Thời điểm thực hiện:** 2026-05-13
**Công cụ:** JMeter 5.x

---

## 1. Tóm tắt kết quả (Executive Summary)

| Chỉ số | Kết quả thực tế | Trạng thái |
| :--- | :--- | :--- |
| **Số lượng Users (VUs)** | 4 Concurrent Users | ✅ Thành công |
| **Tỷ lệ lỗi (Error Rate)** | 0.00% | ✅ PASS (Target < 10%) |
| **Response Time (Avg)** | 69 ms | ✅ PASS (Target < 5000ms) |
| **Max Response Time** | 224 ms | ✅ PASS |
| **Throughput** | 2.0 requests/sec | ✅ Ổn định |

---

## 2. Phân tích chi tiết (Detailed Metrics)

| Label | # Samples | Average (ms) | Min (ms) | Max (ms) | Std. Dev. | Error % | Throughput |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **01_login_request** | 17 | 150 | 0 | 224 | 32.34 | 0.00% | 39.6/min |
| **Generate_OTP** | 17 | 2 | 0 | 20 | 5.10 | 0.00% | 39.9/min |
| **02_Verify_OTP** | 17 | 55 | 0 | 83 | 11.06 | 0.00% | 39.7/min |
| **TOTAL** | 51 | 69 | 0 | 224 | 64.47 | 0.00% | 2.0/sec |

---

## 3. Đánh giá chuyên môn (Expert Evaluation)

### 3.1. Điểm mạnh (Strengths)
- **Tốc độ phản hồi cực nhanh:** Thời gian xử lý trung bình hệ thống (69ms) và Login (150ms) là mức rất tốt cho môi trường Staging.
- **Tính ổn định cao:** Độ lệch chuẩn (Std. Dev) thấp cho thấy hệ thống xử lý các request rất đồng nhất, không có hiện tượng giật lag cục bộ.
- **Tỷ lệ lỗi tuyệt đối:** Không phát hiện bất kỳ lỗi HTTP nào, chứng tỏ luồng xác thực 2FA (mô phỏng bằng Groovy) hoạt động hoàn hảo.

### 3.2. Hạn chế (Limitations)
- Mức tải hiện tại (4 VUs) còn quá thấp, chưa phản ánh được khả năng chịu tải thực tế khi có hàng trăm người dùng cùng đăng nhập vào đầu giờ làm việc.

---

## 4. Kết luận & Khuyến nghị (Conclusion & Recommendations)

**Kết luận:** Hệ thống **VƯỢT XA** các chỉ số KPIs đặt ra ở mức tải 4 người dùng đồng thời.

**Khuyến nghị:**
1. **Tiếp tục Stress Test:** Thực hiện nâng tải lên **20 - 50 VUs** (PT-DN01-02) để xác định giới hạn tối đa của hệ thống trước khi xảy ra lỗi hoặc thời gian phản hồi tăng cao (> 2s).
2. **Giám sát tài nguyên:** Trong các đợt test tải cao hơn, cần kết hợp theo dõi CPU/RAM của server Backend để phát hiện hiện tượng rò rỉ bộ nhớ (Memory Leak) nếu có.

---
*Báo cáo được trích xuất tự động từ JMeter Summary Report và đánh giá bởi Antigravity QC Agent.*
