# Jira Status Transition Hook (Integration)

Quy định này áp dụng cho việc theo dõi tự động các thay đổi trạng thái của Bug trên hệ thống Jira để kích hoạt quy trình Re-test kịp thời. Không liên quan đến logic chạy Automation script.

## 1. Điều kiện kích hoạt (The Hook)
Agent thực hiện quét Jira định kỳ (Cronjob) dựa trên các điều kiện:
1. **Chuyển trạng thái:** Khi một Ticket chuyển từ `In Progress` hoặc `Fixed` sang **`Ready for Test`** (hoặc trạng thái tương đương theo config từng dự án).
2. **Lịch trình (Cron):** Mặc định quét vào **9:00 AM hàng ngày** để tổng hợp danh sách các bug đã được Dev fix xong, sẵn sàng để QA kiểm thử lại.

## 2. Logic xử lý (The Action)
Khi chạy Hook, Agent thực hiện:
1. **Quét JQL:** Dùng API gọi câu lệnh `project = [Key] AND issuetype = Bug AND status = "Ready for Test"`.
2. **So sánh Snapshot:** Đối chiếu với bản báo cáo Jira của ngày hôm trước để lọc ra danh sách "Newly Ready for Test".
3. **Khởi tạo thông báo:**
    - Tạo file báo cáo lưu tại `report/daily-bug-notification_YYYYMMDD.md`.
    - Trích xuất: ID, Tiêu đề, Link Jira, và Comments dặn dò của Dev (nếu có).
4. **Thông báo:** Gửi tóm tắt danh sách bug mới này trực tiếp cho User qua Chat hoặc File notification.
