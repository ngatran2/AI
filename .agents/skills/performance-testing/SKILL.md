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

### Phase 2: Sinh Performance Test Plan
Dùng template `template/perf_test_plan_template.md` để sinh ra bản kế hoạch chi tiết.
- Đảm bảo định nghĩa rõ 3 loại test cơ bản nếu phù hợp: Load, Spike, Stress.
- Định nghĩa rõ các chỉ số KPIs (Error Rate 0%, P90 < 2000ms).
- Phân tích rủi ro hệ thống (Database deadlocks, Rate limit, Memory leaks).

Lưu file với định dạng: `execution/report/[UC-ID]_[feature]_perf-plan_[YYYYMMDD]_v[N].md`

### Phase 3: Sinh Script / Thiết lập Công cụ (Nếu User yêu cầu)
Nếu User yêu cầu script (VD: JMeter, k6):
- **Với JMeter:** 
  - Khuyên người dùng thiết lập UI các bước cơ bản (Thread Group, HTTP Request).
  - Cung cấp các đoạn script xử lý logic khó (PreProcessor bằng Groovy, Regular Expression Extractor, JSON Extractor).
  - Cung cấp file CSV Data mẫu để load.
- **Với k6:**
  - Viết hoàn chỉnh đoạn script `.js` chứa kịch bản load test (VU, Duration, Stages, HTTP requests, Checks).

## Anti-Hallucination Guardrails & Boundaries
1. **No Direct Execution:** Agent TUYỆT ĐỐI KHÔNG được tự ý chạy các script k6 hoặc JMeter (VD: không dùng lệnh terminal để gõ `k6 run`). Skill này CHỈ phục vụ việc sinh ra Test Plan và Script code. Việc chạy thực tế phải do người dùng tự thực hiện.
2. KHÔNG bịa đặt API endpoints nếu tài liệu không cung cấp. Hãy để dưới dạng `[API_ENDPOINT_TBD]`.
3. PHẢI cảnh báo người dùng về việc Rate Limit / WAF có thể block các công cụ load test.
4. PHẢI đề xuất giải pháp xử lý Dữ liệu động (Dynamic Data) như Token, OTP, UUID. Nếu bỏ qua bước Extract Token, load test sẽ fail ở lỗi 401.

## Output Contract
- File Test Plan (.md).
- File Test Data (.csv) (nếu cần).
- Hướng dẫn cấu hình công cụ chi tiết hoặc Script code (K6/Groovy) cung cấp qua giao diện chat.
