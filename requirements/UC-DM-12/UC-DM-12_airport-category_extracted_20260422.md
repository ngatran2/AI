# UC-DM-12: Quản lý danh mục sân bay

| Field       | Value                    |
|-------------|--------------------------|
| Source      | https://docs.google.com/document/d/1OfaNXQmPYw6p_aRSsWvWQ3mZ1b_VD-JMd1ZWZyXBrvc/edit |
| Extracted   | 2026-04-22               |
| Agent       | docs-reader               |
| UC-ID       | UC-DM-12                  |
| Version     | v1.0                      |

### **2.2.12 UC-DM-12: Quản lý danh mục sân bay**

| ID | Use case | Mô tả |
| :--- | :--- | :--- |
| UC-DM-12 | Quản lý danh mục sân bay | Màn hình Danh mục sân bay bao gồm các UC:<br><ul><li>UC-SB-12.1: Xem danh mục sân bay</li><li>UC-SB-12.2: Thêm sân bay</li><li>UC-SB-12.3: Xem chi tiết sân bay</li><li>UC-SB-12.4: Sửa sân bay</li><li>UC-SB-12.5: Xóa sân bay</li></ul> |

Người dùng đăng nhập vào hệ thống, chọn “Danh mục - Sân bay” tại sidebar để truy cập chức năng Quản lý danh mục sân bay của hệ thống.

**Trigger**
Người dùng chọn “Danh mục - Sân bay” tại sidebar.

**Pre-conditions**
*   Người dùng đăng nhập hệ thống thành công.
*   Người dùng có quyền truy cập các chức năng quản lý danh mục sân bay tùy theo phân quyền của người dùng, cụ thể từng chức năng được mô tả chi tiết tại từng use case bên dưới.

**Post-conditions**
Tùy theo phân quyền của người dùng, người dùng có thể:
*   Xem được danh mục các sân bay có trong hệ thống và chi tiết từng loại.
*   Thêm được sân bay mới vào danh mục.
*   Sửa thông tin sân bay trong danh mục.
*   Xóa sân bay khỏi danh mục.

---

#### **2.2.12.1 UC-SB-12.1: Xem danh mục sân bay**

| ID | Use case | Mô tả |
| :--- | :--- | :--- |
| UC-SB-12.1 | Xem danh mục sân bay | Người dùng có thể xem và tìm kiếm trong danh mục các sân bay có trong hệ thống. |

**Trigger**
Người dùng chọn “Danh mục - Sân bay” tại sidebar.

**Pre-conditions**
*   Người dùng đăng nhập hệ thống thành công.
*   Người dùng có quyền truy cập chức năng Xem Danh mục - Sân bay.

**Post-conditions**
*   Người dùng được điều hướng tới màn **UI-12.1-a: Danh mục sân bay**.
*   Người dùng xem được danh sách các sân bay trên hệ thống.

**Basic Flow**
1. Người dùng chọn “Danh mục - Sân bay” tại sidebar.
2. Hệ thống điều hướng người dùng tới màn **UI-12.1-a: Danh mục sân bay**.
3. Hệ thống tải và hiển thị danh sách sân bay trong bảng Danh mục sân bay.

**Alternative flow**
**[Tìm kiếm sân bay trong bảng Danh mục sân bay]**
4. Người dùng nhấn icon Search tại các cột của bảng Danh mục sân bay.
5. Hệ thống mở Popup search ([CMR-09]) trên màn **UI-12.1-a**.
6. Người dùng nhập từ khóa tìm kiếm vào popup.
7. Người dùng gõ phím Enter.
8. Hệ thống thực hiện tìm kiếm dựa trên từ khóa đã nhập.
9. Hệ thống tải và hiển thị danh sách sân bay tương ứng.

**[Không có dữ liệu hoặc không có kết quả tìm kiếm]**
Hiển thị màn trống trong bảng Danh mục sân bay ([CMR-08]).

**2.2.12.1.2 Wireframe/UI**
Danh sách UI:
- UI-12.1-a: Danh mục sân bay

**2.2.12.1.3 Mô tả màn hình và quy tắc nghiệp vụ**
Màn hình UI-12.1-a: Danh mục sân bay

