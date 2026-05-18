# Stability & Resource Engine

Đây là hệ thống bảo vệ giúp quá trình chạy TCs số lượng lớn (Scale-readiness) không bị crash, rò rỉ bộ nhớ, và tránh báo cáo sai do Flaky.

## 1. Flaky Detection Layer (Khám bệnh chập chờn)
Nếu một Test Case bị FAIL, Agent không được báo Bug ngay lập tức. Phải re-run tối đa 2 lần. Nếu kịch bản `FAIL -> PASS -> FAIL` thì đánh dấu là **FLAKY**.
Nguyên nhân thường gặp cần xử lý:
- **Trễ Timing:** Do UI animation, spinner chưa tắt. Phải dùng Web-first assertion (toBeVisible).
- **Parallel Data Conflict:** Chạy song song làm ghi đè data. Phải cách ly Namespace.
- **Unstable Locator:** Thẻ HTML sinh động. Dùng thẻ Semantic XPath hoặc TestID.
- **Environment/Infra:** Backend sập, DB lock. Dùng retry API.

## 2. Resource Governance (Quản trị tài nguyên)
- **Browser Recycling:** Dọn dẹp context, xóa cache và restart lại Browser sau mỗi block 50 TCs để tránh Memory Leak.
- **Timeout Budget:** Mọi request, click, navigation phải bọc trong Global/Action Timeout. Quá hạn là Fail-fast để giải phóng RAM.
- **Artifact Retention (Dọn rác tự động):** 
  - CHỈ LƯU Screenshots / Logs / Traces của các TCs có kết quả `FAIL` hoặc `FLAKY`.
  - Bắt buộc Tự Động Xóa (Auto-delete) bằng chứng hình ảnh của các TCs báo `PASS` để chống tràn ổ đĩa.
