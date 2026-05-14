# Test Scenarios: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v2 (Surgical Precision)
**Ngày thực hiện:** 2026-04-21
**Tác giả:** Antigravity (QA Engineer)
**Tài liệu tham chiếu:** 
- [Audited Requirement v5](file:///d:/AI/JOYS-V2/requirements/UC-DM-10/UC-DM-10_airline-category_audited_20260421_v5.md)
- [Common Rules v1.0](file:///d:/AI/JOYS-V2/requirements/COMMON/COMMON_common-rules_extracted_20260421.md)

---

## 1. GUI & Search Control Scenarios

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_GUI_01** | Kiểm tra hiển thị màn hình Danh sách | Xác nhận hiển thị 2 cột (Mã, Tên), các icon thao tác và phân trang 20/trang. |
| **UC-DM-10_GUI_02** | Kiểm tra hành vi nút [Khôi phục] | Xác nhận xóa dữ liệu trong search box và tự động **Đóng popup**. |
| **UC-DM-10_GUI_03** | Kiểm tra hành vi nút [Đóng] trong popup | Xác nhận đóng popup và **Giữ nguyên** dữ liệu đang nhập dở. |
| **UC-DM-10_GUI_04** | Kiểm tra hành vi nút [Đặt lại bộ lọc] | Xác nhận xóa toàn bộ các chip filter đang active và hiển thị danh sách mặc định. |
| **UC-DM-10_GUI_05** | Kiểm tra hiển thị Ellipsis | Xác nhận tên hãng bay quá dài hiển thị "..." trên 1 dòng. |

---

## 2. Search & Filtering Scenarios (Logic)

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_SCH_01** | Tìm kiếm kết hợp AND (Mã + Tên) | Xác nhận kết quả thỏa mãn đồng thời cả 2 điều kiện lọc. |
| **UC-DM-10_SCH_02** | Tìm kiếm tương đối (Partial Match) | Xác nhận tìm được bản ghi khi chỉ nhập một phần tên hoặc mã. |
| **UC-DM-10_SCH_03** | Nhấn ENTER để thực hiện tìm kiếm | Xác nhận kết quả thay đổi sau khi nhấn ENTER trong search box (CMR-09). |

---

## 3. Functional Scenarios (Surgical Precision)

### 3.1 Thêm mới & Chỉnh sửa
| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_FUNC_01** | Thêm mới thành công với thông báo chuẩn | Xác nhận Toast: `“Thêm mới [mã hãng bay - hãng bay] thành công.”` |
| **UC-DM-10_FUNC_02** | Cập nhật thành công với thông báo chuẩn | Xác nhận Toast: `“Cập nhật [mã hãng bay - hãng bay] thành công.”` |
| **UC-DM-10_FUNC_03** | Kiểm tra khóa Mã khi Sửa | Xác nhận trường Mã hãng bay hiển thị **Read-only** trên popup Sửa. |
| **UC-DM-10_FUNC_04** | Thêm mới trùng Mã hãng bay | Xác nhận thông báo lỗi: "Mã hãng bay đã tồn tại trong hệ thống." |

### 3.2 Xóa (Business Logic 10.6)
| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_FUNC_05** | Xóa thành công (Soft Delete) | Xác nhận Soft Delete và Toast: `“Xóa [mã hãng bay - hãng bay] và các loại thẻ liên quan thành công.”` |
| **UC-DM-10_FUNC_06** | Xóa thất bại do vướng Scanning Session | Xác nhận Error Toast: `“Không thể xóa khi hãng bay và loại thẻ liên quan đang được sử dụng.”` |
| **UC-DM-10_FUNC_07** | Xóa thất bại do vướng Cấu hình điều kiện | Xác nhận Error Toast: `“Không thể xóa khi hãng bay và loại thẻ liên quan đang được sử dụng.”` |

---

## 4. RBAC Scenarios

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_RBAC_01** | Kiểm tra quyền Admin | Hiển thị Thêm, Sửa, Xóa. |
| **UC-DM-10_RBAC_02** | Kiểm tra quyền Role Sửa | Hiển thị Thêm, Sửa. Ẩn Xóa. |
| **UC-DM-10_RBAC_03** | Kiểm tra quyền Role Xóa | Hiển thị Xem, Xóa. Ẩn Thêm, Sửa. |

---

## 5. Non-functional Scenarios

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_NFC_01** | Kiểm tra Trim khoảng trắng | Xác nhận tự động xóa khoảng trắng đầu/cuối của dữ liệu nhập vào. |
| **UC-DM-10_NFC_02** | Kiểm tra Max length (Mã 10, Tên 100) | Xác nhận chặn nhập vượt quá giới hạn ký tự. |