| ID | Field Name | Field type | Validation Rule / Behaviour |
| :--- | :--- | :--- | :--- |
| 1 | Danh mục sân bay | Table | Display rule:<br>- Refer CMR-08<br>- Mặc định hiển thị danh sách được sắp xếp theo thời gian tạo giảm dần. |
| 2 | Mã sân bay | Text | Display rule: Hiển thị mã sân bay tương ứng với dữ liệu trong bảng Sân bay. |
| 3 | Sân bay | Text | Display rule: Hiển thị tên sân bay tương ứng với dữ liệu trong bảng Sân bay. |
| 4 | Xem | Button | Display rule: Không hiển thị nếu người dùng có thêm quyền sửa hoặc quyền xóa Danh mục sân bay.<br>Behavior: Khi nhấn nút, hệ thống thực thi chức năng UC-SB-12.3: Xem chi tiết sân bay. |
| 5 | Sửa | Button | Display rule: Chỉ hiển thị nếu người dùng có quyền sửa Danh mục sân bay.<br>Behavior: Khi nhấn nút, hệ thống thực thi chức năng UC-SB-12.4: Sửa sân bay. |
| 6 | Xóa | Button | Display rule: Chỉ hiển thị nếu người dùng có quyền xóa Danh mục sân bay.<br>Behavior: Khi nhấn nút, hệ thống thực thi chức năng UC-SB-12.5: Xóa sân bay. |
| 7 | Thêm mới | Button | Display rule: Chỉ hiển thị nếu người dùng có quyền thêm Danh mục sân bay.<br>Behavior: Khi nhấn nút, hệ thống thực thi chức năng UC-SB-12.2: Thêm sân bay. |

---

#### **2.2.12.2 UC-SB-12.2: Thêm sân bay**

| ID | Use case | Mô tả |
| :--- | :--- | :--- |
| UC-SB-12.2 | Thêm sân bay | Người dùng thêm sân bay mới vào danh mục sân bay của hệ thống. |

**Trigger**
Người dùng nhấn nút “Thêm mới” trên màn **UI-12.1-a: Danh mục sân bay**.

**Pre-conditions**
*   Người dùng đăng nhập hệ thống thành công.
*   Người dùng đang ở màn **UI-12.1-a: Danh mục sân bay**.
*   Người dùng có quyền truy cập chức năng Thêm Danh mục - Sân bay.

**Post-conditions**
*   Sân bay mới được thêm vào danh mục.
*   Hệ thống hiển thị success toast message.
*   Sân bay mới hiển thị ở các danh sách sân bay được sử dụng trên toàn hệ thống.
*   Hệ thống log lịch sử thực hiện hành động:
    *   Tiêu đề: Tạo sân bay mới
    *   Nội dung chi tiết: Tạo mới sân bay [Mã sân bay] vào Danh mục sân bay.

**Basic Flow**
1. Người dùng nhấn nút “Thêm mới”.
2. Hệ thống mở màn **UI-12.2-a: Popup thêm sân bay**.
3. Người dùng nhập các thông tin sân bay.
4. Người dùng nhấn nút “Thêm mới”.
5. Hệ thống thực hiện kiểm tra các ràng buộc dữ liệu ([CMR-01]).
6. Hệ thống thực hiện thêm sân bay mới vào DB.
7. Hệ thống hiển thị success toast message ([CMR-02]).
8. Hệ thống đóng Popup và tải lại danh sách trên màn **UI-12.1-a**.

**Alternative flow**
**[Người dùng nhấn nút Đóng hoặc icon đóng popup]**
1. Người dùng nhấn nút Đóng hoặc icon đóng popup.
2. Hệ thống đóng popup và không lưu dữ liệu.

**Business rule**
*   **BR-12.2.** Mã sân bay phải là duy nhất trên toàn danh mục.
*   **BR-12.3.** Có thể thêm mới mã sân bay trùng với mã sân bay đã bị xóa.
*   **BR-12.4.** Giữ nguyên các điều kiện filter/search và vị trí phân trang sau khi thêm mới thành công.
*   **BR-12.5.** Kiểm tra trạng thái và quyền người dùng tại thời điểm xử lý API.

**2.2.12.2.3 Mô tả màn hình và quy tắc nghiệp vụ**
Màn hình UI-12.2-a: Popup thêm sân bay

