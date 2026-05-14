# /qc-api-test-gen — API Automation & Test Generation Workflow

## Purpose
Workflow này được sử dụng để tự động hóa quy trình kiểm thử API từ tài liệu Swagger/OpenAPI. Hỗ trợ từ việc lập kịch bản đến việc sinh code automation hoàn chỉnh.

## Các bước thực hiện

### Bước 1: Tiếp nhận Spec
1. Agent yêu cầu User cung cấp Swagger URL hoặc file Spec (JSON/YAML).
2. Sử dụng skill `qc-api-automation` để phân tích cấu trúc API.

### Bước 2: Xác nhận Scope (CHECKPOINT)
1. Liệt kê danh sách các Endpoints và nhóm chức năng phát hiện được.
2. Đề xuất Mode (SPEC hoặc FULL) và Tech Stack.
3. **DỪNG LẠI** và chờ User xác nhận danh sách API cần test và Mode thực hiện.

### Bước 3: Thiết kế & Sinh Code
1. Sinh bộ Test Scenarios chi tiết trong file `api_test_cases_draft.md`.
2. Nếu là **Mode FULL**:
    - Khởi tạo cấu trúc thư mục dự án tại `execution/[UC-ID]/scripts/api/`.
    - Sinh mã nguồn cho Models, Clients và Test Classes.
    - Sinh Test Data thông qua skill `test-data-generator`.

### Bước 4: Thực thi & Kiểm chứng
1. Chạy thử các test cases vừa sinh.
2. Nếu có lỗi: Tự động sửa lỗi (Auto-Heal) tối đa 5 lần.
3. Báo cáo kết quả cuối cùng cho User kèm theo bằng chứng thực thi.

## Lệnh kích hoạt
- `npx antigravity /qc-api-test-gen [Swagger_URL]`
- Hoặc yêu cầu trực tiếp: "Sinh test API cho Swagger này [URL]"
