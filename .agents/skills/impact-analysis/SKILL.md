# Impact Analysis Skill (Phân tích Tác động Change Request)

## Purpose
Phân tích tác động của một sự thay đổi (Change Request - CR) hoặc phiên bản Requirement mới so với bản cũ. Từ đó, khoanh vùng chính xác các module và chức năng liên quan cần phải chạy lại kiểm thử (Regression Test), tránh lãng phí tài nguyên.

## Khi nào kích hoạt?
Kích hoạt THỦ CÔNG khi User thông báo có Change Request lớn, khách hàng đổi luồng logic cốt lõi, hoặc có bản cập nhật Requirement mới.
- Lệnh: `/impact-analysis`

## Đầu vào (Input)
1. Cặp file Requirement: Bản cũ (v[N-1]) và Bản mới (v[N]). Hoặc mô tả Change Request từ User.
2. File bản đồ cấu trúc hệ thống: `requirements/COMMON/Integration_flow.md`.

## Quy trình thực hiện (Workflow)

### Phase 1: Delta Analysis (Tìm điểm khác biệt)
1. So sánh v[N-1] và v[N] để tìm ra "Delta" (Sự thay đổi: Thêm field dữ liệu, đổi logic Validate, đổi luồng API/Trạng thái).
2. Lọc độ nhiễu: Phớt lờ các thay đổi về Typo (chính tả) hoặc UI/Màu sắc không ảnh hưởng đến luồng logic.

### Phase 2: Traceability & Impact Mapping
1. Ánh xạ sự thay đổi "Delta" vào `Integration_flow.md` để rà soát các module "bị lây nhiễm" (Affected Modules).
2. *Ví dụ:* Logic sinh `Card_ID` ở UC-DM-11 thay đổi -> Ảnh hưởng tới luồng Tạo Khách Hàng (UC-KH-01) do xài chung Card_ID -> Đánh dấu UC-KH-01 bị tác động.

### Phase 3: Sinh Regression Suite Suggestion
Sinh file báo cáo `requirements/[UC-ID]/impact-reports/Impact_Analysis_[YYYYMMDD]_v[N].md` gồm:
- **Change Summary:** Tóm tắt chính xác điều gì vừa thay đổi.
- **Impact Level:** Đánh giá mức độ lan truyền (High/Medium/Low).
- **Mini-Regression Suite:** Danh sách cụ thể các kịch bản (Scenarios) hoặc Test Cases của các UC vệ tinh cần phải chạy lại.

## Tiêu chí đánh giá (Evaluation Criteria)
Kết quả phân tích tác động phải đáp ứng:
1. **Độ chính xác (Accuracy):** TUYỆT ĐỐI KHÔNG đưa các Use Case không có chung luồng dữ liệu (Data flow) hoặc không có liên kết API vào danh sách Regression.
2. **Tiết kiệm tài nguyên (Cost-effective):** Bộ Mini-Regression được đề xuất không được vượt quá 30% tổng số lượng Test Case của hệ thống, trừ khi có sự thay đổi lớn ở Database cốt lõi.
3. **Phân loại tác động rõ ràng:**
   - **High:** Thay đổi cấu trúc DB / Logic nghiệp vụ chính / Thuật toán.
   - **Medium:** Thay đổi Validation Rule / Điều kiện UI hiển thị.
   - **Low:** Thay đổi Text / Màu sắc UI (Trường hợp này đánh dấu "No Regression").

## Guardrails (Quy tắc an toàn)
- NẾU Agent phát hiện thay đổi quá nhỏ (typo), phải báo ngay cho User: *"No Logic Change Detected. No Regression Required"* và dừng quy trình để tiết kiệm token.
