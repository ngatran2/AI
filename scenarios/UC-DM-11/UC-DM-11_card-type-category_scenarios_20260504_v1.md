# Test Scenarios

> [!WARNING]
> **Human Checkpoint:** User cần review danh sách High-Level Scenarios dưới đây để bổ sung các trường hợp rủi ro đặc thù (nếu có) trước khi Agent tiến hành sinh Test Cases chi tiết ở bước tiếp theo.

## 1. Traceability Matrix & Gap Analysis

| Req-ID | Module / Feature | Covered by Scenarios | Status |
|--------|------------------|----------------------|--------|
| REQ-11.1 | Xem danh mục & Tìm kiếm | TS_UCDM11_001, 002, 025 | Covered |
| REQ-11.2 | Thêm loại thẻ | TS_UCDM11_003, 004, 005, 006, 007, 008, 009, 010 | Covered |
| REQ-11.3 | Xem chi tiết loại thẻ | TS_UCDM11_011 | Covered |
| REQ-11.4 | Sửa loại thẻ | TS_UCDM11_012, 013, 014, 015 | Covered |
| REQ-11.5 | Xóa loại thẻ & Soft Delete | TS_UCDM11_016, 017, 018 | Covered |
| REQ-11.6 | Phân quyền truy cập (RBAC) | TS_UCDM11_019, 020, 021, 022, 023 | Covered |
| REQ-11.7 | Lưu vết hệ thống (Audit Log) | TS_UCDM11_024 | Covered |

---

## 2. Detailed Scenarios

### UC-DM-11 — Quản lý danh mục loại thẻ

### Scenario ID: TS_UCDM11_001
**Scenario Title:** Xem danh sách loại thẻ khi có dữ liệu
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.1
**Test Type:** UI / Functional
**Description:** Kiểm tra bảng danh mục hiển thị đầy đủ các cột dữ liệu (Mã thẻ, Loại thẻ, Hãng bay) và sắp xếp mặc định theo thời gian tạo giảm dần.
**Test Focus:** Happy path

### Scenario ID: TS_UCDM11_002
**Scenario Title:** Xem danh sách loại thẻ khi không có dữ liệu
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.1
**Test Type:** UI / Functional
**Description:** Kiểm tra bảng danh mục hiển thị màn hình trống (Empty state - CMR-08) khi chưa có loại thẻ nào trong hệ thống.
**Test Focus:** Alternative flow / UI State

### Scenario ID: TS_UCDM11_003
**Scenario Title:** Thêm mới loại thẻ thành công
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.2
**Test Type:** Functional / End-to-End
**Description:** Nhập đầy đủ thông tin hợp lệ (Mã thẻ, Loại thẻ, Hãng bay) và lưu thành công, bản ghi hiển thị trên lưới.
**Test Focus:** Happy path

### Scenario ID: TS_UCDM11_004
**Scenario Title:** Thêm mới loại thẻ - Bỏ trống trường bắt buộc
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.2
**Test Type:** Functional
**Description:** Để trống trường Mã thẻ hoặc Hãng bay và nhấn Thêm mới, kiểm tra hệ thống hiển thị câu cảnh báo "[Tên field] là trường bắt buộc" dưới các trường và border đỏ.
**Test Focus:** Validation / Error flow

### Scenario ID: TS_UCDM11_005
**Scenario Title:** Thêm mới loại thẻ - Kiểm tra biên (BVA) cho độ dài chuỗi
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.2
**Test Type:** Functional
**Description:** Kiểm tra nhập đúng 30 ký tự cho Mã thẻ và 100 ký tự cho Loại thẻ (Boundary exact match). Kiểm tra UI không cho phép nhập ký tự thứ 31 và 101.
**Test Focus:** Boundary

