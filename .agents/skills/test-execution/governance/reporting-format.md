# Reporting & Output Format

Quy chuẩn xuất báo cáo Excel và Log để đảm bảo tính Auditability (Khả năng kiểm toán) cho doanh nghiệp.

## 1. Execution Metadata (Reproducibility)
Bất kỳ báo cáo thực thi nào cũng PHẢI có Header chứa Execution Metadata để Dev có thể reproduce lỗi. Thông tin bao gồm:
- **Build Version:** (VD: v2.1.0-rc1)
- **Environment:** (VD: Staging, Pre-prod)
- **Browser/Device:** (VD: Chromium 120 / iPhone 13)
- **Execution Timestamp:** (VD: 2026-05-18T10:00:00Z)
- **Git Commit Hash:** (Nếu có)
- **Test Data Group ID:** (Tập dữ liệu dùng để chạy)

## 2. Excel Result Format
Bắt buộc copy file gốc, xuất ra thư mục `execution/[UC-ID]/reports/` theo quy chuẩn `naming-convention.md`.
- Ghi đè vào các cột bắt đầu từ **Column H**.
  - `[Status]`: Điền `PASS`, `FAIL`, `BLOCKED`, `SKIPPED`.
  - `[Actual Result]`: Mô tả chính xác màn hình hiện gì.
  - `[Note]`: Ghi chú thêm, gắn Link Ảnh, Code RCA, Trace ID.
- **Master Cell Rule:** Nếu ô là Merge Cell, luôn `.strip()` ID và ghi kết quả vào **Top-Left Cell**.
- Set `row.hidden = False` và Font màu đen để hiển thị rõ. Chữ PASS xanh, FAIL đỏ.

## 3. Bug Report (12 Cột)
Nếu Log ra Bug report riêng, phải có đủ 12 cột:
Bug ID, Environment, Data Test, TC ID, Bug Title, Pre-condition, Steps, Actual Result, Expected Result, Evidence (Links), Severity, Priority.
> Mọi Bug FAIL đều phải đính kèm RCA Code (R1-R4) ở cột Note hoặc Note của Evidence.
