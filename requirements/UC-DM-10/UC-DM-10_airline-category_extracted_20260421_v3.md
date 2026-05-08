# UC-DM-10: Quản lý danh mục hãng bay (FULL DETAILS)

## 1. Mô tả (Description)
Chức năng cho phép Admin hoặc các Role được phân quyền quản lý thông tin các hãng hàng không (Airlines). Dữ liệu này được dùng chung cho module Quản lý chuyến bay.

## 2. Giao diện Danh sách & Bộ lọc (List & Search UI)
- **Cấu trúc bảng (Grid):**
    - `Mã hãng bay`: Text, hiển thị đầy đủ, không giới hạn.
    - `Hãng bay`: Text, hiển thị trên 1 dòng (Ellipsis nếu quá dài).
    - `Thao tác`: Chứa các icon Xem, Sửa, Xóa tùy theo Role.
- **Bộ lọc (Filter Bar):**
    - Tìm kiếm theo `Mã hãng bay` và `Hãng bay`.
    - Hỗ trợ: Tìm kiếm chính xác, tìm kiếm tương đối (Partial match).
    - Logic: Kết hợp AND (Tìm theo cả 2 trường cùng lúc).
- **Phân trang:** 20 bản ghi/trang. Có nút [Trang trước], [Trang sau].

## 3. Luồng nghiệp vụ & Thông báo (Flows & Messages)

### 3.1 Luồng Thêm mới (Create Flow)
1. Bấm nút [Thêm mới] -> Hiển thị Popup Form.
2. Nhập các trường: Mã hãng bay (Bắt buộc, Duy nhất), Tên hãng bay (Bắt buộc), Quốc gia (Dropdown), Trạng thái (Toggle), Mô tả.
3. Bấm [Lưu].
4. **Thông báo lỗi (Error Messages):**
    - Trùng mã: "Mã hãng bay đã tồn tại trong hệ thống."
    - Thiếu trường bắt buộc: "[Tên trường] là trường bắt buộc."
    - Vượt quá ký tự: "Độ dài tối đa là [N] ký tự."
5. **Thông báo thành công:** "Thêm mới hãng bay thành công."

### 3.2 Luồng Chỉnh sửa (Update Flow)
1. Bấm icon [Sửa] trên dòng dữ liệu -> Hiển thị Popup Form với dữ liệu cũ.
2. **Ràng buộc:** Mã hãng bay bị Disable (không cho sửa).
3. Cập nhật thông tin và bấm [Lưu].
4. **Thông báo thành công:** "Cập nhật hãng bay thành công."

### 3.3 Luồng Xóa (Delete Flow)
1. Bấm icon [Xóa] -> Hiển thị Popup xác nhận "Bạn có chắc chắn muốn xóa hãng bay này?".
2. Nếu bấm [Đồng ý]:
    - Kiểm tra BR-01: Nếu đang liên kết chuyến bay -> Thông báo lỗi: "Không thể xóa hãng bay đang có dữ liệu liên kết chuyến bay."
    - Nếu hợp lệ -> Thực hiện **Soft Delete**.
3. **Thông báo thành công:** "Xóa hãng bay thành công."

## 4. Phân quyền (RBAC Matrix)
- **Admin:** Thấy nút Thêm, Sửa, Xóa.
- **Role Sửa:** Thấy nút Thêm, Sửa.
- **Role Xóa:** Thấy nút Xem, Xóa.

## 5. Business Rules
- **BR-01:** Ràng buộc xóa (Referential Integrity).
- **BR-02:** Khóa Mã hãng bay khi sửa.
- **BR-03:** Mặc định "Hoạt động" khi thêm mới.
