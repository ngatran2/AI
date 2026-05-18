# Execution Readiness Audit (ERA)

Trước khi tiến hành chạy bất kỳ Test Case nào, Agent đóng vai trò là Gatekeeper để chấm điểm xem bộ Test đã đủ điều kiện chạy chưa.

## Scoring Rubric (Total: 100 points)
1. **Prerequisites (20 pts):** URLs, roles, và initial data (Pre-condition) có được định nghĩa rõ ràng không?
2. **Account Alignment (20 pts):** Các Role liệt kê trong test case có khớp 1:1 với config môi trường hiện tại không?
3. **Technical Spec Alignment (20 pts):** Nếu đợt chạy có kiểm tra DB (High/Critical Risk), tài liệu DB Schema, Trace ID format và State Transition Map có được cung cấp không? Bắt buộc = Có, nếu Thiếu = 0 điểm.
4. **Step Clarity (25 pts):** Các bước thao tác có rành mạch (atomic), dễ hiểu và có Expected Result rõ ràng không?
5. **Data Precision (15 pts):** Test Data đầu vào có chính xác và khả thi không?

## Verdict Thresholds
- **90-100:** ✅ **READY** (Cho phép chạy).
- **70-89:** ⚠️ **CONDITIONALLY READY** (Cho phép chạy, nhưng phải log cảnh báo những điểm yếu).
- **< 70:** ❌ **NOT READY** (Chặn ngay lập tức, báo cáo User để sửa Requirement/Test Case).

## Bảng Report (Mẫu Bắt Buộc)
Agent in ra bảng sau trước khi chạy code:
| Metric | Score | Notes |
| :--- | :--- | :--- |
| Prerequisites | X/20 | ... |
| Account Alignment | X/20 | ... |
| Technical Spec Alignment | X/20 | ... |
| Step Clarity | X/25 | ... |
| Data Precision | X/15 | ... |
| **Overall Score** | **XX / 100** | **[VERDICT]** |
