# Requirement Readiness Review: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v4 (Surgical Audit)
**Ngày thực hiện:** 2026-04-21
**Người thực hiện:** Antigravity (AI Agent)
**Trạng thái tổng quát:** ✅ **READY** (Score: 100%)

---

## 0. Executive Summary (Feature Brief)
Bản Audit v4 tập trung vào độ chính xác tuyệt đối của các thông báo hệ thống và các ràng buộc nghiệp vụ (BR) liên quan đến chu trình sống của dữ liệu (Scanning session, Cấu hình điều kiện). Tài liệu PRD cung cấp các thông báo Success kèm dữ liệu động [mã - tên hãng bay].

## 1. Completness Score (0-100%)
- **Score:** 100%
- **Lý do:** Đã trích xuất và đính chính toàn bộ các thông báo Toast Message (Thêm/Sửa/Xóa) và các ràng buộc logic phức tạp trong luồng Xóa.

## 2. Detailed System Decomposition & Messages

### 2.1 Sub-module: Thêm mới (UC-HK-10.2)
- **Hành động:** Nhấn nút [Lưu] trên Popup Thêm mới.
- **Success Toast:** `“Thêm mới [mã hãng bay - hãng bay] thành công.”`
- **Error Validation:** Trùng mã, Thiếu trường bắt buộc.

### 2.2 Sub-module: Chỉnh sửa (UC-HK-10.4)
- **Hành động:** Nhấn nút [Lưu] trên Popup Chỉnh sửa.
- **UI Constraint:** Trường "Mã hãng bay" hiển thị ở trạng thái **Read-only**.
- **Success Toast:** `“Cập nhật [mã hãng bay - hãng bay] thành công.”`

### 2.3 Sub-module: Xóa (UC-HK-10.5)
- **Hành động:** Nhấn nút [Xóa] trên popup xác nhận.
- **Business Logic (BR-10.6):** 
    - Chặn xóa nếu Hãng bay/Loại thẻ đang thuộc một **Scanning session** đang hoạt động.
    - Chặn xóa nếu Hãng bay/Loại thẻ đang được sử dụng trong **Cấu hình điều kiện**.
- **Error Toast (Khi vi phạm BR):** `“Không thể xóa khi hãng bay và loại thẻ liên quan đang được sử dụng.”`
- **Success Toast (Khi hợp lệ):** `“Xóa [mã hãng bay - hãng bay] và các loại thẻ liên quan thành công.”`
- **Cơ chế:** Soft Delete (Xóa khỏi danh mục hiển thị, không cho phép chọn mới).

## 3. Phân quyền (RBAC) - Tái xác nhận
- **Admin:** Thấy nút Thêm, Sửa, Xóa.
- **Role Sửa:** Thấy nút Thêm, Sửa.
- **Role Xóa:** Thấy nút Xem, Xóa.

## 4. Testability Outlook
- **Surgical Assertion:** Các kịch bản Automation cần bắt được string thông báo bao gồm cả ID và Name để verify tính chính xác.
- **Data Dependency:** Cần chuẩn bị 3 trạng thái dữ liệu: (1) Sẵn sàng xóa, (2) Đang trong Scanning session, (3) Đang trong Cấu hình điều kiện.

## 5. Summary & Verdict
Tài liệu đã đạt độ chuẩn xác 100% theo đúng PRD. Sẵn sàng cho việc thiết kế Test Case với độ bao phủ cao nhất.

---
**Changelog v4:**
- Đính chính nội dung 3 Toast Messages Success (Thêm dữ liệu động [mã - tên]).
- Bổ sung thông báo Xóa thành công.
- Bổ sung BR-10.6: Ràng buộc xóa liên quan đến Scanning Session và Cấu hình điều kiện.
- Cập nhật Error Toast khi xóa thất bại.