### Scenario ID: TS_UCDM11_006
**Scenario Title:** Thêm mới loại thẻ - Định dạng ký tự không hợp lệ (EP)
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.2
**Test Type:** Functional
**Description:** Nhập ký tự đặc biệt (VD: @, #, $) hoặc có dấu tiếng Việt vào trường Mã thẻ, kiểm tra hệ thống tự động loại bỏ hoặc báo lỗi. Nhập ký tự in thường hệ thống phải tự động in hoa.
**Test Focus:** Error flow / EP Validation

### Scenario ID: TS_UCDM11_007
**Scenario Title:** Thêm mới loại thẻ - Trùng mã thẻ trong CÙNG hãng bay
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.2
**Test Type:** Functional
**Description:** Nhập Mã thẻ đã tồn tại trong cùng 1 Hãng bay đang chọn, kiểm tra lỗi "Mã thẻ đã tồn tại trong hãng bay này."
**Test Focus:** Error flow / Business Rule

### Scenario ID: TS_UCDM11_008
**Scenario Title:** Thêm mới loại thẻ - Trùng mã thẻ KHÁC hãng bay
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.2
**Test Type:** Functional
**Description:** Nhập Mã thẻ đã tồn tại nhưng chọn Hãng bay khác, kiểm tra hệ thống cho phép tạo mới thành công.
**Test Focus:** Alternative flow / Business Rule

### Scenario ID: TS_UCDM11_009
**Scenario Title:** Thêm mới loại thẻ - Trùng mã thẻ ĐÃ BỊ XÓA (Soft delete)
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.2
**Test Type:** Functional
**Description:** Nhập Mã thẻ trùng với mã đã bị xóa trước đó trong CÙNG hãng bay, kiểm tra hệ thống vẫn cho phép tạo mới thành công theo BR-11.4.
**Test Focus:** Alternative flow / Business Rule

### Scenario ID: TS_UCDM11_010
**Scenario Title:** Thêm mới loại thẻ - Hết hạn phiên làm việc
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.2, REQ-11.7
**Test Type:** Integration / Security
**Description:** Giả lập Access Token hết hạn trước khi nhấn nút "Thêm mới", hệ thống phải từ chối API (401), hiển thị error toast và đẩy người dùng ra trang Đăng nhập.
**Test Focus:** Exception / Security

### Scenario ID: TS_UCDM11_011
**Scenario Title:** Xem chi tiết loại thẻ
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.3
**Test Type:** UI / Functional
**Description:** Mở popup Xem chi tiết của một loại thẻ, kiểm tra các trường Mã thẻ và Hãng bay bị disable hoàn toàn.
**Test Focus:** Happy path / UI State

### Scenario ID: TS_UCDM11_012
**Scenario Title:** Cập nhật loại thẻ thành công
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.4
**Test Type:** Functional
**Description:** Mở popup Sửa của một loại thẻ không bị khóa, thay đổi tên Loại thẻ và lưu, kiểm tra dữ liệu thay đổi trên lưới.
**Test Focus:** Happy path

### Scenario ID: TS_UCDM11_013
**Scenario Title:** Cập nhật loại thẻ - Không thay đổi dữ liệu
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.4
**Test Type:** UI / Functional
**Description:** Mở popup Sửa nhưng không thay đổi giá trị nào, kiểm tra nút "Cập nhập" bị Disable.
**Test Focus:** Alternative flow / UI State

### Scenario ID: TS_UCDM11_014
**Scenario Title:** Cập nhật loại thẻ - Đang được sử dụng trong Scanning Session
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.4
**Test Type:** Integration / Functional
**Description:** Sửa một loại thẻ đang tham gia vào một phiên quét vé hoạt động, hệ thống từ chối cập nhật và hiển thị lỗi "Không thể cập nhập khi loại thẻ đang được sử dụng."
**Test Focus:** Exception / Business Rule

### Scenario ID: TS_UCDM11_015
**Scenario Title:** Cập nhật loại thẻ - Đang tham chiếu trong Cấu hình phòng chờ
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.4
**Test Type:** Integration
**Description:** Sửa loại thẻ đang được dùng làm điều kiện trong Cấu hình phòng chờ. Cập nhật thành công, thông tin thay đổi tự động hiển thị ở các màn hình tham chiếu.
**Test Focus:** Alternative flow / Integration

### Scenario ID: TS_UCDM11_016
**Scenario Title:** Xóa loại thẻ thành công (Soft Delete)
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.5
**Test Type:** Functional / Data Integrity
**Description:** Xóa loại thẻ không bị ràng buộc. Thẻ biến mất khỏi UI danh sách (ẩn hoàn toàn) nhưng kiểm tra database hoặc báo cáo cũ thì dữ liệu vẫn còn tồn tại để giữ lịch sử giao dịch.
**Test Focus:** Happy path / Data Integrity

### Scenario ID: TS_UCDM11_017
**Scenario Title:** Xóa loại thẻ - Bị khóa do đang sử dụng
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.5
**Test Type:** Integration / Functional
**Description:** Xóa loại thẻ đang được cấu hình cho phòng chờ hoặc đang dùng trong session quét, hệ thống hiển thị lỗi "Không thể xóa khi loại thẻ đang được sử dụng."
**Test Focus:** Exception / Business Rule

### Scenario ID: TS_UCDM11_018
**Scenario Title:** Xóa loại thẻ - Hủy thao tác
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.5
**Test Type:** Functional
**Description:** Tại Popup Xóa, nhấn Đóng. Kiểm tra popup biến mất và bản ghi không bị xóa.
**Test Focus:** Alternative flow

### Scenario ID: TS_UCDM11_019
**Scenario Title:** Phân quyền - Role Admin
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.6
**Test Type:** Security / Role
**Description:** Đăng nhập bằng Role Admin, xác nhận thấy đầy đủ các nút: Thêm mới, Sửa, Xóa và có thể thực hiện thành công các action này. (Không có nút Xem do được ghi đè bằng Sửa).
**Test Focus:** Role/Permission

### Scenario ID: TS_UCDM11_020
**Scenario Title:** Phân quyền - Role View (Chỉ xem)
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.6
**Test Type:** Security / Role
**Description:** Đăng nhập bằng Role View, xác nhận thấy nút Xem, nhưng không thấy các nút Thêm mới, Sửa, Xóa. Gọi API CUD báo lỗi 403.
**Test Focus:** Role/Permission

### Scenario ID: TS_UCDM11_021
**Scenario Title:** Phân quyền - Role Edit (Sửa & Thêm)
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.6
**Test Type:** Security / Role
**Description:** Đăng nhập bằng Role Edit, xác nhận thấy nút Thêm mới, Sửa (và ẩn nút Xóa).
**Test Focus:** Role/Permission

### Scenario ID: TS_UCDM11_022
**Scenario Title:** Phân quyền - Role Delete (Chỉ xóa)
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.6
**Test Type:** Security / Role
**Description:** Đăng nhập bằng Role Delete, xác nhận thấy nút Xem, Xóa (và ẩn Thêm mới, Sửa).
**Test Focus:** Role/Permission

### Scenario ID: TS_UCDM11_023
**Scenario Title:** Phân quyền - Role Locked
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.6
**Test Type:** Security / Role
**Description:** Tài khoản đang truy cập thì bị Locked từ hệ thống quản trị. Thực hiện Thêm/Sửa/Xóa sẽ báo lỗi 401/403 và đẩy ra màn login.
**Test Focus:** Exception / Security

### Scenario ID: TS_UCDM11_024
**Scenario Title:** Kiểm tra lưu vết hệ thống (Audit Log Verbatim)
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.7
**Test Type:** Functional / Data Integrity
**Description:** Sau khi thực hiện các hành động Create/Update/Delete thành công, kiểm tra bảng Audit Log ghi đúng thông tin: "Tạo mới thẻ [Mã thẻ]...", "Thay đổi thông tin thẻ... Giá trị trước ==> Giá trị sau", "Xóa thẻ...".
**Test Focus:** Happy path / Business Rule

### Scenario ID: TS_UCDM11_025
**Scenario Title:** Tìm kiếm kết hợp (Combinatorics Filter)
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-11.1
**Test Type:** Functional / Decision Table
**Description:** Sử dụng Search box nhập từ khóa đúng, đồng thời chọn bộ lọc (Filter) theo 1 Hãng bay. Kiểm tra danh sách kết quả thỏa mãn cả 2 điều kiện (AND logic).
**Test Focus:** Combinatorics

---

## ⚠️ Out-of-Scope Flags

| Scenario Area | Reason | Recommended Action |
|--------------|--------|--------------------|
| Khả năng chịu tải khi import 10.000 loại thẻ | NFR: LOAD | Giao cho kỹ sư Performance Testing. |
