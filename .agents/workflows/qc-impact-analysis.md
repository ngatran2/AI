# Workflow: Change Request Impact Analysis
// turbo-all

## Mô tả
Chạy luồng phân tích tác động (Impact Analysis) khi có sự cố thay đổi Requirement lớn (Change Request) để xác định chính xác khu vực cần kiểm thử hồi quy (Regression Test).

## Các bước thực hiện:
1. **Thu thập Input:** Yêu cầu User cung cấp file Requirement v[Cũ] và v[Mới], hoặc đoạn văn bản mô tả Change Request.
2. **Kích hoạt Skill:** Áp dụng skill `impact-analysis`. Đọc `Integration_flow.md` để rà soát sự lan truyền logic.
3. **Đánh giá sơ bộ:** NẾU thay đổi quá nhỏ (typo), dừng Workflow và báo User. NẾU có thay đổi logic/DB, tiến hành Bước 4.
4. **Sinh Báo cáo:** Tạo file `requirements/[UC-ID]/impact-reports/Impact_Analysis_[YYYYMMDD]_v[N].md`.
5. **Kế hoạch hành động:** Đề xuất User cập nhật lại file Scenarios/Test Cases của các tính năng bị ảnh hưởng.
