# UC-DM-10: Quản lý danh mục hãng bay

## 1. Mô tả (Description)
- Chức năng cho phép người dùng quản lý thông tin các hãng hàng không (Airlines) trong hệ thống LAMS.
- Bao gồm các hành động: Xem danh sách, Thêm mới, Chỉnh sửa, và Xóa thông tin hãng bay.

## 2. Thông tin các trường dữ liệu (Field Information)

| Tên trường | Kiểu dữ liệu | Bắt buộc | Ràng buộc |
| :--- | :--- | :--- | :--- |
| Mã hãng bay | String | Có | Duy nhất, không dấu, không khoảng trắng, max 10 ký tự |
| Tên hãng bay | String | Có | Max 100 ký tự |
| Quốc gia | Dropdown | Có | Chọn từ danh sách quốc gia có sẵn |
| Trạng thái | Toggle | Có | Hoạt động / Ngừng hoạt động |
| Mô tả | Textarea | Không | Max 500 ký tự |

## 3. Luồng nghiệp vụ (Business Flows)

### 3.1 Thêm mới hãng bay
1. Người dùng chọn nút [Thêm mới].
2. Hệ thống hiển thị Form nhập liệu.
3. Người dùng nhập thông tin và nhấn [Lưu].
4. Hệ thống kiểm tra tính duy nhất của Mã hãng bay.
5. Nếu hợp lệ, lưu vào DB và hiển thị thông báo thành công.

### 3.2 Chỉnh sửa hãng bay
1. Người dùng chọn icon [Sửa] tại dòng tương ứng trên danh sách.
2. Hệ thống hiển thị Form với dữ liệu cũ.
3. Người dùng cập nhật thông tin và nhấn [Lưu].
4. Hệ thống cập nhật dữ liệu và hiển thị thông báo thành công.

### 3.3 Xóa hãng bay
1. Người dùng chọn icon [Xóa].
2. Hệ thống hiển thị popup xác nhận.
3. Nếu người dùng chọn [Đồng ý], hệ thống xóa (hoặc xóa mềm) và thông báo thành công.

## 4. Business Rules
- **BR-01:** Không được phép xóa hãng bay nếu hãng đó đang có dữ liệu liên kết trong phần Quản lý chuyến bay.
- **BR-02:** Mã hãng bay sau khi tạo không được phép chỉnh sửa.
- **BR-03:** Trạng thái mặc định khi thêm mới là "Hoạt động".
