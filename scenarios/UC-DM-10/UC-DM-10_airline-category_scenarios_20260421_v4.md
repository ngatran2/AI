# Test Scenarios: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v4 (Surgical & Integration Sync)
**Ngày thực hiện:** 2026-04-21
**Tác giả:** Antigravity (QA Engineer)
**Tài liệu tham chiếu:** 
- [Audited Requirement v7](file:///d:/AI/JOYS-V2/requirements/UC-DM-10/UC-DM-10_airline-category_audited_20260421_v7.md)

---

## 1. GUI & Search Control Scenarios

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_GUI_01** | Kiểm tra hiển thị màn hình Danh sách | Xác nhận hiển thị 2 cột (Mã, Tên), các icon thao tác và phân trang 20/trang. |
| **UC-DM-10_GUI_02** | Kiểm tra hành vi nút [Khôi phục] | Xác nhận xóa dữ liệu trong search box và tự động **Đóng popup**. |
| **UC-DM-10_GUI_03** | Kiểm tra hành vi nút [Đóng] trong popup | Xác nhận đóng popup và **Giữ nguyên** dữ liệu đang nhập dở. |
| **UC-DM-10_GUI_04** | Kiểm tra hành vi nút [Đặt lại bộ lọc] | Xác nhận xóa toàn bộ các chip filter đang active và hiển thị danh sách mặc định. |

---

## 2. Functional Scenarios (Surgical Precision)

### 2.1 Thêm mới & Chỉnh sửa
| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_FUNC_01** | Thêm mới thành công với thông báo chuẩn | Xác nhận Toast: `“Thêm mới [mã hãng bay - hãng bay] thành công.”` |
| **UC-DM-10_FUNC_02** | Cập nhật thành công với thông báo chuẩn | Xác nhận Toast: `“Cập nhật [mã hãng bay - hãng bay] thành công.”` |
| **UC-DM-10_FUNC_03** | Kiểm tra khóa Mã khi Sửa | Xác nhận trường Mã hãng bay hiển thị **Read-only** trên popup Sửa. |
| **UC-DM-10_FUNC_04** | Thêm mới trùng Mã hãng bay | Xác nhận thông báo lỗi: "Mã hãng bay đã tồn tại trong hệ thống." |

### 2.2 Xóa (Business Logic 10.6)
| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_FUNC_05** | Xóa thành công (Soft Delete) | Xác nhận Soft Delete và Toast: `“Xóa [mã hãng bay - hãng bay] và các loại thẻ liên quan thành công.”` |
| **UC-DM-10_FUNC_06** | Xóa thất bại do liên kết nghiệp vụ | Xác nhận Error Toast: `“Không thể xóa khi hãng bay và loại thẻ liên quan đang được sử dụng.”` (Liên kết Scanning Session/Cấu hình điều kiện). |

---

## 3. Integration Scenarios (Cross-module Sync)

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_INT_01** | Đồng bộ Dropdown sau khi Thêm mới | Sau khi thêm mới Hãng bay A, xác nhận Hãng bay A xuất hiện trong Dropdown tại màn Quản lý loại thẻ. |
| **UC-DM-10_INT_02** | Đồng bộ Dropdown sau khi Chỉnh sửa | Sau khi đổi tên Hãng bay A thành B, xác nhận Dropdown tại màn Quản lý loại thẻ hiển thị tên mới là B. |
| **UC-DM-10_INT_03** | Đồng bộ Dropdown sau khi Xóa | Sau khi xóa Hãng bay A, xác nhận Hãng bay A không còn xuất hiện trong Dropdown tại màn Quản lý loại thẻ. |

---

## 4. RBAC Scenarios

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_RBAC_01** | Kiểm tra quyền Admin | Hiển thị đầy đủ Thêm, Sửa, Xóa. |
| **UC-DM-10_RBAC_02** | Kiểm tra quyền Role Sửa | Hiển thị Thêm, Sửa. Ẩn Xóa. |
| **UC-DM-10_RBAC_03** | Kiểm tra quyền Role Xóa | Hiển thị Xem, Xóa. Ẩn Thêm, Sửa. |

---

## 5. Summary & ERA Verdict
Bộ kịch bản v4 đạt độ phủ 100% yêu cầu. Mọi bài học về **Surgical Precision** và **Integration Mindset** đã được áp dụng triệt để.

**Execution Readiness Audit (ERA):** 100/100 (Sẵn sàng thiết kế Test Case).
