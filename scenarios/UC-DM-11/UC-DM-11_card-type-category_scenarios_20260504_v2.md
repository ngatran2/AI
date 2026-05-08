# Test Scenarios

> [!WARNING]
> **Human Checkpoint:** User cần review danh sách High-Level Scenarios dưới đây để bổ sung các trường hợp rủi ro đặc thù (nếu có) trước khi Agent tiến hành sinh Test Cases chi tiết ở bước tiếp theo. Đặc biệt chú ý luật Validate mới về "Mã thẻ không có khoảng trắng" (v4).

## 1. Traceability Matrix & Gap Analysis

| Req-ID | Module / Feature | Covered by Scenarios | Status |
|--------|------------------|----------------------|--------|
| REQ-01 | UI Danh mục thẻ & Hiển thị | TS_UCDM11_001, 002 | Covered |
| REQ-02 | Validate UI Form (Mã thẻ, Loại thẻ) | TS_UCDM11_003, 004, 005, 006, 007, 008, 009, 010, 011 | Covered |
| REQ-03 | Xử lý Thêm mới (Logic & Happy Path) | TS_UCDM11_012, 013, 014, 015 | Covered |
| REQ-04 | Cập nhật Loại thẻ (UI, Block, Success)| TS_UCDM11_016, 017, 018, 019 | Covered |
| REQ-05 | Xóa Loại thẻ (Block, Soft Delete) | TS_UCDM11_020, 021 | Covered |
| REQ-06 | Phân quyền truy cập (RBAC - 5 Roles) | TS_UCDM11_022, 023, 024, 025, 026 | Covered |
| REQ-07 | Xử lý ngoại lệ (Exception Flows) | TS_UCDM11_027 | Covered |

---

## 2. Detailed Scenarios

### UC-DM-11 — Quản lý danh mục loại thẻ

#### Nhóm 1: UI Danh mục thẻ (REQ-01)
### Scenario ID: TS_UCDM11_001
**Scenario Title:** Hiển thị danh sách thẻ hợp lệ
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-01
**Test Type:** UI
**Description:** Kiểm tra bảng hiển thị đúng 20 records/trang, sắp xếp thời gian tạo giảm dần, chứa các cột: Mã thẻ, Loại thẻ, Hãng bay.
**Test Focus:** Happy path

### Scenario ID: TS_UCDM11_002
**Scenario Title:** Hiển thị Empty State khi danh mục thẻ trống
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-01
**Test Type:** UI
**Description:** Kiểm tra hệ thống hiển thị thông báo chuẩn CMR-08 khi Database chưa có loại thẻ nào.
**Test Focus:** UI State

#### Nhóm 2: Validate Thêm/Sửa (REQ-02)
### Scenario ID: TS_UCDM11_003
**Scenario Title:** Mã thẻ hợp lệ với độ dài tối đa (BVA)
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** Functional
**Description:** Nhập chính xác 30 ký tự chữ và số vào trường Mã thẻ, hệ thống chấp nhận.
**Test Focus:** Boundary

### Scenario ID: TS_UCDM11_004
**Scenario Title:** Tự động Auto-Capitalize trường Mã thẻ
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** UI
**Description:** Người dùng gõ chữ thường vào ô Mã thẻ, hệ thống tự động ép kiểu thành chữ in hoa.
**Test Focus:** UI State

### Scenario ID: TS_UCDM11_005
**Scenario Title:** Báo lỗi khi Mã thẻ chứa khoảng trắng (Updated v4)
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** Functional
**Description:** Nhập chuỗi có chứa dấu cách (VD: "VIP CARD") vào Mã thẻ, form chặn và báo lỗi hợp lệ.
**Test Focus:** Error/Exception

