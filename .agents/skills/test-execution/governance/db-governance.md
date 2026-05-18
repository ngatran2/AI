# Enterprise Database Governance (Layer 2)

Quản trị toàn bộ các thao tác Database trong quá trình Automation (Dành cho High/Critical Risk Validation).
> **Input bắt buộc:** Không chạy module này nếu User chưa cấp DB Schema, Business State Transition Map và cấu trúc Trace/Correlation ID.

## 1. Ràng buộc An toàn
- CHỈ CHO PHÉP chạy lệnh `SELECT` thông qua MCP DB Server.
- CẤM TIỆT mọi script gọi `INSERT`, `UPDATE`, `DELETE` bằng SQL. Dữ liệu phải được sinh ra và xóa đi từ giao diện UI/API theo đúng Business Flow.

## 2. DB Validation Contract (Hợp đồng Xác thực Dữ liệu)
Khi verify một testcase PASS ở CSDL, không dùng `SELECT * LIMIT 1` bừa bãi. Phải verify 3 lớp:
1. **Key Identifier:** Truy vấn dựa trên Trace ID / Correlation ID được đẩy từ UI/API vào DB để đảm bảo lấy đúng record.
2. **Expected Delta:** Kiểm tra sự chuyển biến (Ví dụ: Order status từ `Pending` -> `Paid`) thay vì check tĩnh.
3. **Relational Integrity (Tính toàn vẹn đa bảng):** Nếu business phức tạp, query phải JOIN hoặc scan ở các bảng bị ảnh hưởng (Order, Transaction, Ledger, Audit Log).

## 3. Negative Assertion (Chống rác)
Đảm bảo hành vi không đẻ ra dữ liệu sai:
- Check không có bản ghi Duplicate.
- Check không có Orphan Record (Bản ghi mồ côi không có parent khóa ngoại).

## 4. Async Processing & Stability Window (Bất đồng bộ)
Hệ thống microservices thường dùng Queue. UI báo PASS không có nghĩa DB đã ghi kịp.
- Áp dụng **Commit Stability Window**: Script phải chờ 3-5 giây (hoặc thiết lập Polling Timeout) trước khi chạy lệnh `SELECT` kiểm tra DB.
- Nếu query lần 1 không có data, không báo Fail ngay mà chạy cơ chế Wait & Retry chống Eventual Consistency delay.
