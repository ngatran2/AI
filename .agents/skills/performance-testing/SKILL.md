---
name: performance-testing
description: Sinh kế hoạch kiểm thử hiệu năng (Performance Test Plan) và hỗ trợ viết script (JMeter/k6) từ tài liệu requirement hoặc Use Case. Trigger khi user nói "viết performance test plan", "tạo script jmeter", "load test".
---
# Performance Testing Skill

## Purpose
Tạo Kế hoạch Kiểm thử Hiệu năng (Performance Test Plan) và hỗ trợ sinh kịch bản/scripts tự động hóa (JMeter JMX cấu hình, Groovy scripts, k6 JavaScript) dựa trên tài liệu đặc tả nghiệp vụ (UC/Requirement).

## Khi nào kích hoạt?
Khi người dùng yêu cầu:
- "Viết Performance Test Plan cho UC-XXX"
- "Tạo script JMeter cho chức năng Y"
- "Làm thế nào để load test 1000 users cho hệ thống này"

## Đầu vào (Input)
1. Tài liệu requirement (đã audit) hoặc mô tả chức năng từ người dùng.
2. Thông số tải kỳ vọng (VD: 100 users, 1000 concurrent users).
3. (Tùy chọn) Yêu cầu cụ thể về công cụ (JMeter, k6, Gatling).

## Quy trình thực hiện (Workflow)

### Phase 1: Phân tích Kịch bản & Dữ liệu
1. Đọc và hiểu luồng nghiệp vụ của tính năng cần test.
2. Xác định các API/Endpoints chịu tải chính (Thường là các API có lưu trữ Data, Login, Export, Search phức tạp).
3. Phân tích các ràng buộc về Dữ liệu (VD: API cần Access Token, cần xử lý OTP, cần tạo dữ liệu ngẫu nhiên chống trùng lặp).

### Phase 1.5: Xác nhận thông số tải & KPIs (USER INPUT)
BẮT BUỘC hỏi người dùng các thông số sau trước khi sinh Phase 2:
1. **Thông số tải:** Số lượng Concurrent Users (VUs), thời gian chạy (Duration), công cụ (JMeter/k6).
2. **Tiêu chí đánh giá (KPIs):** Ngưỡng Response Time tối đa (P95), Error Rate cho phép.
3. **Môi trường:** URL/IP của hệ thống mục tiêu.

*Ghi chú:* Nếu người dùng không cung cấp thông tin hoặc yêu cầu "tự suggest", Agent sẽ đưa ra đề xuất dựa trên kinh nghiệm (VD: Staging: 50-100 VUs, Production: 500-1000 VUs) và yêu cầu người dùng xác nhận lại.

### Phase 2: Sinh Performance Test Plan
Dùng template `template/perf_test_plan_template.md` để sinh ra bản kế hoạch chi tiết dựa trên các thông số đã được người dùng xác nhận ở Phase 1.5.

### Phase 3: Sinh Script / Thiết lập Công cụ (Nếu User yêu cầu)
Nếu User yêu cầu script (VD: JMeter, k6):
- **Với JMeter:** 
  - Khuyên người dùng thiết lập UI các bước cơ bản (Thread Group, HTTP Request).
  - Cung cấp các đoạn script xử lý logic khó (PreProcessor bằng Groovy, Regular Expression Extractor, JSON Extractor).
  - Cung cấp file CSV Data mẫu để load.
- **Với k6:**
  - Viết hoàn chỉnh đoạn script `.js` chứa kịch bản load test (VU, Duration, Stages, HTTP requests, Checks).
  
## Tiêu chí đánh giá (Evaluation Criteria)
Các tệp sinh ra từ skill này PHẢI đáp ứng các tiêu chuẩn sau:
1. **Alignment (Tính Nhất quán):** Test Plan phải khớp 100% với các thông số tải và KPIs mà User đã nhập (hoặc đã xác nhận từ Suggestion) ở Phase 1.5.
2. **Dynamic Data Capability (Khả năng xử lý Dữ liệu Động):** Kịch bản/Script không được hardcode Token hay OTP. Phải có Regex/JSON Extractor (với JMeter) hoặc tương đương (với k6) để tự động bắt thông tin từ bước Auth.
3. **Data Integrity Check (Tính Toàn vẹn Dữ liệu):** Code sinh ra phải chứa thuật toán ngẫu nhiên hóa dữ liệu gửi lên (ví dụ: Random string, Timestamp) để tránh lỗi trùng lặp khi chạy vòng lặp (Loop).
4. **Metric Definition:** Kế hoạch phải rõ ràng các ngưỡng Baseline (Hiện tại) vs Target (Kỳ vọng) để có cơ sở nghiệm thu.

## Anti-Hallucination Guardrails & Boundaries
1. **No Direct Execution:** Agent TUYỆT ĐỐI KHÔNG được tự ý chạy các script k6 hoặc JMeter (VD: không dùng lệnh terminal để gõ `k6 run`). Skill này CHỈ phục vụ việc sinh ra Test Plan và Script code. Việc chạy thực tế phải do người dùng tự thực hiện.
2. KHÔNG bịa đặt API endpoints nếu tài liệu không cung cấp. Hãy để dưới dạng `[API_ENDPOINT_TBD]`.
3. PHẢI cảnh báo người dùng về việc Rate Limit / WAF có thể block các công cụ load test.
4. PHẢI đề xuất giải pháp xử lý Dữ liệu động (Dynamic Data) như Token, OTP, UUID. Nếu bỏ qua bước Extract Token, load test sẽ fail ở lỗi 401.

## Output Contract
- File Test Plan (.md).
- File Test Data (.csv) (nếu cần).
- Hướng dẫn cấu hình công cụ chi tiết hoặc Script code (K6/Groovy) cung cấp qua giao diện chat.