| ID | Field Name | Field type | Validation Rule / Behaviour |
| :--- | :--- | :--- | :--- |
| 1 | Popup thêm sân bay | Popup | Validation Rule / Behaviour: Refer CMR-09. |
| 2 | Mã sân bay | Input text | Validation Rule: Bắt buộc nhập, tối đa 255 ký tự, refer CMR-01, BR-12.2. |
| 3 | Sân bay | Input text | Validation Rule: Bắt buộc nhập, tối đa 255 ký tự, refer CMR-01. |
| 4 | Đóng | Button | Behavior: Đóng popup không lưu dữ liệu. |
| 5 | Thêm mới | Button | Behavior: Thực hiện thêm mới dữ liệu. |

---

#### **2.2.12.3 UC-SB-12.3: Xem chi tiết sân bay**

| ID | Use case | Mô tả |
| :--- | :--- | :--- |
| UC-SB-12.3 | Xem chi tiết sân bay | Người dùng có thể xem chi tiết thông tin của một sân bay có trong hệ thống. |

**Trigger**
Người dùng nhấn nút “Xem” trên màn **UI-12.1-a: Danh mục sân bay**.

**Basic Flow**
1. Người dùng nhấn nút Xem của một sân bay trên Danh mục.
2. Hệ thống mở màn **UI-12.3-a: Popup chi tiết sân bay**.

**2.2.12.3.3 Mô tả màn hình và quy tắc nghiệp vụ**
Màn hình UI-12.3-a: Popup chi tiết sân bay

| ID | Field Name | Field type | Validation Rule / Behaviour |
| :--- | :--- | :--- | :--- |
| 1 | Mã sân bay | Text | Display only: Hiển thị mã sân bay. |
| 2 | Sân bay | Text | Display only: Hiển thị tên sân bay. |
| 3 | Xóa | Button | Behavior: Thực thi chức năng UC-SB-12.5: Xóa sân bay. |
| 4 | Cập nhật | Button | Behavior: Thực thi chức năng UC-SB-12.4: Sửa sân bay. |
| 5 | Icon đóng popup | Button | Behavior: Đóng popup. |

---

#### **2.2.12.4 UC-SB-12.4: Sửa sân bay**

| ID | Use case | Mô tả |
| :--- | :--- | :--- |
| UC-SB-12.4 | Sửa sân bay | Người dùng sửa thông tin của một sân bay đã có trong danh mục của hệ thống. |

**Post-conditions**
*   Thông tin sân bay được cập nhật.
*   Hệ thống log lịch sử: Cập nhật thông tin sân bay [Mã sân bay].

**Basic Flow**
1. Người dùng nhấn “Cập nhật” (UI-12.3-a) hoặc “Sửa” (UI-12.1-a).
2. Hệ thống mở màn **UI-12.4-a: Popup sửa sân bay**.
3. Người dùng sửa thông tin và nhấn “Lưu”.
4. Hệ thống kiểm tra dữ liệu, cập nhật DB và hiển thị thông báo thành công.

**2.2.12.4.3 Mô tả màn hình và quy tắc nghiệp vụ**
Màn hình UI-12.4-a: Popup sửa sân bay

| ID | Field Name | Field type | Validation Rule / Behaviour |
| :--- | :--- | :--- | :--- |
| 1 | Mã sân bay | Input text | Validation Rule: Read-only. |
| 2 | Sân bay | Input text | Validation Rule: Bắt buộc nhập, tối đa 255 ký tự. |
| 3 | Hủy | Button | Behavior: Đóng popup không lưu. |
| 4 | Cập nhật | Button | Behavior: Cập nhật dữ liệu vào DB (Disable nếu không có thay đổi). |

---

#### **2.2.12.5 UC-SB-12.5: Xóa sân bay**

| ID | Use case | Mô tả |
| :--- | :--- | :--- |
| UC-SB-12.5 | Xóa sân bay | Người dùng có thể xóa một sân bay ra khỏi danh mục của hệ thống. |

**Basic Flow**
1. Người dùng nhấn nút “Xóa”.
2. Hệ thống hiển thị popup confirm xóa ([CMR-03]).
3. Người dùng nhấn “Xóa” trên popup confirm.
4. Hệ thống thực hiện xóa khỏi DB và hiển thị thông báo thành công.

**2.2.12.5.2 Mô tả màn hình và quy tắc nghiệp vụ (Popup Confirm Xóa)**

| ID | Field Name | Field type | Validation Rule / Behaviour |
| :--- | :--- | :--- | :--- |
| 1 | Popup confirm xóa | Popup | Refer CMR-03. |
| 2 | Hủy | Button | Behavior: Đóng popup không xóa. |
| 3 | Xóa | Button | Behavior: Thực hiện xóa dữ liệu. |
