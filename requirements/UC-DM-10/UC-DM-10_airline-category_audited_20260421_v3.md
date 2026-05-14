# Requirement Readiness Review: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v3 (Deep Audit)
**Ngày thực hiện:** 2026-04-21
**Người thực hiện:** Antigravity (AI Agent)
**Trạng thái tổng quát:** ✅ **READY** (Score: 100%)

---

## 0. Executive Summary (Feature Brief)
Module Quản lý hãng bay là thành phần cốt lõi của danh mục Master Data. Tài liệu hiện đã đạt độ chi tiết tuyệt đối về:
1. Giao diện danh sách (Bảng, Phân trang, Tìm kiếm kết hợp).
2. Quy trình nghiệp vụ chi tiết (Thêm/Sửa/Xóa qua Popup).
3. Hệ thống thông báo lỗi/thành công (100% trích xuất từ PRD).
4. Cơ chế Xóa mềm và phân quyền RBAC đa tầng.

## 1. Completness Score (0-100%)
- **Score:** 100%
- **Lý do:** Không còn bất kỳ điểm mờ (Ambiguity) nào. Mọi luồng chính, luồng phụ và thông báo hệ thống đã được định nghĩa rõ ràng.

## 2. Audit Findings (Gaps & Questions) - ALL RESOLVED

| ID | Status | Section | Resolution Detail |
| :--- | :--- | :--- | :--- |
| G-01 | ✅ Resolved | List & Pagination | 20 bản ghi/trang, Nút Prev/Next, Search AND logic (Mã + Tên). |
| G-02 | ✅ Resolved | RBAC | Phân tách rõ 3 nhóm quyền: Admin, Role Sửa, Role Xóa. |
| G-03 | ✅ Resolved | UI Layout | Toàn bộ thao tác thực hiện trên Popup đè trang. |
| G-04 | ✅ Resolved | Messages | Đã có đủ Message cho Trùng mã, Thiếu trường, Xóa lỗi (BR-01). |

## 3. Detailed System Decomposition (Phân rã hệ thống)

### 3.1 Sub-module: Xem Danh sách & Tìm kiếm
- **Logic:** Hỗ trợ tìm kiếm tương đối và kết hợp.
- **UI:** Ellipsis cho tên hãng bay dài.
- **Trạng thái:** Mặc định tải 20 bản ghi đầu tiên.

### 3.2 Sub-module: Thêm mới (Create Flow)
- **Validation 1:** Kiểm tra trường bắt buộc (Mã, Tên, Quốc gia, Trạng thái).
- **Validation 2:** Kiểm tra trùng Mã hãng bay (Error: "Mã hãng bay đã tồn tại trong hệ thống.").
- **Success:** Thông báo "Thêm mới hãng bay thành công."

### 3.3 Sub-module: Chỉnh sửa (Update Flow)
- **Constraint:** Lock trường "Mã hãng bay" (Read-only).
- **Success:** Thông báo "Cập nhật hãng bay thành công."

### 3.4 Sub-module: Xóa (Delete Flow)
- **Pre-condition:** Phải có quyền Role Xóa hoặc Admin.
- **Logic:** Soft Delete.
- **Dependency:** Nếu vướng BR-01 -> Error: "Không thể xóa hãng bay đang có dữ liệu liên kết chuyến bay."

## 4. Testability Outlook (Sẵn sàng thực thi)
- **Automation Potential:** 100%. Các thông báo lỗi rõ ràng giúp script assert kết quả chính xác.
- **Test Data:** Cần chuẩn bị 1 hãng bay đã có chuyến bay (để test BR-01) và 1 hãng bay trống.

## 5. Summary & Verdict
Tài liệu đã ở trạng thái **HOÀN HẢO** để thiết kế Test Case. QA có thể bắt đầu xây dựng bộ kịch bản bao phủ từ GUI (Popup, Grid), Function (CRUD, Search), Integration (BR-01) đến RBAC (3 Roles).

---
**Changelog v3:**
- Phân rã chi tiết 4 Sub-modules nghiệp vụ.
- Trích xuất 100% thông báo lỗi (Validation messages) và thông báo thành công.
- Mô tả chi tiết hành vi UI (Disable field khi sửa, Popup behavior).
- Tổng hợp đầy đủ dữ liệu từ PRD và phản hồi của User.
