# Test Scenarios

> [!WARNING]
> **Human Checkpoint:** User cần review danh sách High-Level Scenarios dưới đây để bổ sung các trường hợp rủi ro đặc thù (nếu có) trước khi Agent tiến hành sinh Test Cases chi tiết ở bước tiếp theo.

## 1. Traceability Matrix & Gap Analysis

| Req-ID | Module / Feature | Covered by Scenarios | Status |
|--------|------------------|----------------------|--------|
| REQ-12.1 | Xem danh mục sân bay (Hiển thị, Phân trang, Search) | TS_12.1_001, TS_12.1_002, TS_12.1_003, TS_12.1_004, TS_12.1_005 | Covered |
| REQ-12.2 | Thêm sân bay (Validation, BVA, Duplicate, BR-12.3, BR-12.4) | TS_12.2_001, TS_12.2_002, TS_12.2_003, TS_12.2_004, TS_12.2_005, TS_12.2_006, TS_12.2_007, TS_12.2_008 | Covered |
| REQ-12.3 | Xem chi tiết sân bay | TS_12.3_001 | Covered |
| REQ-12.4 | Sửa sân bay (Read-only ID, Disable nút Lưu, Cập nhật Tên) | TS_12.4_001, TS_12.4_002, TS_12.4_003, TS_12.4_004 | Covered |
| REQ-12.5 | Xóa sân bay (Xóa thành công, Chặn xóa khi có liên kết) | TS_12.5_001, TS_12.5_002, TS_12.5_003 | Covered |
| REQ-INT | Tích hợp hiển thị danh sách sân bay sang Phòng chờ | TS_INT_001, TS_INT_002 | Covered |
| REQ-RBAC | Phân quyền truy cập chức năng (Admin vs View) | TS_RBAC_001, TS_RBAC_002 | Covered |

---

## 2. Detailed Scenarios

### UC-SB-12.1 — Xem danh mục sân bay

### Scenario ID: TS_12.1_001
**Scenario Title:** Kiểm tra hiển thị mặc định bảng Danh mục sân bay và phân trang
**UC Reference:** UC-SB-12.1 Xem danh mục sân bay
**Req-ID:** REQ-12.1
**Test Type:** Functional
**Description:** Đảm bảo bảng danh sách hiển thị đúng các cột, sắp xếp giảm dần theo thời gian tạo, phân trang 20 bản ghi/trang theo CMR-08.
**Test Focus:** Happy path

### Scenario ID: TS_12.1_002
**Scenario Title:** Tìm kiếm tương đối có kết quả theo Tên sân bay
**UC Reference:** UC-SB-12.1 Xem danh mục sân bay
**Req-ID:** REQ-12.1
**Test Type:** Functional
**Description:** Mở popup search ở cột Sân bay, nhập từ khóa tìm kiếm (tương đối), nhấn Enter và verify danh sách trả về đúng các bản ghi chứa từ khóa.
**Test Focus:** Happy path

### Scenario ID: TS_12.1_003
**Scenario Title:** Tìm kiếm chính xác có kết quả theo Mã sân bay
**UC Reference:** UC-SB-12.1 Xem danh mục sân bay
**Req-ID:** REQ-12.1
**Test Type:** Functional
**Description:** Mở popup search ở cột Mã sân bay, nhập mã tìm kiếm chính xác, nhấn Enter và verify danh sách trả về đúng 1 bản ghi.
**Test Focus:** Happy path

### Scenario ID: TS_12.1_004
**Scenario Title:** Tìm kiếm với từ khóa không tồn tại (Empty State)
**UC Reference:** UC-SB-12.1 Xem danh mục sân bay
**Req-ID:** REQ-12.1
**Test Type:** UI
**Description:** Tìm kiếm bằng một Mã/Tên không có trong hệ thống và verify bảng hiển thị màn hình trống "[Không có dữ liệu hoặc không có kết quả tìm kiếm]".
**Test Focus:** Alternative flow

