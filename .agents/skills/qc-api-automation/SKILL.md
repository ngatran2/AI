---
name: qc-api-automation
description: Sinh API test cases và automation scripts từ Swagger/OpenAPI specification. Hỗ trợ 2 mode — SPEC (chỉ test cases) và FULL (test cases + automation scripts).
---

# API Automation & Test Design Skill

## Purpose
Kỹ năng này giúp Agent phân tích tài liệu Swagger/OpenAPI (JSON/YAML) để tự động hóa quy trình QA cho lớp API, bao gồm việc thiết kế kịch bản kiểm thử chi tiết và sinh mã nguồn kiểm thử tự động (Automation Scripts) theo nhiều ngôn ngữ/framework khác nhau.

## Mode thực thi
1. **SPEC Mode (Mặc định):** Tập trung vào việc trích xuất và thiết kế Test Cases dưới dạng Markdown. Phù hợp khi cần review kịch bản trước khi code.
2. **FULL Mode:** Sinh toàn bộ cấu trúc dự án Automation, bao gồm Base Client, DTO/Models, Test Data Factory và các Test Classes với đầy đủ Assertions.

## Nguyên tắc thực thi (STRICT)
- **Tất cả output bằng Tiếng Việt.**
- **KHÔNG ĐOÁN:** Phải đọc chính xác Schema từ Spec. Nếu Spec thiếu thông tin, phải đánh dấu `[TBD]`.
- **Auto-Heal (Rule E3):** Khi chạy test thất bại, Agent phải tự đọc log, phân tích lỗi và sửa code. Chỉ hỏi User khi lỗi thuộc về hạ tầng hoặc logic nghiệp vụ mâu thuẫn.
- **Traceable Data:** Sử dụng skill `test-data-generator` để sinh dữ liệu có định danh (VD: `api_test_{timestamp}`).

## Quy trình thực hiện

### 1. Phân tích Spec
- Sử dụng `read_url_content` (cho URL) hoặc `view_file` (cho local file).
- Trích xuất: Base URL, Auth Method, Endpoints (Path + Method), Request Body/Params, Response Schema.

### 2. Thiết kế Scenarios (5 Pillars)
Mọi Endpoint phải có đủ 5 loại kịch bản:
- **✅ Happy Path:** Request chuẩn, mã trả về 2xx.
- **❌ Validation:** Sai kiểu dữ liệu, thiếu trường bắt buộc, vượt độ dài.
- **❌ Authentication:** Token sai, hết hạn, hoặc thiếu quyền.
- **🔲 Boundary:** Kiểm tra giá trị biên (min/max), chuỗi rỗng.
- **⚡ Edge Cases:** Trùng lặp dữ liệu, payload cực lớn, ký tự Unicode/Emoji.

### 3. Sinh Automation Script (Chỉ cho FULL Mode)
- **Frameworks:** REST Assured (Java), Playwright API (TS), Pytest Requests (Python).
- **Cấu trúc:** Áp dụng mô hình Layered Architecture (Models -> API Clients -> Tests).
- **Assertions & Error Reporting (BẮT BUỘC):** 
    - Kiểm tra Status Code và Schema.
    - **Failure Diagnostics:** Khi test thất bại, Agent BẮT BUỘC phải ghi rõ nguyên nhân vào cột Note/Actual Result (VD: "404 - Endpoint mismatch", "401 - Token Expired").
    - Kiểm tra tính đúng đắn của dữ liệu trong Response Body.

## Tiêu chí đánh giá (Evaluation Criteria)
Sản phẩm của quá trình tự động hóa API phải đạt:
1. **Coverage (Độ bao phủ):** 100% các API Endpoints được trích xuất phải có Test Case bao trùm đủ 5 Pillars đã định nghĩa.
2. **Reusability (Tính tái sử dụng):** Code sinh ra phải sử dụng biến môi trường (Environment Variables) cho Base URL và Token, không hardcode.
3. **Traceability (Truy xuất lỗi):** Log lỗi sinh ra khi chạy test phải chứa đầy đủ Payload (Body đã gửi) và Response.
4. **Data Cleansing (Dọn dẹp):** Mọi kịch bản POST/PUT sinh ra rác trong DB đều phải có hàm/hook (vd: @After/Teardown) gọi API DELETE tương ứng để dọn dẹp dữ liệu cuối mỗi test run.

## Output Contract
- **Test Cases:** `testcases/[UC-ID]/[UC-ID]_api_testcases_[YYYYMMDD]_v[N].md`
- **Scripts:** `execution/[UC-ID]/scripts/api/`
- **Report:** `execution/[UC-ID]/api_execution_report_[YYYYMMDD].md`
