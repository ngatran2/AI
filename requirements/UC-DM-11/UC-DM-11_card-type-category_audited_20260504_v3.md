# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

## Feature Brief

Chức năng Quản lý Danh mục Loại thẻ (UC-DM-11) cho phép người dùng (tùy theo phân quyền) thực hiện các thao tác Xem, Thêm, Sửa, và Xóa loại thẻ hội viên của từng hãng bay. Tính năng được quản lý với các quy tắc chặt chẽ về toàn vẹn dữ liệu (Data Integrity) như cấm xóa/sửa khi thẻ đang được sử dụng trong các phiên quét (scanning session), hỗ trợ soft-delete để không mất dữ liệu lịch sử, và tích hợp lưu vết Audit Log chi tiết (verbatim) cho mọi thay đổi.

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `98.5 / 100` | ✅ READY |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC-DM-11 | Quản lý danh mục loại thẻ | v3 | Finalized |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| docs-reader | Antigravity | 2026-04-23 | 2026-05-04 |

---

## 1. Objective & Scope

### 1.1 Objective
Quản lý các loại thẻ hội viên của hãng bay trong hệ thống, cung cấp danh mục dữ liệu chuẩn (Master Data) để tham chiếu cho các quá trình cấu hình điều kiện phòng chờ và mapping dữ liệu trong quá trình scan thẻ.

### 1.2 In Scope
- UC-LT-11.1: Xem danh mục loại thẻ
- UC-LT-11.2: Thêm loại thẻ
- UC-LT-11.3: Xem chi tiết loại thẻ
- UC-LT-11.4: Sửa loại thẻ
- UC-LT-11.5: Xóa loại thẻ

### 1.3 Out of Scope
Không có. Toàn bộ các chức năng quản lý danh mục thẻ cơ bản đều nằm trong scope.

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Người dùng hệ thống | Primary | Người dùng có tài khoản truy cập hệ thống. Các quyền (Xem, Thêm, Sửa, Xóa) phụ thuộc vào RBAC được cấu hình tại chức năng Quản lý người dùng. |

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng đăng nhập hệ thống thành công.
- Session/Access Token hợp lệ và đang hoạt động.
- Người dùng có quyền truy cập chức năng Xem/Thêm/Sửa/Xóa Danh mục loại thẻ tương ứng.

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Xem danh mục | Bảng dữ liệu hiển thị danh sách loại thẻ (hoặc màn hình trống nếu không có dữ liệu). Các nút Action hiển thị đúng theo phân quyền (VD: Chỉ có quyền xem thì hiện nút Xem, có quyền sửa thì hiện nút Sửa). |
| Thêm loại thẻ | Loại thẻ mới được lưu vào CSDL, hiển thị Toast thành công, và được log lại vào hệ thống (Audit log). Có thể tra cứu tại các danh mục toàn hệ thống. |
| Sửa loại thẻ | Dữ liệu thẻ được cập nhật (nếu không vướng điều kiện runtime), hiển thị Toast thành công, log Audit chi tiết (Giá trị cũ -> mới). |
| Xóa loại thẻ | Loại thẻ bị xóa (Soft Delete - ẩn khỏi giao diện nhưng giữ lịch sử), log Audit hệ thống, hiển thị Toast thành công. Không thể dùng để cấu hình mới hay scan mới. |

---

## 4. UI Object Inventory & Mapping

| Category | Component Name | Description & Constraints |
|----------|----------------|---------------------------|
| **Data Display Structure** | Bảng Danh mục loại thẻ | Mặc định 20 records/trang. Sắp xếp mặc định: Thời gian tạo giảm dần. Nếu trống -> CMR-08. Hiển thị cột: Mã thẻ, Loại thẻ, Hãng bay. |
| **Control System** | Popup Thêm/Sửa loại thẻ | Bao gồm các trường: Mã thẻ (Text 30 ký tự, Required), Loại thẻ (Text 100 ký tự), Hãng bay (Dropdown, Required). |
| **Control System** | Popup Xóa loại thẻ | Form cảnh báo, yêu cầu Xác nhận hoặc Đóng. |
| **Navigation & Actions** | Các Nút bấm | Xem, Sửa, Xóa, Thêm mới, Đóng, Xác nhận, Cập nhập. Các nút này hiển thị tuỳ theo phân quyền của người dùng. |
| **Other Components** | Toast Message | Hiển thị các thông báo (Success, Error) theo cấu hình của CMR-04. |