### Scenario ID: TS_UCDM11_006
**Scenario Title:** Báo lỗi khi Mã thẻ chứa ký tự đặc biệt
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** Functional
**Description:** Nhập ký tự đặc biệt (!@#$) vào Mã thẻ, form chặn và báo lỗi hợp lệ.
**Test Focus:** Error/Exception

### Scenario ID: TS_UCDM11_007
**Scenario Title:** Báo lỗi vượt quá 30 ký tự Mã thẻ (BVA)
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** Functional
**Description:** Nhập 31 ký tự vào trường Mã thẻ, form chặn không cho nhập thêm.
**Test Focus:** Boundary

### Scenario ID: TS_UCDM11_008
**Scenario Title:** Báo lỗi bỏ trống trường bắt buộc Mã thẻ
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** Functional
**Description:** Nhấn Lưu khi Mã thẻ để trống, hệ thống highlight báo lỗi Required.
**Test Focus:** Error/Exception

### Scenario ID: TS_UCDM11_009
**Scenario Title:** Báo lỗi bỏ trống trường bắt buộc Hãng bay
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** Functional
**Description:** Nhấn Lưu khi chưa chọn Hãng bay, hệ thống highlight báo lỗi Required.
**Test Focus:** Error/Exception

### Scenario ID: TS_UCDM11_010
**Scenario Title:** Loại thẻ hợp lệ với độ dài tối đa (BVA)
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** Functional
**Description:** Nhập chính xác 100 ký tự vào trường Loại thẻ, hệ thống chấp nhận.
**Test Focus:** Boundary

### Scenario ID: TS_UCDM11_011
**Scenario Title:** Báo lỗi vượt quá 100 ký tự Loại thẻ (BVA)
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-02
**Test Type:** Functional
**Description:** Nhập 101 ký tự vào trường Loại thẻ, form chặn không cho nhập thêm.
**Test Focus:** Boundary

#### Nhóm 3: Logic Thêm Mới (REQ-03)
### Scenario ID: TS_UCDM11_012
**Scenario Title:** Hủy thao tác thêm mới
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-03
**Test Type:** Functional
**Description:** Điền form nhưng nhấn "Đóng", popup đóng lại và data không được lưu.
**Test Focus:** Alternative flow

### Scenario ID: TS_UCDM11_013
**Scenario Title:** Validation lỗi trùng Mã thẻ trong CÙNG Hãng bay
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-03
**Test Type:** Functional
**Description:** Thêm mới Mã thẻ đã tồn tại với CÙNG Hãng bay. Báo lỗi "Mã thẻ đã tồn tại trong hãng bay này."
**Test Focus:** Error/Exception

### Scenario ID: TS_UCDM11_014
**Scenario Title:** Validation cho phép trùng Mã thẻ KHÁC Hãng bay
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-03
**Test Type:** Functional
**Description:** Thêm mới Mã thẻ đã tồn tại nhưng với MỘT Hãng bay khác. Hệ thống lưu thành công.
**Test Focus:** Happy path

### Scenario ID: TS_UCDM11_015
**Scenario Title:** Thêm mới thẻ thành công (Happy Path)
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-03
**Test Type:** End-to-End
**Description:** Nhập dữ liệu hợp lệ và lưu. Verify Toast success, Record hiện trên grid, và ghi nhận Audit Log.
**Test Focus:** Happy path

#### Nhóm 4: Logic Cập Nhật (REQ-04)
### Scenario ID: TS_UCDM11_016
**Scenario Title:** Mã thẻ và Hãng bay bị Disable khi Sửa
**UC Reference:** UC-LT-11.4 Sửa loại thẻ
**Req-ID:** REQ-04
**Test Type:** UI
**Description:** Mở form Sửa, kiểm tra 2 trường Mã thẻ và Hãng bay là read-only/disable.
**Test Focus:** UI State

### Scenario ID: TS_UCDM11_017
**Scenario Title:** Nút Cập nhập Disable khi không có thay đổi
**UC Reference:** UC-LT-11.4 Sửa loại thẻ
**Req-ID:** REQ-04
**Test Type:** UI
**Description:** Mở form Sửa và không sửa gì, nút Cập nhập không cho phép click.
**Test Focus:** UI State

### Scenario ID: TS_UCDM11_018
**Scenario Title:** Chặn sửa thẻ đang trong phiên Scan (Runtime Block)
**UC Reference:** UC-LT-11.4 Sửa loại thẻ
**Req-ID:** REQ-04
**Test Type:** Functional
**Description:** Cập nhật một thẻ đang được sử dụng trong phiên scan. Báo lỗi "Không thể cập nhập khi loại thẻ đang được sử dụng."
**Test Focus:** Error/Exception

### Scenario ID: TS_UCDM11_019
**Scenario Title:** Cập nhật Loại thẻ thành công
**UC Reference:** UC-LT-11.4 Sửa loại thẻ
**Req-ID:** REQ-04
**Test Type:** End-to-End
**Description:** Đổi tên trường Loại thẻ hợp lệ, lưu thành công. Verify Toast, hiển thị trên grid, và ghi nhận Audit Log thay đổi.
**Test Focus:** Happy path

#### Nhóm 5: Logic Xóa (REQ-05)
### Scenario ID: TS_UCDM11_020
**Scenario Title:** Chặn xóa thẻ đang sử dụng (Runtime Block)
**UC Reference:** UC-LT-11.5 Xóa loại thẻ
**Req-ID:** REQ-05
**Test Type:** Functional
**Description:** Xác nhận xóa một thẻ đang dùng trong phiên scan / cấu hình điều kiện phòng chờ. Báo lỗi "Không thể xóa khi loại thẻ đang được sử dụng."
**Test Focus:** Error/Exception

### Scenario ID: TS_UCDM11_021
**Scenario Title:** Xóa thẻ hợp lệ (Soft Delete)
**UC Reference:** UC-LT-11.5 Xóa loại thẻ
**Req-ID:** REQ-05
**Test Type:** End-to-End
**Description:** Xác nhận xóa thẻ không vướng điều kiện block. Verify thẻ ẩn khỏi grid, Toast success, Audit Log ghi nhận xóa.
**Test Focus:** Happy path

#### Nhóm 6: Phân quyền RBAC (REQ-06)
### Scenario ID: TS_UCDM11_022
**Scenario Title:** Phân quyền Admin
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-06
**Test Type:** Integration
**Description:** Đăng nhập Role Admin. Có thể thấy tất cả nút (Thêm, Sửa, Xoá, Xem) và thao tác toàn quyền.
**Test Focus:** Permission/Role

### Scenario ID: TS_UCDM11_023
**Scenario Title:** Phân quyền Edit
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-06
**Test Type:** Integration
**Description:** Đăng nhập Role Edit. Thấy nút Thêm, Sửa, KHÔNG thấy nút Xoá.
**Test Focus:** Permission/Role

### Scenario ID: TS_UCDM11_024
**Scenario Title:** Phân quyền Delete
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-06
**Test Type:** Integration
**Description:** Đăng nhập Role Delete. Thấy nút Xóa, KHÔNG thấy nút Thêm, Sửa.
**Test Focus:** Permission/Role

### Scenario ID: TS_UCDM11_025
**Scenario Title:** Phân quyền View
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-06
**Test Type:** Integration
**Description:** Đăng nhập Role View. Chỉ thấy nút Xem, popup là view-only (Mã thẻ, Loại thẻ, Hãng bay bị mờ), KHÔNG thấy Thêm, Sửa, Xoá.
**Test Focus:** Permission/Role

### Scenario ID: TS_UCDM11_026
**Scenario Title:** Phân quyền Locked
**UC Reference:** UC-DM-11 Quản lý danh mục loại thẻ
**Req-ID:** REQ-06
**Test Type:** Integration
**Description:** Tài khoản bị khóa (Locked Role) cố gắng đăng nhập và không thể truy cập hệ thống.
**Test Focus:** Permission/Role

#### Nhóm 7: Xử lý ngoại lệ khác (REQ-07)
### Scenario ID: TS_UCDM11_027
**Scenario Title:** Token hết hạn khi thao tác
**UC Reference:** UC-LT-11.2 Thêm loại thẻ
**Req-ID:** REQ-07
**Test Type:** Integration
**Description:** Giả lập Session/Token hết hạn, bấm nút Lưu. Trình duyệt đẩy về trang Login kèm Toast lỗi.
**Test Focus:** Error/Exception

---

## ⚠️ Out-of-Scope Flags

| Scenario Area | Reason | Recommended Action |
|--------------|--------|--------------------|
| Kiểm tra tải (Load Test) phân trang | [NFR: LOAD] | Chuyển cho Performance tester xử lý riêng. |
| SQL Injection qua ô Mã thẻ | [NFR: SECURITY] | Chuyển cho đội ngũ Pentest. |
