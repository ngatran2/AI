# Test Scenarios: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v3 (Final Integration Sync)
**Ngày thực hiện:** 2026-04-21
**Tác giả:** Antigravity (QA Engineer)
**Tài liệu tham chiếu:** 
- [Audited Requirement v7](file:///d:/AI/JOYS-V2/requirements/UC-DM-10/UC-DM-10_airline-category_audited_20260421_v7.md)

---

## 1. GUI & Search Control Scenarios
*(Kế thừa v2: Khôi phục, Đóng, Đặt lại bộ lọc)*

---

## 2. Functional Scenarios (Surgical Precision)
*(Kế thừa v2: Thêm/Sửa/Xóa với thông báo [Mã - Tên])*

---

## 3. Integration & Cross-module Scenarios (MỚI)

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_INT_01** | Kiểm tra đồng bộ Dropdown Thêm mới | Sau khi thêm mới Hãng bay A thành công, mở màn hình Quản lý loại thẻ và xác nhận Hãng bay A xuất hiện trong Dropdown "Hãng bay". |
| **UC-DM-10_INT_02** | Kiểm tra đồng bộ Dropdown Chỉnh sửa | Sau khi đổi tên Hãng bay A thành B, mở màn hình Quản lý loại thẻ và xác nhận Dropdown hiển thị tên mới là B. |
| **UC-DM-10_INT_03** | Kiểm tra đồng bộ Dropdown Xóa | Sau khi xóa Hãng bay A thành công, mở màn hình Quản lý loại thẻ và xác nhận Hãng bay A không còn xuất hiện trong Dropdown "Hãng bay" (Xóa mềm). |

---

## 4. RBAC & Business Rules (Logic 10.6)
*(Kế thừa v2: Chặn xóa khi vướng session/cấu hình)*

---

## 5. Summary
Bộ Scenarios v3 đã bao phủ toàn bộ vòng đời của dữ liệu từ khi khởi tạo trong module Hãng bay cho đến khi được tiêu thụ tại module Loại thẻ. Đảm bảo tính nhất quán của hệ thống (Data Integrity).