---

## 5. Object Attributes & Behavior Definition

| Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|--------------------|---------------|--------------------|---------------------------------------------|
| **Trường Mã thẻ** | Text field | Nhập text | Tự động viết hoa khi nhập chữ thường. Tối đa 30 ký tự. Chỉ nhận chữ, số, space. Required. |
| **Trường Loại thẻ** | Text field | Nhập text | Tối đa 100 ký tự. |
| **Trường Hãng bay** | Dropdown list | Click Dropdown | Trích xuất toàn bộ danh mục hãng bay (CMR-02). Required. Không được sửa ở chế độ Sửa (Disable). |
| **Nút Thêm mới (Danh sách)** | Button | Click | Chỉ hiển thị nếu có quyền Thêm. Mở Popup thêm loại thẻ. |
| **Nút Sửa (Danh sách)** | Button | Click | Chỉ hiển thị nếu có quyền Sửa. Mở Popup chi tiết thẻ ở trạng thái cho phép cập nhật. |
| **Nút Xem (Danh sách)** | Button | Click | Hiển thị nếu có quyền Xem NHƯNG KHÔNG CÓ quyền Sửa. Mở popup chi tiết thẻ dạng view-only. |
| **Nút Xóa (Danh sách/Popup)** | Button | Click | Chỉ hiển thị nếu có quyền Xóa. Mở popup xác nhận xóa. |

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function Name: Thêm loại thẻ (UC-LT-11.2)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Người dùng | Nhấn "Thêm mới" | Mở popup Thêm loại thẻ | N/A | N/A |
| 2 | Người dùng | Nhập các trường và nhấn "Thêm mới" | Validate form -> Đóng popup -> Lưu database -> Hiện Toast "Thêm mới [mã thẻ - loại thẻ] thành công." | Nhấn "Đóng": Hủy thao tác | Trùng mã thẻ trong cùng hãng bay: Thông báo lỗi dưới trường "Mã thẻ đã tồn tại trong hãng bay này." |
| 3 | Hệ thống | Background | Ghi Audit Log "Tạo mới thẻ [Mã thẻ] vào Danh mục loại thẻ" | Giữ nguyên filter/pagination | Token hết hạn: Đẩy ra Login, Toast lỗi. |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Mã thẻ | Yes | Chữ hoa, số, khoảng trắng | Max 30 | "Mã thẻ đã tồn tại trong hãng bay này." |
| Hãng bay | Yes | Dropdown | N/A | *(Theo chuẩn CMR-07)* |

### 6.2 Function Name: Sửa loại thẻ (UC-LT-11.4)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Người dùng | Nhấn "Sửa" | Mở popup chi tiết, Mã thẻ và Hãng bay bị Disable. Loại thẻ Enable. | N/A | N/A |
| 2 | Người dùng | Sửa "Loại thẻ" và nhấn "Cập nhập" | Cập nhật DB -> Toast "Cập nhập [mã loại thẻ - loại thẻ] thành công." | Nhấn "Đóng": Hủy thao tác | Đang được dùng trong scanning session: Toast lỗi "Không thể cập nhập khi loại thẻ đang được sử dụng." |

**B. Business Rules & Validations**
| Field / Object | Required | Format / Constraint | Min / Max | Error Message *(exact text)* |
|----------------|----------|---------------------|-----------|-------------------------------|
| Loại thẻ | No | Text | Max 100 | N/A |
| Nút "Cập nhập" | N/A | Disable nếu không có thay đổi | N/A | "Không thể cập nhập khi loại thẻ đang được sử dụng." |

### 6.3 Function Name: Xóa loại thẻ (UC-LT-11.5)