### Scenario ID: TS_12.1_005
**Scenario Title:** Bỏ qua khoảng trắng khi tìm kiếm (Trim Text)
**UC Reference:** UC-SB-12.1 Xem danh mục sân bay
**Req-ID:** REQ-12.1
**Test Type:** Functional
**Description:** Nhập toàn khoảng trắng (space) vào ô tìm kiếm và nhấn Enter. Hệ thống tự động trim, coi như không nhập (hiển thị dữ liệu mặc định).
**Test Focus:** Boundary / Edge Case

---

### UC-SB-12.2 — Thêm sân bay

### Scenario ID: TS_12.2_001
**Scenario Title:** Thêm mới sân bay thành công với biên dưới (1 ký tự)
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-12.2
**Test Type:** Functional
**Description:** Điền 1 ký tự vào Mã sân bay và 1 ký tự vào Tên sân bay, verify thêm mới thành công và hiển thị Toast "Thêm mới [mã sân bay - sân bay] thành công.".
**Test Focus:** Boundary

### Scenario ID: TS_12.2_002
**Scenario Title:** Thêm mới sân bay thành công với biên trên (255 ký tự)
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-12.2
**Test Type:** Functional
**Description:** Điền chính xác 255 ký tự vào Mã sân bay và Tên sân bay, verify thêm mới thành công và hiển thị Toast "Thêm mới [mã sân bay - sân bay] thành công.".
**Test Focus:** Boundary

### Scenario ID: TS_12.2_003
**Scenario Title:** Thêm mới thất bại khi nhập quá giới hạn maxlength (256 ký tự)
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-12.2
**Test Type:** Functional
**Description:** Thử copy-paste chuỗi 256 ký tự vào các input. Hệ thống tự động cắt chuỗi (truncate) phần dữ liệu thừa.
**Test Focus:** Error/Exception / Boundary

### Scenario ID: TS_12.2_004
**Scenario Title:** Thêm mới thất bại khi bỏ trống các trường bắt buộc
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-12.2
**Test Type:** UI
**Description:** Để trống Mã sân bay hoặc Sân bay và nhấn Thêm mới. Verify hệ thống bôi đỏ viền và hiển thị text lỗi theo format {Tên field} + " là trường bắt buộc" (VD: "Mã sân bay là trường bắt buộc").
**Test Focus:** Error/Exception

### Scenario ID: TS_12.2_005
**Scenario Title:** Thêm mới thất bại khi Mã sân bay trùng lặp
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-12.2
**Test Type:** Functional
**Description:** Nhập Mã sân bay đã tồn tại trong danh sách. Hệ thống báo lỗi "Mã sân bay đã tồn tại" chặn thêm mới (BR-12.2).
**Test Focus:** Error/Exception / Business Rule

### Scenario ID: TS_12.2_006
**Scenario Title:** Thêm mới thành công Mã sân bay đã bị xóa
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-12.2
**Test Type:** Functional
**Description:** Thêm mới một sân bay có Mã sân bay trùng với một Mã đã bị thao tác xóa trước đó. Hệ thống tạo thành công (BR-12.3).
**Test Focus:** Happy path / Business Rule

### Scenario ID: TS_12.2_007
**Scenario Title:** Giữ nguyên điều kiện Filter và Phân trang sau khi tạo mới
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-12.2
**Test Type:** UI
**Description:** Đang ở trang 2 và đang áp dụng từ khóa search, nhấn Thêm mới thành công -> Verify sau khi popup đóng, hệ thống vẫn giữ nguyên trang 2 và từ khóa search (BR-12.4).
**Test Focus:** UI State / Business Rule

### Scenario ID: TS_12.2_008
**Scenario Title:** Đóng popup thêm mới không lưu dữ liệu
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-12.2
**Test Type:** UI
**Description:** Nhập dữ liệu dở dang, nhấn Đóng. Mở lại popup verify các trường đã bị reset về rỗng.
**Test Focus:** Alternative flow

