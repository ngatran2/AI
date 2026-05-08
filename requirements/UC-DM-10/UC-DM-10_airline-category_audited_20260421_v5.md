# Requirement Readiness Review: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v5 (UI Control Precision)
**Ngày thực hiện:** 2026-04-21
**Người thực hiện:** Antigravity (AI Agent)
**Trạng thái tổng quát:** ✅ **READY** (Score: 100%)

---

## 0. Executive Summary (Feature Brief)
Bản Audit v5 bổ sung chi tiết về các nút điều khiển (Controls) của bộ lọc tìm kiếm dựa trên Design Mockup. Tài liệu hiện đã phủ kín cả luồng nghiệp vụ (Business Logic), thông báo (Messages) và hành vi chi tiết của UI (Search Popover behaviors).

## 1. Detailed UI & Search Control Analysis (Bổ sung mới)

### 1.1 Search Popover (Trong cột Mã hãng bay)
- **Input Search:** Cho phép nhập text tìm kiếm.
- **Nút [Khôi phục] (Khôi phục):**
    - **Hành vi:** Xóa text đang nhập trong input search và tự động **Đóng popup**.
- **Nút [Đóng] (Đóng):**
    - **Hành vi:** Đóng popup tìm kiếm, giữ nguyên trạng thái text hiện tại (không thay đổi dữ liệu).

### 1.2 Filter Active Bar (Thanh "Lọc theo")
- **Chip Filter:** Hiển thị điều kiện đang lọc (Ví dụ: `Mã hãng bay: M x`).
- **Nút [Đặt lại bộ lọc] (Đặt lại bộ lọc):**
    - **Vị trí:** Cạnh các chip filter đang active.
    - **Hành vi:** Xóa toàn bộ các điều kiện lọc đang áp dụng và tải lại danh sách đầy đủ.

## 2. Detailed System Decomposition & Messages (Updated)

### 2.1 Sub-module: Thêm mới (UC-HK-10.2)
- **Success Toast:** `“Thêm mới [mã hãng bay - hãng bay] thành công.”`

### 2.2 Sub-module: Chỉnh sửa (UC-HK-10.4)
- **UI Constraint:** Mã hãng bay là **Read-only**.
- **Success Toast:** `“Cập nhật [mã hãng bay - hãng bay] thành công.”`

### 2.3 Sub-module: Xóa (UC-HK-10.5)
- **Business Logic (BR-10.6):** Chặn xóa nếu đang trong **Scanning session** hoặc **Cấu hình điều kiện**.
- **Error Toast (Vi phạm):** `“Không thể xóa khi hãng bay và loại thẻ liên quan đang được sử dụng.”`
- **Success Toast:** `“Xóa [mã hãng bay - hãng bay] và các loại thẻ liên quan thành công.”`

## 3. RBAC & Logic Tái xác nhận
- **Soft Delete:** Duy trì cơ chế xóa mềm.
- **Admin/Role Sửa/Role Xóa:** Tuân thủ ma trận quyền đã định nghĩa.

## 4. Testability Outlook
- **GUI Test:** Cần verify hành động Đóng popup của cả 2 nút [Khôi phục] và [Đóng].
- **Search Test:** Verify nút [Đặt lại bộ lọc] phải clear được tất cả các chip filter đang hiển thị.

## 5. Summary & Verdict
Tài liệu đạt trạng thái **READY** hoàn hảo. Mọi tiểu tiết về hành vi nút bấm trên UI đã được làm rõ, đảm bảo Automation script không bị "lạc hướng" khi tương tác với các nút có tên gọi tương tự nhưng hành vi khác nhau.
