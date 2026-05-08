# Test Scenarios: UC-DM-10: Quản lý danh mục hãng bay

**Phiên bản:** v1
**Ngày thực hiện:** 2026-04-21
**Tác giả:** Antigravity (QA Engineer)
**Tài liệu tham chiếu:** 
- [Audited Requirement v3](file:///d:/AI/JOYS-V2/requirements/UC-DM-10/UC-DM-10_airline-category_audited_20260421_v3.md)
- [Common Rules v1.0](file:///d:/AI/JOYS-V2/requirements/COMMON/COMMON_common-rules_extracted_20260421.md)

---

## 1. GUI & UX Scenarios (Giao diện & Trải nghiệm)

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_GUI_01** | Kiểm tra hiển thị màn hình Danh sách | Xác nhận Breadcrumb, Tiêu đề, Bảng dữ liệu (Mã, Tên, Thao tác) và Phân trang hiển thị đúng chuẩn. |
| **UC-DM-10_GUI_02** | Kiểm tra hiển thị Popup Thêm/Sửa | Xác nhận Popup hiển thị đè trên trang, có nút đóng [X] và các trường nhập liệu đúng Layout. |
| **UC-DM-10_GUI_03** | Kiểm tra hiển thị Ellipsis cho tên hãng bay dài | Xác nhận văn bản quá dài trên bảng dữ liệu được rút gọn bằng "..." (CMR-08). |
| **UC-DM-10_GUI_04** | Kiểm tra hiển thị Loading state | Xác nhận Loading overlay xuất hiện khi Tải trang, Tìm kiếm hoặc Lưu dữ liệu (CMR-12). |
| **UC-DM-10_GUI_05** | Kiểm tra trạng thái Button [Lưu] | Xác nhận Button [Lưu] luôn Enable ngay cả khi chưa nhập liệu (CMR-07). |

---

## 2. Search & Filtering Scenarios (Tìm kiếm & Lọc)

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_SCH_01** | Tìm kiếm chính xác theo Mã hãng bay | Xác nhận kết quả trả về đúng 1 bản ghi khớp 100% Mã đã nhập. |
| **UC-DM-10_SCH_02** | Tìm kiếm tương đối theo Hãng bay | Xác nhận kết quả trả về các hãng bay có chứa chuỗi ký tự đã nhập. |
| **UC-DM-10_SCH_03** | Tìm kiếm kết hợp (AND Logic) | Xác nhận kết quả lọc đồng thời theo Mã hãng bay VÀ Tên hãng bay. |
| **UC-DM-10_SCH_04** | Tìm kiếm không có kết quả (Empty State) | Xác nhận hiển thị màn hình trống khi không tìm thấy hãng bay phù hợp. |
| **UC-DM-10_SCH_05** | Xóa bộ lọc tìm kiếm | Xác nhận nhấn ENTER khi Search box trống sẽ hiển thị lại toàn bộ dữ liệu (CMR-09). |

---

## 3. Functional Scenarios (Chức năng CRUD)

### 3.1 Thêm mới (Create)
| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_FUNC_01** | Thêm mới hãng bay thành công | Xác nhận lưu dữ liệu hợp lệ và hiển thị Toast Success "Thành công - Thêm mới hãng bay thành công." |
| **UC-DM-10_FUNC_02** | Thêm mới với Mã hãng bay đã tồn tại | Xác nhận hiển thị lỗi "Mã hãng bay đã tồn tại trong hệ thống." |
| **UC-DM-10_FUNC_03** | Kiểm tra cơ chế Trim khoảng trắng | Xác nhận hệ thống tự động xóa khoảng trắng đầu/cuối của Mã và Tên hãng bay (CMR-03). |
| **UC-DM-10_FUNC_04** | Kiểm tra Validation trường bắt buộc | Xác nhận báo đỏ và hiển thị "{Field} là trường bắt buộc" khi để trống các trường Required. |

### 3.2 Chỉnh sửa (Update)
| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_FUNC_05** | Chỉnh sửa thông tin hãng bay thành công | Xác nhận cập nhật Tên/Quốc gia/Trạng thái và hiển thị Toast Success. |
| **UC-DM-10_FUNC_06** | Kiểm tra khóa trường Mã hãng bay | Xác nhận trường "Mã hãng bay" bị Read-only/Disabled khi mở Popup Sửa (BR-02). |

### 3.3 Xóa (Delete)
| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_FUNC_07** | Xóa thành công hãng bay không có liên kết | Xác nhận Soft Delete thành công sau khi xác nhận Popup. |
| **UC-DM-10_FUNC_08** | Xóa thất bại hãng bay đang có chuyến bay | Xác nhận hiển thị lỗi BR-01: "Không thể xóa hãng bay đang có dữ liệu liên kết chuyến bay." |

---

## 4. RBAC Scenarios (Phân quyền)

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_RBAC_01** | Kiểm tra quyền của Role Admin | Xác nhận hiển thị đầy đủ nút [Thêm mới] và các icon [Sửa], [Xóa] trên danh sách. |
| **UC-DM-10_RBAC_02** | Kiểm tra quyền của Role Sửa | Xác nhận chỉ hiển thị nút [Thêm mới] và icon [Sửa]. Ẩn icon [Xóa]. |
| **UC-DM-10_RBAC_03** | Kiểm tra quyền của Role Xóa | Xác nhận chỉ hiển thị icon [Xem] và [Xóa]. Ẩn nút [Thêm mới] và icon [Sửa]. |

---

## 5. Non-functional & Boundary Scenarios

| Scenario ID | Scenario Title | Objective |
| :--- | :--- | :--- |
| **UC-DM-10_NFC_01** | Kiểm tra độ dài tối đa của Mã hãng bay | Xác nhận không cho nhập quá 10 ký tự hoặc tự động cắt nếu paste (CMR-03). |
| **UC-DM-10_NFC_02** | Kiểm tra ký tự đặc biệt trong Mã hãng bay | Xác nhận hệ thống chặn nhập dấu và khoảng trắng cho Mã hãng bay. |
| **UC-DM-10_NFC_03** | Kiểm tra kết nối mạng bị gián đoạn | Xác nhận hiển thị Toast lỗi CMR-12 khi mất mạng trong lúc Lưu. |