---

### UC-SB-12.3 & 12.4 — Xem chi tiết & Sửa sân bay

### Scenario ID: TS_12.3_001
**Scenario Title:** Xem chi tiết thông tin sân bay
**UC Reference:** UC-SB-12.3 Xem chi tiết sân bay
**Req-ID:** REQ-12.3
**Test Type:** Functional
**Description:** Nhấn nút Xem, hiển thị đúng thông tin Mã và Tên của sân bay đã chọn. Nút Xóa/Cập nhật điều hướng đúng.
**Test Focus:** Happy path

### Scenario ID: TS_12.4_001
**Scenario Title:** Trường Mã sân bay Read-only khi Sửa
**UC Reference:** UC-SB-12.4 Sửa sân bay
**Req-ID:** REQ-12.4
**Test Type:** UI
**Description:** Mở màn hình Sửa, xác nhận input Mã sân bay bị khóa (Read-only), không thể chỉnh sửa.
**Test Focus:** UI State

### Scenario ID: TS_12.4_002
**Scenario Title:** Vô hiệu hóa nút Cập nhật khi không có thay đổi
**UC Reference:** UC-SB-12.4 Sửa sân bay
**Req-ID:** REQ-12.4
**Test Type:** UI
**Description:** Vừa mở popup Sửa hoặc sau khi Cập nhật thành công, nếu không thay đổi thêm giá trị Tên sân bay nào, nút Cập nhật ở trạng thái Disabled.
**Test Focus:** UI State / Boundary

### Scenario ID: TS_12.4_003
**Scenario Title:** Cập nhật thành công Tên sân bay
**UC Reference:** UC-SB-12.4 Sửa sân bay
**Req-ID:** REQ-12.4
**Test Type:** Functional
**Description:** Sửa trường Tên sân bay (hợp lệ), nhấn Cập nhật. Toast message hiển thị thành công, hệ thống tự động đóng popup.
**Test Focus:** Happy path / UI State

### Scenario ID: TS_12.4_004
**Scenario Title:** Cập nhật thất bại khi bỏ trống Tên sân bay
**UC Reference:** UC-SB-12.4 Sửa sân bay
**Req-ID:** REQ-12.4
**Test Type:** Functional
**Description:** Xóa trắng Tên sân bay, verify hệ thống chặn Lưu và báo lỗi "Sân bay là trường bắt buộc".
**Test Focus:** Error/Exception / EP Validation

---

### UC-SB-12.5 — Xóa sân bay

### Scenario ID: TS_12.5_001
**Scenario Title:** Xóa sân bay thành công
**UC Reference:** UC-SB-12.5 Xóa sân bay
**Req-ID:** REQ-12.5
**Test Type:** Functional
**Description:** Nhấn Xóa một sân bay chưa có bất kỳ liên kết phòng chờ nào -> Xác nhận xóa trên popup -> Toast message báo "Xóa [mã sân bay - sân bay] và các phòng chờ liên quan thành công." và bản ghi biến mất khỏi lưới.
**Test Focus:** Happy path

### Scenario ID: TS_12.5_002
**Scenario Title:** [SKIPPED - Chưa làm] Chặn xóa sân bay đang được sử dụng
**UC Reference:** UC-SB-12.5 Xóa sân bay
**Req-ID:** REQ-12.5
**Test Type:** Functional
**Description:** Cố gắng xóa một sân bay đã được gán vào ít nhất 1 Phòng chờ. Hệ thống chặn lại và cảnh báo "Không thể xóa khi sân bay đang được sử dụng."
**Test Focus:** Error/Exception / Business Rule

### Scenario ID: TS_12.5_003
**Scenario Title:** Hủy xác nhận Xóa
**UC Reference:** UC-SB-12.5 Xóa sân bay
**Req-ID:** REQ-12.5
**Test Type:** UI
**Description:** Nhấn nút Xóa để mở popup CMR-03, chọn "Hủy". Popup đóng và dữ liệu sân bay không bị xóa.
**Test Focus:** Alternative flow

