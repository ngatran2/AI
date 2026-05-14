# Hệ thống Lounge Access Management - Common Rules (Yêu cầu chung)

| Field       | Value                    |
|-------------|--------------------------|
| Source      | [Google Doc](https://docs.google.com/document/d/1OfaNXQmPYw6p_aRSsWvWQ3mZ1b_VD-JMd1ZWZyXBrvc/edit?usp=sharing) |
| Extracted   | 2026-04-21               |
| Agent       | docs-reader               |
| UC-ID       | COMMON                    |
| Version     | 1.0                       |

## 1. Yêu cầu chung (Common Rules)

### CMR-01: Breadcrumb
- **Hiển thị:**
    - Áp dụng cho các màn hình không phải Dashboard và Hồ sơ người dùng.
    - Thứ tự từ trái sang phải, từ cấp cao đến thấp, ngăn cách bởi "/".
    - Nếu quá dài: Rút gọn cấp trung gian bằng "...". Cấp đầu và cấp cuối luôn hiển thị.
    - Không hiển thị trên popup/modal.
- **Hành vi:**
    - Cấp đầu (Header sidebar): Không thể click.
    - Cấp trung gian: Có thể click để điều hướng, đổi màu khi hover.
    - Cấp cuối (Trang hiện tại): Không thể click, highlight text.

### CMR-02: Dropdown list
- Hiển thị toàn bộ tùy chọn khi nhấn.
- Hiển thị tối đa 5 tùy chọn. Nhiều hơn 5 thì có thanh cuộn (scroll).
- Tên quá dài: Hiển thị "..." ở cuối, cho phép hover để xem đầy đủ.
- Khi chọn: Giá trị thay thế placeholder, dropdown tự đóng. Tùy chọn đang chọn được highlight khi mở lại.

### CMR-03: Text field / Text area / Search box
- Tự động loại bỏ khoảng trắng ở đầu và cuối (Trim).
- Nếu chỉ nhập khoảng trắng -> Coi như không có nội dung.
- Hỗ trợ copy-paste. Nếu dài quá giới hạn -> Tự động cắt bỏ ký tự thừa.
- Khi click: Hiển thị con trỏ nhập liệu, text thay thế placeholder. Xóa hết text -> Placeholder hiện lại.

### CMR-04: Toast message
- Thời gian hiển thị: 5 giây.
- Vị trí: Góc dưới bên trái màn hình.
- **Success:** Tiêu đề "Thành công", nội dung theo từng UC.
- **Error:** Tiêu đề "Thất bại", nội dung theo từng UC.

### CMR-05: Validation
- Check lỗi sau khi click button xác nhận.
- Thông báo lỗi hiển thị dưới trường thông tin, bôi đỏ border input.
- Khi nhập đúng dữ liệu -> Ẩn thông báo lỗi.

### CMR-06: Phân trang (Pagination)
- Luôn hiển thị ở các bảng dữ liệu.
- Hiển thị tổng số bản ghi (Total).
- Tối đa 20 bản ghi/trang.
- Nút Previous/Next: Điều hướng trang, disable khi ở trang đầu/cuối.

### CMR-07: Required field (Trường bắt buộc)
- Nút xác nhận vẫn luôn enable.
- Sau khi click, nếu trường trống -> Hiển thị "{Tên field} là trường bắt buộc" và bôi đỏ khung input.

### CMR-08: Table (Bảng dữ liệu)
- Mặc định hiện 20 bản ghi.
- Text quá dài -> Hiển thị "..." ở cuối (ellipsis).
- Hỗ trợ icon Search (CMR-09), Filter (CMR-10), Sort (CMR-11) tại header.
- Tại một thời điểm chỉ mở 1 Search/Filter box của 1 cột.
- Hỗ trợ lọc đa cột (multi-column) theo cơ chế tuần tự (Lọc cột A -> Kết quả A -> Lọc tiếp cột B trên kết quả A).
- Màn hình trống: Hiển thị khi không có dữ liệu hoặc không có kết quả lọc.

### CMR-09: Search (Tìm kiếm trong bảng)
- Chuẩn Ant Design table column.
- Nhấn ENTER để thực hiện search.
- Search box trống + ENTER -> Hiển thị toàn bộ dữ liệu mặc định.
- Đang nhập nhưng chưa confirm (chuyển trang/out focus) -> Giữ nguyên text trong box.

### CMR-10: Filter (Lọc trong bảng)
- Chuẩn Ant Design filter search.
- Hiển thị tối đa 5 mục, quá 5 có thanh cuộn.
- Đang chọn nhưng chưa confirm (chuyển trang/out focus) -> Giữ nguyên lựa chọn.
- Mặc định khi truy cập màn hình: Không áp dụng bộ lọc.

### CMR-11: Sort (Sắp xếp trong bảng)
- Chuẩn Ant Design table column.

### CMR-12: Loading state
- Áp dụng cho mọi hành động gọi API (Search, Save, Submit, Reload, Filter...).
- Khi nhấn nút trigger API:
    - Nút: Disable.
    - Trang/Bảng: Hiển thị loading overlay.
- Hiển thị đến khi có response hoặc quá 60s (Timeout).
- Sau 60s -> Error toast: "Không thể kết nối tới hệ thống. Vui lòng thử lại."
- Mất kết nối mạng: Tắt loading, giữ dữ liệu cũ, Toast: "Kết nối mạng bị gián đoạn. Vui lòng kiểm tra và thử lại."

### CMR-13: Lỗi 404 (Not found)
- Toast/Message: "Không tìm thấy dữ liệu - Bản ghi có thể đã bị xóa hoặc không còn khả dụng."

### CMR-14: Lỗi 403 (Forbidden)
- Giữ ở màn hiện tại.
- Toast: "Người dùng không có quyền truy cập chức năng này"

### CMR-15: Lỗi 400 (Bad request)
- Hiển thị thông báo lỗi tương ứng theo định nghĩa từng UC.

### CMR-16: Lỗi 500 (Internal server error)
- Toast: "Lỗi hệ thống. Vui lòng thử lại"

### CMR-17: Ngày tháng năm
- Định dạng mặc định: dd/mm/yyyy

### CMR-18: Lỗi 401 (Unauthorized)
- Toast: "Phiên đăng nhập hết hạn. Vui lòng thử lại."
- Điều hướng về màn UI-01-a: Đăng nhập.

## 2. Header & Sidebar (Phụ lục)

### Header (WF_2.2.0.1)
- **Ngôn ngữ:** Dropdown Tiếng Việt/Tiếng Anh. Cập nhật toàn bộ hệ thống sau khi chọn.
- **Profile:** 
    - Hiển thị tên đầy đủ.
    - Menu: Đổi mật khẩu (UC-MK-03), Đăng xuất.
    - Đăng xuất: Hiển thị popup xác nhận, xóa session, về màn Login. Chặn Back browser sau khi đăng xuất.

### Sidebar (WF_2.2.0.2 & 0.3)
- Hỗ trợ trạng thái Mở rộng và Thu gọn.
- Logo: Click về Dashboard.
- Menu list: Phân nhóm (Scan, Văn bản - Tài liệu, Danh mục, Báo cáo, Hệ thống).
- Trạng thái Thu gọn: Hiển thị icon, hover highlight, click mở rộng dropdown.
