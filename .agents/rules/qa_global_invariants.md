# QA Global Invariants (Hệ thống Bất biến)

Đây là các quy tắc sống còn áp dụng ở tầng nhận thức (System Level) cho toàn bộ các Agent (Reviewer, Designer, Executor) tham gia vào quy trình QA. Tuyệt đối **BẤT KHẢ KHÁNG**.

1. **Zero-Hallucination Data (Chống ảo giác tuyệt đối):**
   - Tuyệt đối KHÔNG tự bịa ra cấu trúc Database, tên bảng (Table), tên cột (Column), trạng thái (State) hoặc Locator UI nếu không có tài liệu Spec hoặc DOM minh chứng.
   - Nếu thiếu input, BẮT BUỘC phải dừng và hỏi User.

2. **Security & PII Masking (Bảo mật & Ẩn danh):**
   - Tuyệt đối KHÔNG in, log, hoặc export mật khẩu thật, token thật, thông tin cá nhân nhạy cảm (PII - số dư, số thẻ, số điện thoại) ra màn hình console hay báo cáo Excel.
   - Bắt buộc phải dùng biến môi trường (ENV/Vault) và Masking (`***`) khi chụp ảnh/lưu log.

3. **Evidence Integrity (Tính vẹn toàn của bằng chứng):**
   - Mọi bằng chứng (Screenshots, API Logs, DB Logs) phải khớp hoàn toàn về mốc thời gian (Timestamp) trong khoảng cho phép.
   - NGHIÊM CẤM hành vi tái sử dụng bằng chứng cũ, ảnh chụp cũ để ghép vào Test Case chạy sau (Evidence Forged).

4. **Read-Only Database Constraints (An toàn hạ tầng):**
   - Đối với CSDL, Agent Automation thông qua MCP chỉ có quyền thực thi lệnh `SELECT`.
   - TUYỆT ĐỐI KHÔNG chạy `INSERT`, `UPDATE`, `DELETE` bằng script ngoài luồng UI/API.

5. **No Blind Skipped (Minh bạch thực thi):**
   - Không được phép bỏ qua Test Case mà không có lý do. 
   - Mọi trạng thái `SKIPPED` hoặc `BLOCKED` đều phải đi kèm một mã Reason Code chuẩn hóa (VD: `ENV_DOWN`, `DATA_MISSING`, `DEPENDENCY_BLOCK`, `OUT_OF_SCOPE`). Tỷ lệ này không được vượt quá ngưỡng cho phép (3%).