---

### Integration & Phân Quyền (RBAC)

### Scenario ID: TS_INT_001
**Scenario Title:** Tích hợp: Dữ liệu Sân bay đồng bộ sang form tạo Phòng chờ
**UC Reference:** UC-SB-12.2 Thêm sân bay
**Req-ID:** REQ-INT
**Test Type:** Integration
**Description:** Sau khi thêm mới 1 Sân bay thành công, sang module Phòng chờ (Tạo mới), kiểm tra dropdown Mã sân bay và Tên sân bay đã xuất hiện dữ liệu vừa tạo.
**Test Focus:** Happy path / Cross-module

### Scenario ID: TS_INT_002
**Scenario Title:** Tích hợp: Cập nhật Tên sân bay đồng bộ sang các module sử dụng
**UC Reference:** UC-SB-12.4 Sửa sân bay
**Req-ID:** REQ-INT
**Test Type:** Integration
**Description:** Cập nhật Tên sân bay thành công, sang module Phòng chờ, kiểm tra dropdown hiển thị đúng Tên sân bay mới.
**Test Focus:** Happy path / Cross-module

### Scenario ID: TS_RBAC_001
**Scenario Title:** Phân quyền: Role Admin thực hiện full quyền CUD
**UC Reference:** UC-DM-12
**Req-ID:** REQ-RBAC
**Test Type:** Security / Access Control
**Description:** Đăng nhập bằng tài khoản có quyền Admin Sân bay, xác nhận nút Xem bị ẩn, các nút Thêm/Sửa/Xóa hiển thị và hoạt động bình thường.
**Test Focus:** Role/Permission

### Scenario ID: TS_RBAC_002
**Scenario Title:** Phân quyền: Role View bị ẩn các chức năng thao tác dữ liệu
**UC Reference:** UC-DM-12
**Req-ID:** REQ-RBAC
**Test Type:** Security / Access Control
**Description:** Đăng nhập bằng tài khoản chỉ có quyền View, xác nhận chỉ thấy nút Xem chi tiết. Các nút Thêm/Sửa/Xóa bị ẩn hoàn toàn (Kiểm thử cố gọi API CUD sẽ bị báo lỗi 403 CMR-14).
**Test Focus:** Role/Permission

### Scenario ID: TS_RBAC_003
**Scenario Title:** Phân quyền: Role Edit chỉ có quyền Sửa và Thêm
**UC Reference:** UC-DM-12
**Req-ID:** REQ-RBAC
**Test Type:** Security / Access Control
**Description:** Đăng nhập bằng tài khoản chỉ có quyền Edit, xác nhận nút Sửa và Thêm hiển thị và thao tác thành công. Các nút Xóa và Xem bị ẩn.
**Test Focus:** Role/Permission

### Scenario ID: TS_RBAC_004
**Scenario Title:** Phân quyền: Role Delete chỉ có quyền Xóa và Xem
**UC Reference:** UC-DM-12
**Req-ID:** REQ-RBAC
**Test Type:** Security / Access Control
**Description:** Đăng nhập bằng tài khoản chỉ có quyền Delete, xác nhận nút Xóa và Xem hiển thị và thao tác thành công. Các nút Thêm và Sửa bị ẩn.
**Test Focus:** Role/Permission

### Scenario ID: TS_RBAC_005
**Scenario Title:** Phân quyền: Role Locked bị khóa tài khoản
**UC Reference:** UC-DM-12
**Req-ID:** REQ-RBAC
**Test Type:** Security / Access Control
**Description:** Đăng nhập bằng tài khoản Locked, hệ thống báo lỗi không thể đăng nhập hoặc không thể thực hiện bất kỳ hành động nào.
**Test Focus:** Role/Permission