**A. Workflows**
| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | Người dùng | Nhấn "Xóa" trên danh sách hoặc popup | Mở popup Xóa loại thẻ | N/A | N/A |
| 2 | Người dùng | Nhấn "Xác nhận" | Soft Delete bản ghi -> Đóng popup -> Toast "Xóa [mã thẻ - loại thẻ] thành công." | Nhấn "Đóng": Hủy thao tác | Đang dùng trong scanning session / cấu hình điều kiện: Toast lỗi "Không thể xóa khi loại thẻ đang được sử dụng." |

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Thêm/Xóa loại thẻ | Ảnh hưởng trực tiếp đến dữ liệu hiển thị trên Dropdown Loại thẻ ở màn hình cấu hình phòng chờ và scan vé. | Dữ liệu phải được update tức thì ở các màn hình khác. Thẻ đã xóa không được hiện ở dropdown tạo mới dữ liệu. |
| Xóa loại thẻ | Soft Delete đảm bảo lịch sử Scan (Báo cáo) không bị mất dẫu loại thẻ đó đã bị xóa. | Các report về tần suất loại thẻ vào phòng chờ phải vẫn hiển thị đúng số liệu quá khứ của thẻ bị xoá. |
| Cập nhật loại thẻ | Update ở màn cấu hình phòng chờ nếu thẻ đang được sử dụng để cấu hình điều kiện. | Tên loại thẻ phải đồng bộ (Cascade Update) hoặc dùng Join id ở mọi UI có chứa nó. |

---

## 8. Acceptance Criteria

| AC # | Scenario | Given *(precondition)* | When *(user action)* | Then *(expected result)* |
|------|----------|------------------------|----------------------|--------------------------|
| AC-01 | Thêm mới thẻ hợp lệ | Đăng nhập có quyền Thêm, đang ở UI Thêm Thẻ, data không trùng. | Nhấn Thêm mới | Toast success, data xuất hiện ở lưới, ghi Audit Log. |
| AC-02 | Thêm mới trùng mã thẻ | Đăng nhập có quyền Thêm, mã thẻ nhập vào trùng với 1 mã có cùng hãng bay. | Nhấn Thêm mới | Lỗi dưới ô input "Mã thẻ đã tồn tại trong hãng bay này.", Nút Thêm mới không tắt. |
| AC-03 | Sửa thẻ bị Runtime Block | Đăng nhập có quyền Sửa, thẻ đang được scan tại sảnh. | Nhấn Cập nhập | Hệ thống báo lỗi Toast "Không thể cập nhập khi loại thẻ đang được sử dụng." |
| AC-04 | Sửa thẻ thành công | Đăng nhập có quyền Sửa, thẻ không bị khóa, sửa tên thẻ. | Nhấn Cập nhập | Toast success, ghi Audit Log đổi dữ liệu cũ -> mới. |
| AC-05 | Phân quyền View | Tài khoản chỉ có quyền View. | Mở màn Danh sách | Nút "Thêm", "Sửa", "Xóa" bị ẩn. Có nút "Xem". Mã thẻ & Hãng bay ở popup bị disable. |

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| API Timeout | Yêu cầu API phản hồi, quá 60s hiển thị timeout toast. | CMR-12 |
| Security | Check Authorization ở tầng API với từng hành động CUD (Create/Update/Delete). | BR-11.6 & CMR-18 |

---

## 10. Open Questions & Dependencies

### 10.1 Open Questions
| # | Question / Issue | Context | Owner | Status |
|---|-----------------|---------|-------|--------|
| *(Không có)* | Toàn bộ yêu cầu nghiệp vụ đã rất rõ ràng, logic được kiểm soát chặt chẽ. | N/A | N/A | Resolved |

### 10.2 Dependencies
- Phụ thuộc danh mục Hãng Bay (Hiển thị Dropdown).
- Phụ thuộc RBAC Role system.

---

## 11. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v3 | 2026-05-04 | Antigravity | Audit Requirement UC-DM-11 dựa trên Common Rules và Data Integrity Flow. |

---

*UC Readiness Template v3.0 — For QA Test Design*
