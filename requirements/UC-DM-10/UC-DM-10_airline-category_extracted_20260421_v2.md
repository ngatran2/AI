# UC-DM-10: Quản lý danh mục hãng bay

## 1. Mô tả (Description)
- Chức năng cho phép người dùng quản lý thông tin các hãng hàng không (Airlines) trong hệ thống LAMS.
- Bao gồm các hành động: Xem danh sách, Thêm mới, Chỉnh sửa, và Xóa thông tin hãng bay.

## 2. Giao diện Danh sách (List Screen)
- **Cột hiển thị:**
    - `Mã hãng bay`: Hiển thị mã tương ứng, không giới hạn ký tự.
    - `Hãng bay`: Hiển thị tên hãng bay, giới hạn hiển thị trên 1 dòng.
- **Bộ lọc tìm kiếm:**
    - Trường tìm kiếm: `Mã hãng bay`, `Hãng bay`.
    - Cơ chế: Tìm kiếm chính xác, tìm kiếm tương đối, nhập tất cả ký tự.
    - Logic: Cho phép tìm kiếm kết hợp (AND) nhiều tiêu chí cùng lúc.
- **Phân trang:**
    - Cấu hình: 20 bản ghi/trang.
    - Điều hướng: Nút [Trang trước], [Trang sau].

## 3. Thông tin các trường dữ liệu (Form Fields) - Hiển thị trên Popup
| Tên trường | Kiểu dữ liệu | Bắt buộc | Ràng buộc |
| :--- | :--- | :--- | :--- |
| Mã hãng bay | String | Có | Duy nhất, không dấu, không khoảng trắng, max 10 ký tự |
| Tên hãng bay | String | Có | Max 100 ký tự |
| Quốc gia | Dropdown | Có | Chọn từ danh sách quốc gia có sẵn |
| Trạng thái | Toggle | Có | Hoạt động / Ngừng hoạt động |
| Mô tả | Textarea | Không | Max 500 ký tự |

## 4. Luồng nghiệp vụ (Business Flows)
- **Thêm/Sửa:** Khi click vào nút [Thêm mới] hoặc icon [Sửa], hệ thống hiển thị **Popup** đè lên trang danh sách.
- **Xóa:** Sử dụng cơ chế **Soft delete** (Xóa mềm).
- **Thông báo:** Đã có định nghĩa thông báo Thành công/Thất bại trong tài liệu gốc.

## 5. Phân quyền (RBAC Matrix)
| Role | Xem | Thêm | Sửa | Xóa |
| :--- | :--- | :--- | :--- | :--- |
| Role Xóa | ✅ | ❌ | ❌ | ✅ |
| Role Sửa | ✅ | ✅ | ✅ | ❌ |
| Admin | ✅ | ✅ | ✅ | ✅ |

## 6. Business Rules
- **BR-01:** Không được phép xóa hãng bay nếu hãng đó đang có dữ liệu liên kết trong phần Quản lý chuyến bay.
- **BR-02:** Mã hãng bay sau khi tạo không được phép chỉnh sửa.
- **BR-03:** Trạng thái mặc định khi thêm mới là "Hoạt động".
